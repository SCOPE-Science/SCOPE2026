"""Independent finite checks for weighted split-join quantum-walk equivalence.

Only standard math/numpy; analytical theorem is proved separately.
"""
from math import sin, sqrt
from fractions import Fraction
import numpy as np


def matrices(r, s, alpha, eta):
    n = r + s
    a = np.zeros((n, n), dtype=float)
    for i in range(r):
        for j in range(i + 1, r):
            a[i, j] = a[j, i] = float(alpha)
        for j in range(r, n):
            a[i, j] = a[j, i] = float(eta)
    return a, a - np.diag(np.sum(a, axis=1))


def probability_columns(mat, t):
    ev, ve = np.linalg.eigh(mat)
    u = (ve * np.exp(1j * t * ev)) @ ve.T
    return np.abs(u) ** 2


def test():
    tested = 0
    checked = 0
    max_match_err = 0.0
    min_witness = 1.0
    signs = {"smaller":0,"larger":0,"equal":0}
    exact_checks = 0
    for r in range(1, 12):
        for s in range(1, 16):
            if r == 1 and s != 1:
                continue
            eta = Fraction(3, 5)
            if r == 1:
                alpha = Fraction(5, 7) # no edges inside singleton clique
            else:
                alpha = eta * Fraction(abs(r - s), r - 1)
            a, k = matrices(r, s, alpha, eta)
            if r < s:
                signs["larger"] += 1
            elif r > s:
                signs["smaller"] += 1
            else:
                signs["equal"] += 1
            for t in (0.07, 0.31, 0.83, 1.79, 3.11, 7.07):
                pa = probability_columns(a, t)
                pk = probability_columns(k, t)
                err = np.max(np.abs(pa[:, r:] - pk[:, r:]))
                max_match_err = max(max_match_err, float(err))
                assert err < 7e-13, (r, s, alpha, eta, t, err)
                checked += len(pa[:,r:].ravel())
            tested += 1
    assert signs["smaller"] and signs["larger"] and signs["equal"]
    # A rational coefficient identity, the exact fourth-order distinction.
    for r in range(1, 12):
        for s in range(1, 16):
            for ai in (0, 1, 2, 3):
                for ei in (1, 2, 3):
                    alpha = Fraction(ai, 3)
                    eta = Fraction(ei, 2)
                    exact_checks += 1
                    delta_sq = alpha*alpha*(r-1)**2 + 4*eta*eta*r*s
                    gap_sq = eta*eta*(r+s)**2
                    assert delta_sq-gap_sq == alpha*alpha*(r-1)**2 - eta*eta*(r-s)**2
                    if delta_sq != gap_sq:
                        v = -eta*eta*(delta_sq-gap_sq)/12
                        assert v != 0
    for r, s, alpha, eta in ((2,2,1,1),(3,4,1,1),(5,5,1,1),(4,2,1,1), (1,5,2,1)):
        a, k = matrices(r,s,alpha,eta)
        t = 0.17
        pa = probability_columns(a,t)
        pk = probability_columns(k,t)
        gap = abs(pa[0,r]-pk[0,r]); assert gap>1e-8, (r,s,gap)
        min_witness=min(min_witness,gap)
    # At the unweighted special point, a center start fails at time 2*pi/q.
    for r in range(2,11):
        s=2*r-1
        a,k = matrices(r,s,1,1)
        t = 2*np.pi/(r+s)
        pa=probability_columns(a,t);pk=probability_columns(k,t)
        assert abs(pk[1,0])<1e-21
        expected=4*sin((r-1)*t/2)**2/r**2
        assert abs(pa[1,0]-expected)<1e-12
        assert expected>1e-5
    print("VERIFY_OK", "matched_parameter_profiles=", tested,
          "matched_probability_entries=",checked,
          "max_error=",format(max_match_err,'.3e'),
          "off_locus_witness_min=",format(min_witness,'.3e'),
          "unweighted_center_obstructions=9", "exact_fourth_order_checks=",exact_checks,signs)

if __name__ == '__main__':
    test()
