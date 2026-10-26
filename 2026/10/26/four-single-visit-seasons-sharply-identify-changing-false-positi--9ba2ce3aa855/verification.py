"""Exact rational verification of four-season occupancy reconstruction.

Python 3.10+ standard library only. Usage: python verification.py
Produces a deterministic certificate.json in the current working directory.
"""
import json
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path


def root_rational(x):
    assert x >= 0
    numerator, denominator = isqrt(x.numerator), isqrt(x.denominator)
    assert numerator * numerator == x.numerator
    assert denominator * denominator == x.denominator
    return Q(numerator, denominator)


def observed_law(pi, lam, f, d):
    assert len(f) == len(d)
    assert -1 < lam < 1 and lam != 0 and 0 < pi < 1
    gamma, epsilon = pi * (1 - lam), (1 - pi) * (1 - lam)
    assert 0 < gamma < 1 and 0 < epsilon < 1
    assert all(0 < a < b < 1 for a, b in zip(f, d))
    hidden = {(0,): 1 - pi, (1,): pi}
    for _ in range(1, len(f)):
        updated = {}
        for history, mass in hidden.items():
            current = history[-1]
            for subsequent in (0, 1):
                transition = ((1 - gamma) if current == 0 else epsilon) if subsequent == 0 else (gamma if current == 0 else (1 - epsilon))
                updated[history + (subsequent,)] = mass * transition
        hidden = updated
    observed = {history: Q(0) for history in product((0, 1), repeat=len(f))}
    for hidden_history, hidden_mass in hidden.items():
        for observed_history in observed:
            mass = hidden_mass
            for i, (latent, result) in enumerate(zip(hidden_history, observed_history)):
                detection = d[i] if latent else f[i]
                mass *= detection if result else (1 - detection)
            observed[observed_history] += mass
    assert sum(observed.values()) == 1
    return observed


def moments(distribution):
    seasons = len(next(iter(distribution)))
    means = [sum(outcome[i] * probability for outcome, probability in distribution.items()) for i in range(seasons)]
    covariances = {(i, j): sum((outcome[i] - means[i]) * (outcome[j] - means[j]) * probability for outcome, probability in distribution.items()) for i in range(seasons) for j in range(i + 1, seasons)}
    third = sum((outcome[0] - means[0]) * (outcome[1] - means[1]) * (outcome[2] - means[2]) * probability for outcome, probability in distribution.items())
    return means, covariances, third


def invert(distribution):
    means, covariances, third = moments(distribution)
    assert len(means) == 4
    c = lambda i, j: covariances[i, j]
    ratio = third**2 / (c(0, 1) * c(1, 2) * c(0, 2))
    variance = 1 / (4 + ratio)
    sign_t = (third > 0) - (third < 0)
    pi = (1 - sign_t * root_rational(1 - 4 * variance)) / 2
    lam = ((c(0, 1) > 0) - (c(0, 1) < 0)) * root_rational(c(0, 2) * c(1, 3) / (c(0, 1) * c(2, 3)))
    delta1 = root_rational(c(0, 1) * c(1, 2) / (variance * c(0, 2)))
    delta = [c(0, 1) / (variance * delta1 * lam), delta1, c(1, 2) / (variance * delta1 * lam), c(1, 3) / (variance * delta1 * lam**2)]
    f = [mean - pi * diff for mean, diff in zip(means, delta)]
    d = [a + b for a, b in zip(f, delta)]
    return pi, lam, f, d


def main():
    f = [Q(1, 10), Q(1, 8), Q(1, 6), Q(1, 12)]
    d = [Q(4, 5), Q(3, 4), Q(5, 6), Q(2, 3)]
    parameter_cases = [(Q(2, 5), Q(1, 2)), (Q(3, 5), Q(-1, 3)), (Q(1, 2), Q(2, 5)), (Q(1, 3), Q(-1, 4))]
    passed = []
    for pi, lam in parameter_cases:
        law = observed_law(pi, lam, f, d)
        assert invert(law) == (pi, lam, f, d)
        passed.append({'occupancy': str(pi), 'memory': str(lam), 'outcomes': len(law), 'exact_recovery': True})

    pi, lam = parameter_cases[0]
    original = observed_law(pi, lam, f[:3], d[:3])
    means, _, _ = moments(original)
    different_memory = Q(3, 5)
    delta = [d[i] - f[i] for i in range(3)]
    changed_delta = [delta[0] * lam / different_memory, delta[1], delta[2] * lam / different_memory]
    changed_f = [means[i] - pi * changed_delta[i] for i in range(3)]
    changed_d = [changed_f[i] + changed_delta[i] for i in range(3)]
    competing = observed_law(pi, different_memory, changed_f, changed_d)
    assert original == competing and lam != different_memory
    assert all(0 < a < b < 1 for a, b in zip(changed_f, changed_d))
    report = {
        'statement': 'Four-season moment inverse and three-season nonidentifiability',
        'arithmetic': 'Python fractions.Fraction; all calculations exact',
        'four_season_checks': passed,
        'three_season_counterexample': {
            'occupancy': str(pi), 'first_memory': str(lam), 'second_memory': str(different_memory),
            'first_false_positive_rates': [str(x) for x in f[:3]],
            'second_false_positive_rates': [str(x) for x in changed_f],
            'first_true_positive_rates': [str(x) for x in d[:3]],
            'second_true_positive_rates': [str(x) for x in changed_d],
            'all_eight_observed_history_probabilities_equal': original == competing,
            'observed_probabilities': {''.join(map(str, k)): str(v) for k, v in sorted(original.items())},
        },
        'scope': 'Finite exact test cases; unrestricted claims rest on symbolic proof in RESULT.md',
    }
    path = Path('certificate.json')
    path.write_text(json.dumps(report, sort_keys=True, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('All exact reconstruction and observational-aliasing checks passed.')


if __name__ == '__main__':
    main()
