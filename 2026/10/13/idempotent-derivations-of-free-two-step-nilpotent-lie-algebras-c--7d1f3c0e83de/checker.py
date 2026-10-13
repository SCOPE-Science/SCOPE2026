"""Independent finite-field tests of composition-idempotent Lie derivations.

Usage: python3 checker.py (standard library only).
"""
from collections import Counter
from itertools import product
from math import comb


def gaussian(n,r,q):
    if r < 0 or r > n:
        return 0
    # Exact Gaussian coefficient, with numerator and denominator accumulated separately.
    a=b=1
    for j in range(r):
        a*=q**(n-j)-1
        b*=q**(r-j)-1
    assert a%b == 0
    return a//b


def expected(n,q):
    ans=Counter()
    if q%2:
        s=n-1
        ans[0]=1
        ans[n]=gaussian(n,1,q)*q**(s+s*s+s*(s-1)//2)
    else:
        for r in range(n+1):
            s=n-r
            exp=r*s+r*(r*(r-1)//2+s*(s-1)//2+s*s)
            ans[r*(s+1)]+=gaussian(n,r,q)*q**exp
    return ans


def rank_binary(cols):
    piv={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x
                break
            x^=piv[k]
    return len(piv)


def enumeration_char2(n):
    assert n <= 3
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    m=len(pairs)
    out=Counter()
    for A in product(range(2), repeat=n*n):
        # A[i*n+j] is row i and column j.
        low=[sum(A[i*n+j]<<i for i in range(n)) for j in range(n)]
        high=[]
        for a,b in pairs:
            val=0
            for k,(i,j) in enumerate(pairs):
                v=(A[i*n+a]*(j==b) + A[j*n+a]*(i==b)
                   +A[i*n+b]*(j==a) + A[j*n+b]*(i==a))%2
                val |= v<<k
            high.append(val<<n)
        for F in product(range(2), repeat=n*m):
            cols=[low[j] | (sum(F[j*m+k]<<k for k in range(m))<<n) for j in range(n)] + high
            # Compute matrix square directly as compositions on each basis vector.
            for c in cols:
                v=0
                for i in range(n+m):
                    if c>>i & 1:
                        v ^= cols[i]
                if v != c:
                    break
            else:
                out[rank_binary(cols)]+=1
    return out


def rank_mod(cols,q):
    d=len(cols)
    A=[[cols[j][i] for j in range(d)] for i in range(d)]
    r=0
    for j in range(d):
        pivot=next((i for i in range(r,d) if A[i][j]%q),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][j],-1,q)
        for k in range(j,d):
            A[r][k]=A[r][k]*inv%q
        for i in range(r+1,d):
            x=A[i][j]
            for k in range(j,d):
                A[i][k]=(A[i][k]-x*A[r][k])%q
        r+=1
    return r


def enumeration_n2_prime(q):
    out=Counter()
    for a,b,c,d,u,v in product(range(q),repeat=6):
        cols=[(a,c,u),(b,d,v),(0,0,(a+d)%q)]
        squares=[]
        for j in range(3):
            squares.append(tuple(sum(cols[k][i]*cols[j][k] for k in range(3))%q for i in range(3)))
        if squares==list(cols):
            out[rank_mod(cols,q)]+=1
    return out


def main():
    for n in (2,3):
        got=enumeration_char2(n)
        assert got==expected(n,2),(n,got,expected(n,2))
        print('GF(2)',n,dict(sorted(got.items())))
    for q in (3,5):
        got=enumeration_n2_prime(q)
        assert got==expected(2,q),(q,got,expected(2,q))
        print('GF(%d)'%q,2,dict(sorted(got.items())))
    for n in (3,4,5):
        for q in (2,4,8):
            coeffs=expected(n,q)
            assert sum(coeffs.values())>=1
            # Idempotent rank cannot exceed the ambient dimension.
            assert max(coeffs)<=n+n*(n-1)//2
    print('VERIFY_OK')

if __name__=='__main__':
    main()
