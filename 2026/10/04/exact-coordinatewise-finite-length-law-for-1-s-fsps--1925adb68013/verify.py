from fractions import Fraction
from math import isqrt


def clip_ratio(x, gamma):
    if x > gamma:
        return Fraction(1)
    if x < -gamma:
        return Fraction(-1)
    return x / gamma


def run(x0, radii, gammas, chi=Fraction(2)):
    assert len(x0) == len(radii)
    assert chi > 1
    assert all(g > 0 for g in gammas)
    assert all(gammas[i+1] <= gammas[i] for i in range(len(gammas)-1))
    assert all(-r <= x <= r for x, r in zip(x0, radii))
    x = list(x0)
    # k=0: z0=0, so x1=x0.
    l1_length = Fraction(0)
    squared_steps = []
    for k in range(1, len(gammas)):
        prev = list(x)
        for i in range(len(x)):
            z = clip_ratio(prev[i], gammas[k-1])
            x[i] = prev[i] - gammas[k] * z / chi
            assert -radii[i] <= x[i] <= radii[i]
            if prev[i] > 0:
                assert 0 < x[i] <= prev[i]
            elif prev[i] < 0:
                assert prev[i] <= x[i] < 0
            else:
                assert x[i] == 0
        step_abs = [abs(a-b) for a,b in zip(x,prev)]
        l1_step = sum(step_abs, Fraction(0))
        l1_length += l1_step
        # Squared Euclidean step is at most squared l1 step.
        sq2 = sum((d*d for d in step_abs), Fraction(0))
        assert sq2 <= l1_step*l1_step
        squared_steps.append((sq2,l1_step))
    assert l1_length == sum((abs(v) for v in x0), Fraction(0)) - sum((abs(v) for v in x), Fraction(0))
    return x, l1_length, squared_steps


def main():
    schedules = [
        [Fraction(1, k+1) for k in range(1, 90)],
        [Fraction(3, k+3) for k in range(1, 90)],
        [Fraction(1)] + [Fraction(1,2)]*20 + [Fraction(1, k+3) for k in range(1,70)],
    ]
    tests = [
        ([Fraction(3,4), Fraction(-5,6), Fraction(0)], [Fraction(2)]*3),
        ([Fraction(2), Fraction(1,3), Fraction(-7,5), Fraction(1,8)], [Fraction(3)]*4),
    ]
    for x0, radii in tests:
        for gs in schedules:
            run(x0, radii, gs)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
