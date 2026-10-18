"""Exact rational checks for inscribed ellipsoids of two-layer Boolean polytopes.

Run with Python 3 (standard library only). This finite verifier checks specified
matrix identities, supporting halfspaces, and John contact certificates. The
proof for every dimension is a separate analytic argument.
"""
from fractions import Fraction as F
from math import isqrt


def verify(n, k):
    assert 3 <= n and 1 <= k < n
    ell = min(k, n-k)
    u = F(ell*ell, n*(n+1))
    v = F(k*k, n*(n+1)**2)
    t = F(k, n+1)
    c = [t]*n
    Q = [[(u if i == j else F(0)) + (v-u)/n
          for j in range(n)] for i in range(n)]
    assert all(Q[i][i] > 0 for i in range(n))
    assert u > 0 and v > 0
    def quad(a):
        z=sum(a)
        return u*sum(x*x for x in a)+(v-u)*z*z/n
    lower_margin = t*t - quad([F(int(j == 0)) for j in range(n)])
    a = [F(1 - (k if i == 0 else 0)) for i in range(n)]
    angled_margin = ((n-k)*t)**2 - quad(a)
    assert lower_margin >= 0 and angled_margin >= 0
    assert lower_margin == 0 if 2*k <= n else lower_margin > 0
    assert angled_margin == 0 if 2*k >= n else angled_margin > 0
    assert (k-n*t)**2 == quad([F(1)]*n)
    p0 = [F(k,n)]*n
    contacts = [p0]
    for i in range(n):
        if 2*k <= n:
            p = [F(0) if j == i else F(k,n) for j in range(n)]
        else:
            p = [F(n-1,n) if j == i else F(k-1,n) for j in range(n)]
        contacts.append(p)
    for idx,p in enumerate(contacts):
        s = sum(p)
        assert all(x >= 0 for x in p)
        assert all(k*x <= s for x in p)
        assert s <= k
        if idx == 0:
            assert s == k
        elif 2*k <= n:
            assert p[idx-1] == 0
        else:
            assert k*p[idx-1] == s
    dd = [[x-t for x in p] for p in contacts]
    # Each contact lies on the proposed ellipsoid, not just on its facet.
    for d in dd:
        sd=sum(d)
        norm_sq=(sum(x*x for x in d)-sd*sd/n)/u+sd*sd/(n*v)
        assert norm_sq == 1
    # Contact point for each supporting hyperplane is unique by strict convexity.
    # Outward top normal is +1; active lower normal is -e_i;
    # active oblique normal is k e_i - 1.
    for i,p in enumerate(contacts):
        if i==0:
            normal=[F(1)]*n
            denom=F(k,n+1)
        elif 2*k<=n:
            normal=[F(-int(j==i-1)) for j in range(n)]
            denom=t
        else:
            normal=[F(k*int(j==i-1)-1) for j in range(n)]
            denom=(n-k)*t
        zn=sum(normal)
        assert all(dd[i][j]==(u*normal[j]+(v-u)*zn/n)/denom for j in range(n))
    assert all(sum(d[i] for d in dd) == 0 for i in range(n))
    factor = F(n,n+1)
    for i in range(n):
        for j in range(n):
            assert factor*sum(d[i]*d[j] for d in dd) == Q[i][j]
    det = u**(n-1)*v
    assert det == F(k*k*ell**(2*n-2), n**n*(n+1)**(n+1))
    assert (u==v) == (k>n/2 and isqrt(n+1)**2==n+1 and k==n+1-isqrt(n+1))
    return (lower_margin, angled_margin)


def main():
    count=0
    both=0
    spherical=[]
    for n in range(3,26):
        for k in range(1,n):
            m0,m1=verify(n,k)
            count+=1
            both+=(m0==0 and m1==0)
            if n+1==isqrt(n+1)**2 and k==n+1-isqrt(n+1):
                spherical.append((n,k))
    print('PASS:',count,'exact dimension/rank profiles;',both,'double-contact transitions')
    print('spherical profiles:',spherical)
    print('All support inequalities, n+1 contact points, moment identities, determinants, and sphere criteria passed.')

if __name__=='__main__':
    main()
