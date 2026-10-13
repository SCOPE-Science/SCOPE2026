# Scientific review — correlated rare-disease pooling

## Correctness — PASS

The beta integral gives the exact negative-pool probability \(Q_k=(\tau-a)_k/(\tau)_k\). The adjacent-cost identity is verified by a one-step recurrence and its normalized comparison ratio is strictly increasing for \(0<a<\min\{1,\tau\}\). The gamma-ratio tail proves the threshold is crossed at most once and eventually. Uniform logarithmic expansion of the beta product, together with digamma harmonic sums, then proves that every minimizing size obeys \(a k_*\to1\) and fixes the constant in the two-term cost expansion. The independent-comparison bound follows from matching upper and lower scales. Exact rational test cases and numerical examples were reproduced with the included verifier. The proof is mathematical; the samples alone do not certify the asymptotic.

## Originality — PASS, with residual risk

Lendle, Hudgens, and Qaqish's correlated pooled-screening model directly encompasses the beta-mixture assumptions and already gives expected-test formulae. Augenblick et al. already demonstrate that correlation favors larger groups. Landolfi and Lall provide a more general finite optimization framework for exchangeable testing. The assessed incremental claim is the precise rare-prevalence asymptotic at fixed positive correlation, plus the explicit all-size adjacent-sign unimodality criterion; these statements are not found in the materially inspected portions of accessible full primary works. **Important residual risk:** the complete Lendle manuscript, including any mathematical appendix, could not be retrieved from authorized sources, so equivalent pre-existing analytic coverage remains possible. Other mathematical formulations of beta-ratio optimizing sequences might also subsume the result.

## Value — PASS

The theorem resolves an interpretable screening-design singular limit: constant positive intracluster correlation changes the scaling of optimal pool size from inverse-square-root prevalence to inverse prevalence, and of minimal expected assay demand from square-root prevalence to prevalence times its logarithm. The leading constants and one-crossing decision rule can be checked for arbitrary admissible beta-mixture parameters. These facts have model-design value even without a finite-population cost-benefit optimization, although the required large pools may be medically infeasible because of dilution or cluster-size limits.

## Limitations

Perfect equal-cost tests, beta-mixture within-pool exchangeability, fixed concentration, and unlimited group size are necessary model assumptions. No epidemiological detection guarantee or optimality for heterogeneous constrained pools is asserted. The closest inaccessible primary appendix poses a real historical-coverage risk, not a theorem-verification gap.

Self-review: passed. Independent audit: not yet performed.
