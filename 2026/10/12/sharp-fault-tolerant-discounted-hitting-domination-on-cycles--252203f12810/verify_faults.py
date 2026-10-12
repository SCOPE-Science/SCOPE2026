#!/usr/bin/env python3
"""Exhaustive exact-rational tests of fault-tolerant discounted domination of cycles.

Original discounted potentials are recomputed from the independent pinned
random-walk linear system on every nonempty source subset. Every adversarial
failure of up to three sources, as well as the n-1-failure extreme, is checked
against the proposed cyclic-gap theorem at strict and equality thresholds.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(a,b):
    n=len(b)
    a=[row[:] + [b[i]] for i,row in enumerate(a)]
    for j in range(n):
        t=next(t for t in range(j,n) if a[t][j])
        a[j],a[t]=a[t],a[j]
        piv=a[j][j]
        for p in range(j,n+1):a[j][p]/=piv
        for i in range(n):
            if i!=j:
                fac=a[i][j]
                if fac:
                    for p in range(j,n+1):a[i][p]-=fac*a[j][p]
    return [a[i][-1] for i in range(n)]


def source_support(n,S,lam):
    if not S:return F(0)
    U=[v for v in range(n) if v not in S]
    where={v:i for i,v in enumerate(U)}
    A=[[F(int(i==j)) for j in range(len(U))] for i in range(len(U))]
    rhs=[F(0)]*len(U)
    for i,v in enumerate(U):
        for w in ((v-1)%n,(v+1)%n):
            if w in S:rhs[i]+=lam/2
            else:A[i][where[w]]-=lam/2
    h=solve(A,rhs)
    return min(h) if h else F(1)


def gap_thresholds(n,lam):
    even=[F(1),1/lam]
    odd=[F(1),2/lam-1]
    for j in range(n+2):
        even.append((2/lam)*even[-1]-even[-2])
        odd.append((2/lam)*odd[-1]-odd[-2])
    return [None]+[1/(even[j//2] if j%2==0 else odd[j//2]) for j in range(1,n+1)]


def gaps(n,S):
    order=sorted(S);k=len(order)
    return [((order[(j+1)%k]-order[j])%n or n) for j in range(k)]


def max_window(g,w):
    return max(sum(g[(i+j)%len(g)] for j in range(w)) for i in range(len(g)))


def comps(n,k):
    for cut in combinations(range(1,n),k-1):
        previous=0;g=[]
        for nextpoint in (*cut,n):
            g.append(nextpoint-previous);previous=nextpoint
        yield g


def count_optimal(n,k,L,w):
    count=sum(max_window(g,w)<=L for g in comps(n,k))
    assert n*count%k==0
    return n*count//k


def main():
    systems=failures=parameter_profiles=membership_checks=optima=0
    for n in range(3,10):
        allS=[frozenset(v) for k in range(1,n+1) for v in combinations(range(n),k)]
        for lam in (F(1,2),F(2,3),F(4,5)):
            H=gap_thresholds(n,lam)
            assert H[1]==1 and all(H[j]>H[j+1] for j in range(1,n))
            scores={S:source_support(n,S,lam) for S in allS}
            systems+=len(allS)
            taus=sorted(set(H[1:]+[(H[j]+H[j+1])/2 for j in range(1,n)]+[F(1,100000)]))
            for f in sorted(set(list(range(1,min(3,n-1)+1))+[n-1])):
                w=f+1
                # Exact worst-case score for every source set under f deletions.
                robust={}
                for S in allS:
                    if len(S)<=f:robust[S]=F(0);continue
                    robust[S]=min(scores[S-frozenset(D)] for D in combinations(S,f))
                    failures+=len(tuple(combinations(S,f)))
                maximum_gap={S:max_window(gaps(n,S),w) for S in allS if len(S)>f}
                for tau in taus:
                    L=max(j for j in range(1,n+1) if H[j]>=tau)
                    actual={S for S,v in robust.items() if v>=tau}
                    expected={S for S in allS if len(S)>f and maximum_gap[S]<=L}
                    assert actual==expected,('membership',n,lam,f,tau,L)
                    if L<w:
                        assert not actual,('impossible',n,lam,f,tau)
                    else:
                        k=max(w,(w*n+L-1)//L)
                        assert actual and k==min(map(len,actual)),('optimum',n,lam,f,tau,L,k)
                        num=sum(len(S)==k for S in actual)
                        predicted=count_optimal(n,k,L,w)
                        assert num==predicted,('count',n,lam,f,tau,L,k,num,predicted)
                        optima+=num
                    parameter_profiles+=1
                    membership_checks+=len(allS)
    print('PASS: full exact-rational recomputation of adversarial source failures')
    print('nonempty pinned systems solved:',systems)
    print('adversarial failed-source cases:',failures)
    print('boundary/intermediate threshold profiles:',parameter_profiles)
    print('set-membership decisions cross-checked:',membership_checks)
    print('optimal-source-set instances cross-checked:',optima)
    for n,lam,tau,f in [(12,F(1,2),F(1,3),2),(20,F(3,4),F(1,5),3),(25,F(2,3),F(1,2),1)]:
        H=gap_thresholds(n,lam)
        L=max(j for j in range(1,n+1) if H[j]>=tau)
        w=f+1
        k=max(w,(w*n+L-1)//L) if L>=w else None
        print('example n,lambda,tau,failures,L,minimum:',n,str(lam),str(tau),f,L,k)

if __name__=='__main__':main()
