# Exact mosaic mobility edge at Liouville frequency: a proved Gordon window

## Context

The kappa=2 quasiperiodic mosaic Schroedinger operator on l^2(Z),

(H_theta u)_n = u_{n+1} + u_{n-1} + V(n) u_n, V(n) = 2 lambda cos(2 pi (theta + n alpha)) if n even, 0 otherwise,

with fixed lambda != 0 and irrational frequency alpha, admits exact mobility edges Ec = +-1/lambda when alpha is Diophantine (Wang-Xia-You-Zheng-Zhou; Wang et al. PRL 2020): purely absolutely continuous (a.c.) spectrum for every theta at |E| < 1/|lambda| and Anderson localization for a.e. theta at |E| > 1/|lambda|. The target question asks whether this verbatim dichotomy persists for fixed Liouvillean alpha with 0 < beta(alpha) < infinity, or whether an intermediate singular-continuous window opens around Ec, with sharp arithmetic threshold delta(alpha) set by beta(alpha) or beta(2 alpha).

## Definitions

beta(omega) = limsup_q (-log ||q omega|| / q) measures exponential Liouvillean quality (beta = 0 iff Diophantine in the exponential sense; 0 < beta < infinity is the Liouvillean regime). W := {E : 1 < |lambda E| < e^{beta(2 alpha)}} is the candidate window above Ec. E=0 is excluded from the reduction; the transition lines |lambda E| = 1 and |lambda E| = e^{beta(2 alpha)} are excluded from all spectral-type conclusions.

## Result (proved headline)

Let lambda != 0, alpha with 0 < beta(alpha) < infinity, E != 0, excluding |lambda E| = 1 and |lambda E| = e^{beta(2 alpha)}. Then:

1. Arithmetic lemma: beta(alpha) <= beta(2 alpha) <= 2 beta(alpha); hence delta(alpha) := beta(2 alpha) satisfies 0 < delta < infinity and W is a nonempty open union of two intervals around +-1/lambda.
2. Exact reduction: for E != 0 the even sublattice v_m = u_{2m} satisfies exactly v_{m+1} + v_{m-1} + 2 (lambda E) cos(2 pi (theta + 2 m alpha)) v_m = (E^2 - 2) v_m, i.e. an effective almost Mathieu equation with coupling lambda_eff = lambda E, frequency 2 alpha, energy E' = E^2 - 2, via exact constant conjugacy P D_E P^{-1} = S^eff with P = [[1,0],[-1,E]].
3. On-spectrum Lyapunov formula: for E in the spectrum, L(E) = (1/2) max{0, log|lambda E|}, by Avila global theory on the conjugate AMO cocycle.
4. Unconditional Gordon window: for every theta, H_theta has no eigenvalue anywhere in W. Hence verbatim Anderson localization immediately above Ec is false.
5. Conditional character: since L(E) > 0 on W intersected with spectrum, Kotani theory gives no a.c. component there; so sigma(H_theta) cap W, whenever nonempty, is purely singular continuous. Nonemptiness of W cap sigma in infinite volume is not proved here.

## Proof / evidence

Lemma: beta(2 alpha) = limsup_m (-log ||2 m alpha|| / m) <= 2 beta(alpha) since evens form a subset of integers; conversely ||2x|| <= 2||x|| along alpha-resonances gives beta(2 alpha) >= beta(alpha). Conjugacy verified by direct multiplication (P D_E P^{-1} = [[E a - 2, -1],[1, 0]] = S^eff, det 1) and numerically to <= 8.9e-16. Schur reduction: odd-site equation E u_{2m+1} = v_m + v_{m+1} (E != 0) gives u_{2m+1} = (v_m + v_{m+1})/E; an l^2 mosaic eigenfunction induces a nonzero l^2 effective eigenfunction (restriction v in l^2; if v = 0 then odd sites vanish). Fixed-E Gordon transfer: at E in W, 0 < log|lambda E| < beta(2 alpha); 2 alpha convergents satisfy ||q_n 2 alpha|| < e^{-(beta(2 alpha)-o(1)) q_n}, potential mismatch <= e^{-(beta(2 alpha)-o(1)) q_n} beats Lyapunov growth e^{(log|lambda E|+o(1)) q_n}, blocking l^2 solutions pointwise in E and uniformly in theta; no Fubini or LDT input needed. L > 0 on W kills a.c. by Kotani conditional on spectrum intersection. Finite-volume numerics (L=400) are illustrative only.

## Limitations

Transition lines |lambda E| = 1, e^{beta(2 alpha)} excluded; E = 0 excluded. Population of the window (W cap sigma != empty) not proved. Subcritical purely-a.c. transfer (C1) and sharp supercritical a.e.-theta localization above e^{beta(2 alpha)}/|lambda| (C2) are explicitly demoted to conjectures: uniform large-deviation/Green estimates, E-dependent conjugacy norm control, Fubini measure unification, and singular-strip spectral-measure transfer are missing.

## Reproducibility

Artifacts: mosaic_window.py (Liouvillean alpha construction, conjugacy check, LE curve, finite-volume window counts) and mosaic_window.json (parameters, LE rows, IPR representatives). Conjugacy identity re-verified symbolically. Infinite-volume claims depend only on the analytic proof, not on numerics.

## References

Wang et al., PRL 125, 196604 (2020), arXiv:2004.11155; Wang-Xia-You-Zheng-Zhou, CMP (2023), arXiv:2110.00962; Avila-Jitomirskaya-Zhou, Math. Ann. 370, 271-285 (2018); Avila, Acta Math. 215 (2015); Gordon-Jitomirskaya-Last-Simon, Acta Math. 178 (1997).
