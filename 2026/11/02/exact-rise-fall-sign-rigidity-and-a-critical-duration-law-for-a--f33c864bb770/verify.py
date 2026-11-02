"""Numerical checks for an ideal 1:2 two-harmonic tide theorem.

This script supplements, but does not replace, the analytic argument.
Only the Python standard library is required.
"""
import math

TAU = 2.0 * math.pi


def height_prime(t, amp, phase):
    return -2.0 * math.sin(2.0*t) - amp*math.sin(t+phase)


def height_second(t, amp, phase):
    return -4.0 * math.cos(2.0*t) - amp*math.cos(t+phase)


def stationary_points(amp, phase, sample_count=8192):
    mesh = [TAU*j/sample_count for j in range(sample_count+1)]
    roots = [x % TAU for x in mesh[:-1] if abs(height_prime(x, amp, phase)) < 1e-11]
    for lo, hi in zip(mesh, mesh[1:]):
        flo = height_prime(lo, amp, phase)
        fhi = height_prime(hi, amp, phase)
        if abs(flo) < 1e-11 or abs(fhi) < 1e-11 or flo*fhi > 0.0:
            continue
        else:
            for _ in range(60):
                mid = (lo + hi)/2.0
                fm = height_prime(mid, amp, phase)
                if flo*fm <= 0.0:
                    hi, fhi = mid, fm
                else:
                    lo, flo = mid, fm
            r = (lo + hi)/2.0
        r = r % TAU
        if not any(min(abs(r-s), TAU-abs(r-s)) < 1e-7 for s in roots):
            roots.append(r)
    return sorted(roots)


def rise_length(amp, phase):
    roots = stationary_points(amp, phase)
    assert len(roots) == 4, (amp, phase, roots)
    # The positive derivative intervals are from minima to following maxima.
    rising = 0.0
    for j, r in enumerate(roots):
        if height_second(r, amp, phase) > 0:
            next_r = roots[(j+1) % 4]
            rising += (next_r - r) % TAU
    return rising


def formula_at_quarter_phase(amp):
    disc = math.sqrt(amp*amp + 32.0)
    alpha = math.asin((disc-amp)/8.0)
    beta = math.asin((disc+amp)/8.0)
    return 2.0*(alpha+beta)


def test():
    count = 0
    for a in (0.1, 0.5, 1.0, 1.5, 1.9, 1.99):
        for phi in (0.0, 0.2, math.pi/4, 1.0, math.pi/2,
                    2.0, math.pi, 4.0, 5.3):
            length = rise_length(a, phi)
            delta = length - math.pi
            assert abs(delta) < math.pi
            if abs(math.sin(2.0*phi)) < 1e-10:
                assert abs(delta) < 1e-10, (a,phi,delta)
            else:
                assert delta*math.sin(2.0*phi) > 1e-10, (a,phi,delta)
            count += 1
        direct = rise_length(a, math.pi/4)
        closed = formula_at_quarter_phase(a)
        assert abs(direct-closed) < 1e-10, (a,direct,closed)
    # The coefficient in the quadratic small-amplitude law.
    a = 1e-2
    phi = 0.4
    asymptotic = (a*a/8.0)*math.sin(2.0*phi)
    actual = rise_length(a, phi) - math.pi
    assert abs(actual/asymptotic - 1.0) < 3e-5, (actual,asymptotic)
    # Check the cubic moment independently by full-period quadrature.
    for a, phi in ((0.5,0.2),(1.0,0.7),(1.7,2.0)):
        N = 8000
        moment = sum(height_prime(TAU*(j+0.5)/N, a, phi)**3
                     for j in range(N))/N
        expected = -1.5*a*a*math.sin(2*phi)
        assert abs(moment-expected) < 2e-12, (a,phi,moment,expected)
    # Critical square-root law: error divided by (2-a) stays bounded.
    for a in (1.9,1.99,1.999):
        delta = formula_at_quarter_phase(a)-math.pi
        leading = math.pi/3-2.0*math.sqrt((2.0-a)/3.0)
        assert abs(delta-leading) <= 0.21*(2.0-a)
    print('PASS:', count, 'root-count/sign checks; phase-locked formula;')
    print('quadratic coefficient, cubic moment and critical scaling checks')
    print('F(1, pi/4)-pi = %.15f' % (formula_at_quarter_phase(1.0)-math.pi))


if __name__ == '__main__':
    test()
