"""Exact finite-step and numerical checks for two-coordinate randomized least squares.

Python 3.10+ standard library only. The analytical proof, not finite tests,
establishes the all-parameter and asymptotic assertions.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def project(z, a):
    ip = sum(x*y for x, y in zip(z, a))
    return tuple(x - ip*y for x, y in zip(z, a))


def norm2(z):
    return sum(x*x for x in z)


def exact_checks(p, r, s, depth=8):
    assert r*r+s*s == 1 and 0 < r < 1 and 0 < p < 1
    a1, a2 = (F(1), F(0)), (r, s)
    z0 = tuple(a1[i] + 2*a2[i] for i in (0, 1))
    columns = (a1, a2)
    probs = (p, 1-p)
    h = 1-r*r
    xi = ((1-p)*h, p*h)
    mean_xi = p*xi[0] + (1-p)*xi[1]
    state = None
    enumerated = 0
    for k in range(1, depth+1):
        weights = [F(0), F(0)]
        weight_xif = F(0)
        for choices in product((0,1), repeat=k):
            z, w = z0, F(1)
            for j in choices:
                z = project(z, columns[j])
                w *= probs[j]
            val = w*norm2(z)
            weights[choices[-1]] += val
            weight_xif += xi[choices[-1]]*val
            enumerated += 1
        u = tuple(weights)
        if state is not None:
            nxt = (p*(state[0]+r*r*state[1]),
                   (1-p)*(r*r*state[0]+state[1]))
            assert u == nxt, (k, u, nxt)
        total = sum(u)
        assert sum(xi[i]*u[i] for i in range(2)) == weight_xif
        if k < depth:
            # Exact one-step contraction identity, using state recursion.
            next_total = (1-xi[0])*u[0]+(1-xi[1])*u[1]
            cov = weight_xif - mean_xi*total
            assert next_total == (1-mean_xi)*total - cov
        state = u
    return enumerated


def spectral_checks():
    samples = 0
    for ip in range(1,200):
        p=ip/200
        t=4*p*(1-p)
        for ir in range(1,101):
            r=ir/101
            v=r*r
            lam=(1+sqrt(1-t+t*v*v))/2
            average=1-t*(1-v)/2
            gap=lam-average
            assert gap >= -2e-14
            assert gap < 0.125+2e-14
            rhs=(sqrt(1-t+t*v*v)-(1-t+t*v))/2
            assert abs(gap-rhs)<5e-15
            if abs(p-0.5)>1e-8:
                assert gap>0
            else:
                assert abs(gap)<1e-13
            assert abs((1-t+t*v*v)-(1-t+t*v)**2-t*(1-t)*(1-v)**2)<1e-12
            samples+=1
    for denom in (100,1000,10000):
        r=1/denom
        p=0.25
        lam=(1+sqrt((2*p-1)**2+4*p*(1-p)*r**4))/2
        average=1-2*p*(1-p)*(1-r*r)
        assert abs((lam-average)-0.125)<0.4*r*r
    # A nontrivial case: the expected squared-norm ratio has the Perron limit.
    p,r=0.25,0.6
    q=1-p
    states=[p*(1-r*r),q*(1-r*r)]
    lam=(1+sqrt((2*p-1)**2+4*p*q*r**4))/2
    for k in range(160):
        nxt=[p*(states[0]+r*r*states[1]),q*(r*r*states[0]+states[1])]
        states=nxt
    nxt=[p*(states[0]+r*r*states[1]),q*(r*r*states[0]+states[1])]
    assert abs(sum(nxt)/sum(states)-lam)<1e-13
    return samples


def main():
    triples=((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17)))
    ps=(F(1,4),F(2,5),F(1,2),F(3,4),F(1,7))
    checked=0
    for r,s in triples:
        for p in ps:
            checked+=exact_checks(p,r,s)
    grid=spectral_checks()
    print(f"VERIFY_OK exact_enumerated_paths={checked} spectral_grid={grid} sharp_supremum=1/8")


if __name__ == "__main__":
    main()
