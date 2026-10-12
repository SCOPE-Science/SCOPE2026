"""Independent arithmetic tests for power-denominator Farey neighbor statistics.

No external dependencies. The theorem is proved analytically; this script checks
finite examples with two independent enumeration algorithms.
"""
from math import gcd, isqrt, gamma, pi


def root_floor(n, e):
    lo, hi = 1, n+1
    while lo+1 < hi:
        m = (lo+hi)//2
        if m**e <= n: lo = m
        else: hi = m
    return lo


def pair_set(N, r, s):
    U, V = root_floor(N,r),root_floor(N,s)
    return {(u**r, v**s) for u in range(1,U+1)
            for v in range(1,V+1) if gcd(u,v)==1 and u**r+v**s>N}


def farey_set(N, r, s):
    rpow={u**r for u in range(1,root_floor(N,r)+1)}
    spow={v**s for v in range(1,root_floor(N,s)+1)}
    a,b,c,d=0,1,1,N
    out=set()
    while c<=N:
        assert b*c-a*d==1
        if b in rpow and d in spow: out.add((b,d))
        k=(N+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
    return out


def area(r,s):
    return 1-gamma(1+1/r)*gamma(1+1/s)/gamma(1+1/r+1/s)


def main():
    num=0
    for N in (10,20,55,120,300):
      for r in (2,3,4):
       for s in (2,3,4):
        p=pair_set(N,r,s)
        f=farey_set(N,r,s)
        assert p==f,(N,r,s,p^f)
        num+=1
    for r,s in ((2,2),(2,3),(3,2),(3,3)):
      N=10**7
      cnt=len(pair_set(N,r,s))
      lead=6/pi**2*area(r,s)*N**(1/r+1/s)
      print(f'SCALING N={N} r={r} s={s} count={cnt} lead={lead:.5f} ratio={cnt/lead:.5f}')
    print(f'BIJECTION_OK tests={num} all_ordered_Farey_pairs_matched')

if __name__=='__main__': main()
