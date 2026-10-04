# Fresh audit — SCOPE-20260907-010

Date (UTC): 2026-09-30

## Final claim

The five listed capacity-24 cutting-stock instances each have exact Gilmore–Gomory gap one; every defined Hamming-1 neighbor has gap zero; and the stated k-at-most-3 box contains 3,520 two-type and 84,465 three-type instances, all satisfying IRUP. Full k-at-most-6 maximality is not claimed.

## Correctness

**PASS** — Fresh verification independently enumerated complete patterns for all five catalog entries, solved the configuration LP and converted both primal and dual solutions to exact rational certificates, and independently proved the claimed integer optima by complete item-branching search. A separate exact low-dimensional dual-vertex enumeration plus dynamic program reproduced all 3,520 two-type and 84,465 three-type IRUP instances. The 63 Hamming-1 neighbors were regenerated and independently checked by exact rational primal-dual equality plus complete packing search, with zero gap-one neighbors.

Residual risk: The much larger k=4 through k=6 box was not exhaustively classified, consistent with the record's explicit limitation.

## Originality

**PASS** — Kartak–Kurz–Ripatti–Scheithauer proves proper IRUP through total demand 9 and gives non-IRUP examples from total demand 10, while the present capacity-24 high-multiplicity instances have different total demands and are not implied by that result. MIRUP papers give general or subproblem bounds rather than this capacity-stratified exact catalog. Exact searches for the listed size/demand vectors did not locate prior matches.

Residual risk: Small benchmark instances can circulate in solver test sets without searchable prose; no such exact match was found.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and whether prior results imply the present claim.

## Value

**PASS** — Exact configuration-LP versus integer-gap witnesses with complete primal-dual and packing certificates are directly useful as reproducible column-generation and branch-and-price benchmarks. The exhaustive low-type boundary and strict local gap maxima give mathematically motivated structure beyond merely reporting random hard instances.

Residual risk: The full capacity-24 k-at-most-6 maximality remains open, so the value is in the certified benchmark/boundary data rather than a global extremal theorem.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/010/RESULT.md — Full result inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/010/artifacts/recheck.py — Actual standalone exact verifier inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/010/artifacts/catalog.json — Complete pattern/primal/dual/packing certificates for all five entries inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/7/SCOPE010 — Exact semantic search; own record was the direct match.
- https://arxiv.org/abs/1405.5988 — Kartak–Kurz–Ripatti–Scheithauer primary record inspected; its total-demand stratification does not imply this capacity-24 typed-demand catalog.
- https://doi.org/10.1016/0377-2217(95)00022-I — MIRUP literature checked; provides the property and numerical context, not the exact present table.
- https://ideas.repec.org/a/spr/mathme/v48y1998i1p105-115.html — Published MIRUP subcase results checked for broader coverage; no implication of the exact five-instance catalog was found.

## Overall disposition

PASS
