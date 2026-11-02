"""Independent finite-arithmetic and simulation checks for two-point SGLM examples.

The theorem and its infinite-horizon moment assertions require mathematical proof;
this script checks algebraic identities, transition boundaries, and finite trials.
"""
import math
import random
from fractions import Fraction


def bounds(q):
    assert 1 / math.sqrt(2) < q < 1
    r = math.sqrt(2 * q*q - 1)
    return (2/(1+q*q), (1-r)/(1-q*q),
            (1+r)/(1-q*q), 2/(1-q*q))


def product(t, q):
    return (1-(1+q)*t)*(1-(1-q)*t)


def finite_variance(h, lam, sigma):
    return (2-h*lam)/(2*lam-h*(lam*lam+sigma*sigma))


def checks():
    n = 0
    for q in [.71, .75, .8, .9, .99]:
        ms, low, high, up = bounds(q)
        assert 0 < ms < low < high < up
        n += 1
        for j in range(1000):
            t = up*(j+.5)/1000
            stable = (t < low or high < t < up)
            assert (abs(product(t,q)) < 1) == stable
            n += 1
        assert math.isclose(product(low,q), -1, rel_tol=0, abs_tol=1e-10)
        assert math.isclose(product(high,q), -1, rel_tol=0, abs_tol=1e-10)
        assert math.isclose(product(up,q), 1, rel_tol=0, abs_tol=1e-10)
        n += 3
    # The reset family is a genuinely continuous parameter curve.
    for q in [.71, .75, .8, .9]:
        h=1/(1-q)
        r=2*q/(1-q)
        ms, low, high, up = bounds(q)
        assert high < h < up
        assert math.isclose(product(h,q),0,rel_tol=0,abs_tol=3e-13)
        for k in range(35):
            v_y=(h/2)*(2*r/(r+1)*r**(2*k)-(r-1)/(r+1))
            v_z=v_y+h/2
            expected=h/(r+1)*(r**(2*k+1)+1)
            assert math.isclose(v_z,expected,rel_tol=1e-12,abs_tol=1e-12)
            if k:
                old_v_y=(h/2)*(2*r/(r+1)*r**(2*(k-1))-(r-1)/(r+1))
                assert math.isclose(v_y,r*r*old_v_y+(r-1)**2*(h/2),rel_tol=1e-12,abs_tol=1e-12)
            n += 2
        n += 2
    a = Fraction(5, 2)
    A_low = Fraction(1) - 5 * Fraction(1,5)
    A_high = Fraction(1) - 5 * Fraction(9,5)
    assert (A_low, A_high) == (0,-8)
    n += 1
    for k in range(35):
        vy = a * (Fraction(16,9)*64**k-Fraction(7,9))
        vz = vy+a
        assert vz == Fraction(5,9)*(8*64**k+1)
        if k:
            prev = a * (Fraction(16,9)*64**(k-1)-Fraction(7,9))
            assert vy == 64*prev+49*a
        n += 2
    for p in [0.1, .2, 1/3, .4, 1, 2]:
        expected = p < 1/3
        assert (8**p / 2 < 1) == expected
        n += 1
    # The actual independent noise at adjacent SGLM steps is reused.
    rng = random.Random(3721)
    for _ in range(10000):
        h = .4
        old_y = rng.uniform(-5, 5)
        old_chi = rng.gauss(0,1)
        new_chi = rng.gauss(0,1)
        a0 = 1-h*(1+rng.choice([-0.8,+0.8]))
        s = math.sqrt(h/2)
        z = old_y+s*old_chi
        z_next = a0*z+s*(old_chi+new_chi)
        y_next = a0*old_y+s*(a0+1)*old_chi
        assert math.isclose(z_next,y_next+s*new_chi,rel_tol=2e-15,abs_tol=2e-15)
        n += 1
    for h in [.02,.1,.2,.4,.6, .9, 1.15]:
        rho=(1-h)**2+(.8*h)**2
        assert rho < 1
        m = finite_variance(h, 1, .8)
        assert m > 1
        assert math.isclose(m, (h*(2-h))/(1-rho),rel_tol=1e-12)
        n += 1
    for h in [.01, .1, .8, 1.9]:
        assert math.isclose(finite_variance(h, 1, 0),1,rel_tol=0,abs_tol=1e-12)
        n += 1
    # Stationary second moment of full SGLM via a seeded long run.
    h=.4
    q=.8
    nrun=180000
    chi=rng.gauss(0,1)
    y=0.0
    acc=0.0
    for j in range(nrun):
        a0 = 1-h*(1+rng.choice([-q,q]))
        s=math.sqrt(h/2)
        y = a0*y+s*(a0+1)*chi
        chi = rng.gauss(0,1)
        z=y+s*chi
        if j>10000:
            acc += z*z
    estimate=acc/(nrun-10001)
    exact=finite_variance(h,1,q)
    assert abs(estimate/exact-1)<.08, (estimate,exact)
    n+=1
    print('VERIFY_OK assertions=', n, 'empirical_second_moment=',estimate,
          'theory=',exact,'reset_moment_cutoff=',math.log(2)/math.log(8))


if __name__=='__main__':
    checks()
