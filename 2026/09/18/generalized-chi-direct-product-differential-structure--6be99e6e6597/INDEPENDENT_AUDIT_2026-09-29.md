# Independent audit — 2026-09-29

**Record:** `2026/09/18/generalized-chi-direct-product-differential-structure--6be99e6e6597`  
**Title:** Generalized chi permutations split into independent odd chi blocks  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `c8010ecea59660cb1aad9155929492774230f363`  
**Disposition:** **REPAIRED**

## Correctness

**PASS_AFTER_REPAIR** — The algebraic consequences are correct. With d=gcd(n,v) and ℓ=n/d, the interleaved-track coordinates give a Cartesian product of d copies of ordinary χ_ℓ. Product permutations have the same order as one factor; coordinate relabeling preserves inverse degree and monomial counts; derivative equations separate blockwise, so the DDT is a Kronecker product. Since ordinary odd χ has maximum differential probability 1/4, a difference supported in exactly one block attains 1/4 for the product and differences in multiple blocks cannot exceed it, giving differential uniformity 2^(n-2). The second family inherits the same parameters under the source's elementary equivalence.

## Originality

**PASS_AFTER_REPAIR** — The filed structural originality claim became false after publication. arXiv:2609.19548v2, revised 21 September 2026, added Remark 1 explicitly saying χ_{n,v} splits into gcd(n,v) interleaved tracks carrying ordinary χ, and Remark 2 explicitly saying χ_{n,v} and χ_{n,-2v} are elementary equivalent. The repair credits those facts to Feng et al. and retains only the explicit inherited order/inverse formulas, DDT Kronecker factorization, exact differential uniformity, and iteration/diffusion consequences. I found no statement of those exact derived formulas in v2.

## Scientific value

**PASS_AFTER_REPAIR** — Once the decomposition is credited correctly, the remaining contribution is elementary but useful: it turns the source's qualitative stretching observation into exact cryptographic and dynamical invariants, most notably a closed differential-uniformity value 2^(n-2) and an explicit DDT factorization. The repair no longer portrays the decomposition itself as a new theorem.

## Findings

- Feng et al. v2 was posted 21 September 2026, after the 18 September SCOPE record, and explicitly added the interleaved-track decomposition.
- The same v2 explicitly states elementary equivalence of χ_{n,v} and χ_{n,-2v}.
- The order, inverse-degree, DDT-product, and differential-uniformity consequences remain correct and are not stated in those v2 remarks.
- The original record's statement that the paper did not state the map-level decomposition/equivalence is now stale and must be removed.

## Independent checks

- Inspected arXiv:2609.19548v2 and its revision metadata.
- Read and visually checked the page containing Remarks 1–3.
- Re-derived the direct-product DDT factorization and differential-uniformity formula.
- Cross-checked ordinary χ order, inverse-degree, and differential-probability formulas against the cited Schoone–Daemen work.

## Sources

- https://arxiv.org/abs/2609.19548 — Feng et al. v2, revised 21 September 2026; Remarks 1 and 2 now explicitly state the interleaved-track decomposition and elementary equivalence.
- https://doi.org/10.1007/s10623-023-01349-8 — Schoone–Daemen state-diagram/order results for ordinary χ.
- https://doi.org/10.1007/s10623-024-01395-w — Schoone–Daemen algebraic and differential properties of ordinary χ.

## Limitations

- No priority is claimed for the structural decomposition or equivalence after the v2 revision.
- The surviving claims are elementary invariant transfers once the v2 decomposition is known.
- No cryptanalytic break of a full cipher with external diffusion is claimed.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
