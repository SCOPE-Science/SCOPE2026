"""Exact arithmetic checks for a modular Klein-plane-curve classification.

Finite checks corroborate, but do not substitute for, the uniform proof.
"""
from math import gcd


def prime_factors(n):
    factors = []
    d = 2
    while d*d <= n:
        if n%d == 0:
            q = 1
            while n%d == 0:
                n //= d
                q *= d
            factors.append((d,q))
        d += 1
    if n > 1:
        factors.append((n,n))
    return factors


def mod_inverse(a, p):
    return pow(a % p, -1, p)


def partials(m, p, x, y, z):
    fx = (m*pow(x,m-1,p)*y + pow(z,m,p)) % p
    fy = (pow(x,m,p) + m*pow(y,m-1,p)*z) % p
    fz = (pow(y,m,p) + m*pow(z,m-1,p)*x) % p
    f = (pow(x,m,p)*y + pow(y,m,p)*z + pow(z,m,p)*x) % p
    return (f, fx, fy, fz)


def verify(m, p):
    N = m*m-m+1
    assert N % p == 0
    assert p%2 == 1 and m % p not in (0,1)
    q = 1
    t = N
    while t%p == 0:
        t//=p
        q*=p
    N0=t
    s0=(-m*mod_inverse(m-1,p))%p
    assert s0 != 0
    c=(-m*pow(s0,m-1,p))%p
    # Every singular torus point is of form [1:u:s0/u^(m-1)].
    us=[u for u in range(1,p) if pow(u,N,p)==c]
    for u in us:
        v=s0*pow(pow(u,m-1,p),-1,p)%p
        assert partials(m,p,1,u,v) == (0,0,0,0)
    if p<=31 and m<=10:
        actual=[(u,v) for u in range(1,p) for v in range(1,p)
                if partials(m,p,1,u,v)==(0,0,0,0)]
        expected=[(u,s0*pow(pow(u,m-1,p),-1,p)%p) for u in us]
        assert sorted(actual)==sorted(expected)
    # The local derivative of phi(s)=1+s+cu*s^m is zero at s0;
    # its second derivative is -(m-1)/s0 !=0 modulo p.
    cu=(-mod_inverse(m*pow(s0,m-1,p),p))%p
    assert (1+s0+cu*pow(s0,m,p))%p == 0
    assert (1+m*cu*pow(s0,m-1,p))%p == 0
    assert (m*(m-1)*cu*pow(s0,m-2,p))%p !=0
    assert (N0*(q-1))%2==0
    genus=(N0-1)//2
    assert m*(m-1)//2-N0*(q-1)//2==genus
    assert N0*q == N
    return (m,p,N,q,N0,genus,len(us))


if __name__=='__main__':
    rows=[]
    for m in range(2,46):
        N=m*m-m+1
        for p,q in prime_factors(N):
            rows.append(verify(m,p))
    assert any(m==3 and p==7 and n0==1 and g==0 for m,p,N,q,n0,g,s in rows)
    assert any(m==8 and p==19 and n0==3 and g==1 for m,p,N,q,n0,g,s in rows)
    assert any(m==8 and p==3 and n0==19 and g==9 for m,p,N,q,n0,g,s in rows)
    assert any(m==2 and p==3 and n0==1 for m,p,N,q,n0,g,s in rows)
    assert any(m==31 and p==7 and q==49 and n0==19 for m,p,N,q,n0,g,s in rows)
    print('VERIFY_OK instances=%d m_range=2..45 examples=%s' %
          (len(rows), [r for r in rows if r[0] in (2,3,5,8)]))
