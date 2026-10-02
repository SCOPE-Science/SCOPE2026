# Independent scientific audit — SCOPE-20260918-120f5c07b3b8

Audited at: 2026-10-01T07:11:57.147372Z

Disposition: **passed**

## Correctness — PASS

The identity is exact. Writing the normalized inverse covariance as \(T_N(\rho)=\rho T_N(1)+(1-\rho)^2I+\rho(1-\rho)(e_0e_0^T+e_{N-1}e_{N-1}^T)\), DCT-II conjugation diagonalizes \(T_N(1)\) and maps the two endpoint vectors to \(q\) and \(Sq\). This gives the two parity-separated diagonal-plus-rank-one blocks for every \(N\ge2\). The odd DCT-II parity split then gives the DCT-VI/DCT-VIII fixed cores. An independent numerical reconstruction over several sizes and correlations reproduced the full-order identity to about \(2.3\times10^{-15}\), while the repository verifier independently checks additional parity and diagonalization residuals; the analytic proof does not depend on those finite tests.

## Originality — PASS

The two highly relevant 2026 primary papers were inspected in full. The fixed-core paper explicitly restricts its theorem to even order, whereas the all-order paper's odd factorization proceeds through the residual KLT and an arrowhead stage. Neither supplies the nonrecursive odd DCT-VI/DCT-VIII diagonal-plus-rank-one completion stated here.

### Equivalent formulations

No equivalent earlier odd fixed-core statement was located.

### Broader coverage

Their union still does not mechanically imply the stated nonrecursive odd fixed-DCT correction formula without the new generator decomposition.

### Exact database or table

This is a structural factorization rather than a table lookup.

### Claim versus prior implication

The final odd formula is not a special case of either published theorem.

## Value — PASS

The result gives a natural all-order structural completion of a newly introduced fast-factorization framework: odd lengths acquire the same fixed-transform plus structured-correction architecture as even lengths, eliminating the residual-KLT/arrowhead representation while retaining the exact transform.

## Sources inspected

- Exact fast factorizations of the AR(1) Karhunen–Loève transform — https://arxiv.org/abs/2609.20221. NOT_COVERING_ODD_FIXED_CORE: The fixed-core factorization is explicitly formulated for even \(N\).
- Direct Factorization of the Karhunen–Loève Transform of AR(1) Sources — https://arxiv.org/abs/2608.06522. NOT_COVERING_NONRECURSIVE_ODD_CORE: The odd theorem uses a residual KLT plus an arrowhead stage and remains recursive.

## Checked sources

- https://arxiv.org/abs/2609.20221
- https://arxiv.org/abs/2608.06522
- Resultary semantic search

## Residual risks

- The two relevant preprints are very recent, so simultaneous work remains possible.
- The factorization does not itself prove a new floating-point stability theorem for accelerated Cauchy application.

## Limitations

- The theorem treats real stationary AR(1) covariances with \(0<\rho<1\). It is an exact algebraic factorization, not a floating-point backward-stability theorem; negative correlation, nonstationary models, and higher-order autoregressions are outside scope. The previously published recursive odd-order method already has the same asymptotic complexity, so the contribution is structural and nonrecursive.
