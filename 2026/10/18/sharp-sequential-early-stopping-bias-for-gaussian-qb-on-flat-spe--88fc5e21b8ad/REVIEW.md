# Scientific review

## Correctness

**PASS.** The theorem is scoped to real standard-Gaussian unit-block QB on the identity. The source algorithm is specialized exactly: each fresh residual innovation has independent \(\chi^2_{n-i+1}\) norm-square and independent complement \(\chi^2_{i-1}\), jointly independent across inspections. This proves the incomplete-beta inspection law with the stated degrees of freedom. Uniform concentration of the running norm and upper/lower chi-square moderate deviations give the extreme-value threshold \(\sqrt2\,\varepsilon\) rather than a finite-simulation inference. The optional prune alters the rank by at most one; exact projection error is \(\sqrt{n-K_n}\). Numerical checks verify the finite QR representation and beta marginal, with remaining finite-dimensional deviations explicitly acknowledged.

## Originality

**PASS under accessible evidence, with source-coverage risk.** Source code `randQB_MF_Fro.m` and `Prune_Rank_Fro.m` were read in full, including the stopping branch, norm estimator, and rank pruning. They specify the algorithm but do not report the sharp sequential first-hit law. Yu–Gu–Li's exact-energy indicator has no random inspection first-crossing bias; the classical independent-probe literature gives single-test error control rather than the derived identity-matrix sequential asymptotic. Relevant indexed research records and web literature were searched using aliases for Gaussian QR, randomized QB, chi-square first passage, and repeated testing. No located result implied both the exact beta inspection law and the \(\sqrt{n\log n}\) rank shift. The motivating 2026 manuscript and some broad background works were inaccessible in full and could conceivably contain a stronger comparison.

## Value

**PASS.** A flat-spectrum input is a canonical calibration case for rank-revealing algorithms. Independent unbiased residual estimators may seem protective against adaptive stopping errors, but the theorem proves a diverging rank deficit and a probability-one asymptotic accuracy miss with sharp constants. The universal normalized error overshoot identifies a concrete multiple-inspection risk even in exact arithmetic and without residual-estimator reuse.

## Limits

The finding does not establish a fixed-size practical failure rate or failure on the empirical workloads of the motivating manuscript. The additive error overshoot vanishes as dimension increases even though its sign and sharp scale are determined. Full text of the motivating manuscript was unavailable; only its complete companion algorithm implementation, abstract, and bibliographic metadata were inspected.

Self-review: passed. Independent audit: not yet performed.
