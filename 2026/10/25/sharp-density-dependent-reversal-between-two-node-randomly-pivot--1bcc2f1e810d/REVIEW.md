# Scientific assessment

## Correctness — PASS

The feature-map proof identifies the unique normal to two distinct site features, projects the kernel mean feature onto that normal, and averages first over common rotation and then over the site separation. The RP residual density is computed directly from the original Schur-complement pivot rule and normalized explicitly; the iid expectations reduce to an elementary exact trigonometric integral. Algebraic factorization gives the full strict/equality boundary at kernel amplitude \(b=8\) and the density-modulation threshold \(t=\sqrt{8/b}\) for \(b>8\). The standalone numerical verifier passed its 3,170 assertions; analytical identities, not those tests, support the all-parameter statements.

## Originality — PASS with residual uncertainty

The 2023 RPCholesky quadrature paper already defines the sampling and optimal weights and empirically compares iid and RPCholesky, without deriving the two-point, target-dependent sharp comparison. A particularly strong prior result, the 2020 continuous volume sampling expected interpolation-error formula, **already covers the RP-only risk** because these two-node laws coincide for the stationary circle kernel. The new assessed claim is precisely the iid-versus-RP comparison and its uniform positive-density dominance boundary and reversal. No covering statement was identified by the recorded published-finding corpus searches or inspected source texts; unlocated specialized two-node Fourier examples remain a priority risk. No claim of discovering volume sampling or RPCholesky is made.

## Mathematical value — PASS

The 2023 source directly motivates empirical comparison against iid optimally weighted kernel quadrature. The complete sharp calculation for the first nontrivial finite-rank translation-invariant kernel shows that numerical rankings depend jointly on kernel amplitude and target-density modulation. It gives an exact, reproducible positive-density benchmark and a natural failure boundary for uniform superiority rather than an arbitrary slice or negligible constant improvement. This is a narrow two-node classification, not a general error-rate theorem.

## Limits and closest work

The comparison concerns only expected **squared worst-case RKHS error**, optimal unrestricted weights, two nodes, and a rank-three circle kernel. Belhadji–Bardenet–Chainais, Theorem 4 (2020), covers the separate volume-sampling risk but not the iid difference law or crossover. Epperly–Moreno (2023), Sections 3–5, covers both sampling methods and numerical comparisons but not the stated exact formulas. Potential equivalent specialized Fourier calculations have not been excluded comprehensively.

Self-review: passed. Independent audit: not yet performed.
