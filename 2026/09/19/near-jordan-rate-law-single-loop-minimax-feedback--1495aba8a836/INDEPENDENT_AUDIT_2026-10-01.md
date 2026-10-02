# Independent mathematical audit — SCOPE-20260919-1495aba8a836

Final disposition: **PASS**.

## Correctness
**PASS** — The stated two-dimensional feedback recurrence was independently reconstructed algebraically from the package's explicit update specialization. Exact symbolic calculation gives det(M)=alpha A. After clearing the positive denominator, the discriminant is the stated degree-nine polynomial times a positive factor; expressing its negative in the degree-nine Bernstein basis gives ten strictly positive coefficients, certifying a complex-conjugate pair for every kappa at least one. Series expansion then yields the displayed damping, phase, H-limit, and sign-flip constants. These are analytic certificates, not a replayed success log.

## Originality
**PASS** — Resultary search found no earlier published theorem with this exact feedback block or near-Jordan constants. The complete current v2 of Zhang-Xu was inspected through all 19 pages: it gives the algorithm, Lyapunov convergence theorem, experiments, and complexity result but no exact separable-quadratic spectral law, all-kappa underdamping certificate, sign-reversal law, or these constants. The assigned record concerns the earlier v1 parameter specialization; the source has since revised its recommended parameter regime, which is retained as a relevance/originality risk but does not create prior coverage.

### Equivalent formulations
Generic accelerated or underdamped interpretations do not imply the source-specific exact matrix law.

### Broader coverage
General convergence bounds do not determine the exact eigenvalues, phase, or first-sign-reversal law.

### Exact database or table
No external finite database is relevant; the exact-result search was for prior theorem coverage.

### Claim versus prior implication
The final claim is additional exact dynamics rather than a corollary of the source convergence theorem.

## Value
**PASS** — The exact mode analysis exposes a nontrivial dynamical mechanism behind a newly proposed feedback method: the square-root condition scale is genuinely realized on a separable quadratic while the theorem's logarithmic condition-number overhead is not. The all-kappa underdamping certificate and quantitative phase/damping law are structural, not a routine rate substitution.

## Source inspections
- **Near-Optimal Single-Loop Predictor-Corrector Extragradient Method for Strongly Convex-Strongly Concave Minimax Optimization** (https://arxiv.org/abs/2609.20327): complete 19-page current v2, including Algorithm 1, Section 3 Lyapunov theorem, experiments, conclusion, and references Assessment: PRIMARY_SOURCE_NOT_COVERING_EXACT_V1_MODE_LAW. Evidence: The paper proves a general Lyapunov rate and gives experiments but does not state the assigned exact two-by-two spectral formulas or underdamping theorem.
- **Assigned verification program** (repository artifact artifacts/verify_near_jordan_feedback.py): complete source program plus independent symbolic reconstruction of its certificate Assessment: SUPPORTING_COMPUTATION_RECONSTRUCTED. Evidence: The determinant identity, discriminant factorization, positive Bernstein coefficients, and asymptotic series were independently checked.

## Residual risks
- The motivating paper was revised to v2 on September 28 with a changed recommended parameter regime, so the exact constants apply to the explicitly stated v1 specialization rather than automatically to the current prescription.
- An equivalent control-theoretic analysis under different terminology could exist outside the searches performed.
