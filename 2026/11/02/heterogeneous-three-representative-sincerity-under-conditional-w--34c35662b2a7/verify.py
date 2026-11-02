"""Exact-rational finite checks for three-representative conditional winner sharing.

The accompanying analytic argument is the proof for all positive efforts.
This program checks the independent payoff enumeration against its formula.
"""
from fractions import Fraction as F
from itertools import product


def reward(x, i, ballots):
    total = sum(x)
    support = [j for j in range(3) if ballots[j] == ballots[i]]
    supporting = sum(x[j] for j in support)
    if len(support) < 2:
        return F(0)
    if 2 * supporting > total:
        chance = F(1)
    elif 2 * supporting == total:
        chance = F(1, 2)
    else:
        chance = F(0)
    return chance * x[i] / supporting


def expected_state_difference(x, i, state_good):
    others = [j for j in range(3) if j != i]
    result = F(0)
    for signals in product((False, True), repeat=2):
        prob = F(1)
        for j, signal in zip(others, signals):
            acc = F(1, 2) + x[j]
            prob *= acc if (signal == state_good) else (1 - acc)
        ballots = [False] * 3
        for j, signal in zip(others, signals):
            ballots[j] = signal
        ballots[i] = True
        r_accept = reward(x, i, ballots)
        ballots[i] = False
        r_reject = reward(x, i, ballots)
        result += prob * (r_accept - r_reject)
    return result


def coefficient(x, i):
    a = x[i]
    b, c = [x[j] for j in range(3) if j != i]
    total = a + b + c
    def win(winners, loser):
        return F(1) if winners > loser else (F(1, 2) if winners == loser else F(0))
    return (b+c)/total + (b-c)*(win(a+b,c)/(a+b)-win(a+c,b)/(a+c))


def posterior(prior, effort, signal):
    p = F(1, 2) + effort
    yes = prior * (p if signal else 1-p)
    no = (1-prior) * (1-p if signal else p)
    return yes/(yes+no)


def main():
    grids = 0
    state_checks = 0
    posterior_checks = 0
    tie_cases = 0
    for nums in product(range(1, 11), repeat=3):
        x = tuple(F(q, 20) for q in nums)
        grids += 1
        for i in range(3):
            a = x[i]
            others = [x[j] for j in range(3) if j != i]
            b, c = others
            if a+b==c or a+c==b:
                tie_cases += 1
            h = coefficient(x, i)
            assert h > 0, (x, i, h)
            positive = expected_state_difference(x, i, True)
            negative = expected_state_difference(x, i, False)
            assert positive == a*h, (x,i,positive,a*h)
            assert negative == -a*h, (x,i,negative,-a*h)
            state_checks += 2
            for prior in [F(1, 2), F(12, 25), F(13, 25)]:
                for signal in (False, True):
                    post = posterior(prior, a, signal)
                    mixed = post*positive + (1-post)*negative
                    assert mixed == a*(2*post-1)*h
                    if abs(prior-F(1,2)) < min(x):
                        assert mixed > 0 if signal else mixed < 0
                    posterior_checks += 1
    print(f'PASS: {grids} heterogeneous/equal effort triples, {state_checks} exact state-payoff checks, '
          f'{posterior_checks} posterior identities, {tie_cases} evaluated tie cases.')

if __name__ == '__main__':
    main()
