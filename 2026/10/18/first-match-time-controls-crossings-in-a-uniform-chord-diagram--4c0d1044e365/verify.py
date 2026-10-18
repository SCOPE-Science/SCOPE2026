"""Exact finite-model checks for first-closure regression in uniform chord matchings."""
from fractions import Fraction
from functools import lru_cache
from collections import defaultdict
from math import comb

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    first = vertices[0]
    return tuple(((first, vertices[j]),) + rem
                 for j in range(1, len(vertices))
                 for rem in matchings(vertices[1:j] + vertices[j+1:]))

def crossings(matching):
    return sum(a < c < b < d or c < a < d < b
               for i, (a, b) in enumerate(matching)
               for c, d in matching[i+1:])

def conditional_regression(n, t):
    return Fraction(2*n*n-6*n+t*t+t-2, 12)

def run():
    checks = 0
    for n in range(2, 8):
        samples = matchings(tuple(range(1, 2*n+1)))
        tab = defaultdict(lambda: [0, 0])
        total_c = total_c2 = total_t = total_t2 = total_ct = 0
        for M in samples:
            t = min(b for a, b in M)
            c = crossings(M)
            tab[t][0] += c
            tab[t][1] += 1
            total_c += c
            total_c2 += c*c
            total_t += t
            total_t2 += t*t
            total_ct += c*t
        N = len(samples)
        assert N == (2*n-1)*len(matchings(tuple(range(1, 2*n-1))))
        checks += 1
        for t in range(2, n+2):
            s, z = tab[t]
            assert z > 0
            assert Fraction(s, z) == conditional_regression(n, t), (n,t)
            assert (conditional_regression(n,t) - Fraction(n*(n-1), 6)
                    == Fraction(t*t+t-4*n-2, 12))
            checks += 2
        mean = Fraction(total_c, N)
        var = Fraction(total_c2, N)-mean*mean
        assert mean == Fraction(n*(n-1), 6)
        assert var == Fraction(n*(n-1)*(n+3),45)
        assert Fraction(total_t2+total_t, N) == 4*n+2
        c_t_cov = Fraction(total_ct, N)-mean*Fraction(total_t,N)
        et = Fraction(total_t, N)
        et2 = Fraction(total_t2, N)
        et3 = Fraction(sum(t*t*t*z for t, (_, z) in tab.items()), N)
        assert c_t_cov == (et3-et2*et+et2-et*et)/12
        assert c_t_cov > 0
        checks += 5
    for n in range(2, 300):
        q = [conditional_regression(n,t) for t in range(2,n+2)]
        assert all(q[i+1]-q[i] == Fraction(i+3,6) for i in range(len(q)-1))
        checks += 1
    print('PASS',checks,'exact assertions; complete enumeration through seven chords')
if __name__=='__main__':run()
