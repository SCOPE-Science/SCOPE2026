"""Reproducible numerical checks for the delayed two-input Bateman peak theorem.

Run with Python 3.10+: python verify.py. No external dependencies.
The mathematical proof, not these finite tests, establishes the theorem.
"""
import math
import random


def impulse(t, slow, fast):
    if t <= 0:
        return 0.0
    if fast == slow:
        return t * math.exp(-slow * t)
    return (math.exp(-slow * t) - math.exp(-fast * t)) / (fast - slow)


def impulse_derivative(t, slow, fast):
    if fast == slow:
        return (1.0 - slow * t) * math.exp(-slow * t)
    return (-slow * math.exp(-slow * t) + fast * math.exp(-fast * t)) / (fast - slow)


def isolated_peak(slow, fast):
    if fast == slow:
        return 1.0 / slow
    return math.log(fast / slow) / (fast - slow)


def critical_ratio(slow, fast):
    if fast == slow:
        return math.exp(-2)
    ratio = fast / slow
    return math.exp(-((ratio + 1)/(ratio - 1))*math.log(ratio))


def second_peak_time(delay, dose_ratio, slow, fast):
    if fast == slow:
        # After the delayed input, the common exponential has affine prefactor.
        return (1 + dose_ratio * math.exp(slow*delay) +
                slow*dose_ratio*delay*math.exp(slow*delay)) / (slow*(1 + dose_ratio*math.exp(slow*delay)))
    return (math.log(fast / slow) +
            math.log1p(dose_ratio*math.exp(fast*delay)) -
            math.log1p(dose_ratio*math.exp(slow*delay))) / (fast - slow)


def relative_decay(delay, slow, fast):
    return -impulse_derivative(delay, slow, fast) / impulse_derivative(0, slow, fast)


def combined(t, delay, m, slow, fast):
    return impulse(t, slow, fast) + m*impulse(t-delay, slow, fast)


def combined_derivative(t, delay, m, slow, fast):
    return impulse_derivative(t, slow, fast) + (m*impulse_derivative(t-delay, slow, fast) if t > delay else 0.)


def bisect(fun, left, right):
    fl = fun(left)
    fr = fun(right)
    assert fl * fr <= 0
    for _ in range(100):
        mid = 0.5*(left+right)
        fm = fun(mid)
        if (fl <= 0 and fm <= 0) or (fl >= 0 and fm >= 0):
            left, fl = mid, fm
        else:
            right, fr = mid, fm
    return 0.5*(left+right)


def deterministic_checks():
    a, b, m = 1.0, 3.0, 0.05
    p = isolated_peak(a,b)
    threshold = critical_ratio(a,b)
    assert abs(threshold - 1/9) < 1e-14
    left = bisect(lambda d: relative_decay(d,a,b) - m, p, 2*p)
    right = bisect(lambda d: relative_decay(d,a,b)-m, 2*p, 10.0)
    assert abs(left - 0.6563865023143630) < 1e-12
    assert abs(right - 2.2700439184542944) < 1e-12
    for d, two_expected in [(0.4, False), (0.6, True), (0.7, False),
                            (1.1, False), (2.0, False), (3.0, True)]:
        two = d > p and m > relative_decay(d,a,b)
        assert two == two_expected
        if d > p:
            assert (second_peak_time(d,m,a,b) > d) == (m > relative_decay(d,a,b))
    for t in [0.1,0.6,1.,2.,5.]:
        h = 1e-5
        x = impulse(t,a,b)
        assert abs((impulse(t+h,a,b)-impulse(t-h,a,b))/(2*h)-impulse_derivative(t,a,b)) < 2e-9
        assert x > 0
    assert abs(critical_ratio(1,1)-math.exp(-2)) < 1e-15
    assert abs(relative_decay(2,1,1)-math.exp(-2)) < 1e-15
    print('deterministic boundary and reentrance checks: PASS')


def randomized_checks(count=2200):
    rng=random.Random(731451)
    checked=0
    for i in range(count):
        slow=math.exp(rng.uniform(math.log(.25),math.log(2.5)))
        fast = slow if i%11 == 0 else slow*math.exp(rng.uniform(math.log(1.05),math.log(4.)))
        m=math.exp(rng.uniform(math.log(.005),math.log(2)))
        p=isolated_peak(slow,fast)
        d=p*rng.uniform(0.3,5.0)
        q=relative_decay(d,slow,fast)
        rhs = m > q
        # Verify the separate post-input stationary point by analytic rate equation.
        after=second_peak_time(d,m,slow,fast)
        if d > p and abs(m-q)>1e-8:
            assert (after>d)==rhs, (slow,fast,m,d,after,q)
        # Verify derivative jumps at the delayed input and unique sign per segment.
        before_slope=impulse_derivative(d,slow,fast)
        after_slope=before_slope+m*impulse_derivative(0,slow,fast)
        assert abs(after_slope-impulse_derivative(0,slow,fast)*(m-q)) < 2e-12
        if d > p and abs(m-q)>1e-8:
            assert (after_slope>0)==rhs
            assert before_slope < 0
        # Numerically differentiate the fully superposed response away from the kink.
        t=d+rng.uniform(.05,.8)*p
        step=1e-5*min(p,t-d)
        fd=(combined(t+step,d,m,slow,fast)-combined(t-step,d,m,slow,fast))/(2*step)
        derivative=combined_derivative(t,d,m,slow,fast)
        assert abs(fd-derivative) < 5e-7*(1+abs(derivative)), (fd,derivative)
        checked+=1
    print(f'randomized direct finite-difference and peak-sign checks: PASS ({checked})')


if __name__=='__main__':
    deterministic_checks()
    randomized_checks()
