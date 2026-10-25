# Scientific review

## Correctness — PASS
The proof directly reconstructs the exact rank-one power-Nyström formula. Spectral weights evolve by exponential tilting, so the weighted mean of the increasing values \(f(a)\) rises while the weighted harmonic mean of the eigenvalues rises. Convexity of \(t\mapsto f(1/t)\) supplies the critical Jensen inequality \(f(\lambda_q)\le\sum_i p_i(q)f(a_i)\). These three independently checked facts imply the squared Frobenius error derivative is nonpositive, and strictness follows under the stated spectral support hypothesis. Fixed-seed asymptotics follow from the two largest supported eigenvalues. The Gaussian formula follows from an exact half-Cauchy density and two elementary integrals. A rational example shows the weaker scalar-monotonicity class can fail.

The standalone standard-library verifier passed 18,081 cross-checks of independently formed full matrices, reduced formulas, rational identities, Gaussian quadrature, and asymptotic coefficients. Numerical experiments are auxiliary, not proofs of universal statements.

## Originality — PASS, qualified
The primary 2022 funNyström paper introduces the algorithm and studies high-probability errors, whereas the 2023 algorithm-agnostic paper establishes near-optimality transfers and discusses power-iteration improvement for approximating \(A\) itself. Those statements do not by themselves give the transformed pathwise Frobenius theorem, exact Gaussian mean risk, or rate-exponent separation. published-finding corpus semantic searches for matrix-function Nyström rank-one power iterations, pathwise monotonicity, Gaussian mean rates, and exact two-dimensional risks did not identify a dominating scientific claim. Search failure alone does not prove originality; the exact theorem/proof comparison supports this provisional status. Residual risk: a related one-vector spectral-tilting or matrix-function projection argument may have appeared under a different name.

## Mathematical value — PASS
The distinction between sketchwise and expected error is mathematically substantive in randomized numerical linear algebra: additional power iterations improve every individual realization, yet rare nearly orthogonal Gaussian sketches determine a strictly slower expectation rate. The closed two-eigenvalue formula makes the distinction exact; the constructive monotone-function counterexample identifies why the operator-monotone/reciprocal-convex condition matters. No general rank or finite-precision claim is inferred.

## Comparison and limitations
Closest: Persson–Kressner, arXiv:2209.11023 (power-Nyström for operator-monotone functions); Persson–Meyer–Musco, arXiv:2311.14023 (algorithm-agnostic error transfer and improvement for \(A\)); Gittens–Mahoney, arXiv:1303.1849 (structural Nyström approximations). The exact claim remains restricted to rank-one approximations, fixed seeds, and the two-dimensional Gaussian expected-risk model. Priority against all mathematical literature is not independently certified.

Self-review: passed. Independent audit: not yet performed.
