#!/usr/bin/env python3
from collections import defaultdict
from math import pi, sqrt, exp


def boundary_data(k, T):
    ns=[]; qs=[]
    for s in range(k):
        n=T+((s-T)%k)
        ns.append(n); qs.append((n-s)//k)
    return ns, qs


def coeff_vectors(k, T):
    ns, qs = boundary_data(k,T)
    vecs=[]
    for x in range(T+k):
        v=[]
        for s in range(k):
            a = (1 if x <= qs[s] else 0)
            if x <= ns[s] and x % k == s:
                a += 1
            v.append(a)
        vecs.append(tuple(v))
    return vecs


def exact_count(k,T,c):
    d={(0,)*k: 1}
    for v in coeff_vectors(k,T):
        nd=defaultdict(int)
        for z,n in d.items():
            zp=tuple(z[i]+v[i] for i in range(k))
            zm=tuple(z[i]-v[i] for i in range(k))
            nd[zp]+=n; nd[zm]+=n
        d=nd
    return d.get((2*c,)*k,0)


def C(k):
    return (8*k/pi)**(k/2)/sqrt(k+3)


def gaussian_factor(k, lam):
    return exp(-2*k*k*lam*lam/(k+3))


def covariance(k,T):
    V=coeff_vectors(k,T)
    S=[[0]*k for _ in range(k)]
    for v in V:
        for i in range(k):
            for j in range(k):
                S[i][j]+=v[i]*v[j]
    return S


def det_float(A):
    A=[list(map(float,row)) for row in A]
    n=len(A); ans=1.0
    for i in range(n):
        p=max(range(i,n), key=lambda r: abs(A[r][i]))
        if abs(A[p][i]) < 1e-30: return 0.0
        if p != i:
            A[i],A[p]=A[p],A[i]; ans=-ans
        piv=A[i][i]; ans*=piv
        for r in range(i+1,n):
            f=A[r][i]/piv
            for j in range(i+1,n):
                A[r][j]-=f*A[i][j]
    return ans


def main():
    print('Constants')
    for k in (2,3,4,5):
        print(k, f'{C(k):.15f}')

    print('\nFixed-c exact counts: normalized by 2^T T^{-k/2}')
    for k, Ts in ((2,(40,80,120)), (3,(30,60,90))):
        print('k=',k)
        for T in Ts:
            n=exact_count(k,T,0)
            ratio=n/(2**T*T**(-k/2))
            print(T, n, f'{ratio:.12f}', 'target', f'{C(k):.12f}')

    print('\nSquare-root-scale profile')
    for k,T,c in ((2,120,5),(2,120,11),(3,90,5),(3,90,9)):
        n=exact_count(k,T,c)
        norm=n/(2**T*T**(-k/2))
        pred=C(k)*gaussian_factor(k,c/sqrt(T))
        print(k,T,c,f'{norm:.12f}',f'{pred:.12f}')

    print('\nCovariance determinant check')
    T=10000
    for k in (2,3,4,5):
        S=covariance(k,T)
        normalized=[[S[i][j]/T for j in range(k)] for i in range(k)]
        got=det_float(normalized)
        target=(k+3)/(k**k)
        print(k,f'{got:.12f}',f'{target:.12f}')

    print('\nParity check: every boundary coefficient sum is even')
    for k in (2,3,4,5):
        V=coeff_vectors(k,137)
        sums=[sum(v[s] for v in V) for s in range(k)]
        print(k,sums,[x%2 for x in sums])

if __name__=='__main__':
    main()
