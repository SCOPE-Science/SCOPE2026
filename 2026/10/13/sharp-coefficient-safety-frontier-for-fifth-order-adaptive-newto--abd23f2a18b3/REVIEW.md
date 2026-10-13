# Self-review

## Correctness — PASS

The matrix update retains its singular vectors and is exactly a scalar iteration on each positive singular value. The derivative of the scalar squared-magnitude map factors, leaving one maximizer on the initial residual interval. The identity comparing this maximum with the negative fixed-point barrier yields the explicit cubic threshold. Below the threshold, the open interval \((-1/(2u),1)\) is invariant for every admissible coefficient, with strict positive/negative residual monotonicity. That proves convergence under arbitrary coefficient switching. An exact residual expansion proves eventual uniform quadratic convergence. At and above the threshold, the maximizing starting value reaches the exceptional non-unit fixed point or enters a divergent half-line, respectively. The identities were reconstructed and evaluated from the included verification program. No finite experiment is invoked as proof.

## Originality — PASS, with residual literature risk

The primary comparison is PRISM, arXiv:2601.22137v1: its Section 4 and Appendix A.1 specify the same degree-two residual polynomial and empirically recommend \([3/8,29/20]\); Theorem 2 and Appendix B concern degree one. The new theorem proves pathwise convergence for the empirically recommended fifth-degree interval, derives the exact cubic endpoint, and shows sharp endpoint/supercritical failures for arbitrary bounded coefficient schedules. Polar Express, arXiv:2505.16932v5, instead optimizes compositions of unrestricted odd-degree polynomials for spectral minimax error; the Chebyshev-type CANS study, arXiv:2506.10935v2, uses interval-dependent best-approximation polynomials. Neither directly implies this exact coefficient interval or arbitrary-switching invariant set. Closest indexed mathematical results concern two-stage Richardson, scalar Newton relaxation, and Aitken–Steffensen; their scalar maps and objects differ. No uniqueness inference is based simply on lack of search hits. An equivalent older scalar-iteration classification may exist.

## Value — PASS

The motivating computational method provides an empirically selected fifth-degree coefficient constraint, yet its analysis concentrates on degree one. Rigorous safety for **every** adaptive or randomized coefficient choice is an operationally meaningful gap because sketch errors cannot invalidate the mathematical convergence conclusion once the coefficient is constrained. The exact frontier identifies only a small margin between the recommended upper coefficient \(29/20\) and the first possible obstruction, while proving that enlarging the allowable range beyond the cubic root makes worst-case divergence possible even for one positive singular value. This is a structural robustness boundary, not a reparameterization of a standard Newton convergence rate.

## Scientific limitations and relationship to literature

The exact-arithmetic full-rank hypothesis and normalization are essential to the stated proof. The counterexample concerns arbitrary constant coefficients at/above the frontier, not necessarily the coefficient chosen by any least-squares sketch policy. Unconditional convergence alone does not provide uniform finite-time complexity or finite-precision guarantees. The main unclosed originality risk is equivalent older work in polynomial matrix-sign/polar iteration under alternative notation.

Self-review: passed. Independent audit: not yet performed.
