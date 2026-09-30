# Independent audit — 2026-09-29

**Record:** `2026/09/18/gaussian-magnitude-renyi2-total-correlation--4eebefe6d8fe`  
**Title:** Exact Rényi-2 total correlation of Gaussian magnitudes  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `fa9aa46caa218d430b0e9894c7f2bbd88973e173`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The exact determinant sign-sum formula, finiteness iff λmax(R)<2, bivariate identity, and equicorrelation threshold all re-derive correctly from the folded Gaussian sign mixture. The weak-correlation expansion is also correct: in the Hermite expansion only even multi-indices survive folding; doubled edges first contribute ε^4 Σ A_ij^4 and triangles contribute 8ε^6 Σ A_ij^2A_ik^2A_jk^2. Because the first nonconstant term is order ε^4, taking log does not alter coefficients through order ε^6.

## Originality

**PASS** — The motivating Ouimet–Greaves paper gives a Rényi total-correlation certificate but not this exact determinant evaluation or the weak-correlation graph expansion. Generic Gaussian-mixture L2 overlap identities make the determinant computation method standard, so the strongest originality rests on combining the exact spectral phase transition with the even-Hermite/graph expansion. I found no indexed source stating that combination. The weaker same-day SCOPE spectral-threshold record is redundant with this one, not vice versa.

## Scientific value

**PASS** — The record gives a complete computable expression for order-2 total correlation of Gaussian magnitudes, an exact divergence/no-divergence spectral boundary, and a local expansion that identifies pair-edge and triangle dependence motifs. Those pieces form a coherent quantitative dependence theorem beyond the motivating product inequality.

## Findings

- Folded-density integration gives the stated 2^n determinant sum and the exact λmax(R)<2 threshold.
- The ε^4 doubled-edge coefficient is 1 and the ε^6 triangle coefficient is 8 under the record's normalization.
- No log-correction enters before order ε^8.
- This record strictly subsumes the weaker same-day spectral-threshold record on the core theorem and adds the substantive graph expansion.

## Independent checks

- Re-derived the Gaussian integral and spectral equivalence.
- Verified bivariate and equicorrelation specializations algebraically.
- Reconstructed the Hermite coefficient counting for doubled edges and triangles.
- Compared against Ouimet–Greaves and current folded-normal/Gaussian-mixture literature.

## Sources

- https://arxiv.org/abs/2609.20234 — Motivating Gaussian product inequality paper; includes a Rényi total-correlation certificate but not the exact determinant or graph expansion.
- https://doi.org/10.1007/s00362-025-01711-z — Recent multivariate folded-normal context.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/gaussian-magnitude-renyi2-spectral-threshold--76f68ff917a5 — Weaker same-day internal record compared for duplication.

## Limitations

- Positive-definite correlation matrices and Rényi order 2 only.
- The exact sign sum is exponential-size in general.
- Generic Gaussian-mixture overlap literature remains a residual priority risk for the determinant identity considered in isolation.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
