"""Exact finite tests for the three-seat, four-candidate reciprocal-JR theorem.

Run: python verify.py. Standard library only. Finite checks supplement the proof.
"""
from fractions import Fraction
from itertools import product


def analyze(ballots, qualities, r):
    n = len(ballots)
    assert len(qualities) == 4
    support = [sum(bool(b & (1 << c)) for b in ballots) for c in range(4)]
    assert min(support) >= r
    exclusive = [sum(b == (1 << c) for b in ballots) for c in range(4)]
    opt = sum(qualities) - min(qualities)
    admissible = [sum(qualities) - qualities[c] for c in range(4)
                  if 3 * exclusive[c] * qualities[c] < n]
    assert admissible, ('no reciprocal-JR outcome', ballots, qualities)
    attained = max(admissible)
    target = (Fraction(2) + Fraction(n, 3 * (n-r))) / 3 if 3*r < 2*n else Fraction(1)
    assert attained / opt >= target, (ballots, qualities, r, target)
    return attained, opt


def check():
    total = 0
    # All profiles on two or three voters, exact rational grid of three qualities.
    for n in (2, 3):
        for ballots in product(range(1, 16), repeat=n):
            support = [sum(bool(b & (1 << c)) for b in ballots) for c in range(4)]
            if min(support) == 0:
                continue
            for Q in product((Fraction(1, 2), Fraction(3, 4), Fraction(1)), repeat=4):
                for r in range(1, min(support) + 1):
                    analyze(ballots, Q, r)
                    total += 1
    # A deterministic, non-exhaustive four- and five-voter stress test.
    for n in (4, 5):
        for t in range(1500):
            ballots = tuple(1 + ((17 * t + 11 * i + i*i + t//(i+1)) % 15)
                            for i in range(n))
            support = [sum(bool(b & (1 << c)) for b in ballots) for c in range(4)]
            if min(support) == 0:
                continue
            Q = tuple(Fraction(1 + ((19*t + 7*c + (t//(c+1))) % 7), 7)
                      for c in range(4))
            for r in range(1, min(support) + 1):
                analyze(ballots, Q, r)
                total += 1
    witness_count = 0
    for n in range(2, 41):
        for r in range(1, n+1):
            if 3*r >= 2*n:
                continue
            q = Fraction(n, 3*(n-r))
            # r voters support the three top candidates; n-r support the fourth.
            # If necessary, extra fourth-candidate approvals create the floor r.
            overlap = max(0, 2*r-n)
            ballots = tuple((0b1111 if i < overlap else 0b0111)
                            for i in range(r)) + tuple(0b1000 for _ in range(n-r))
            obtained, optimum = analyze(ballots,
                                        (Fraction(1),Fraction(1),Fraction(1),q), r)
            assert optimum == 3 and obtained == 2 + q
            witness_count += 1
    print(f'VERIFY_OK exact_profile_checks={total} sharp_witnesses={witness_count}')


if __name__ == '__main__':
    check()
