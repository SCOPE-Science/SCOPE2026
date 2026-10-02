# Independent audit — SCOPE-20260918-4e870c1cf2eb

Audit date (UTC): 2026-10-01

## Final claim

For fixed \(k>1\) and integers \(c_T\) with \(c_T/\sqrt T\to\gamma\), the eventual weighted-representation partition count has the stated exact \(2^T T^{-k/2}\) asymptotic constant and Gaussian \(\sqrt T\)-scale profile.

## Correctness

**PASS** — The boundary reduction was rechecked from the source identity: constancy for all \(n\ge T\) is equivalent to exactly \(k\) boundary equations plus the deterministic tail recursion, so initial signs through \(T+k-1\) parameterize all solutions. Reconstructing the coefficient columns yields positive-density families \(\mathbf 1+e_r\) and \(e_r\), one bounded transition column, and covariance \(\Sigma_k=(kI+(k+2)J)/k^2\) with determinant \((k+3)/k^k\). The repeated coordinate columns force exactly \(2^k\) parity-compatible major arcs, all with the same phase; bounded columns and positive-definite covariance give the Gaussian local limit. Multiplying the probability by the \(2^{T+k}\) initial sign vectors reproduces the constant and offset exponent. A fresh dynamic program independently reproduced representative exact counts for \(k=2,3\) and their convergence toward the predicted constants.

## Originality

**PASS** — The 2026 primary source was inspected in full HTML and proves only two-sided order bounds \(F_{k,c}(T)\asymp 2^T/T^{k/2}\) for fixed \(c\). The 2025 Yan--Shan paper gives uniqueness/exact formulas in small-threshold regimes, not the large-\(T\) local limit. Earlier weighted-representation papers establish structural existence and eventual-equality results. No prior exact leading constant or square-root-scale Gaussian offset profile was located.

### Equivalent formulations

Aliases, parameter normalizations, and source-specific formulations were compared by implication rather than by title similarity. Exact-title, exact-claim, alias, and primary-literature searches found no equivalent stronger statement beyond the qualifications below.

### Broader coverage

The closest general results and source theorems were inspected directly. General machinery that is prior art is excluded from the novelty claim; none of the inspected broader statements implies the final claim at the stated strength.

### Exact database or table

Finite computations and tables were treated as corroborative evidence only. They were not used to infer an infinite theorem or to establish novelty.

### Claim versus prior implication

The 2026 primary source was inspected in full HTML and proves only two-sided order bounds \(F_{k,c}(T)\asymp 2^T/T^{k/2}\) for fixed \(c\). The 2025 Yan--Shan paper gives uniqueness/exact formulas in small-threshold regimes, not the large-\(T\) local limit. Earlier weighted-representation papers establish structural existence and eventual-equality results. No prior exact leading constant or square-root-scale Gaussian offset profile was located.

## Value

**PASS** — The theorem upgrades a newly proved order of magnitude to a sharp asymptotic, determines the leading constant, sharpens cross-weight comparisons to asymptotic ratios, and identifies a natural fluctuation profile. This is a mathematically motivated local-limit refinement of a current counting problem, not an arbitrary finite computation.

## Sources inspected

- A problem of Yang and Chen on weighted representation functions — https://arxiv.org/html/2609.20385v1 — NOT_COVERING: proves only two-sided order estimates for fixed offset; no exact constant or square-root offset profile.
- Partitions of the set of natural numbers and their weighted representation functions — https://doi.org/10.1007/s11139-025-01113-7 — NOT_COVERING: exact formulas concern small-threshold/uniqueness regimes, not the large-threshold local-limit theorem.
- Partitions of natural numbers and their weighted representation functions — https://doi.org/10.1017/S0004972723001053 — BACKGROUND: weighted-representation structure, not the claimed local asymptotic.

## Residual risks and limitations

- The motivating order-bound preprint is extremely recent; an unindexed contemporaneous follow-up remains an originality risk.
- The 2012 Yang--Chen full text was not obtained in this run; its role was checked through the 2026 primary paper and bibliographic records, so the priority assessment remains best-of-knowledge.

## Disposition

**PASSED**
