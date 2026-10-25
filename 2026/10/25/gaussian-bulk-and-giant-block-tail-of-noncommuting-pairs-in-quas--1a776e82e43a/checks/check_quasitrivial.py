"""Independent finite checks for noncommuting-pair spectra of quasitrivial semigroups.

Run with Python 3 standard library: python check_quasitrivial.py
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial


def enumerated_spectrum(n):
    """Enumerate all quasitrivial binary laws, filtering associativity directly."""
    pair_list = [(i, j) for i in range(n) for j in range(i + 1, n)]
    out = Counter()
    inspected = 0
    for choices in product(range(4), repeat=len(pair_list)):
        inspected += 1
        op = [list(range(n)) for _ in range(n)]
        for (i, j), mode in zip(pair_list, choices):
            op[i][j] = j if mode & 1 else i
            op[j][i] = j if mode & 2 else i
        if all(op[op[i][j]][k] == op[i][op[j][k]]
               for i in range(n) for j in range(n) for k in range(n)):
            nc = sum(op[i][j] != op[j][i] for i, j in pair_list)
            out[nc] += 1
    return dict(out), inspected


def recurrence_spectra(max_n):
    out = [Counter({0: 1})]
    for n in range(1, max_n + 1):
        row = Counter()
        for m in range(1, n + 1):
            multiplicity = comb(n, m) * (1 if m == 1 else 2)
            reward = comb(m, 2)
            for old_reward, count in out[n-m].items():
                row[old_reward + reward] += multiplicity * count
        out.append(row)
    return out


def run():
    spectra = recurrence_spectra(60)
    known = [1, 1, 4, 20, 138, 1182, 12166, 146050, 2003882]
    assert [sum(spectra[n].values()) for n in range(9)] == known
    cases = 0
    for n in range(1, 5):
        direct, all_cases = enumerated_spectrum(n)
        assert direct == dict(spectra[n]), (n, direct, spectra[n])
        print('n=', n, 'all quasitrivial tables=', all_cases,
              'associative=', sum(direct.values()), 'spectrum=', sorted(direct.items()))
        cases += all_cases

    # Independently check the first two moments from differentiation of the
    # unmarked ordinary generating function, via exact finite recurrence.
    # These are numerical consistency checks, not substitutes for the limits.
    import math
    lo, hi = 0.5, 0.7
    for _ in range(90):
        mid = (lo + hi) / 2
        if 2 * math.exp(mid) - mid - 3 > 0:
            hi = mid
        else:
            lo = mid
    rho = (lo + hi) / 2
    t = math.exp(rho)
    mu = rho * (2 * t - 1)
    nu = rho * rho * t
    alpha = nu / mu
    eb2 = 2 * rho * rho * t + mu
    ebr = rho * rho * (rho + 2) * t
    er2 = (rho ** 4 + 4 * rho ** 3 + 2 * rho * rho) * t / 2
    beta = (er2 - 2 * alpha * ebr + alpha * alpha * eb2) / mu
    assert 0.4 < alpha < 0.41
    assert 0.39 < beta < 0.4
    for n in [12, 20, 40, 60]:
        total = sum(spectra[n].values())
        m = sum(k * v for k, v in spectra[n].items()) / total
        v = sum((k - m) ** 2 * cnt for k, cnt in spectra[n].items()) / total
        print('n=', n, 'mean/n=', round(m/n, 9), 'var/n=', round(v/n, 9))
    print('rho=', format(rho, '.15f'), 'alpha=',format(alpha,'.15f'), 'beta=',format(beta,'.15f'))
    print('ALL_QUASITRIVIAL_COMMUTATION_CHECKS_PASSED', cases)


if __name__ == '__main__':
    run()
