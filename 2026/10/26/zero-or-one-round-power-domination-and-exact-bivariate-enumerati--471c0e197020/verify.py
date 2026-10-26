"""Independent exhaustive checks for power domination of multipartite line graphs.

Run: python verify.py
No external packages or data are required.
"""
from itertools import combinations
from math import comb


def line_instance(parts):
    labels = [i for i, size in enumerate(parts) for _ in range(size)]
    edges = [(a,b) for a in range(len(labels)) for b in range(a+1,len(labels))
             if labels[a] != labels[b]]
    neighborhood = []
    for a,(u,v) in enumerate(edges):
        neighborhood.append(sum(1<<j for j,(w,z) in enumerate(edges)
                                if a != j and ({u,v} & {w,z})))
    return labels,edges,neighborhood


def actual_pds(mask, neighborhoods):
    if not mask: return False
    all_ = (1 << len(neighborhoods)) - 1
    colored = mask
    for v,nb in enumerate(neighborhoods):
        if (mask >> v) & 1: colored |= nb
    while colored != all_:
        gain = 0
        for v,nb in enumerate(neighborhoods):
            if (colored >> v) & 1:
                rem = nb & ~colored
                if rem and rem & (rem - 1) == 0: gain |= rem
        if not gain: break
        colored |= gain
    return colored == all_


def predicted_pds(mask, labels, edges, r):
    if not mask: return False
    touched = set()
    for j,(u,v) in enumerate(edges):
        if (mask >> j) & 1: touched.update((u,v))
    u_counts = [0]*r
    for v,part in enumerate(labels):
        if v not in touched: u_counts[part] += 1
    positive = [u for u in u_counts if u]
    return len(positive) <= 1 or (len(positive) == 2 and min(positive) == 1)


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for a in range(1,n-r+2):
            for rest in compositions(n-a, r-1): yield (a,)+rest


def exhaustive(max_vertices=6):
    tested_instances, tested_selections = 0,0
    examples={}
    for n in range(2,max_vertices+1):
        for r in range(2,n+1):
            for sizes in compositions(n,r):
                labels,edges,neighborhoods=line_instance(sizes)
                counts={}
                for mask in range(1<<len(edges)):
                    yes=actual_pds(mask,neighborhoods)
                    criterion=predicted_pds(mask,labels,edges,r)
                    assert yes==criterion,(sizes,mask,yes,criterion)
                    if yes:
                        k=mask.bit_count()
                        counts[k]=counts.get(k,0)+1
                    tested_selections+=1
                examples[sizes]=counts
                tested_instances+=1
    return tested_instances,tested_selections,examples


def exact_polynomial_ie(parts):
    # Compute the polynomial through inclusion-exclusion over endpoint supports.
    r=len(parts)
    E=sum(a*b for i,a in enumerate(parts) for b in parts[i+1:])
    ans=[0]*(E+1)
    def vectors(bound):
        if not bound:
            yield ()
        else:
            for x in range(bound[0]+1):
                for ys in vectors(bound[1:]): yield (x,)+ys
    for u in vectors(parts):
        pos=[x for x in u if x]
        if not (len(pos)<=1 or (len(pos)==2 and min(pos)==1)): continue
        t=tuple(a-b for a,b in zip(parts,u))
        if not sum(t): continue
        ways=1
        for a,b in zip(parts,u): ways*=comb(a,b)
        for s in vectors(t):
            weight=ways*(-1)**(sum(t)-sum(s))
            for a,b in zip(t,s): weight*=comb(a,b)
            es=sum(a*b for i,a in enumerate(s) for b in s[i+1:])
            for k in range(0,es+1): ans[k]+=weight*comb(es,k)
    assert ans[0]==0,(parts,ans[0])
    return {k:v for k,v in enumerate(ans) if v}

if __name__=='__main__':
    count, selections, examples=exhaustive(6)
    print(f'PASS: {count} ordered part-size instances and {selections} edge-subset selections.')
    cases=[(2,2),(3,3),(2,2,2),(3,2,1),(1,1,1,1),(1,5),(1,2,3),(1,1,4)]
    for case in cases:
        assert exact_polynomial_ie(case)==examples[case],(case,exact_polynomial_ie(case),examples[case])
        print(f'P{case}: {examples[case]}')
    print('PASS: independent inclusion-exclusion coefficient calculations match exhaustive propagation.')

# Extra independent test of inclusion-minimal power-dominating sets of J(n,2).
def triangular_minimal_check(max_n=6):
    for n in range(3,max_n+1):
        labels,edges,neighbor=line_instance((1,)*n)
        sizes=[]
        for mask in range(1,1<<len(edges)):
            if not actual_pds(mask,neighbor): continue
            if any(actual_pds(mask & ~(1<<e),neighbor)
                   for e in range(len(edges)) if (mask>>e)&1): continue
            deg=[0]*n
            for e,(u,v) in enumerate(edges):
                if (mask>>e)&1: deg[u]+=1;deg[v]+=1
            unseen=sum(d==0 for d in deg)
            if unseen==2:
                assert all(deg[u]==1 or deg[v]==1 for e,(u,v) in enumerate(edges) if (mask>>e)&1)
            else:
                assert unseen==1 and all(deg[u]==deg[v]==1 for e,(u,v) in enumerate(edges) if (mask>>e)&1)
            sizes.append(mask.bit_count())
        assert min(sizes)==(n-2+1)//2 and max(sizes)==max(1,n-3),(n,min(sizes),max(sizes))
        print(f'Triangular J({n},2): min/max minimal size {min(sizes)}/{max(sizes)}; {len(sizes)} inclusion-minimal sets.')
    print('PASS: triangular inclusion-minimal characterization and sharp bounds.')

if __name__ == '__main__':
    triangular_minimal_check()


def actual_round_count(mask, neighborhoods):
    """Return -1 on failure; otherwise the number of parallel forcing rounds."""
    if not mask:
        return -1
    entire=(1<<len(neighborhoods))-1
    colored=mask
    for v,nb in enumerate(neighborhoods):
        if (mask>>v)&1:colored|=nb
    rounds=0
    while colored != entire:
        additions=0
        for v,nb in enumerate(neighborhoods):
            if (colored>>v)&1:
                rem=nb&~colored
                if rem and rem & (rem-1)==0:additions|=rem
        if not additions:return -1
        colored|=additions
        rounds+=1
    return rounds


def exhaustive_round_check(max_vertices=6):
    tuples=0; selections=0
    for n in range(2,max_vertices+1):
        for r in range(2,n+1):
            for sizes in compositions(n,r):
                labels,edges,neighborhoods=line_instance(sizes)
                for mask in range(1<<len(edges)):
                    if not mask:
                        expected=-1
                    else:
                        touched=set()
                        for j,(u,v) in enumerate(edges):
                            if (mask>>j)&1:touched.update((u,v))
                        uc=[sum(v not in touched and labels[v]==i for v in range(n)) for i in range(r)]
                        pos=[x for x in uc if x]
                        expected=(0 if len(pos)<=1 else (1 if len(pos)==2 and min(pos)==1 else -1))
                    got=actual_round_count(mask,neighborhoods)
                    assert got==expected,(sizes,mask,got,expected)
                    selections+=1
                tuples+=1
    print(f'PASS: {selections} direct parallel-round simulations across {tuples} part-size tuples.')

if __name__=='__main__':
    exhaustive_round_check()
