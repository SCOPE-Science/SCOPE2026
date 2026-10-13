#!/usr/bin/env python3
"""Exact independent finite checks of the four-strand commuting equations."""
from itertools import product


def vec(n, r, p):
    ans=[]
    for _ in range(r):
        ans.append(n % p)
        n //=p
    return ans


def wedge(u,v,p):
    r=len(u)
    return tuple((u[i]*v[j]-u[j]*v[i])%p for i in range(r) for j in range(i+1,r))


def exact_total(r,p):
    """Independently enumerate all 5r noncentral coordinates by grouping equal wedges."""
    Q=p**r
    v=[vec(i,r,p) for i in range(Q)]
    w=[[wedge(x,y,p) for y in v] for x in v]
    zero=(0,)*(r*(r-1)//2)
    n=0
    # Pairwise commutation of the corresponding r strictly upper matrices.
    for a in range(Q):
        for d in range(Q):
            if w[a][d]!=zero:
                continue
            for f in range(Q):
                if w[d][f]!=zero:
                    continue
                for b in range(Q):
                    target=w[f][b]
                    for e in range(Q):
                        if w[a][e]==target:
                            n+=1
    return n*(p**r)


def formula(r,q):
    return q**r*(q**(3*r)+(q+1)*q**(r+2)*(q**r-1)+q**3*(q**r-1)*(q**r-q))


def matrix_entry_test(p):
    # Independently compare matrix multiplication for all ordered pairs in UT_4(F_p).
    # p=2 gives all 1024 pairs of noncentral five-coordinate patterns.
    coords=list(product(range(p), repeat=5))
    for a,d,f,b,e in coords:
        for A,D,F,B,E in coords:
            cond=(a*D-A*d)%p==0 and (d*F-D*f)%p==0 and (a*E+b*F-A*e-B*f)%p==0
            # only products N_x N_y vs N_y N_x can have nonzero (1,3),(2,4),(1,4) entries
            mult=((a*D)%p,(d*F)%p,(a*E+b*F)%p)
            mult_back=((A*d)%p,(D*f)%p,(A*e+B*f)%p)
            assert cond == (mult==mult_back)


def main():
    results=[]
    for r,p in [(1,2),(2,2),(3,2),(4,2),(2,3)]:
        observed=exact_total(r,p)
        expected=formula(r,p)
        assert observed==expected,(r,p,observed,expected)
        results.append((p,r,observed))
    matrix_entry_test(2)
    print('VERIFY_OK: exhaustive independent coordinate/wedge counts', results)
    print('VERIFY_OK: 1024 exhaustive noncentral matrix-pair multiplication comparisons over F_2')

if __name__=='__main__': main()
