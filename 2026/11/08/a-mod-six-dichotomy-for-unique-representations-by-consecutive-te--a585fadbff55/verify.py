"""Exact finite checks for a tetrahedral-semigroup uniqueness classification.

Run with Python 3: python verify.py. No third-party packages.
The finite checks complement, but do not replace, the symbolic proof.
"""
from math import comb


def data(n):
    assert n >= 4
    a = tuple(comb(n + i + 2, 3) for i in range(4))
    c = lambda j: comb(n + j, 4)
    r = n % 6
    if r == 0:
        B = (2*c(5), 4*c(4), 4*c(3)//3)
        F = (n-3)//3*a[1] + n*a[2] + n//2*a[3] - a[0]
    elif r == 1:
        B = (4*c(5)//3, 2*c(4), 4*c(3))
        F = (n-1)*a[1] + (n-1)//2*a[2] + (n-1)//3*a[3] - a[0]
    elif r == 2:
        B = (2*c(5), 4*c(4)//3, 4*c(3))
        F = (n-1)*a[1] + (n-2)//3*a[2] + n//2*a[3] - a[0]
    elif r == 3:
        B = (4*c(5), 2*c(4), 4*c(3)//3)
        F = (n-3)//3*a[1] + (n-1)//2*a[2] + (n+1)*a[3] - a[0]
    elif r == 4:
        B = (4*c(5)//3, 2*c(4), 4*c(3))
        F = (n+2)//3*a[2] + (n+2)//2*a[1] + (n+2)*a[0] - a[3]
    else:
        B = (4*c(5), 4*c(4)//3, 2*c(3))
        F = (n+4)*a[2] + (n+1)//3*a[1] + (n+1)//2*a[0] - a[3]
    return a,B,F


def main():
    total_states = 0
    principal = 0
    nonprincipal = 0
    for n in range(4, 31):
        a,B,F=data(n)
        b=min(B)
        # Unbounded four-denomination DP, capped at two (distinguishes 0, 1, >=2).
        bound=F+b
        cnt=bytearray(bound+1)
        cnt[0]=1
        for coin in a:
            for t in range(coin,bound+1):
                cnt[t]=min(2,cnt[t]+cnt[t-coin])
        # Independently compute membership in S, rather than deduce it from the count.
        reach=bytearray(bound+1)
        reach[0]=1
        for t in range(1,bound+1):
            reach[t]=int(any(t>=coin and reach[t-coin] for coin in a))
        assert max(t for t in range(bound+1) if not reach[t])==F
        assert sum(v==0 for v in cnt[:F+1])==(F+1)//2
        # Every multiple factorization is supported above a published Betti degree.
        for t in range(bound+1):
            ideal=any(t>=degree and reach[t-degree] for degree in B)
            assert ideal==(cnt[t]==2),(n,t,'Betti ideal')
        # Exact classification of principal versus nonprincipal nonunique ideals.
        should=(n%6 in (0,2,3))
        principal_here=all(not(t>=degree and reach[t-degree]) or
                           (t>=b and reach[t-b])
                           for degree in B for t in range(degree,bound+1))
        assert principal_here==should,(n,'principal')
        g1=max(t for t in range(bound+1) if cnt[t]<=1)
        H1=sum(v<=1 for v in cnt)
        if should:
            assert g1==F+b,(n,'g1')
            assert H1==b+(F+1)//2,(n,'genus')
            assert all((cnt[t]==1)==(reach[t] and (t<b or not reach[t-b]))
                       for t in range(bound+1))
            principal+=1
        else:
            assert g1<F+b,(n,'strict')
            nonprincipal+=1
        total_states+=bound+1
        print('n=%d residue=%d F=%d b=%d g1=%d unique_count=%d principal=%s' %
              (n,n%6,F,b,g1,H1,should))
    print('PASS: 27 parameter cases; %d directly evaluated states; '
          '%d principal, %d nonprincipal' %
          (total_states,principal,nonprincipal))

if __name__=='__main__':
    main()
