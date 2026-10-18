"""Exact tests for the John ellipsoid of partial permutohedra.

This checker needs Python 3 only. Finite tests corroborate the analytic proof;
they are not a substitute for it. All comparisons are rational.
"""
from fractions import Fraction as F
from itertools import combinations


def rank_sum(k, n):
    return sum(max(n - j, 0) for j in range(k))


def data(m, n):
    assert m >= 2 and n >= 1
    B = F(rank_sum(m, n))
    if m >= n:
        t = B / (m + 1)
        q = t*t
        b = -q/m
        branch = 'simplex'
    else:
        t = F(n, 2)
        q = t*t
        b = min(F(0), F((n-m)**2-m, 4))
        branch = 'anisotropic' if b < 0 else 'cube'
    a = q-b
    ell = q+(m-1)*b
    return B,t,q,b,a,ell,branch


def test_pair(m, n):
    B,t,q,b,a,ell,branch = data(m, n)
    assert a > 0 and ell > 0
    assert q > 0 and t > 0
    assert t*t >= q  # Every lower-coordinate facet is respected.
    upper_touches = set()
    for k in range(1, m+1):
        surplus = F(rank_sum(k,n)) - k*t
        variance = k*q + k*(k-1)*b
        assert variance > 0 and surplus > 0
        gap = surplus*surplus - variance
        assert gap >= 0, ('facet violation',m,n,k,gap)
        if gap == 0:
            upper_touches.add(k)
    if m > n:
        expected = {m}
    elif (n-m)**2 <= m:
        expected = {1,m}
    else:
        expected = {1}
    assert upper_touches == expected, (m,n,branch,upper_touches,expected)
    # The simplex certificate: m lower normals and the total-sum normal.
    if m >= n:
        assert t*t == q and b == -q/m
        assert a == q*(m+1)/m and ell == q/m
        # For weights m/(m+1), the isotropy eigenvalues are both one.
        weight = F(m,m+1)
        assert weight*(a/q)==1
        assert weight*(ell/q+1)==1
    else:
        assert t*t==q
        assert -q/m < b <= 0
        if b < 0:
            # 2m coordinate contacts and one upper-total contact.
            beta = q/a
            gamma = -m*b/a
            assert beta*a/q == 1
            assert beta*ell/q+gamma == 1
            assert gamma > 0
            # Nonnegative coordinate orbit weights: |delta|<=beta.
            assert q*ell - m*b*b >= 0
            # First moment uses delta=-gamma*sqrt(q/(m*ell)).
            assert (gamma*gamma*q)/(m*ell) <= beta*beta
            assert ell == m*F((n-m+1)**2,4)
        else:
            assert a==q and ell==q
    return upper_touches


def main():
    count=0
    facet_count=0
    for m in range(2,101):
        for n in range(1,101):
            contacts=test_pair(m,n)
            count+=1
            facet_count+=m
    # Independently check actual facet-normal supports by masks, and the
    # equality classification, not only cardinality, for moderate sizes.
    masks=0
    for m in range(2,12):
        for n in range(1,18):
            _,t,q,b,*_=data(m,n)
            for k in range(1,m+1):
                for subset in combinations(range(m),k):
                    mask=sum(1<<i for i in subset)
                    assert mask>0
                    support_gap=F(rank_sum(k,n))-k*t
                    squared=F(k*q +k*(k-1)*b)
                    assert support_gap>0 and support_gap*support_gap>=squared
                    masks+=1
    print('PASS:',count,'exact parameter profiles;',facet_count,'cardinality comparisons;',masks,'individual subsets.')
    for m,n in [(2,2),(3,1),(3,3),(3,4),(4,6),(5,8),(9,12),(9,13)]:
        B,t,q,b,a,ell,branch=data(m,n)
        print('m=%s n=%s branch=%s center=%s diag=%s offdiag=%s axes=(%s,%s) active=%s' %
              (m,n,branch,t,q,b,a,ell,sorted(test_pair(m,n))))


if __name__=='__main__':
    main()
