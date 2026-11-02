"""Reproducibility checks for the central-section side-count law of right regular pentagonal prisms.

Only standard-library Python is required. Independent edge crossing counts are
compared against closed-form probabilities at three different prism heights.
"""
from math import sin, cos, pi, sqrt, asin
from random import Random

ALPHA = pi/5
R = 1.0


def exact_probabilities(q):
    assert q > 0
    def G(t): return asin(sin(t)/sqrt(1+q*q))
    c = 2/ALPHA
    A0 = c*G(ALPHA/2)
    A3 = c*(G(ALPHA)-G(ALPHA/2))
    A2 = c*(G(3*ALPHA/2)-G(ALPHA))
    A1 = c*(G(2*ALPHA)-G(3*ALPHA/2))
    A4 = c*(G(5*ALPHA/2)-G(2*ALPHA))
    probs = {4: A4, 5: 1-A0+A1-A4,
             6: A0-A3+A2-A1, 7: A3-A2}
    assert all(0 < p < 1 for p in probs.values())
    assert abs(sum(probs.values())-1) < 1.e-13
    return probs


def edge_count(normal, h):
    vertices = [(cos(2*pi*j/5),sin(2*pi*j/5),z*h)
                for z in (-1,1) for j in range(5)]
    edges = []
    for j in range(5):
        edges.extend([(j,(j+1)%5), (j+5,(j+1)%5+5), (j,j+5)])
    signs = [sum(x*y for x,y in zip(v,normal)) for v in vertices]
    # Generic section vertices are exactly the transversely crossed edges.
    return sum(signs[a]*signs[b] < 0 for a,b in edges)


def observed_distribution(q, samples=180000, seed=743):
    rng = Random(seed)
    counts={4:0,5:0,6:0,7:0}
    for _ in range(samples):
        azimuth = 2*pi*rng.random()
        z = rng.random()     # upper hemisphere: |normal_z| uniform [0,1]
        rho = sqrt(1-z*z)
        n = (rho*cos(azimuth),rho*sin(azimuth),z)
        s = edge_count(n, q)
        assert s in counts, (q,s,n)
        counts[s]+=1
    return {k:v/samples for k,v in counts.items()}


def independent_quadrature(q, subdivisions=20000):
    # Numerically integrate the conditional edge count from direct vertex
    # projection thresholds, without using any antiderivative.
    out = {4:0.,5:0.,6:0.,7:0.}
    dphi=ALPHA/(2*subdivisions)
    for it in range(subdivisions):
        phi=(it+0.5)*dphi
        vals=[cos(2*pi*j/5-phi) for j in range(5)]
        boundaries=sorted([0.]+[abs(x) for x in vals]+[float('inf')])
        for l,r in zip(boundaries[:-1],boundaries[1:]):
            k=(l+r)/2 if r != float('inf') else l+1.0
            p=sum(x>k for x in vals)
            m=sum(x < -k for x in vals)
            N=5-p-m+2*(int(p>0)+int(m>0))
            if N not in out: raise ValueError((q,phi,k,N))
            def F(t): return 1.0 if t==float('inf') else t/sqrt(q*q+t*t)
            out[N]+=F(r)-F(l)
    return {k:v/subdivisions for k,v in out.items()}


if __name__=='__main__':
    for q in (0.23, sin(ALPHA), 1.7):
        exact = exact_probabilities(q)
        quadrature = independent_quadrature(q)
        simulated = observed_distribution(q)
        err_quad=max(abs(exact[k]-quadrature[k]) for k in exact)
        err_mc=max(abs(exact[k]-simulated[k]) for k in exact)
        print(f'q={q:.12f}', 'exact', {k:round(v,12) for k,v in exact.items()})
        print('quadrature max error', f'{err_quad:.3g}', 'MC max error', f'{err_mc:.5g}')
        assert err_quad < 2.e-8, err_quad
        assert err_mc < 0.008, err_mc
    print('PASS: independent edge-count simulation and direct conditional quadrature')
