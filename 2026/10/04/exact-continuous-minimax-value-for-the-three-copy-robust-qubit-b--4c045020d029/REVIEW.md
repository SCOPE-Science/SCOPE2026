# Same-model review

## Correctness
PASS. The proof reduces the binary POVM to a Hermitian contraction on the four-dimensional symmetric subspace. The three-point nuisance prior gives an exact Helstrom upper bound because its averaged difference matrix has spectrum \(\{-\sqrt{2114}/104,0,0,\sqrt{2114}/104\}\). The proposed measurement is valid because its kernel correction has eigenvalues \(\pm4/39\), while the complementary two-dimensional subspace carries eigenvalues \(\pm1\). Its success profile factors into nonnegative terms on the entire nuisance interval, so the continuum lower bound is analytic rather than numerical.

Risk: transcription errors in the explicit matrices or normalization would invalidate the exact constant. These identities were independently reconstructed and replayed from the packaged checker; the checker is corroborative and the displayed analytic factorization supplies the infinite-interval argument.

## Originality
PASS. The 2026 source treats exactly this benchmark numerically, reporting \(0.72\) after finite-grid optimization and finer-grid evaluation, and explicitly distinguishes the finite-grid problem from the continuous one. It does not state the exact value, the three-point weights, or a closed-form continuous success profile. The closest general minimax state-discrimination paper from 2005 minimizes over unknown state-label priors, not over a common external unitary nuisance parameter with fixed label priors. Robust binary coherent-state work concerns a different physical family and receiver-imperfection model.

Residual risk: an equivalent semi-infinite robust binary-detection calculation could exist under older control-theoretic or covariant-detection terminology not surfaced by the targeted searches. No searched source implied the displayed benchmark-specific constant or profile.

## Value
PASS. The result replaces the source paper's illustrative rounded grid value by an exact continuous optimum and supplies both sides of a sharp certificate: a finite-support least-favorable prior and an explicit collective measurement valid for every nuisance value in the interval. This directly addresses the source paper's stated discretization limitation and provides a reusable exact benchmark for testing future continuous-parameter algorithms.

The contribution is deliberately narrow: it solves one benchmark exactly and does not claim a general closed form for arbitrary copy number or nuisance interval.

## Closest literature and limitations
The primary comparison is arXiv:2609.04020v1, Sec. IV.2 and Table 1. The main broader comparison is arXiv:quant-ph/0504048. The 2018 coherent-state robustness paper is physically related but not implication-covering. The remaining risk is terminological rather than a known stronger theorem.

Same-model review: passed. Independent audit: not yet performed.
