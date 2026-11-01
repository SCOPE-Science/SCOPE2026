"""Independent numerical diagnostics for sharp angular-sector Bergman concentration.

Requires Python 3, NumPy and SciPy. Finite checks supplement the proof; they do
not establish the infinite-weight asymptotic or the all-parameter uniqueness.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq


def constants(a, b):
    tau = (math.log(math.sin(b)) - math.log(math.sin(a))) / (b - a)
    theta = math.atan2(1.0, tau)
    left = theta - a
    right = b - theta
    u = 1.0 / math.tan(a) - tau
    v = tau - 1.0 / math.tan(b)
    delta = math.log(math.sin(theta) / math.sin(a)) - tau * left
    shift = math.log(right * u / (left * v)) / (2.0 * (b - a))
    k = (math.exp(2.0 * shift * left) / u
         + math.exp(-2.0 * shift * right) / v) / (
             math.sin(theta) * math.sqrt(2.0 * math.pi))
    return tau, theta, delta, shift, k


def observables(a, b, weight, shift):
    tau = constants(a, b)[0] + 2.0 * shift / weight
    center = math.atan2(1.0, tau)
    def h(x):
        return math.log(math.sin(x)) - tau * x
    origin = h(center)
    def w(x):
        return math.exp(weight * (h(x) - origin))
    def raw(lo, hi):
        mass = quad(w, lo, hi, epsabs=1e-13)[0]
        first = quad(lambda x: x * w(x), lo, hi, epsabs=1e-13)[0]
        return mass, first
    left, ml = raw(0.0, a)
    inside, mi = raw(a, b)
    right, mr = raw(b, math.pi)
    deriv = (inside * mr - mi * right) - (mi * left - inside * ml)
    loss = (left + right) / (left + inside + right)
    return loss, deriv


def main():
    count = 0
    a, b = math.pi / 3.0, 2.0 * math.pi / 3.0
    tau, theta, delta, shift, k = constants(a, b)
    for observed, target in ((tau, 0.0), (theta, math.pi / 2.0),
                             (shift, 0.0),
                             (delta, math.log(2.0 / math.sqrt(3.0))),
                             (k, math.sqrt(6.0 / math.pi))):
        assert abs(observed - target) < 1e-12
        count += 1
    intervals = [(a, b), (0.55, 1.90), (0.25, 1.40), (1.15, 2.80)]
    for lo, hi in intervals:
        tau, theta, delta, shift, k = constants(lo, hi)
        for test in (lo < theta < hi, delta > 0.0, k > 0.0):
            assert test
            count += 1
        ratios = []
        drifts = []
        for lam in (20.0, 50.0, 100.0, 200.0):
            root = brentq(lambda d: observables(lo, hi, lam, d)[1],
                          shift - 5.0, shift + 5.0, xtol=1e-12)
            loss, derivative = observables(lo, hi, lam, root)
            predicted = k * math.exp(-lam * delta) / math.sqrt(lam)
            assert abs(derivative) < 1e-9
            assert 0.0 < loss < 1.0
            assert abs(root - shift) < 0.025
            assert 0.8 < loss / predicted < 1.02
            count += 4
            ratios.append(loss / predicted)
            drifts.append(abs(root - shift))
        assert ratios[-1] > ratios[0] and ratios[-1] > 0.97
        count += 1
        assert drifts[-1] < drifts[0] + 1e-10
        count += 1
    print(f"passed {count} finite numerical checks")


if __name__ == '__main__':
    main()
