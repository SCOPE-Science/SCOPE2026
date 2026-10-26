"""Exact rank/flag checks for uniformly sampled square-zero maps and subspaces.

No external libraries. The finite checks support but do not prove the limits.
"""
from collections import Counter
from itertools import combinations, product
from math import prod


def gauss(n, r, q):
    if r < 0 or r > n:
        return 0
    a = [[0]*(n+1) for _ in range(n+1)]
    a[0][0] = 1
    for i in range(1,n+1):
        a[i][0]=a[i][i]=1
        for j in range(1,i):
            a[i][j]=a[i-1][j]+q**(i-j)*a[i-1][j-1]
    return a[n][r]


def gl(r,q):
    return prod(q**r-q**j for j in range(r))


def differential_count(n,r,q):
    return gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)


def flag_count(n,r,m,b,t,q):
    """Number of m-subspaces W with dim(W cap ker D)=b and
    dim((W cap ker D + im D)/im D)=t, for a fixed rank-r D^2=0.
    """
    h=n-2*r
    s=n-r
    a=b-t
    if a < 0 or a > r or t < 0 or t > h or m-b < 0 or m-b > n-s:
        return 0
    return (gauss(r,a,q)*gauss(h,t,q)*q**(t*(r-a))
            *gauss(n-s,m-b,q)*q**((s-b)*(m-b)))


def transform(cols,x):
    out=0
    for i,c in enumerate(cols):
        if x & (1<<i):out^=c
    return out


def rank(cols):
    piv={}
    for c in cols:
        v=c
        while v:
            k=v.bit_length()-1
            if k in piv:v^=piv[k]
            else:
                piv[k]=v
                break
    return len(piv)


def subspaces(n,m):
    spaces=set()
    for basis in combinations(range(1,1<<n),m):
        s={0}
        for b in basis:s|={x^b for x in list(s)}
        if len(s)==(1<<m):spaces.add(frozenset(s))
    return spaces


def check_exhaustive():
    checked_maps=0
    checked_pairs=0
    for n in range(1,5):
        m=n//2
        spaces=subspaces(n,m)
        assert len(spaces)==gauss(n,m,2)
        found=Counter()
        for cols in product(range(1<<n),repeat=n):
            if any(transform(cols,col) for col in cols):continue
            r=rank(cols)
            K={x for x in range(1<<n) if transform(cols,x)==0}
            I={transform(cols,x) for x in range(1<<n)}
            assert len(K)==(1<<(n-r)) and len(I)==(1<<r) and I<=K
            checked_maps+=1
            for W in spaces:
                b=(len(W & K)).bit_length()-1
                a=(len(W & I)).bit_length()-1
                found[(r,b,b-a)]+=1
                checked_pairs+=1
        expected=Counter()
        for r in range(n//2+1):
            for b in range(m+1):
                for t in range(b+1):
                    v=differential_count(n,r,2)*flag_count(n,r,m,b,t,2)
                    if v:expected[(r,b,t)]+=v
        assert found==expected, (n,found,expected)
    return checked_maps,checked_pairs


def check_normalization():
    tests=0
    for q in (2,3,4):
        for n in range(2,13):
            m=n//2
            for r in range(n//2+1):
                total=sum(flag_count(n,r,m,b,t,q)
                          for b in range(m+1) for t in range(b+1))
                assert total==gauss(n,m,q),(q,n,m,r,total)
                tests+=1
    return tests


def limit_witness(q,epsilon,kmax=12,jmax=30):
    Q=1/q
    fac=[1.]
    for i in range(1,4*jmax+2):fac.append(fac[-1]*(1-Q**i))
    weights=[Q**(2*k*(k+epsilon))/fac[2*k+epsilon] for k in range(kmax)]
    z=sum(weights)
    p0=0.
    for k,w in enumerate(weights):
        h=epsilon+2*k
        for j in range(jmax):
            beta=fac[-1]*Q**(j*(j+k))/(fac[j]*fac[j+k])
            p0+=(w/z)*beta*Q**(h*(k+j))
    return 1-p0


if __name__=='__main__':
    nm,np=check_exhaustive()
    nt=check_normalization()
    a=limit_witness(2,0)
    b=limit_witness(2,1)
    assert 0.3374<a<0.3375 and 0.4361<b<0.4362
    print('SQUARE_ZERO_RANDOM_SUBSPACE_OK',nm,np,nt,'even',format(a,'.12f'),'odd',format(b,'.12f'))
