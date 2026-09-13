# Even–odd variance oscillation for the cubic trace in the symmetric two-cut quartic model

## Context

In Hermitian one-matrix models with a multi-cut equilibrium measure, fluctuations
of linear eigenvalue statistics decompose into a continuous Gaussian part and a
discrete part coming from filling-fraction fluctuations. General theorems of
Borot–Guionnet and Shcherbina establish this Gaussian-plus-discrete-Gaussian
structure with quasi-periodic dependence on N, but leave the period matrix,
Bergman-kernel constant, conditional-mean gap, and theta-function values
unevaluated at any specific point. This record gives the fully evaluated case
at a natural integer reference point for the observable most sensitive to
filling imbalance.

## Definitions

Let mu_N(dM) = Z_N^{-1} exp(-N Tr(-2 M^2 + M^4/4)) dM on N x N Hermitian
matrices, i.e. potential V(x) = x^4/4 - 2 x^2, at (r,g) = (-4,1), h = 0, in the
symmetric two-cut regime. Define v_N = N^2 Var_{mu_N}(N^{-1} Tr M^3), which
equals Var(Tr M^3). Let v_even = lim_k v_{2k} and v_odd = lim_k v_{2k+1} when
the limits exist.

## Result

The full limit lim_{N->infinity} v_N does not exist. The even and odd
subsequential limits exist, are finite, and are distinct:

v_even = 20.638585560287026, v_odd = 85.23552024924541,

with decomposition v_even = V_G + c0^2 V_even^d, v_odd = V_G + c0^2 V_odd^d,
where V_G = 8c + 16 ≈ 18.16355553661471 with c ≈ 0.27044444207683908,
c0 ≈ 16.37807472315768 (c0^2 ≈ 268.24133163733653),
V_even^d = sum k^2 q^{k^2}/sum q^{k^2} ≈ 0.009226877933258118,
V_odd^d = sum (k+1/2)^2 q^{(k+1/2)^2}/sum q^{(k+1/2)^2} ≈ 0.25004336320292464,
q = exp(-pi t) ≈ 0.004656401135402466, t = f_B/f_A ≈ 1.7091688865574871,
f_A ≈ 0.8283190851182971, f_B ≈ 1.4157372084259562. In particular
v_odd - v_even ≈ 64.6 ≠ 0.

## Proof / evidence

Equilibrium: loop-equation ansatz gives sigma(x) = x^4 - 8x^2 + 12, so
a^2 = 2, b^2 = 6, support [-b,-a] ∪ [a,b], density
rho(x) = x sqrt((b^2-x^2)(x^2-a^2))/(2 pi) on [a,b] with even extension, mass
1/2 per cut (verified by quadrature), square-root edge vanishing, fillings
(1/2,1/2).

Two-point kernel: genus-one W_{2,0} of the form (1) with
Q = x1^2 x2^2 - 4x1^2 - 4x2^2 + 12 + c(x1-x2)^2; the constant c = 2C is fixed by
vanishing A-periods. Numerically K(x2)/(2 f_A) is x2-independent to ~1e-15 over
{0, 0.5, 3, 10, i}, giving C ≈ 0.13522222103841954,
c ≈ 0.27044444207683908. Independently re-verified.

Gaussian part: with x_i = 1/u_i and s_e expansion
(1-8u^2+12u^4)^{-1/2} = 1 + 4u^2 + 18u^4 + 88u^6 + O(u^8), exact truncated
polynomial matching gives M/(u1-u2)^2 coefficient of u1^2 u2^2 equal to
16c + 32, hence Cov_G(3,3) = 8c + 16 ≈ 18.16355553661471. Independently
confirmed by symbolic solve; sanity checks Var_G(Tr M^2) = 2.

Discrete part: normalised holomorphic differential gives period tau = i t with
t = f_B/f_A = K(1-lambda)/K(lambda), lambda = ((b-a)/(b+a))^2 ≈ 0.0717967697,
nome q = e^{-pi t} ≈ 0.004656401135402466. Filling fluctuation n_+ - N/2 is
asymptotically an independent discrete Gaussian on Z (even N) or Z + 1/2
(odd N) with zero tilt by symmetry. Conditional means: unnormalised
mu_+ = ∫_a^b x^3 rho ≈ 4.09451868078942, so gap c0 = E_+ - E_- ≈ 16.37807472315768.
Theta sums give V_even^d ≈ 0.009226877933258118 and
V_odd^d ≈ 0.25004336320292464.

Separation: with q ≤ 0.005, V_even^d ≤ 0.011 and |V_odd^d - 1/4| ≤ 0.002 by
geometric tail domination; with c0^2 ≥ 100 (restricting ∫x^3 rho to [2,√6]),
v_odd - v_even ≥ 20 > 0 (numerically ≈ 64.6). The o(1) is uniform in parity,
so even/odd subsequences converge to the stated finite values while the full
sequence cannot converge.

## Limitations

The o(1) uniformity of the multi-cut Gaussian-plus-discrete-Gaussian expansion,
edge regularity, and theta-characteristic shift are invoked from the cited
multi-cut works rather than re-proved. Numerical enclosures are
validated-quadrature values at 80-digit precision with grid/precision
cross-checks, not formal interval arithmetic; the inequality v_even ≠ v_odd
uses only crude analytic bounds robust to quadrature error < 1.

## Reproducibility

Script output/artifacts/compute_values.py (mpmath, 80 digits) recomputes
f_A, f_B, t, C/c, V_G, mass, mu, c0, q, theta sums, v_even, v_odd, and the gap,
with grid-independence and tail-bound checks; all values reproduced to ≥12
digits in independent re-execution.

## References

- G. Borot, A. Guionnet, Asymptotic expansion of beta matrix models in the
  multi-cut regime, Forum Math. Sigma (2023).
- M. Shcherbina, Fluctuations of linear eigenvalue statistics of beta matrix
  models in the multi-cut regime, arXiv:1205.7062.
- J. Baik–Deift–Johansson; Deift–Kriecherbauer–McLaughlin edge-regularity;
  Eynard–Orantin topological recursion; Akemann two-cut Bergman kernel.
