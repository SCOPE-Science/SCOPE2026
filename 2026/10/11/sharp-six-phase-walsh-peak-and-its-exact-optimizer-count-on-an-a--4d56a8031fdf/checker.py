"""Exact sixth-root Walsh six-circuit PAPR and projective optimizer count."""
from itertools import product
from collections import Counter

# zeta = exp(pi*i/3) satisfies zeta*zeta = zeta - 1.
ROOTS = ((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))

def norm2(z):
    a,b=z
    return a*a+a*b+b*b

def sample_values(phase):
    z=[ROOTS[t] for t in phase]
    # Physical Walsh samples: 4 independent signs and sixth sign their product.
    vals=[]
    for v in product((-1,1), repeat=4):
        eps=(1,)+v+(v[0]*v[1]*v[2]*v[3],)
        pair=(sum(eps[j]*z[j][0] for j in range(6)),
              sum(eps[j]*z[j][1] for j in range(6)))
        vals.append(norm2(pair))
    return vals

def run():
    # Projective normalization: common sixth-root scalar fixes coefficient zero.
    peaks=Counter()
    first=None
    for tail in product(range(6),repeat=5):
        vals=sample_values((0,)+tail)
        assert sum(vals)==96 # Parseval mean square 6 across 16 samples.
        # The exact fourth-moment identity holds for all unit phases.
        z=[ROOTS[t] for t in (0,)+tail]
        # (a+b*zeta)^2 = (a*a-b*b)+(2*a*b+b*b)*zeta.
        q=(sum(a*a-b*b for a,b in z), sum(2*a*b+b*b for a,b in z))
        assert sum(v*v for v in vals)==16*(60+norm2(q))
        top=max(vals)
        peaks[top]+=1
        if top==12 and first is None:
            first=(0,)+tail
    assert sum(peaks.values()) == 6**5
    assert min(peaks)==12, (min(peaks),peaks)
    assert peaks[12]==480,peaks
    assert first is not None
    example=sample_values((0,1,2,3,4,5))
    assert Counter(example)==Counter({0:4,4:6,12:6}),Counter(example)
    assert sorted(peaks.items()) == [(12,480),(13,320),(16,976),(19,2400),(21,2112),(25,480),(27,320),(28,480),(31,192),(36,16)]
    print('PASS: 7776 normalized vectors; exact optimal peak 12; 480 attaining vectors')
    print('Exact peak histogram:', sorted(peaks.items()))

if __name__=='__main__':
    run()
