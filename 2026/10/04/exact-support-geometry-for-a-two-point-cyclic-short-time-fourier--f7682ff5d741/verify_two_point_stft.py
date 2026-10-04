#!/usr/bin/env python3
from math import gcd
from itertools import combinations


def cycles(N,a):
    seen=set(); out=[]
    for s in range(N):
        if s in seen: continue
        c=[]; x=s
        while x not in seen:
            seen.add(x); c.append(x); x=(x+a)%N
        out.append(c)
    return out


def stats(N,a,S):
    S=set(S); d=gcd(N,a); L=N//d
    A=sum(1 for x in range(N) if x in S or (x+a)%N in S)
    E=sum(1 for x in range(N) if x in S and (x+a)%N in S)
    Q=0
    if L%2:
        Q=sum(1 for c in cycles(N,a) if all(x in S for x in c))
    return d,L,A,E,Q


def predicted(N,a,S):
    d,L,A,E,Q=stats(N,a,S)
    return N*A-d*(E-Q)


def construct_signs(N,a,S):
    S=set(S); d=gcd(N,a); L=N//d
    f={x:0 for x in range(N)}
    for cyc in cycles(N,a):
        occ=[x in S for x in cyc]
        if not any(occ): continue
        if all(occ):
            # Alternating signs around even full cycles; on odd cycles this
            # makes exactly the closing edge bad.
            for i,x in enumerate(cyc): f[x]=1 if i%2==0 else -1
        else:
            # Each occupied component is a path. Alternate signs along it.
            n=len(cyc)
            starts=[i for i in range(n) if occ[i] and not occ[(i-1)%n]]
            for st in starts:
                i=st; sign=1
                while occ[i]:
                    f[cyc[i]]=sign
                    sign=-sign
                    i=(i+1)%n
    assert {x for x,v in f.items() if v}==S
    return f


def support_from_signs(N,a,S):
    S=set(S); f=construct_signs(N,a,S); d=gcd(N,a); L=N//d
    total=0; good=0
    for x in range(N):
        y=(x+a)%N
        inx=x in S; iny=y in S
        if not inx and not iny:
            continue
        if inx ^ iny:
            total += N
        else:
            # A two-term frequency slice has d zeros iff
            # -f[x]/f[y] is an L-th root of unity. For f in {+/-1},
            # +1 always qualifies and -1 qualifies exactly for even L.
            ratio = -f[x]*f[y]  # since f[y] = +/-1
            is_good = (ratio==1) or (ratio==-1 and L%2==0)
            if is_good:
                total += N-d; good += 1
            else:
                total += N
    return total,good


def max_good_combinatorial(N,a,S):
    S=set(S); d,L,A,E,Q=stats(N,a,S)
    # On each partial occupied path, every internal edge can be good.
    # On a full even cycle, every edge can be good; on a full odd cycle,
    # exactly one edge must fail.
    return E-Q


def check_exhaustive(maxN=12):
    cases=0
    for N in range(3,maxN+1):
        for a in range(1,N):
            L=N//gcd(N,a)
            local=[]
            for mask in range(1,1<<N):
                S={i for i in range(N) if mask>>i & 1}
                p=predicted(N,a,S)
                got,good=support_from_signs(N,a,S)
                assert got==p,(N,a,S,p,got)
                assert good==max_good_combinatorial(N,a,S)
                local.append((p,S))
                cases+=1
            mn=min(v for v,_ in local)
            if L==2:
                assert mn==N,(N,a,L,mn)
                mins=[S for v,S in local if v==mn]
                assert all(len(S)==2 and S=={next(iter(S)), (next(iter(S))+a)%N} for S in mins)
            else:
                assert mn==2*N,(N,a,L,mn)
                assert all(len(S)==1 for v,S in local if v==mn)
    return cases


def check_large_corollary(maxN=5000):
    pairs=0
    for N in range(3,maxN+1):
        for a in range(1,N):
            d=gcd(N,a); L=N//d
            claimed=N if L==2 else 2*N
            # Analytic component minima from the proof:
            # partial component with k>=1 vertices contributes
            # (N-d)k + (N+d), minimized at k=1 => 2N;
            # full cycle contributes N(L-1) if L even, else N(L-1)+d.
            partial=2*N
            full=N*(L-1) + (d if L%2 else 0)
            analytic=min(partial,full)
            assert analytic==claimed,(N,a,d,L,analytic,claimed)
            pairs+=1
    return pairs

if __name__=='__main__':
    c=check_exhaustive(12)
    p=check_large_corollary(5000)
    print('EXHAUSTIVE_SUPPORT_CASES',c)
    print('PARAMETER_PAIRS',p)
    print('VERIFY_OK')
