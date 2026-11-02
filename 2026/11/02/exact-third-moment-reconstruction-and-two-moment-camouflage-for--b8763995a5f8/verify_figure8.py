"""Independent exact and numerical checks for two-loop metric-graph distance moments.

Run with Python 3.10+: python verify_figure8.py
No nonstandard dependencies.
"""
from fractions import Fraction as F
from math import comb, sqrt, isclose
from random import Random


def conditional_moment(a, b, order):
    """Integrate conditional laws, before applying any proposed closed form."""
    total = a + b
    # Within one circumference, shortest-distance law is uniform [0, length/2].
    same = sum((h / total) ** 2 * h ** order / (2 ** order * (order + 1))
               for h in (a, b))
    # Across the articulation, independent distances to vertex are uniforms.
    cross_cond = sum(F(comb(order, j), 1) * (a / 2) ** j * (b / 2) ** (order-j)
                     / ((j+1)*(order-j+1)) for j in range(order+1))
    return same + F(2, 1) * a * b / total**2 * cross_cond


def proposed_moments(a, b):
    L = a + b
    c = a*b/L
    mu = (L-c)/4
    return mu, F(4, 3)*mu**2, F(2, 1)*mu**3+c**3/32


def periodic_distance(a, x, y):
    gap = abs(x-y)
    return min(gap, a-gap)


def midpoint_integration(a, b, k, N=240):
    """Independent raw graph-coordinate integration of shortest paths."""
    lengths = [float(a),float(b)]
    total = sum(lengths)
    sums = 0.0
    for i, li in enumerate(lengths):
        for j, lj in enumerate(lengths):
            acc = 0.0
            for u in range(N):
                x=li*(u+0.5)/N
                for v in range(N):
                    y=lj*(v+0.5)/N
                    if i == j:
                        d=periodic_distance(li, x, y)
                    else:
                        d=min(x,li-x)+min(y,lj-y)
                    acc += d**k
            sums += li*lj*acc/N**2
    return sums / total**2


def inverse(mu, omega):
    # Real cube root; the admissibility inequality is checked separately.
    c=(32*(omega-2*mu**3))**(1/3)
    L=4*mu+c
    disc=max(0.0,L*(L-4*c))
    return ((L-sqrt(disc))/2, (L+sqrt(disc))/2)


def test():
    pairs = [(F(1), F(1)), (F(1),F(5)), (F(2),F(3)),
             (F(3,2),F(9,7)), (F(1,4), F(11,5)),
             (F(7,3), F(19,6))]
    exact_checks = 0
    for a,b in pairs:
        explicit=proposed_moments(a,b)
        for k in (1,2,3):
            assert conditional_moment(a,b,k)==explicit[k-1]
            exact_checks += 1
        mu,nu,w=explicit
        L=a+b
        c=a*b/L
        assert nu==F(4,3)*mu**2
        assert 32*(w-2*mu**3)==c**3
        assert F(0)<c<=F(4,3)*mu
        exact_checks += 3
        ai,bi=inverse(float(mu),float(w))
        assert isclose(ai,float(min(a,b)),rel_tol=1e-6,abs_tol=1e-6)
        assert isclose(bi,float(max(a,b)),rel_tol=1e-6,abs_tol=1e-6)
        exact_checks += 2
    numeric_checks=0
    for a,b in ((1.,1.),(1.,5.),(2.,3.)):
        for k in (1,2,3):
            observed=midpoint_integration(a,b,k,N=180)
            expected=float(proposed_moments(F(str(a)),F(str(b)))[k-1])
            assert abs(observed-expected) < 0.00045*max(1., expected),(a,b,k,observed,expected)
            numeric_checks+=1
    # Stochastic independent sampler of the metric graph coordinates.
    rng=Random(20261031)
    a,b=1.25,2.75
    L=a+b
    moment_sums=[0.,0.,0.]
    n=220000
    for _ in range(n):
        r=rng.random()*L
        s=rng.random()*L
        if r<a and s<a:
            d=periodic_distance(a,r,s)
        elif r>=a and s>=a:
            d=periodic_distance(b,r-a,s-a)
        else:
            x=r if r<a else s
            y=s-a if s>=a else r-a
            d=min(x,a-x)+min(y,b-y)
        moment_sums[0]+=d
        moment_sums[1]+=d*d
        moment_sums[2]+=d*d*d
    target=proposed_moments(F(5,4),F(11,4))
    for k in range(3):
        assert abs(moment_sums[k]/n-float(target[k]))<0.016*float(target[k])
        numeric_checks+=1
    # Exact cubic upper boundary and its equality geometry.
    for c in [F(1,10),F(1,2),F(4,3)]:
        mu=F(1)
        w=2*mu**3+c**3/32
        assert 2*mu**3<w<=F(56,27)*mu**3
        L=4*mu+c
        assert L*(L-4*c)>=0
        exact_checks+=2
    print(f'VERIFY_OK {exact_checks} exact rational equalities/inequalities, '
          f'{numeric_checks} independently integrated or sampled tests')

if __name__ == '__main__':
    test()
