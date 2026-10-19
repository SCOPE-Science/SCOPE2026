"""Exact four-point STFT support sanity checks (Gaussian integer inputs).

Finite enumeration is a test, not the proof for all complex coefficients.
"""
from itertools import product
from collections import Counter

ROOT = (1, 1j, -1, -1j)


def ft(row):
    return tuple(sum(row[n] * ROOT[(-n * ell) % 4] for n in range(4)) for ell in range(4))


def rows(f, g):
    return [ft(tuple(f[n] * complex(g[(n-k)%4]).conjugate() for n in range(4))) for k in range(4)]


def count_support(f, g):
    return sum(z != 0 for r in rows(f, g) for z in r)


def classified_six(f, g):
    sf = [k for k,z in enumerate(f) if z]
    sg = [k for k,z in enumerate(g) if z]
    if len(sf) == len(sg) == 2:
        if sf[1]-sf[0] != 2 or sg[1]-sg[0] != 2:
            return False, 'sparse'
        a, b = f[sf[0]], f[sf[1]]
        c, d = g[sg[0]], g[sg[1]]
        t1 = a * c.conjugate() in (b * d.conjugate(), -b * d.conjugate())
        t2 = a * d.conjugate() in (b * c.conjugate(), -b * c.conjugate())
        return t1 != t2, 'sparse'
    if len(sf) == len(sg) == 4:
        rr=rows(f,g)
        for k0 in range(4):
            if sum(z!=0 for z in rr[k0]) != 1 or sum(z!=0 for z in rr[(k0+2)%4]) != 1:
                continue
            gg=[g[(n-k0)%4] for n in range(4)]
            u,v=gg[0],gg[1]
            for eps in (1,-1):
                for r in (0,1):
                    if gg[2]==eps*u and gg[3]==eps*((-1)**r)*v:
                        return (v/u)**4 != (-1)**r, 'full'
        return False, 'full'
    return False, 'other'


def run():
    assert count_support((1,0,2,0),(1,0,2,0)) == 6
    assert count_support((1,1,1,-1),(1,1,1,-1)) == 6
    counter=Counter()
    strata=Counter()
    tested=0
    for f in product((0,1,2,-1), repeat=4):
        if not any(f):
            continue
        f=tuple(complex(z) for z in f)
        for g in product((0,1,2,-1), repeat=4):
            if not any(g):
                continue
            g=tuple(complex(z) for z in g)
            support=count_support(f,g)
            counter[support]+=1
            tested+=1
            assert support >= 4 and support != 5
            result, stratum=classified_six(f,g)
            assert result == (support==6), (f,g,support,stratum)
            if support==6:
                strata[stratum]+=1
    assert tested == 255*255
    assert strata == {'sparse': 64, 'full':80}, strata
    print('PASS: exact arithmetic on %d nonzero signal/window pairs' % tested)
    print('PASS: no STFT support cardinality five')
    print('PASS: every and only support-six pair matches the structural classification')
    print('support distribution:', sorted(counter.items()))
    print('support-six strata:', sorted(strata.items()))
    print('PASS: both support-six witness pairs')

if __name__ == '__main__':
    run()
