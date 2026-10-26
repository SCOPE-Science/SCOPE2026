"""Independent finite verification of Hamiltonian-cycle incidence closures.
Standard library only; the mathematical proof is independent of finite tests.
"""
from itertools import combinations, permutations
from math import comb, factorial
import random

def setup(n):
    edges = tuple(combinations(range(n), 2))
    ix = {e:i for i,e in enumerate(edges)}
    allbits = (1 << len(edges))-1
    def bits(es):
        ans=0
        for u,v in es:
            ans |= 1 << ix[tuple(sorted((u,v)))]
        return ans
    cycles=set()
    for perm in permutations(range(1,n)):
        vs=(0,)+perm
        cycles.add(bits((vs[i],vs[(i+1)%n]) for i in range(n)))
    return edges, allbits, bits, tuple(sorted(cycles))

def structure(n, edges, S):
    deg=[0]*n; adj=[set() for _ in range(n)]; ecount=0
    for i,(u,v) in enumerate(edges):
        if S>>i&1:
            deg[u]+=1;deg[v]+=1;adj[u].add(v);adj[v].add(u);ecount+=1
    if any(d>2 for d in deg): return 'invalid',None
    seen=set(); components=[]
    for v in range(n):
        if v in seen:continue
        stack=[v]; seen.add(v); cv=[]
        while stack:
            w=stack.pop();cv.append(w)
            for a in adj[w]:
                if a not in seen:seen.add(a);stack.append(a)
        components.append(set(cv))
    if len(components)==1 and ecount==n: return 'hamcycle',components
    if ecount!=n-len(components): return 'invalid',None
    return 'forest',components

def predicted(n,edges,bits,full,S):
    typ,components=structure(n,edges,S)
    if typ=='invalid':return full
    if typ=='hamcycle':return S
    count=len(components)
    sizes=sorted(len(c) for c in components)
    if count==1:
        # A spanning path has two endpoints.
        deg=[0]*n
        for i,(u,v) in enumerate(edges):
            if S>>i&1: deg[u]+=1;deg[v]+=1
        ends=[v for v in range(n) if deg[v]==1]
        return S|bits([(ends[0],ends[1])])
    if count==2 and sizes[0]==1:
        single=next(iter(next(c for c in components if len(c)==1)))
        other=next(c for c in components if len(c)>1)
        deg={v:0 for v in range(n)}
        for i,(u,v) in enumerate(edges):
            if S>>i&1:deg[u]+=1;deg[v]+=1
        ends=[v for v in other if deg[v]==1]
        return S|bits((single,v) for v in ends)
    if count==3 and sizes[0]==sizes[1]==1:
        singles=[next(iter(c)) for c in components if len(c)==1]
        return S|bits([(singles[0],singles[1])])
    return S

def make_rules(n,edges,bits,full):
    rules=[]
    # End-point path forcing rules.
    for outside in combinations(range(n),2):
        inside=tuple(v for v in range(n) if v not in outside)
        for p in permutations(inside):
            if p>p[::-1]: continue
            antecedent=bits((p[i],p[i+1]) for i in range(len(p)-1))
            conclusion=bits([outside])
            rules.append((antecedent,conclusion,'path'))
    # Every forbidden claw.
    for center in range(n):
        for leaves in combinations((v for v in range(n) if v!=center),3):
            antecedent=bits((center,v) for v in leaves)
            rules.append((antecedent,full,'claw'))
    # Every proper cycle, without reversal/rotation duplicates.
    for k in range(3,n):
        for support in combinations(range(n),k):
            first=support[0]
            for tail in permutations(support[1:]):
                if tail[0]>tail[-1]:continue
                p=(first,)+tail
                antecedent=bits((p[i],p[(i+1)%k]) for i in range(k))
                rules.append((antecedent,full,'cycle'))
    assert len({a for a,b,t in rules})==len(rules)
    return rules

def closure_by_models(S, cycles, full):
    arr=[C for C in cycles if C&S==S]
    if not arr:return full
    ans=full
    for C in arr:ans &= C
    return ans

def one_round(S,rules):
    out=S
    for a,b,_ in rules:
        if a&S==a:out|=b
    return out

def main():
    rng=random.Random(190421)
    total=0
    for n in range(4,8):
        edges,full,bits,cycles=setup(n)
        rules=make_rules(n,edges,bits,full)
        expected=n*comb(n-1,3)+sum(comb(n,k)*factorial(k-1)//2 for k in range(3,n))+factorial(n)//4
        assert len(rules)==expected
        # n=4: both claw and triangle conclusions are unnecessary in a direct basis.
        direct_rules=[r for r in rules if n!=4 or r[2]=='path']
        if n<=6:
            trials=range(full+1)
        else:
            candidates={0,full}
            candidates.update(r[0] for r in rules)
            candidates.update(rng.getrandbits(len(edges)) for _ in range(2000))
            trials=sorted(candidates)
        observed_closed=0
        for S in trials:
            brute=closure_by_models(S,cycles,full)
            assert predicted(n,edges,bits,full,S)==brute,(n,S,'structure')
            assert one_round(S,direct_rules)==brute,(n,S,'Horn')
            observed_closed+=(brute==S)
            total+=1
        if n<=6:
            forests=0;critical1=0;critical2=0
            for S in range(full+1):
                typ,comp=structure(n,edges,S)
                if typ=='forest' and len(comp)>=2: forests+=1
            # Count all linear forests except spanning paths, then subtract forbidden types.
            forest_upto=sum(1 for S in range(full+1) if structure(n,edges,S)[0]=='forest' and S.bit_count()<=n-2)
            predicted_closed=1+len(cycles)+forest_upto-factorial(n)//4-factorial(n)//2
            assert observed_closed==predicted_closed,(n,observed_closed,predicted_closed)
            # A necessary direct premise must have an edge not generated by its proper subpremises.
            if n>=5:
                for a,b,kind in rules:
                    proper_closures=a
                    for bit in range(len(edges)):
                        if a>>bit&1:
                            proper_closures|=closure_by_models(a^(1<<bit),cycles,full)
                    assert proper_closures!=closure_by_models(a,cycles,full),(n,kind,a)
            else:
                for a,b,kind in direct_rules:
                    assert a.bit_count()==1
                    assert closure_by_models(0,cycles,full)==0
            print(f'EXHAUSTIVE n={n} subsets={full+1} hamilton_cycles={len(cycles)} closed={observed_closed} direct_rules={len(direct_rules)} PASS')
        else:
            print(f'SAMPLED n={n} subsets={len(trials)} hamilton_cycles={len(cycles)} direct_rules={len(direct_rules)} PASS')
    print(f'VERIFY_OK checked_inputs={total} exact_closure=PASS closed_count=PASS one_round=PASS sharp_direct_premises=PASS')

if __name__=='__main__': main()
