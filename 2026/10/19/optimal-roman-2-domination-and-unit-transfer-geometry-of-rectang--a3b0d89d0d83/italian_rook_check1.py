"""Direct finite checker for Roman-{2} optimal rook-grid labels and one-unit reconfiguration.
Run: python italian_rook_check1.py. Only the Python standard library is used.
"""
from itertools import combinations_with_replacement
from math import comb, factorial
from collections import deque, Counter

def candidates(m,n,w):
    for mult in combinations_with_replacement(range(m*n), w):
        if any(mult[k]==mult[k+2] for k in range(len(mult)-2)):
            continue
        f=[0]*(m*n)
        for a in mult:f[a]+=1
        yield tuple(f)

def feasible_direct(f,m,n):
    for i in range(m):
        for j in range(n):
            if f[i*n+j]: continue
            q=sum(f[i*n+k] for k in range(n) if k!=j)
            q+=sum(f[k*n+j] for k in range(m) if k!=i)
            if q<2:return False
    return True

def classified(f,m,n):
    w=sum(f)
    A=(all(sum(f[i*n+j] for i in range(m))==1 for j in range(n))
       and all(sum(f[i*n+j] for j in range(n))>=1 for i in range(m)))
    B=all(sum(f[i*n+j] for j in range(n))==2 for i in range(m))
    assert w==min(n,2*m)
    if n<2*m:return A
    if n>2*m:return B
    return A or B

def edge_neighbors(f,m,n,good):
    for a in range(m*n):
        if f[a]==0: continue
        for b in range(m*n):
            if a==b or f[b]==2:continue
            g=list(f);g[a]-=1;g[b]+=1;g=tuple(g)
            if g in good:yield g

def component_sizes(good,m,n):
    unseen=set(good); sizes=[]
    while unseen:
        seed=next(iter(unseen)); unseen.remove(seed);q=[seed];k=0
        for f in q:
            k+=1
            for g in edge_neighbors(f,m,n,good):
                if g in unseen:
                    unseen.remove(g);q.append(g)
        sizes.append(k)
    return sorted(sizes,reverse=True)

def distance_from(seed,good,m,n):
    dist={seed:0};q=deque([seed])
    while q:
        f=q.popleft()
        for g in edge_neighbors(f,m,n,good):
            if g not in dist:
                dist[g]=dist[f]+1;q.append(g)
    return len(dist),max(dist.values())

def all_surjections(m,n):
    # Count onto maps by inclusion-exclusion, independently of generating them.
    return sum((-1)**j*comb(m,j)*(m-j)**n for j in range(m+1))

def main():
    cases=[(2,n) for n in range(2,7)]+[(3,n) for n in range(3,8)]+[(4,n) for n in range(4,6)]
    for m,n in cases:
        W=min(n,2*m)
        assert not any(feasible_direct(f,m,n) for w in range(W) for f in candidates(m,n,w)), (m,n,'lower')
        states={f for f in candidates(m,n,W) if feasible_direct(f,m,n)}
        assert states and all(classified(f,m,n) for f in states)
        A=all_surjections(m,n)
        B=(n*(n+1)//2)**m
        X=factorial(n)//(2**m) if n==2*m else 0
        target=A if n<2*m else B if n>2*m else A+B-X
        assert len(states)==target,(m,n,len(states),target)
        comps=component_sizes(states,m,n) if len(states)<=25000 else []
        expected=[1]*factorial(m) if m==n else [len(states)]
        assert comps==expected,(m,n,comps,expected)
        sample=list(states)[0]
        reached,ecc=distance_from(sample,states,m,n)
        assert reached==comps[0]
        if n>2*m:assert ecc==2*m,(m,n,ecc)
        print(f'm={m} n={n} min_weight={W} min_functions={len(states)} components={len(comps)} sampled_ecc={ecc}')
    print('DIRECT_EXHAUSTIVE_CHECKS_OK')
if __name__=='__main__':main()
