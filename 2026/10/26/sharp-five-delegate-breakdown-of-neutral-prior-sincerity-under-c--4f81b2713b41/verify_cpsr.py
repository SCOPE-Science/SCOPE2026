"""Exact rational checks for the conditional-coalition voting-incentive theorem.

Run: python3 verify_cpsr.py
No external dependencies or external data.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb


def payment(i, votes, efforts):
    """CPSR gross payment with budget normalized to one."""
    n = len(efforts)
    total = sum(efforts, Q(0))
    yes = tuple(j for j, z in enumerate(votes) if z)
    yes_weight = sum((efforts[j] for j in yes), Q(0))
    no = tuple(j for j, z in enumerate(votes) if not z)

    def winning_share(coalition):
        if i not in coalition or len(coalition) < (n + 1) // 2:
            return Q(0)
        return efforts[i] / sum(efforts[j] for j in coalition)

    if 2 * yes_weight > total:
        return winning_share(yes)
    if 2 * yes_weight < total:
        return winning_share(no)
    return (winning_share(yes) + winning_share(no)) / 2


def state_good_action_advantage(i, efforts):
    """Expected (accept minus reject) payment conditional on state G.

    All representatives other than i vote their independent private signal.
    """
    other = tuple(j for j in range(len(efforts)) if j != i)
    ans = Q(0)
    for flags in product((0, 1), repeat=len(other)):
        prob = Q(1)
        votes = [0] * len(efforts)
        for j, flag in zip(other, flags):
            votes[j] = flag
            prob *= Q(1, 2) + efforts[j] if flag else Q(1, 2) - efforts[j]
        votes[i] = 1
        accept_payment = payment(i, votes, efforts)
        votes[i] = 0
        reject_payment = payment(i, votes, efforts)
        ans += prob * (accept_payment - reject_payment)
    return ans


def three_member_formula(a, b, c):
    """Three-member analytic formula for K_i, including weighted ties."""
    if b < c:
        b, c = c, b
    j_b = Q(1) / (a + b)
    if a + c < b:
        j_c = Q(0)
    elif a + c == b:
        j_c = Q(1) / (2 * (a + c))
    else:
        j_c = Q(1) / (a + c)
    return a * ((b + c) / (a + b + c) + (b - c) * (j_b - j_c))


def five_member_binomial_formula(t, s):
    """Five-member two-high/three-low formula when t > 3s/2."""
    assert Q(0) < s < t <= Q(1, 2) and 2 * t > 3 * s

    def accepting_reward_in_state(sign):
        p = Q(1, 2) + sign * t
        q = Q(1, 2) + sign * s
        high_agrees = Q(0)
        high_disagrees = Q(0)
        for m in range(4):
            chance = comb(3, m) * q ** m * (1 - q) ** (3 - m)
            if m >= 1:
                high_agrees += chance * t / (2 * t + m * s)
            if m >= 2:
                high_disagrees += chance * t / (t + m * s)
        return p * high_agrees + (1 - p) * high_disagrees

    return accepting_reward_in_state(1) - accepting_reward_in_state(-1)


def main():
    witness = [Q(2, 5), Q(2, 5), Q(1, 100), Q(1, 100), Q(1, 100)]
    k = state_good_action_advantage(0, witness)
    expected = -Q(616489, 33459375)
    assert k == expected, (k, expected)
    assert five_member_binomial_formula(Q(2, 5), Q(1, 100)) == k
    assert 2 * witness[0] * k == -Q(2465956, 167296875)
    total = sum(witness)
    assert all(2 * sum((witness[i] for i in range(5) if bits[i]), Q(0)) != total
               for bits in product((0, 1), repeat=5))

    # Independent full-state enumeration against the analytic three-member identity.
    checked = 0
    for raw in product(range(1, 13), repeat=3):
        efforts = [Q(v, 50) for v in raw]
        for i in range(3):
            others = [efforts[j] for j in range(3) if j != i]
            direct = state_good_action_advantage(i, efforts)
            analytic = three_member_formula(efforts[i], *others)
            assert direct == analytic and analytic > 0, (raw, i, direct, analytic)
            checked += 1

    print('Five-member state-G action advantage / budget:', k)
    print('Conditional advantage after a good signal / budget:', 2 * witness[0] * k)
    print('No weighted-majority ties in witness: verified')
    print('Three-member exact comparisons:', checked)
    print('All exact checks passed')


if __name__ == '__main__':
    main()
