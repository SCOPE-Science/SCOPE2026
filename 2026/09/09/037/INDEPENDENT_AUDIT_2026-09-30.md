# Independent audit — SCOPE-20260909-037

Audited at: 2026-09-30T22:49:30Z

Final disposition: **passed**.

## Correctness

**PASS** — Fresh exact recomputation rebuilt the canonical Sylvester S8, checked Gram=8I, exhaustively minimized discrepancy over all 256 full signings and all 255 nonempty column subsets, and evaluated all 12,869 nonempty square submatrices with exact integer determinants. It reproduced disc=4, herdisc=5, the subset-size distribution, and M_k=(1,2,4,16,32,128,512,4096), hence detLB=2*sqrt(2) and ratio 5*sqrt(2)/4.

## Originality

**PASS** — Best-of-knowledge comparison found general determinant-bound gap theorems and Kronecker/Haar constructions, but no source giving this exact S8 tuple plus the complete hereditary/submatrix census.

### Equivalent formulations

Searches checked: published-record search: order 8 Sylvester Hadamard hereditary discrepancy determinant lower bound exact; web: Sylvester S8 discrepancy hereditary determinant lower bound.

Evidence: The exact semantic match was the present SCOPE record; checked discrepancy literature discusses general bounds/examples rather than the S8 finite tuple.

Reasoning: No equivalent published exact S8 statement was located.

### Broader coverage

Searches checked: Matousek 2012 determinant bound almost tight; Jiang-Reis determinant lower bound hereditary discrepancy; Li-Nikolov gap hereditary discrepancy determinant lower bound.

Evidence: These papers establish asymptotic/general gap bounds and constructions, not the exact order-8 Sylvester census.

Reasoning: Their implications do not calculate the claimed finite tuple.

### Exact database or table

Searches checked: small Hadamard discrepancy tables S8 detLB; exact Sylvester Hadamard submatrix determinant spectrum.

Evidence: No checked database/table contained disc=4, herdisc=5 together with M_1..M_8 and the 255-subset discrepancy distribution.

Reasoning: Known Hadamard determinant facts alone do not provide hereditary discrepancy or the full spectrum.

### Claim versus prior implication

Searches checked: Lovasz-Spencer-Vesztergombi determinant lower bound; Hoffman discrepancy gap; Matousek general upper gap.

Evidence: General inequalities only bound relationships; they do not force herdisc(S8)=5 or the exact finite determinant maxima.

Reasoning: The finite exhaustive result is not a corollary of the checked general statements.

### Source inspections

- **The determinant bound for discrepancy is almost tight** (https://arxiv.org/abs/1101.0767): NOT_COVERING. Material read: abstract and theorem scope. General \(O((\log n)^{3/2})\) relation and Hoffman-gap context; no exact S8 computation.
- **On the Gap Between Hereditary Discrepancy and the Determinant Lower Bound** (https://doi.org/10.1137/23M1566790): NOT_COVERING. Material read: publisher abstract and construction scope. General nearly tight gap constructions using Haar/Kronecker ideas, not the canonical S8 exact tuple.

Checked sources: published SCOPE findings search; Matousek 2012; Jiang-Reis 2022; Li-Nikolov 2024.

Residual risks: An obscure small-Hadamard computational table may use different terminology; originality is best-of-knowledge, not a proof of absence.

## Scientific value

**PASS** — The canonical S8 is a natural benchmark object, and the result gives a complete exact calibration of two central discrepancy quantities and their strict separation, including the full determinant/subset census. This is a structured finite invariant package rather than an arbitrary numerical slice.
