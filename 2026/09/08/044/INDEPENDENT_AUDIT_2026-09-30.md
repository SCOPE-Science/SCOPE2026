# Independent audit — 2026-09-30

**Record:** `2026/09/08/044`  
**Audited source tree:** `55baea89136c041ba05ed3f2d9197717e3d863b4`

## Final claim assessed

Exact Steinberg growth rates and golden-ratio minimal-growth witnesses for RACGs on connected graphs with 4-6 vertices

## Correctness — PASS

A fresh enumeration using an independent connected-graph atlas gives exactly 6, 21, and 112 isomorphism types on 4, 5, and 6 vertices. Recomputing clique vectors and the Steinberg denominator for every graph gives finite/subexponential/exponential counts 1/2/3, 1/2/18, and 1/3/108. Independent root calculations reproduce the golden ratio as the minimum exponential rate in every stratum with witness multiplicities 1, 2, and 3; every other exponential row has rate at least 2. The displayed factorizations explain the equality cases exactly.

## Originality — PASS

Terragni proves general monotonicity and a universal Coxeter growth lower bound, not the per-graph right-angled census. Later work on RACG growth polynomials studies broad algebraic families rather than this 139-row exact small-graph classification. Resultary shows a later 2026-09-09 record extending a complete RACG table through seven vertices; because it postdates this 2026-09-08 record, it is downstream coverage rather than prior coverage and does not retroactively defeat originality.

The comparison explicitly checked equivalent formulations, broader coverage, exact database/table matches, and whether prior results logically imply the claim. An unsuccessful search was not treated as proof of novelty.

## Scientific value — PASS

The complete 139-type exact table is a natural finite classification of the smallest connected defining graphs, and the exact golden-ratio minimizers plus a gap to 2 give a clean structural benchmark. The table is reusable for testing growth-series software and for checking conjectures about small RACG growth behavior.

## Source inspections

- **Terragni — On the growth of a Coxeter group** — Full-text PDF: abstract, Theorems A and B, and the discussion of right-angled Coxeter systems. General monotonicity and universal lower-bound theory; no complete n=4 through 6 right-angled graph census or golden-ratio multiplicity classification. https://arxiv.org/abs/1312.3437
- **Oh — Strongly Primitive Salem Growth Polynomials for Right-Angled Coxeter Groups** — Abstract and stated scope from the open-access record; direct PDF retrieval was unavailable during this audit. Infinite-family algebraic results via clique polynomials; no exact enumeration of all connected graphs on at most six vertices. https://arxiv.org/abs/2606.29397
- **Resultary semantic search for small RACG growth tables** — Top ranked result set, including the 2026-09-09 n-at-most-7 RACG table. This record is the exact same-day source; the broader n-at-most-7 table is later and therefore downstream rather than prior art. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE044

## Residual risks

- The general table relies on exact finite enumeration and exact polynomial/root-isolation code rather than a closed-form classification theorem.
- The newer 2026 RACG literature is active; the specific 139-row classification was not found in a predating source.

## Disposition

**PASS.** Correctness, originality, and scientific value each pass for the final claim stated above.
