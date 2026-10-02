# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-e4dd7b4e2fba`

## Correctness — PASS

The theorem reconstructs exactly. With \(M=D+L\), direct multiplication gives \(M^T B M=D-L^T D^{-1}L\), so congruence yields the iff positivity condition \(I-C^TC\succ0\), equivalently \(\|C\|_2<1\). In normalized variables \(X=(I+C)^{-1}\), the identities \(\widetilde B=X+X^T-I=X^T(I-C^TC)X\) and \(\widetilde B^{-1}-H=CC^T+(I+C)C^TC(I-C^TC)^{-1}(I+C^T)\succeq0\) give \(0\prec B\preceq A^{-1}\). Expanding \(\widetilde B H-I\) gives exactly \(-XCC^T-X^TC^TC\), proving the quadratic norm bound. The affine-family first-order matching, the rational three-by-three SPD/indefinite counterexample, and the two-block singular-value formula all check directly. The package verifier was read completely and independently reproduces the algebra numerically; it is corroboration rather than proof.

### Correctness sources

- assigned RESULT.md at tree 6367690d30c1fb7a341a895032594677bb6f1113
- artifacts/verify_abgs.py and verification.txt
- Bai 2003 additive/multiplicative splitting framework
- Saye, arXiv:2606.12577

### Correctness risks

- The condition-number estimate is a worst-case small-coupling bound, not a practical speed guarantee.
- Finite numerical checks do not establish the infinite-dimensional or all-matrix theorem; acceptance rests on the exact algebra.

## Originality — PASS

Fresh semantic searches found the audited formula as the only exact published match. Classical Gauss-Seidel/SSOR, symmetric extrapolation, general additive splitting, and Saye's recent cascading smoothers cover neighboring algorithmic ideas, but no inspected statement gives this specific diagonal-corrected inverse together with its congruence factorization, exact \(\|C\|_2<1\) safety threshold, SPD-system counterexample, and quadratic preconditioned-error law. Several older papers remain a genuine full-text access risk, so this is a best-of-knowledge pass rather than a priority certificate.

### equivalent_formulations

Searches:
- Resultary: additive bidirectional Gauss-Seidel inverse diagonal corrected SPD threshold
- web search: exact algebraic form `(D+L)^-1 +(D+L^T)^-1-D^-1` and symmetric extrapolated Gauss-Seidel

Evidence:
- The exact Resultary hit is the audited theorem; other hits concern different GS/Jacobi stability questions.
- The located Evans–Li–Xue and Evans–Li papers concern extrapolated GS convergence/spectral radius rather than the audited additive inverse statement.

Reasoning:
Equivalent formulations via a congruence of the preconditioner, a parallel additive forward/backward action, and a first-order-cancelled inverse expansion were searched.

### broader_coverage

Searches:
- Bai 2003 additive/multiplicative splitting iterations
- Saye 2026 cascading smoothers
- classical SSOR/SGS reviews

Evidence:
- Bai's abstract treats general additive/multiplicative iteration convergence; Saye's additive construction is Jacobi-style and his multiplicative construction is Gauss-Seidel-style, not their diagonal-corrected sum.

Reasoning:
These broader frameworks do not mechanically supply the exact audited matrix identity or threshold.

### exact_database_or_table

Searches:
- Resultary current numerical-linear-algebra findings
- standard preconditioner review literature

Evidence:
- No exact preconditioner table/database entry containing this operator and threshold was located.

Reasoning:
The claim is an algebraic theorem, not a table lookup.

### claim_vs_prior_implication

Searches:
- implication comparison with SGS, SSOR, extrapolated GS, and generic additive splitting

Evidence:
- Standard SGS has normalized form \(X^TX\), whereas the audited operator is \(X+X^T-I\); their difference is a nonzero quadratic term. Generic splitting convergence does not imply the audited iff SPD threshold or inverse dominance.

Reasoning:
The final claim is not a corollary of the inspected neighboring theorems.

### source_inspections

- **On the convergence of additive and multiplicative splitting iterations for systems of linear equations** — https://doi.org/10.1016/S0377-0427(02)00822-1. Trigger: Closest classical general additive-splitting source. Material read: Published abstract and bibliographic scope; no lawful full text was located in the searched open sources during this run. Method: Scope and implication comparison. Assessment: No covering statement located; residual access risk remains. Evidence: The abstract concerns convergence of general additive/multiplicative splitting iterations for Hermitian and non-Hermitian systems, not the audited inverse formula.
- **The extrapolated Gauss-Seidel methods and generally consistently ordered matrices** — https://doi.org/10.1080/00207168708803609. Trigger: Plausible historical forward/backward/extrapolation overlap. Material read: Published abstract and bibliographic scope. Method: Primary-source scope comparison. Assessment: Not covering on accessible material. Evidence: It studies EGS1/EGS2 convergence and optimum extrapolation factors for consistently ordered matrices.
- **Cascading Smoothers for Multigrid** — https://arxiv.org/abs/2606.12577. Trigger: Recent additive versus multiplicative smoother work. Material read: Primary abstract and detailed public description of the additive and multiplicative formulations. Method: Method comparison. Assessment: Not covering. Evidence: Its additive formulation is a sequence of optimized block-diagonal Jacobi-style actions, whereas the audited theorem studies a fixed sum of forward/backward triangular inverses.
- **Assigned verification program** — artifacts/verify_abgs.py. Trigger: Critical identities and counterexample. Material read: Complete source and saved output. Method: Line-by-line inspection plus independent algebra. Assessment: Correct corroboration. Evidence: Factorization, inverse dominance, quadratic error identity, explicit counterexample, and two-block product all reproduce.

### checked_sources

- current Resultary exact-form search
- https://doi.org/10.1016/S0377-0427(02)00822-1
- https://doi.org/10.1080/00207168708803609
- https://doi.org/10.1016/0024-3795(88)90226-1
- https://arxiv.org/abs/2606.12577
- assigned RESULT.md and verifier

### residual_risks

- Full texts of Evans–Li–Xue 1987, Evans–Li 1988, and Bai 2003 were not available through the searched open routes, so differently phrased historical coverage remains possible.

## Scientific value — PASS

The result addresses a motivated parallelization tradeoff: replacing multiplicative symmetric Gauss-Seidel by two independent triangular actions on the same residual can destroy positivity. The exact safety threshold, explicit SPD counterexample, and second-order weak-coupling clustering quantify precisely when the construction is mathematically safe and why it can approximate the inverse unusually well. This is a structural preconditioner theorem rather than a routine numerical benchmark.

### Value sources

- assigned exact factorization and counterexample
- classical SGS comparison
- current additive/multiplicative splitting literature

### Value risks

- No claim of practical speedup, floating-point stability, or superiority to SGS is made.

## Limitations

- Finite-dimensional real SPD matrices with a fixed SPD block-diagonal split are assumed.
- The additive inverse can be indefinite even when the system matrix is SPD.
- The condition-number bound is a weak-coupling theorem, not a performance guarantee.
- Historical originality remains best-of-knowledge because several older full texts were inaccessible.

## Disposition

**PASSED**
