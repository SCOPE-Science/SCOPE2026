# Scientific audit — SCOPE-20260911-059

Date (UTC): 2026-10-01

## Final claim

For the stated genus-one refined floor-diagram problem on the Hirzebruch surface F0 in bidegree (3,4), there are 105 unmarked decorated classes with 23,352 marked classes; the refined Laurent polynomial has coefficients 6, 96, 798, 4416, 17274, 42432, 17274, 4416, 798, 96, 6 from exponents minus five through five, and the stated lambda-class expansion follows from the published correspondence.

## Correctness

**PASS** — A fresh enumeration from the stated graph, divergence, positivity, automorphism, marking, and quantum-weight definitions reproduced all 105 classes, the marking total 23,352, the complete Laurent polynomial, and value 87,612. A separate exact rational series expansion reproduced the stated first five lambda coefficients. Bousseau's published theorem was checked for the generating-series normalization.

## Originality

**PASS** — Searches found the exact ledger only in this record. Bousseau and related floor-diagram literature provide the general correspondence and definitions but not this complete bidegree-(3,4), genus-one class table or its coefficient vector; no broader theorem located mechanically implies the finite census.

### Equivalent formulations
Equivalent searches by genus, surface, bidegree, class count, and total did not reveal the same statement elsewhere.

### Broader coverage
The general theorem explains what to count but does not mechanically provide the 105-class quotient or coefficient vector.

### Exact database or table
No exact database/table coverage was found.

### Claim versus prior implication
Prior theory does not imply the numerical ledger without carrying out the census.

## Value

**PASS** — This is a natural complete finite classification in a standard enumerative-geometry family, at a size with a genuine genus-one cycle. The complete refined ledger and derived lambda coefficients provide reusable calibration data, not just an isolated arithmetic check.

## Sources inspected

- Package result, census, series, and ledger: https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/11/059/RESULT.md — Supports the exact 105-class ledger and the displayed coefficient vector.
- Refined floor diagrams from higher genera and lambda classes: https://arxiv.org/abs/1904.10311 — Supports the general interpretation and normalization, but does not contain the specific finite (3,4) ledger.
- Resultary published-results search: https://github.com/Resultary/2026/tree/main/2026/9/11/SCOPE059 — No separate exact ledger or stronger census implying these numbers was found.

## Residual risks and limitations

- The lambda-class interpretation relies on the cited general correspondence rather than reproving it.
- The literature search cannot rule out an obscure unpublished table.
- The claim is restricted to F0 and the stated marking/refined-weight convention.

## Disposition

PASSED
