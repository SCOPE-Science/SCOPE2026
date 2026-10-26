"""Reproducible numerical checks for two-pulse infiltration with Horton recovery.

The theorem is proved analytically in RESULT.md; finite tests here are not a proof.
Uses only the Python 3 standard library.
"""
import math
import random


def depth_direct(t1, gap, t2, fmin, amplitude, wet_decay, dry_recovery):
    """Independently compose two wet capacity flows and one dry recovery flow."""
    excess0 = amplitude
    first = fmin * t1 + excess0 * -math.expm1(-wet_decay * t1) / wet_decay
    excess1 = excess0 * math.exp(-wet_decay * t1)
    excess2 = amplitude - (amplitude - excess1) * math.exp(-dry_recovery * gap)
    second = fmin * t2 + excess2 * -math.expm1(-wet_decay * t2) / wet_decay
    return first + second


def equal_depth(gap, horizon, fmin, amplitude, wet_decay, dry_recovery):
    wet = horizon - gap
    z = math.exp(-wet_decay * wet / 2)
    b = math.exp(-dry_recovery * gap)
    return fmin * wet + (amplitude / wet_decay) * (2 * (1-z) - b * (1-z)**2)


def derivative(gap, horizon, fmin, amplitude, wet_decay, dry_recovery):
    z = math.exp(-wet_decay * (horizon-gap) / 2)
    b = math.exp(-dry_recovery * gap)
    r = dry_recovery / wet_decay
    return -fmin + amplitude * (-z + b * (z*(1-z) + r*(1-z)**2))


def second_derivative(gap, horizon, amplitude, wet_decay, dry_recovery):
    z = math.exp(-wet_decay * (horizon-gap)/2)
    b = math.exp(-dry_recovery * gap)
    r = dry_recovery / wet_decay
    B = z*(1-z) + r*(1-z)**2
    Bz = 1-2*z-2*r*(1-z)
    return -amplitude * (wet_decay*z*(1-b*Bz)/2 + dry_recovery*b*B)


def optimum_gap(horizon, fmin, amplitude, wet_decay, dry_recovery):
    if derivative(0, horizon, fmin, amplitude, wet_decay, dry_recovery) <= 0:
        return 0.
    lo, hi = 0., horizon
    for _ in range(75):
        m = (lo+hi)/2
        if derivative(m, horizon, fmin, amplitude, wet_decay, dry_recovery) > 0:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def critical_horizon(fmin, amplitude, wet_decay, dry_recovery):
    eta = fmin/amplitude
    r = dry_recovery/wet_decay
    if r <= eta:
        return math.inf
    zc=(r-eta)/(r+math.sqrt(r+(r-1)*eta))
    return -2*math.log(zc)/wet_decay


def simpson(f, a, b, steps=4096):
    step = (b-a)/steps
    acc = f(a)+f(b)
    for i in range(1,steps):
        acc += (4 if i%2 else 2)*f(a+i*step)
    return step*acc/3


def independent_quadrature(t1,gap,t2,fmin,A,k,h):
    first=simpson(lambda t:fmin+A*math.exp(-k*t),0,t1)
    start=A-(A-A*math.exp(-k*t1))*math.exp(-h*gap)
    second=simpson(lambda t:fmin+start*math.exp(-k*t),0,t2)
    return first+second


def run():
    rng=random.Random(86852715)
    for j in range(3000):
        k=math.exp(rng.uniform(-1,1)); h=k*math.exp(rng.uniform(-2,1))
        A=math.exp(rng.uniform(-1,2)); eta=math.exp(rng.uniform(-2,1.2)); fc=eta*A
        T=rng.uniform(.07,12.)/k
        gap=rng.uniform(.003,.99)*T
        t1=rng.random()*(T-gap);t2=T-gap-t1
        actual=depth_direct(t1,gap,t2,fc,A,k,h)
        # Strict fixed-gap optimality for distinct positive durations.
        best=equal_depth(gap,T,fc,A,k,h)
        assert actual <= best + 5e-11*max(1,best), (j,actual,best)
        eq=depth_direct((T-gap)/2,gap,(T-gap)/2,fc,A,k,h)
        assert math.isclose(eq,best,rel_tol=3e-13,abs_tol=3e-13)
        assert second_derivative(gap,T,A,k,h)<0
        optimal=optimum_gap(T,fc,A,k,h)
        d0=derivative(0,T,fc,A,k,h)
        assert (optimal>0) == (d0>0)
        assert derivative(T,T,fc,A,k,h)<0
        candidate=equal_depth(optimal,T,fc,A,k,h)
        # Assess global optimality versus 51 interval points, not as a proof.
        for m in range(52):
            guess=T*m/51
            assert equal_depth(guess,T,fc,A,k,h) <= candidate + 1e-9*max(1,candidate)
        if j<120:
            q=independent_quadrature(t1,gap,t2,fc,A,k,h)
            assert math.isclose(q,actual,rel_tol=1e-10,abs_tol=1e-10), (q,actual)
        if j<800:
            dh=min(.001*T, gap/3, (T-gap)/3)
            slope=(equal_depth(gap+dh,T,fc,A,k,h)-equal_depth(gap-dh,T,fc,A,k,h))/(2*dh)
            assert abs(slope-derivative(gap,T,fc,A,k,h)) <= 3e-4*(1+abs(slope))
        Tc=critical_horizon(fc,A,k,h)
        if math.isfinite(Tc):
            assert (T>Tc)==(d0>0), (j,T,Tc,d0)
        else:
            assert d0<0
    # Exact power-of-two example.
    k=h=1.;fc=1.;A=8.;T=math.log(32)
    gap=optimum_gap(T,fc,A,k,h)
    assert abs(gap-math.log(2))<3e-13
    assert abs(equal_depth(gap,T,fc,A,k,h)-(math.log(16)+39/4))<1e-12
    assert abs(equal_depth(0,T,fc,A,k,h)-(math.log(32)+31/4))<1e-12
    assert abs(equal_depth(gap,T,fc,A,k,h)-equal_depth(0,T,fc,A,k,h)-(2-math.log(2)))<1e-12
    assert abs(critical_horizon(fc,A,k,h)-2*math.log(16/7))<1e-12
    # Saturation law and monotone optimal gap on a growing horizon.
    dstar=[optimum_gap(T,fc,A,k,h) for T in (2,3,4,8,16,32,64)]
    assert all(x<y for x,y in zip(dstar,dstar[1:])),dstar
    assert dstar[-1] <= math.log(8)
    assert abs(dstar[-1]-math.log(8))<2e-10
    # Linear emergence from the critical horizon.
    zc=7/16; r=1
    Bc=zc*(1-zc)+r*(1-zc)**2
    w=zc*(zc+r*(1-zc))/(zc*(zc+r*(1-zc))+r*Bc)
    Tc=critical_horizon(fc,A,k,h)
    for diff in [1e-3,1e-4,1e-5]:
        d=optimum_gap(Tc+diff,fc,A,k,h)
        assert abs(d/diff-w)<.003,(diff,d/diff,w)
    print('PASS: 3,000 fixed-gap allocation tests, 3,000 strict-concavity checks,')
    print('3,000 global-gap comparisons against 52 grid schedules each,')
    print('120 independent Simpson-integral comparisons, 800 derivative tests,')
    print('exact logarithmic benchmark, horizon criterion, saturation and onset.')
    print('Exact example: T=ln(32); gap*=ln(2); wet pulses=ln(4).')
    print('Optimal uptake=ln(16)+39/4; continuous uptake=ln(32)+31/4.')
    print('Improvement=2-ln(2); saturation gap=ln(8).')

if __name__=='__main__': run()
