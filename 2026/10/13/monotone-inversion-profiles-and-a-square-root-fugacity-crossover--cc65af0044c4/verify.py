"""Standalone exact tests for inversion ordering in fixed-point-weighted involutions.
No external packages are required. The checks are finite confirmations, not the proof.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from math import comb, exp, lgamma, log, sqrt

@lru_cache(None)
def pairings(points):
    if not points:
        return ((),)
    x, tail = points[0], points[1:]
    out = [((x, x),) + q for q in pairings(tail)]
    for j, y in enumerate(tail):
        remain = tail[:j] + tail[j+1:]
        out.extend(((x, y),) + q for q in pairings(remain))
    return tuple(out)

def image(pairs, n):
    out = list(range(n))
    for a, b in pairs:
        out[a], out[b] = b, a
    return tuple(out)

def inversions(p):
    return sum(p[a] > p[b] for a in range(len(p)) for b in range(a+1, len(p)))

def mean_by_bias(rows, theta):
    numer = sum(Fraction(theta)**f * k * count for (f,k), count in rows.items())
    denom = sum(Fraction(theta)**f * count for (f,k), count in rows.items())
    return numer / denom

def exact_tests():
    total_objects = 0
    edges_tested = 0
    weighted_tests = 0
    for n in range(2, 11):
        inv_rows = defaultdict(list)
        inv_count = Counter()
        rows = Counter()
        edge_preimages = Counter()
        for pairing in pairings(tuple(range(n))):
            p = image(pairing, n)
            m = sum(a != b for a, b in pairing)
            f = n-2*m
            k = inversions(p)
            inv_rows[m].append(k)
            rows[(f, k)] += 1
            total_objects += 1
            fixed = [i for i, x in enumerate(p) if i == x]
            for index_a, a in enumerate(fixed):
                for b in fixed[index_a+1:]:
                    q = list(p)
                    q[a], q[b] = b, a
                    target = tuple(q)
                    actual = inversions(q)-k
                    asserted = 1+2*sum(a<p[c]<b for c in range(a+1,b))
                    assert actual == asserted and actual >= 1, (n, p, a, b, actual)
                    edge_preimages[(m+1, target)] += 1
                    edges_tested += 1
        for m, values in inv_rows.items():
            f = n-2*m
            actual = Fraction(sum(values), len(values))
            expected = Fraction((n-f)*(3*n+f), 12)
            assert actual == expected, (n, f, actual, expected)
            assert len(values) == comb(n,2*m) * (1 if m == 0 else __import__('math').factorial(2*m)//(2**m * __import__('math').factorial(m)))
            if m>0:
                assert all(cnt == m for (j,_),cnt in edge_preimages.items() if j == m), (n,m)
        for m in range(len(inv_rows)-1):
            left, right = inv_rows[m], inv_rows[m+1]
            for k in range(n*(n-1)//2+1):
                assert Fraction(sum(x>=k for x in left),len(left)) <= Fraction(sum(x>=k for x in right),len(right))
        for theta in [Fraction(1,2), Fraction(1), Fraction(2), Fraction(3)]:
            weights = defaultdict(Fraction)
            Z = Fraction(0)
            EF = EI = EFI = Fraction(0)
            for (f,k), cnt in rows.items():
                w = theta**f * cnt
                Z += w; EF += f*w; EI += k*w; EFI += f*k*w
            covariance = EFI/Z - EF*EI/(Z*Z)
            assert covariance < 0, (n, theta, covariance)
            weighted_tests+=1
        assert mean_by_bias(rows,Fraction(1,2)) > mean_by_bias(rows,1) > mean_by_bias(rows,2) > mean_by_bias(rows,3)
        print('n=',n,'involutions=',sum(map(len,inv_rows.values())),'m_classes=',len(inv_rows),'PASS')
    print('EXACT_OK', 'involutions=',total_objects,'increment_edges=',edges_tested,'weighted_covariance_checks=',weighted_tests)

def tilted_density(n, theta):
    fvalues = list(range(n%2,n+1,2))
    logs = [lgamma(n+1) + f*log(theta)-lgamma(f+1) -(n-f)/2*log(2)-lgamma((n-f)//2+1) for f in fvalues]
    hi=max(logs)
    ww=[exp(v-hi) for v in logs]
    z=sum(ww)
    return sum(f*w for f,w in zip(fvalues,ww))/(n*z), sum((n-f)*(3*n+f)/12*w for f,w in zip(fvalues,ww))/(n*n*z)

def numerical_tests():
    for a in [0.0, 0.25, 1.0, 2.0, 5.0, float('inf')]:
        s = 0.0 if a==0 else 1.0 if a==float('inf') else (sqrt(a**4+4*a*a)-a*a)/2
        h = (1-s)*(3+s)/12
        n=5000
        theta= 1 if a==0 else n*n if a==float('inf') else a*sqrt(n)
        sf,hi=tilted_density(n,theta)
        assert abs(sf-s)<0.018, (a,s,sf)
        assert abs(hi-h)<0.018, (a,h,hi)
        print('a=',a,'s_expected=',round(s,6),'s_exact_mean=',round(sf,6),'inversion_density=',round(hi,6),'PASS')
    print('ASYMPTOTIC_NUMERIC_OK')

if __name__=='__main__':
    exact_tests()
    numerical_tests()
    print('VERIFY_OK')
