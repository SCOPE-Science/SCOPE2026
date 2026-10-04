# Fresh audit — SCOPE-20260907-008

Date (UTC): 2026-09-30

## Final claim

Up to row and column permutations and transpose, exactly 719 binary 5-by-5 matrices have ordinary rank 3; 713 have nonnegative rank 3 and six have nonnegative rank 4, so none in this stratum has nonnegative rank 5.

## Correctness

**PASS** — A fresh exact implementation independently enumerated all 376,992 column multisets, computed ordinary rank using integer elimination, reproduced the full rank histogram and the 63,015 rank-3 multisets, canonicalized under row/column permutations and transpose to exactly 719 classes, then established 713 nonnegative-rank-3 cases by exact rational nonnegative three-generator factorizations and the remaining six as rank 4 via explicit four-point fooling sets. No case remained unresolved.

Residual risk: Canonicalization and finite enumeration are software-assisted, though the fresh implementation used exact integer/rational checks for the scientific classification.

## Originality

**PASS** — Published-results search found the exact census only in this record. Gillis–Glineur provides general rank-3 geometric theory, and Beasley–Laffey supplies isolated lower-dimensional gap patterns, but neither gives the complete binary 5-by-5 ordinary-rank-3 classification. No exact 719-class table was found elsewhere.

Residual risk: A non-indexed computational table could exist; search cannot prove universal absence.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and whether prior results imply the present claim.

## Value

**PASS** — This is a natural complete classification at the first small binary square size where a rank versus nonnegative-rank gap is visible, with direct relevance to nonnegative factorization and extension complexity; the exact no-rank-5 boundary is a reusable finite fact.

Residual risk: The six gap classes themselves are structurally degenerate, so the value rests mainly in the exhaustive boundary classification.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/008/RESULT.md — Full result inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/008/artifacts/audit.py — Actual package audit source inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/008/artifacts/exact_factors.json — Stored exact factor data inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/008/artifacts/fooling_witnesses.json — All six fooling-set witness records inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/7/SCOPE008 — Exact semantic search; own record was the direct match.
- https://arxiv.org/abs/1009.0880 — Gillis–Glineur primary paper record/full-text source checked for general rank-3 nonnegative-rank geometry; it does not give this finite binary census.
- https://doi.org/10.1016/j.laa.2009.03.050 — Beasley–Laffey gap literature checked for implication; isolated lower-dimensional examples do not furnish the 5-by-5 classification.

## Overall disposition

PASS
