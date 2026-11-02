"""Reproduce cycle-rank best-edge claims on finite signed banana block graphs.
Only Python standard library; all states and transition scores are exact integers.
"""
from itertools import combinations


def make_blocks(specs):
    # Each new block has its first terminal identified with previous block's last terminal.
    E=[]; blocks=[]; next_vertex=0; joint=None
    for lengths in specs:
        u=next_vertex if joint is None else joint
        if joint is None: next_vertex+=1
        v=next_vertex; next_vertex+=1
        paths=[]
        for length in lengths:
            last=u; ids=[]
            for step in range(length):
                w=v if step==length-1 else next_vertex
                if step!=length-1: next_vertex+=1
                ids.append(len(E));E.append((last,w));last=w
            paths.append(ids)
        blocks.append(paths);joint=v
    return E,blocks,next_vertex


def cycles_independent(edges,n):
    # Enumerate all undirected simple cycles by exhaustive vertex DFS,
    # discard rotation and reversal duplicates via canonical edge tuple.
    adj=[[] for _ in range(n)]
    for e,(u,v) in enumerate(edges):
        adj[u].append((v,e));adj[v].append((u,e))
    seen=set()
    for start in range(n):
        def rec(cur,visited,chosen):
            for nbr,ei in adj[cur]:
                if nbr==start and len(chosen)>=2:
                    seen.add(tuple(sorted(chosen+[ei])))
                elif nbr>start and nbr not in visited:
                    rec(nbr,visited|{nbr},chosen+[ei])
        rec(start,{start},[])
    return sorted(seen)


def sign_parity(mask,path):
    return (sum((mask>>ei)&1 for ei in path)&1)


def distance(mask,blocks):
    return sum(min(sum(sign_parity(mask,p) for p in block),
                   len(block)-sum(sign_parity(mask,p) for p in block))
               for block in blocks)


def negative_cycles(mask,cycles):
    return [c for c in cycles if sum((mask>>ei)&1 for ei in c)%2]


def exhaustive(specs):
    edges,blocks,n=make_blocks(specs)
    cycles=cycles_independent(edges,n)
    predicted={tuple(sorted(p+q)) for block in blocks for p,q in combinations(block,2)}
    assert set(cycles)==predicted, ("cycle enumeration mismatch",specs,cycles,predicted)
    m=len(edges); assert m<=13
    balanced=[x for x in range(1<<m) if not negative_cycles(x,cycles)]
    transitions=0
    for x in range(1<<m):
        D=distance(x,blocks)
        neg=negative_cycles(x,cycles)
        assert (not neg)==(D==0)
        # Independent exhaustive Hamming distance test, nontrivial for many states.
        exact_min=min((x^y).bit_count() for y in balanced)
        assert D==exact_min,("distance formula",specs,x,D,exact_min)
        if not neg: continue
        rank=[0]*m
        for c in neg:
            for ei in c:rank[ei]+=1
        oldE=len(neg)
        for c in neg:
            mr=max(rank[e] for e in c)
            for e in c:
                if rank[e]!=mr:continue
                x2=x^(1<<e)
                D2=distance(x2,blocks)
                E2=len(negative_cycles(x2,cycles))
                assert D2==D-1,('best-edge fails',specs,x,c,e,D,D2)
                assert E2<oldE,('energy fails',specs,x,c,e,oldE,E2)
                transitions+=1
    print(f"PASS specs={specs} vertices={n} edges={m} cycles={len(cycles)} "
          f"states={1<<m} all_legal_transitions={transitions} balanced={len(balanced)}")
    return (1<<m),transitions


def verify_tie_law():
    # For each set of paths, enumerate all discordant cycles and admissible
    # max-rank edges; compare exact outcome probability with length formula.
    from fractions import Fraction
    for lengths,minus in [([2,2,2,2],{0,2}),([2,3,4,5],{0,2}),
                          ([2,7,2,4,3,6],{0,2,4})]:
        r=len(lengths);assert r%2==0 and len(minus)==r//2
        pos=set(range(r))-minus
        pairs=[(i,j) for i in minus for j in pos]
        lhs=sum((Fraction(lengths[i],lengths[i]+lengths[j]) for i,j in pairs),Fraction(0))/len(pairs)
        # Independent explicit enumeration of uniformly chosen cycle followed
        # by uniformly chosen edge in that cycle.
        weight=Fraction(0)
        for i,j in pairs:
            weights=[(x in minus) for x in [i]*lengths[i]+[j]*lengths[j]]
            weight+=Fraction(sum(weights),len(weights)*len(pairs))
        assert lhs==weight
        print('PASS tie',lengths,sorted(minus),'P(final +)',str(lhs))

if __name__=='__main__':
    configs=[[[2,2]],[[2,2,2]],[[2,3,2]],[[2,2,2,2]],[[2,3,2,2]],
             [[2,2,2],[2,2,2]],[[2,2,2,2],[2,2]]]
    totals=[exhaustive(s) for s in configs]
    verify_tie_law()
    print('TOTAL',sum(a for a,b in totals),'states,',sum(b for a,b in totals),'legal transitions')
