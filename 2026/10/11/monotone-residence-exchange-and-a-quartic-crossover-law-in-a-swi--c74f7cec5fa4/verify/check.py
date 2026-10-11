"""Standalone quadrature diagnostics for an asymmetric cubic switching center.

Standard-library only. Analytical monotonicity and asymptotic claims require the
proof, not these numerical diagnostics.
"""
import math


def simpson(f, n=8192):
    assert n > 0 and n % 2 == 0
    h = 1.0 / n
    total = f(0.0) + f(1.0)
    total += 4.0 * sum(f(i * h) for i in range(1, n, 2))
    total += 2.0 * sum(f(i * h) for i in range(2, n, 2))
    return total * h / 3.0


def p(alpha, d):
    """Scaled half-return time for V(z)=alpha*z**3/3+d*z**4/4."""
    assert alpha >= 0.0 and d > 0.0
    left, right = 0.0, (4.0 / d) ** 0.25
    # For alpha>0, the turning point lies strictly below the quartic root.
    for _ in range(100):
        z = 0.5 * (left + right)
        if alpha * z**3 / 3.0 + d * z**4 / 4.0 > 1.0:
            right = z
        else:
            left = z
    root = 0.5 * (left + right)
    cubic_share = alpha * root**3 / 3.0
    quartic_share = d * root**4 / 4.0

    def regularized(u):
        v = u * u
        # The square-root endpoint has been removed with z=root*(1-u*u).
        cubic = 3.0 - 3.0 * v + v*v
        quartic = 4.0 - 6.0*v + 4.0*v*v - v*v*v
        return 2.0 / math.sqrt(cubic_share*cubic + quartic_share*quartic)

    return math.sqrt(2.0) * root * simpson(regularized)


def crossover_alpha(dplus, dminus):
    assert dplus > dminus > 0.0
    target = p(0, dplus)
    hi = 1.0
    while p(hi, dminus) > target:
        hi *= 2.0
    lo = 0.0
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if p(mid, dminus) > target:
            lo = mid
        else:
            hi = mid
    return (hi + lo) / 2.0


def energy_fraction(c, dp, dm, e):
    tp = p(0, dp)
    tm = p(c*e**(-0.25), dm)
    return tm/(tm+tp)


def main():
    c4 = math.gamma(.25)*math.gamma(.5)/(2*math.gamma(.75))
    c3 = math.sqrt(2)*3**(1/3)*math.gamma(1/3)*math.gamma(.5)/(3*math.gamma(5/6))
    assert abs(p(0,1)-c4) < 1e-10
    assert abs(p(0,4)-c4/4**.25) < 1e-10
    vals = [p(a,1) for a in [0,0.01,0.1,1,10,100]]
    assert all(a>b for a,b in zip(vals, vals[1:]))
    frac = [energy_fraction(1.,4.,1.,10.**k) for k in [-9,-5,-2,0,3,7,11]]
    assert all(a<b for a,b in zip(frac,frac[1:]))
    assert abs(frac[-1]-(4**.25)/(4**.25+1)) < 2e-4
    q = crossover_alpha(4,1)
    e = q**(-4)
    assert abs(e-0.016370808654774475) < 3e-10
    for dm,dp in [(1,1),(2,1),(1,3)]:
        efrac = energy_fraction(1,dp,dm,1e12)
        assert efrac < 0.500000001 if dp <= dm else efrac > 0.5
    slope = (c4 - p(1e-5,1.))/1e-5
    assert abs(slope-math.sqrt(2)/3) < 2e-5
    k = (4*math.sqrt(2)/(3*c4))**4
    approx = []
    for delta in [0.1,0.05,0.02,0.01]:
        alpha = crossover_alpha(1+delta,1)
        approx.append((alpha**(-4))*delta**4)
    assert abs(approx[-1]/k-1) < 0.02
    assert all(abs(approx[i+1]-k)<abs(approx[i]-k) for i in range(len(approx)-1))
    # Exact on-region and across-region continuity of H at selected points.
    def v(x,cc,dp,dm):
        return dp*x**4/4 if x>=0 else cc*(-x)**3/3+dm*x**4/4
    def force(x,cc,dp,dm):
        return -dp*x**3 if x>=0 else cc*x*x-dm*x**3
    for x in [-2.,-0.5,0,0.5,2.]:
        vprime = dp=4.0
        cc,dm=1.0,1.0
        deriv=(dp*x**3 if x>=0 else -cc*x*x+dm*x**3)
        assert abs(deriv+force(x,cc,dp,dm))<1e-12
        assert v(x,cc,dp,dm)>=0.0
    print('C3=',format(c3,'.12f'),'C4=',format(c4,'.12f'))
    print('example_crossover_E=',format(e,'.15g'))
    print('scaled_small_contrast=',[round(v,10) for v in approx],'target=',round(k,10))
    print('CHECK_OK')

if __name__=='__main__':
    main()
