"""Exact finite checks for the section-count law of three-dimensional parallelotopes.

Run with Python 3 standard library: python verify.py
The analytic proof for all real projection magnitudes is given separately.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def theoretical(a, b, c):
    a, b, c = sorted((F(a), F(b), F(c)), reverse=True)
    assert a > 0 and b >= c >= 0
    w = a + b + c
    if a >= b + c:
        return {3: 2*c/w, 4: 1-4*c/w, 5: 2*c/w, 6: F(0)}
    return {3: 2*c/w, 4: 2*(b-c)/w,
            5: 2*(a-b)/w, 6: (b+c-a)/w}


def intersected_edges(a, b, c, t):
    """Count cube edges with opposite signed vertex levels relative to t."""
    weights = (F(a), F(b), F(c))
    count = 0
    for coordinate in range(3):
        rest = tuple(j for j in range(3) if j != coordinate)
        for s0, s1 in product((-1, 1), repeat=2):
            center = weights[rest[0]]*s0 + weights[rest[1]]*s1
            if center-weights[coordinate] < t < center+weights[coordinate]:
                count += 1
    return count


def geometric_law(a, b, c):
    a, b, c = map(F, (a, b, c))
    w = a+b+c
    heights = sorted(set(s*a+t*b+v*c for s,t,v in product((-1,1),repeat=3)))
    out = {k:F(0) for k in (3,4,5,6)}
    for low, high in zip(heights, heights[1:]):
        n = intersected_edges(a,b,c,(low+high)/2)
        assert n in out, (a,b,c,low,high,n)
        out[n] += (high-low)/(2*w)
    return out


def recovered(law):
    """Unique normalized sorted magnitudes when the hexagon event is possible."""
    p3,p4,p5,p6 = (law[k] for k in (3,4,5,6))
    assert p6>0
    return ((p3+p4+p5)/2, (p3+p4)/2, p3/2)


def run():
    examples = [(1,1,1),(2,1,1),(3,2,1),(7,3,1),
                (5,4,2),(4,4,3),(2,2,1),(5,5,5),
                (4,1,0),(5,0,0),(10,5,4)]
    rng = Random(519211)
    for _ in range(900):
        examples.append(tuple(rng.randint(1,100) for _ in range(3)))
    for raw in examples:
        a,b,c = sorted(raw,reverse=True)
        predicted = theoretical(a,b,c)
        obtained = geometric_law(a,b,c)
        assert predicted == obtained,(raw,predicted,obtained)
        assert sum(predicted.values()) == 1
        assert sum(k*v for k,v in predicted.items()) == 4
        assert F(0)<=sum((k-4)**2*v for k,v in predicted.items())<=2
        if predicted[6]:
            assert recovered(predicted) == tuple(F(x,a+b+c) for x in (a,b,c))

    # Exact law realization at rational points in the entire mean-four simplex.
    for i in range(22):
        for j in range(22-i):
            # Probability mixture of the three extreme laws.
            u,v = F(i,21),F(j,21)
            z = 1-u-v
            law={3:v/2+2*z/3,4:u,5:v/2,6:z/3}
            if law[6]:
                a,b,c = recovered(law)
                assert theoretical(a,b,c)==law
                assert geometric_law(a,b,c)==law
            elif law[3]:
                c=law[3]/2
                # Select the boundary representative a=b+c.
                b=F(1,2)-c
                a=F(1,2)
                assert theoretical(a,b,c)==law
            else:
                assert law=={3:F(0),4:F(1),5:F(0),6:F(0)}
                assert geometric_law(1,0,0)==law

    # Noninjective law for two different sorted triples.
    assert theoretical(F(3,5),F(1,5),F(1,5)) == theoretical(
        F(1,2),F(3,10),F(1,5))
    # Endpoint of noninjective sector has only one realization.
    assert theoretical(2,1,1)=={3:F(1,2),4:F(0),5:F(1,2),6:F(0)}
    # Unique maximum variance at equal magnitudes.
    assert sum((k-4)**2*p for k,p in theoretical(1,1,1).items()) == 2
    print('EDGE_CROSSINGS_AND_ALL_LAW_REGIMES_PASSED')
    print('EXACT_MEAN_AND_VARIANCE_BOUNDS_PASSED')
    print('SIMPLEX_REALIZATION_AND_INVERSE_TESTS_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    run()
