"""Exact checks for joint cyclic-simple-chord and crossing counts.

No external packages. Run: python verify.py
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

CHECKS = 0

def check(a, b, message=''):
    global CHECKS
    CHECKS += 1
    assert a == b, (message, a, b)

def odd_double_factorial(n):
    out = 1
    for t in range(1, 2 * n, 2):
        out *= t
    return out

def cycle_matching_count(n, k):
    assert 2 <= n and 0 <= k <= n
    numerator = 2 * n * comb(2 * n - k, k)
    check(numerator % (2 * n - k), 0, 'integrality of cyclic matching number')
    return numerator // (2 * n - k)

def touchard_riordan(n):
    """Coefficients of q^j in the crossing enumerator of matchings on 2n points."""
    if not n:
        return [1]
    d = n * (n - 1) // 2
    numerator = [0] * (d + n + 1)
    for j in range(-n, n + 1):
        exponent = j * (j - 1) // 2
        numerator[exponent] += (-1 if j % 2 else 1) * comb(2 * n, n + j)
    result = [0] * (d + 1)
    for i in range(d + 1):
        result[i] = numerator[i] - sum((-1 if k % 2 else 1) * comb(n,k) * result[i-k] for k in range(1, min(n,i)+1))
    # Convolution with (1-q)^n reproduces the alternating finite numerator.
    reconstruction = [0] * len(numerator)
    for i, coefficient in enumerate(result):
        for k in range(n + 1):
            reconstruction[i+k] += coefficient * comb(n,k) * (-1 if k % 2 else 1)
    check(reconstruction, numerator, 'Touchard-Riordan polynomial division')
    check(sum(result), odd_double_factorial(n), 'normalization')
    check(all(x >= 0 for x in result), True, 'nonnegative crossings polynomial')
    return result

def predicted_joint(n, tr_cache):
    """Dictionary (simple_chords, crossings) -> exact count."""
    out = Counter()
    for k in range(n + 1):
        multiplicity = cycle_matching_count(n,k)
        for x, c in enumerate(tr_cache[n-k]):
            for s in range(k+1):
                out[(s,x)] += multiplicity * c * comb(k,s) * (-1 if (k-s) % 2 else 1)
    return Counter({key:value for key,value in out.items() if value})

def matching_generator(points):
    if not points:
        yield ()
        return
    first = points[0]
    for i in range(1,len(points)):
        second = points[i]
        for tail in matching_generator(points[1:i]+points[i+1:]):
            yield ((first,second),) + tail

def crossing(a,b):
    (i,j),(k,l) = sorted((a,b))
    return (i < k < j < l) or (k < i < l < j)

def actual_joint(n):
    counts = Counter()
    for matching in matching_generator(tuple(range(2*n))):
        s = sum(1 for a,b in matching if b == a+1 or (a == 0 and b == 2*n-1))
        x = sum(crossing(a,b) for a,b in combinations(matching,2))
        counts[s,x] += 1
    return Counter({key:value for key,value in counts.items() if value})

def empirical_moments(n, joint):
    denominator = odd_double_factorial(n)
    es = Fraction(sum(s*c for (s,x),c in joint.items()), denominator)
    ex = Fraction(sum(x*c for (s,x),c in joint.items()), denominator)
    vs = Fraction(sum(s*s*c for (s,x),c in joint.items()), denominator) - es*es
    vx = Fraction(sum(x*x*c for (s,x),c in joint.items()), denominator) - ex*ex
    cov = Fraction(sum(s*x*c for (s,x),c in joint.items()), denominator)-es*ex
    return es,ex,vs,vx,cov

def main():
    tr_cache = {n: touchard_riordan(n) for n in range(14)}
    for n in range(2, 14):
        F = predicted_joint(n,tr_cache)
        check(sum(F.values()), odd_double_factorial(n), 'joint normalization')
        check(all(v>=0 for v in F.values()),True, 'nonnegative joint polynomial')
        es, ex, vs, vx, cov = empirical_moments(n,F)
        check(es, Fraction(2*n,2*n-1), 'mean of simple chords')
        check(ex, Fraction(n*(n-1),6), 'mean of crossings')
        check(vs, Fraction(4*n*(n-1),(2*n-1)**2), 'variance of simple chords')
        check(vx, Fraction(n*(n-1)*(n+3),45), 'variance of crossings')
        check(cov, Fraction(-2*n*(n-1),3*(2*n-1)), 'mixed covariance')
        check(cov*cov, vs*vx*Fraction(5,n+3), 'squared correlation')
        check(cov < 0, True, 'strict negative covariance')
        print(f'n={n:2d}, terms={len(F):4d}, exact covariance={cov}, correlation=-sqrt(5/{n+3})')
    for n in range(2,8):
        formula = predicted_joint(n,tr_cache)
        exact = actual_joint(n)
        check(formula, exact, f'independent exhaustive enumeration of all {(2*n-1)}!! matchings')
        print(f'enumerated n={n}, {sum(exact.values())} matchings, {len(exact)} joint cells')
    # Independent count of matchings in the 2n-cycle for small n.
    for n in range(2,9):
        edges = [(i,(i+1)%(2*n)) for i in range(2*n)]
        for k in range(n+1):
            count = 0
            for chosen in combinations(edges,k):
                v = [t for e in chosen for t in e]
                count += len(set(v)) == len(v)
            check(count, cycle_matching_count(n,k), 'cycle rook numbers')
    print(f'ALL {CHECKS} EXACT ASSERTIONS PASSED')

if __name__ == '__main__':
    main()
