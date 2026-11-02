"""Exact finite cross-check for a symmetric three-voter default-delegation game.

Uses only Python's standard library and exact rational arithmetic.
The accompanying mathematical proof establishes the parameter-uniform result.
"""
from fractions import Fraction as Q
from itertools import product

PROFILES = tuple(product(range(3), repeat=3))


def name(d):
    return ''.join(str(j + 1) for j in d)


def direct_utility(i, d, p, t):
    """Enumerate all 8 turnout sets, including empty turnout."""
    q = 1 - p
    total = Q(0)
    for flags in product((0, 1), repeat=3):
        prob = Q(1)
        for f in flags:
            prob *= p if f else q
        seen = set()
        v = i
        representative = None
        while v not in seen:
            seen.add(v)
            if flags[v]:
                representative = v
                break
            v = d[v]
        if representative is not None:
            total += prob * (t - abs(i - representative))
    return total


def path_utility(i, d, p, t):
    """Independent first-participant path expansion."""
    q = 1 - p
    ans, rem = Q(0), Q(1)
    seen = set()
    v = i
    while v not in seen:
        seen.add(v)
        ans += rem * p * (t - abs(i - v))
        rem *= q
        v = d[v]
    return ans


def predicted_ne(q, t):
    a = (1 + 2*q)/(1 + q)
    c = 1 + 1/q
    if t < 1:
        return {'123'}
    if t == 1:
        return {'113', '122', '123', '132', '133', '213', '222', '223'}
    if t < a:
        return {'132', '213'}
    if t == a:
        return {'132', '213', '212', '232'}
    if t < c:
        return {'212', '232'}
    if t == c:
        return {'212', '232', '231', '312'}
    return {'231', '312'}


def predicted_opt(q, t):
    a = (1 + 2*q)/(1 + q)
    b = 1 + 1/(2*q)
    if t < 1:
        return {'123'}
    if t == 1:
        return {'113', '122', '123', '132', '133', '213', '222', '223'}
    if t < a:
        return {'132', '213', '222'}
    if t == a:
        return {'132', '213', '222', '212', '232'}
    if t < b:
        return {'212', '232'}
    if t == b:
        return {'212', '232', '231', '312'}
    return {'231', '312'}


def test():
    case_count = payoff_count = 0
    deviation_count = 0
    for q in (Q(1,11), Q(1,5), Q(1,3), Q(1,2), Q(2,3), Q(4,5), Q(10,11)):
        p = 1-q
        a = (1+2*q)/(1+q)
        b = 1+1/(2*q)
        c = 1+1/q
        assert 1 < a < b < c
        cases = {Q(0), Q(1,2), Q(1), (1+a)/2, a,
                 (a+b)/2, b, (b+c)/2, c, c+1, Q(2), Q(100)}
        for t in sorted(cases):
            pay = {}
            for d in PROFILES:
                pay[d] = []
                for i in range(3):
                    u = direct_utility(i, d, p, t)
                    assert u == path_utility(i, d, p, t)
                    pay[d].append(u)
                    payoff_count += 1
            eq = set()
            for d in PROFILES:
                if all(pay[d][i] >= pay[tuple(d[j] if i != j else k for j in range(3))][i]
                       for i in range(3) for k in range(3)):
                    eq.add(name(d))
                deviation_count += 6
            assert eq == predicted_ne(q, t), (q, t, eq, predicted_ne(q,t))
            welfare = {d: sum(pay[d]) for d in PROFILES}
            max_welfare = max(welfare.values())
            opt = {name(d) for d in PROFILES if welfare[d] == max_welfare}
            assert opt == predicted_opt(q, t), (q, t, opt, predicted_opt(q,t))
            worst_eq = min(welfare[d] for d in PROFILES if name(d) in eq)
            gap = max_welfare - worst_eq
            predicted_gap = p*q*(2*q*(t-1)-1) if b < t <= c else Q(0)
            assert gap == predicted_gap, (q, t, gap, predicted_gap)
            case_count += 1
    print('VERIFY_OK', 'exact_parameter_cases=', case_count,
          'event_level_payoffs=', payoff_count,
          'profile_deviation_checks=', deviation_count)


if __name__ == '__main__':
    test()
