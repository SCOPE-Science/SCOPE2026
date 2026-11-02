"""Exact-rational tests of a two-corner finite-face flux identity.

Usage: python3 verify.py
All computations use standard-library Fraction; numerical tests supplement
rather than replace the analytic continuum proof in RESULT.md.
"""
from fractions import Fraction as Q
from random import Random


def scalar_piecewise_integral(t, L, v, p0, q0, dp, dq, phi):
    """Integrate the transported states over y by exact interval partition."""
    a = v * t
    b = L - v * t
    edges = sorted({Q(0), a, b, L})
    total = Q(0)
    for low, high in zip(edges, edges[1:]):
        if low == high:
            continue
        mid = (low + high) / 2
        p = p0 + (dp if mid < a else 0)
        q = q0 + (dq if mid > b else 0)
        total += (high-low) * phi(p, q)
    return total


def integrated_direct(H, L, v, p0, q0, dp, dq, phi):
    """Independent direct integration of exact piecewise-contact solution."""
    assert 0 <= H <= L/v
    cutoff = L/(2*v)
    times = [Q(0)]
    if Q(0) < cutoff < H:
        times.append(cutoff)
    times.append(H)
    out = Q(0)
    for aa, bb in zip(times, times[1:]):
        out += (bb-aa)*(scalar_piecewise_integral(aa,L,v,p0,q0,dp,dq,phi)
                        +scalar_piecewise_integral(bb,L,v,p0,q0,dp,dq,phi))/2
    return out


def formula(H, L, v, p0, q0, dp, dq, phi):
    f00 = phi(p0,q0)
    f10 = phi(p0+dp,q0)
    f01 = phi(p0,q0+dq)
    f11 = phi(p0+dp,q0+dq)
    mix = f11-f10-f01+f00
    isolated = L*H*f00 +v*H*H*(f10+f01-2*f00)/2
    correction = v*max(Q(0),H-L/(2*v))**2*mix
    return isolated+correction, isolated, correction, mix


def test():
    rng=Random(271828)
    families = [
        lambda p,q:p*q,
        lambda p,q:p*p*q,
        lambda p,q:p*q*q,
        lambda p,q:2*p+3*q,
        lambda p,q:p*p+q*q*q,
        lambda p,q:p*q+p*p*q*q,
        lambda p,q:3+p+q+4*p*q+2*p*p*q,
    ]
    tests=0
    for _ in range(250):
        L=Q(rng.randint(1,5),rng.randint(1,4))
        v=Q(rng.randint(1,5),rng.randint(1,4))
        p0=Q(rng.randint(1,7),rng.randint(1,5))
        q0=Q(rng.randint(1,7),rng.randint(1,5))
        dp=Q(rng.randint(1,5),rng.randint(1,5))
        dq=Q(rng.randint(1,5),rng.randint(1,5))
        for frac in [Q(0),Q(1,4),Q(1,2),Q(3,5),Q(9,10),Q(1)]:
            H=frac*L/v
            for phi in families:
                actual=integrated_direct(H,L,v,p0,q0,dp,dq,phi)
                predicted,isolated,correction,mix=formula(H,L,v,p0,q0,dp,dq,phi)
                assert actual==predicted,(actual,predicted)
                if H<=L/(2*v) or mix==0: assert correction==0
                if H>L/(2*v) and mix!=0: assert correction!=0
                tests+=1
    eps=Q(1,10)
    L=v=p0=q0=dp=dq=Q(1)
    H=Q(9,10)
    phi=lambda p,q:p*q
    actual=eps*integrated_direct(H,L,v,p0,q0,dp,dq,phi)
    predicted,isolated,correction,mix=formula(H,L,v,p0,q0,dp,dq,phi)
    assert actual==Q(187,1000)
    assert eps*isolated==Q(171,1000)
    assert eps*correction==Q(16,1000)
    assert mix==1
    # Exact square of the admissible characteristic Courant upper bound.
    assert H*H*(1+eps*eps*4*4)<1
    print(f'PASS: {tests} independent direct rational integrations; sharp example')

if __name__ == '__main__':
    test()
