"""Reproduce exact moment laws for an orientation-copying memory walk."""
import bisect
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import hyp1f1, exp1


def exact_second_moment(t, flip_rate, copy_rate):
    lam = 2 * flip_rate + copy_rate
    if abs(copy_rate - 2 * flip_rate) < 1e-12:
        x = lam * t
        return (2 * t / lam) * (
            math.log(x) + np.euler_gamma - 1 + exp1(x)
            + (-math.expm1(-x)) / x
        )
    nu = 2 * copy_rate / lam
    return (2 * t / (2 * flip_rate - copy_rate)) * (
        1 - hyp1f1(1 - nu, 2, -lam * t)
    )


def numerical_moment(t, gamma, rate):
    lam = 2 * gamma + rate
    def ode(s, state):
        b, bp = state
        return [bp, 2 - lam * bp + 2 * rate * b / s]
    tiny = 1.e-6
    b0 = tiny**2 - (2 * gamma / 3) * tiny**3 + gamma * (6 * gamma + rate) * tiny**4 / 18
    bp0 = 2 * tiny - 2 * gamma * tiny**2 + 2 * gamma * (6 * gamma + rate) * tiny**3 / 9
    sol = solve_ivp(ode, (tiny, t), [b0, bp0], rtol=3e-11, atol=3e-12)
    assert sol.success
    return sol.y[0, -1]


def simulate_one(tmax, gamma, rate, rng):
    t = 0.0
    sign = 1 if rng.random() < 0.5 else -1
    event_times = [0.0]
    event_signs = [sign]
    running = 0.0
    total = gamma + rate
    while True:
        next_t = t + rng.exponential(1 / total)
        if next_t >= tmax:
            running += sign * (tmax - t)
            return running
        running += sign * (next_t - t)
        t = next_t
        if rng.random() < gamma / total:
            sign = -sign
        else:
            past_time = t * rng.random()
            sign = event_signs[bisect.bisect_right(event_times, past_time) - 1]
        event_times.append(t)
        event_signs.append(sign)


def test():
    rng = np.random.default_rng(20261022)
    for gamma, rate, tmax in [(1., .5, 5.), (1., 2., 5.), (1., 5., 5.), (2., 6., 3.)]:
        ex = exact_second_moment(tmax, gamma, rate)
        num = numerical_moment(tmax, gamma, rate)
        assert abs(ex - num) < 3e-8 * max(1, ex), (gamma, rate, ex, num)
        vals = np.array([simulate_one(tmax, gamma, rate, rng) for _ in range(16000)])
        sq = vals**2
        mc = sq.mean()
        se = sq.std(ddof=1) / math.sqrt(len(sq))
        assert abs(mc - ex) < 5.5 * se, (gamma, rate, ex, mc, se)
        print(f"gamma={gamma} r={rate} t={tmax}: exact={ex:.9f} ODE={num:.9f} MC={mc:.9f} SE={se:.9f}")
    for gamma, rate in [(1., 0.5), (1., 2.), (1., 4.)]:
        lam = 2 * gamma + rate
        nu = 2 * rate / lam
        x = 1e10
        b = exact_second_moment(x, gamma, rate)
        if rate < 2 * gamma:
            pred = 2 * x / (2 * gamma - rate)
        elif rate == 2 * gamma:
            pred = (2 * x / lam) * (math.log(lam * x) + np.euler_gamma - 1)
        else:
            pred = (2 * lam**(nu - 1) / ((rate - 2 * gamma) * math.gamma(1 + nu))) * x**nu
        print(f"long time gamma={gamma} r={rate}: ratio={b/pred:.9f}")
        assert abs(b / pred - 1) < 0.003

if __name__ == '__main__':
    test()
