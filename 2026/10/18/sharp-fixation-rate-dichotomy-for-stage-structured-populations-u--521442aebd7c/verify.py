"""Standalone symbolic and numerical checks for pulsed allele-fixation asymptotics.

Run with: python verify.py
The asymptotic theorem is proved analytically in RESULT.md; finite tests are diagnostics.
"""

import numpy as np
import sympy as sp
from scipy.linalg import expm


def positive_perron(matrix):
    eigs, rights = np.linalg.eig(matrix)
    index = int(np.argmax(eigs.real))
    eigenvalue = float(eigs[index].real)
    right = rights[:, index].real
    right *= np.sign(right.sum())
    right /= right.sum()
    eigs_t, lefts = np.linalg.eig(matrix.T)
    index_t = int(np.argmax(eigs_t.real))
    left = lefts[:, index_t].real
    left *= np.sign(left.sum())
    left /= left @ right
    assert np.all(right > 0) and np.all(left > 0)
    return eigenvalue, right, left


def symbolic_checks():
    t, strength, dominance = sp.symbols('t strength dominance', positive=True)
    marginal_resistant = (1 + (1-strength*dominance)*t)/(1+t)
    marginal_susceptible = ((1-strength*dominance)+(1-strength)*t)/(1+t)
    ratio = sp.cancel(t*marginal_susceptible/marginal_resistant)
    expected = t*((1-strength*dominance)+(1-strength)*t)/(1+(1-strength*dominance)*t)
    assert sp.simplify(ratio - expected) == 0
    assert sp.simplify(expected.subs(dominance, 0) - t + strength*t*t/(1+t)) == 0
    resistant, susceptible = sp.symbols('resistant susceptible', positive=True)
    removal = strength*susceptible*susceptible/(resistant+susceptible)
    susceptible_after = susceptible*(1-strength*susceptible/(resistant+susceptible))
    assert sp.simplify(susceptible_after - susceptible + removal) == 0
    print('PASS: exact genotype pulse identities and dominant-resistance quadratic map')


def simulate(A, tau, survival, strength, dominance, steps, checkpoints):
    E = expm(tau*A)
    P = survival[:, None] * E
    eigenvalue, right, left = positive_perron(P)
    selection_average = float(np.dot(strength, right*left))
    R = np.linspace(.2, .4, len(survival))
    S = np.linspace(.9, .6, len(survival))
    outputs = {}
    for step in range(1, steps+1):
        R_before = E @ R
        S_before = E @ S
        susceptible_fraction = S_before/(R_before+S_before)
        resistant_survival = survival*(1-strength*dominance*susceptible_fraction)
        susceptible_survival = survival*(1-strength*dominance-strength*(1-dominance)*susceptible_fraction)
        R = resistant_survival*R_before
        S = susceptible_survival*S_before
        scale = R.sum()
        R /= scale
        S /= scale
        if step in checkpoints:
            outputs[step] = np.array(S/(R+S))
    return E, P, eigenvalue, selection_average, outputs


def multistage_checks():
    A = np.array([[-1.2, 0.0, 1.6], [0.8, -0.65, 0.0], [0.0, 0.4, -0.3]])
    survival = np.array([.26, .42, .19])
    strength = np.array([.65, 0.0, .8])
    E, P, rho, avg, outputs = simulate(A, 2.4, survival, strength,
                                       np.zeros(3), 20000, {1000, 20000})
    target = 1.0/avg
    observed = 20000*outputs[20000]
    assert np.all(np.abs(observed-target) < .004), (observed, target)
    assert np.all(20000*outputs[20000] < 1000*outputs[1000])
    print(f'PASS: three-stage dominant-resistance k*(1-y)={observed}, predicted {target:.9f}')

    h = np.full(3, .4)
    E, P, rho, avg, outputs = simulate(A, 2.4, survival, strength,
                                       h, 1000, {300, 1000})
    Q = (survival*(1-strength*h))[:, None]*E
    rate = np.log(positive_perron(Q)[0]/rho)
    observed_rate = np.log(outputs[1000])/1000
    assert rate < 0
    assert np.all(np.abs(observed_rate-rate) < .002), (observed_rate, rate)
    print(f'PASS: three-stage partial-dominance log rate={observed_rate}, predicted {rate:.9f}')


def one_stage_check():
    # Boundary sanity check: when demographic stage mixing disappears, the
    # classical scalar heterozygote map has the coefficient 1/selection.
    strength = .65
    ratio = .8
    for _ in range(30000):
        ratio -= strength*ratio*ratio/(1+ratio)
    assert abs(30000*ratio -1/strength)<.001
    print(f'PASS: one-stage boundary k*(1-y)={30000*ratio/(1+ratio):.9f}')


def insect_case():
    # The source's Table 2 lists susceptible-genotype survival (delta_11).
    # To preserve those numbers, choose fully dominant resistance with
    # s=1/2 at one selected stage, and set its delta_22=2*delta_11.
    # Other stages have s=0, so their delta_22 equals delta_11.
    a12, a23, a34 = .714, .167, .172
    mu1, mu2, mu3, mu4 = .627, .289, .162, .088
    A = np.array([[-(mu1+a12), 0., 0., 3.069],
                  [a12, -(mu2+a23), 0., 0.],
                  [0., a23, -(mu3+a34), 0.],
                  [0., 0., a34, -mu4]])
    susceptible_genotype_survival = np.array([.172, .241, .003, .052])
    E = expm(20*A)
    asymptotic_coefficients = []
    for selected_stage in range(4):
        d = susceptible_genotype_survival.copy()
        d[selected_stage] *= 2
        assert np.all(d <= 1)
        P = d[:, None]*E
        _, v, w = positive_perron(P)
        pi = v*w
        assert abs(pi.sum()-1)<1.e-10
        asymptotic_coefficients.append(2/pi[selected_stage])
    coeff = np.array(asymptotic_coefficients)
    np.testing.assert_allclose(coeff,
          np.array([8.0627298936, 2.9368065127, 122.2263282041, 3.9952914660]),
          rtol=2.e-7)
    assert coeff[1] < coeff[3] < coeff[0] < coeff[2]
    print(f'PASS: Spinosad susceptible-survival calibrated coefficient examples {coeff}')


if __name__ == '__main__':
    symbolic_checks()
    multistage_checks()
    one_stage_check()
    insect_case()
    print('All diagnostics passed; numerical runs are not substitutes for infinite-time proof.')
