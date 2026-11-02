"""Exact finite-player checks and independently integrated mean-field examples.

Standard-library only: python verify.py
"""
from fractions import Fraction
from itertools import product, permutations, combinations
from math import exp, factorial


def add_bernoulli(dist, p):
    result = [Fraction(0)] * (len(dist) + 1)
    for k, weight in enumerate(dist):
        result[k] += weight * (1 - p)
        result[k + 1] += weight * p
    return result


def payoff(N, sizes, free, tagged):
    assert sum(sizes) + free == N
    d = [Fraction(1)]
    if tagged == 'free':
        assert free > 0
        for _ in range(free - 1):
            d = add_bernoulli(d, Fraction(1, N))
        other = range(len(sizes))
    else:
        assert sizes[tagged] > 0
        for _ in range(free):
            d = add_bernoulli(d, Fraction(1, N))
        other = (j for j in range(len(sizes)) if j != tagged)
    for j in other:
        d = add_bernoulli(d, Fraction(sizes[j], N))
    return sum((prob / (k + 1) for k, prob in enumerate(d)), Fraction(0))


def h_expected(N, sizes, free, omitted, free_n):
    d = [Fraction(1)]
    for _ in range(free_n):
        d = add_bernoulli(d, Fraction(1, N))
    for j in range(len(sizes)):
        if j not in omitted:
            d = add_bernoulli(d, Fraction(sizes[j], N))
    return sum((weight / ((k + 1) * (k + 2)) for k, weight in enumerate(d)), Fraction(0))


def compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for rest in compositions(total - i, n - 1):
                yield (i,) + rest


def check_finite():
    checks = 0
    for N in range(2, 11):
        for K in range(1, min(N, 4) + 1):
            for sizes_and_free in compositions(N, K + 1):
                sizes, free = sizes_and_free[:K], sizes_and_free[K]
                active = [i for i in range(K) if sizes[i] > 0]
                pay = {i: payoff(N, sizes, free, i) for i in active}
                for i, j in combinations(active, 2):
                    h = h_expected(N, sizes, free, {i, j}, free)
                    assert pay[i] - pay[j] == Fraction(sizes[i] - sizes[j], N) * h
                    assert (pay[i] > pay[j]) == (sizes[i] > sizes[j])
                    checks += 1
                if free:
                    p0 = payoff(N, sizes, free, 'free')
                    for i in active:
                        h = h_expected(N, sizes, free, {i}, free - 1)
                        assert pay[i] - p0 == Fraction(sizes[i] - 1, N) * h
                        checks += 1
    return checks


def direct_small_payoffs(N, sizes, free):
    """Separate exhaustive assignment model, for N<=4."""
    assert N <= 4 and sum(sizes) + free == N
    club_assignments = [list(permutations(range(N), g)) for g in sizes]
    sums = [Fraction(0) for _ in range(len(sizes) + (free > 0))]
    count = 0
    for club_choices in product(*club_assignments):
        for free_choices in product(range(N), repeat=free):
            customers = []
            for j, restaurants in enumerate(club_choices):
                customers.extend((r, j) for r in restaurants)
            customers.extend((r, len(sizes)) for r in free_choices)
            assert len(customers) == N
            bins = [0] * N
            for r, j in customers:
                bins[r] += 1
            scores = [Fraction(0) for _ in sums]
            for r, j in customers:
                scores[j] += Fraction(1, bins[r])
            for j, g in enumerate(sizes):
                if g:
                    sums[j] += scores[j] / g
            if free:
                sums[-1] += scores[-1] / free
            count += 1
    return [x / count for x in sums]


def check_direct():
    comparisons = 0
    for N in range(2, 5):
        for K in range(1, min(N, 3) + 1):
            for comp in compositions(N, K + 1):
                sizes, free = comp[:K], comp[K]
                if not all(sizes):
                    continue
                direct = direct_small_payoffs(N, sizes, free)
                for i in range(K):
                    assert direct[i] == payoff(N, sizes, free, i)
                    comparisons += 1
                if free:
                    assert direct[-1] == payoff(N, sizes, free, 'free')
                    comparisons += 1
    return comparisons


def limit_payoffs(b):
    """Poisson/free and club Bernoulli law through convergent Poisson series."""
    free = 1 - sum(b)
    assert free >= -1e-12
    free = max(0.0, free)
    answers = []
    for omitted in range(len(b) + 1):
        d = [1.0]
        for j, prob in enumerate(b):
            if j == omitted:
                continue
            nd = [0.0] * (len(d) + 1)
            for k, weight in enumerate(d):
                nd[k] += weight * (1 - prob)
                nd[k + 1] += weight * prob
            d = nd
        total = 0.0
        pois = exp(-free)
        for v in range(35):
            total += pois * sum(weight / (1 + k + v) for k, weight in enumerate(d))
            pois *= free / (v + 1)
        answers.append(total)
    return answers


def runge_kutta(b, duration=1000., step=0.05):
    K = len(b)
    state = list(b)
    def f(x):
        pay = limit_payoffs(x)
        fre = max(0.0, 1 - sum(x))
        avg = sum(x[j] * pay[j] for j in range(K)) + fre * pay[-1]
        return [x[j] * (pay[j] - avg) for j in range(K)]
    for t in range(round(duration / step)):
        k1 = f(state)
        k2 = f([state[j] + step * k1[j]/2 for j in range(K)])
        k3 = f([state[j] + step * k2[j]/2 for j in range(K)])
        k4 = f([state[j] + step * k3[j] for j in range(K)])
        state = [state[j] + step * (k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(K)]
    return state


def check_dynamic():
    tests = [([0.36,0.29,0.13], [1.,0.,0.]),
             ([0.2,0.2,0.1], [0.5,0.5,0.]),
             ([0.1,0.1,0.1], [1/3]*3),
             ([0.08,0.05,0.03,0.07], [1.,0.,0.,0.])]
    for start, expected in tests:
        end = runge_kutta(start, duration=650)
        assert max(abs(a-b) for a,b in zip(end,expected)) < 1e-5, (start,end)
    return len(tests)


def check_local_spectra():
    # Perturb each equilibrium along an active contrast and an invading face.
    eps = 1e-7
    def flow(b):
        ps = limit_payoffs(b)
        f = 1 - sum(b)
        avg = sum(a*p for a,p in zip(b,ps[:-1])) + f*ps[-1]
        return [a*(p-avg) for a,p in zip(b,ps[:-1])], f*(ps[-1]-avg)
    def integral(func):
        num = 1200
        h = 1/num
        return h/3*(func(0)+func(1)+
                    4*sum(func((2*i+1)*h) for i in range(num//2))+
                    2*sum(func(2*i*h) for i in range(1,num//2)))
    n = 0
    for r in (1,2,3):
        A = lambda t:(r-1+t)/r
        ls = -integral(lambda t:(1-t)*A(t)**(r-1))/r
        inside = [(1-eps)/r]*r
        _, fdot = flow(inside)
        assert abs(fdot/eps - ls) < 1e-6
        inside_abs = [(1-eps)/r]*r + [eps]
        dv, _ = flow(inside_abs)
        assert abs(dv[-1]/eps - ls) < 1e-6
        n += 2
        if r >= 2:
            lu = integral(lambda t:(1-t)*A(t)**(r-2))/r
            inside = [1/r + eps, 1/r - eps] + [1/r]*(r-2)
            dv, _ = flow(inside)
            assert abs((dv[0]-dv[1])/(2*eps)-lu) < 1e-6
            n += 1
    return n


if __name__ == '__main__':
    assert check_finite() > 100
    print('Finite exact payoff comparisons:', check_finite())
    print('Independent exhaustive assignment checks:', check_direct())
    print('Independent numerical dynamical examples:', check_dynamic())
    print('Local spectrum perturbation checks:', check_local_spectra())
    print('PASS')
