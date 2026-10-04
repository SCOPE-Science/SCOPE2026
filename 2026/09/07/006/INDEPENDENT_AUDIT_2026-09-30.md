# Fresh audit — SCOPE-20260907-006

Date (UTC): 2026-09-30

## Final claim

For partitions of 12, the complete unordered Kronecker census has 79,079 S3-orbits, exactly 30,336 vanishing orbits, and maximum coefficient 945 attained uniquely by the orbit of ((5,3,2,1,1),(5,3,2,1,1),(5,3,2,1,1)).

## Correctness

**PASS** — A fresh from-scratch exact Murnaghan–Nakayama implementation enumerated all 77 partitions, rebuilt the full character table, checked the sum of squared dimensions and all row orthogonality identities, then evaluated all 79,079 unordered triples by exact integer class sums. It reproduced 30,336 zeros and a unique maximum 945 at index triple (37,37,37). The package certificate and top-10 table were also inspected at the assigned commit.

Residual risk: As with any software-assisted finite proof, a defect shared by mathematically equivalent implementations remains a residual risk, but the fresh implementation used exact integer arithmetic and did not rely on the package's stored success log.

## Originality

**PASS** — Published-results search returned the record itself as the exact match; a later SCOPE Kronecker atlas covers degrees through 10 as its main census and does not dominate the complete degree-12 census. Primary literature on vanishing complexity, general bounds, dilations, Saxl-type cases, and Durfee bounds does not imply the exact degree-12 zero count or exact maximum. No independent exact degree-12 database/table with these counts was found.

Residual risk: Literature search is not logically exhaustive; an obscure unpublished table could exist.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and whether prior results imply the present claim.

## Value

**PASS** — A complete exact census at a natural symmetric-group degree supplies reusable ground truth for a hard and actively studied positivity problem, and the exact extremal multiplicity plus certificate is a meaningful finite invariant rather than an arbitrary parameter slice.

Residual risk: The contribution is a finite benchmark and does not by itself provide a structural formula or asymptotic theorem.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/006/RESULT.md — Full result text inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/006/artifacts/replay.py — Actual replay source inspected; exact character-table and census logic checked.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/006/artifacts/certificate_Tstar.csv — Exact 77-row extremal class-sum certificate inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/7/SCOPE006 — Exact semantic search; own record was top exact match.
- https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE058 — Related later Kronecker atlas; main complete census only through degree 10.
- https://arxiv.org/abs/1507.02955 — Ikenmeyer–Mulmuley–Walter abstract/full record inspected; establishes complexity context, not the fixed degree-12 census.
- https://arxiv.org/abs/1406.2988 — Pak–Panova bounds comparison searched; no implication of the exact fixed-degree census.

## Overall disposition

PASS
