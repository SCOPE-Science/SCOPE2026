from fractions import Fraction


def component(tau, delta, s, steps=80):
    tau = Fraction(tau)
    delta = Fraction(delta)
    s = Fraction(s)
    y = Fraction(0)
    xs = []
    for _k in range(1, steps + 1):
        x = max(y - tau, Fraction(0))
        xs.append(x)
        y = y + delta * (s - x)
    return xs


def floor_fraction(q):
    return q.numerator // q.denominator


def ceil_fraction(q):
    return (q.numerator + q.denominator - 1) // q.denominator


taus = [Fraction(1, 3), Fraction(2), Fraction(17, 5), Fraction(11, 7)]
deltas = [Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(4, 3), Fraction(7, 4)]
amplitudes = [Fraction(1, 5), Fraction(2, 3), Fraction(3, 2), Fraction(5)]

for tau in taus:
    for delta in deltas:
        for s in amplitudes:
            xs = component(tau, delta, s)
            kappa = floor_fraction(tau / (delta * s)) + 2
            positive = [idx + 1 for idx, x in enumerate(xs) if x > 0]
            assert positive[0] == kappa
            x0 = xs[kappa - 1]
            assert 0 < x0 <= delta * s
            e0 = x0 - s
            for n in range(0, min(30, len(xs) - kappa + 1)):
                assert xs[kappa - 1 + n] - s == (1 - delta) ** n * e0
                assert xs[kappa - 1 + n] > 0
            if delta == 1:
                settling = ceil_fraction(tau / s) + 2
                assert xs[settling - 1] == s
                assert all(x == s for x in xs[settling - 1:])

# A four-direction matching sample: rank equals the number of activated directions.
tau = Fraction(9, 4)
delta = Fraction(4, 3)
ss = [Fraction(1, 2), Fraction(3, 4), Fraction(5, 3), Fraction(7, 2)]
sequences = [component(tau, delta, s, steps=50) for s in ss]
kappas = [floor_fraction(tau / (delta * s)) + 2 for s in ss]
for k in range(1, 51):
    rank = sum(1 for seq in sequences if seq[k - 1] > 0)
    expected = sum(1 for kappa in kappas if k >= kappa)
    assert rank == expected

print("VERIFY_OK")
