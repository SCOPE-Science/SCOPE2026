# Independent audit — SCOPE-20260914-044

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For Einstein algebraic curvature operators in dimension four with Ric=g, positive sectional curvature does not imply 3-positivity, and Wu’s sufficient threshold K>1/12 is sharp at the pointwise algebraic level.

## Correctness

**PASS** — The 4-dimensional Einstein curvature operator splits into trace-one self-dual and anti-self-dual 3-by-3 blocks, and the minimum sectional curvature is half the sum of their least eigenvalues. Fresh exact arithmetic verifies the explicit counterexample and the one-parameter family: at t=1/5 the minimum sectional curvature is 1/15 while the three-smallest-eigenvalue sum is -1/15; at t=1/6 they are 1/12 and 0. These identities prove the counterexample and pointwise sharpness directly. The package’s exact certificate source was also inspected.

## Originality

**PASS** — Wu proves the sufficient bound K>1/12 and poses the positive-sectional-curvature versus 3-positivity question for Einstein four-manifolds, but the inspected source does not give the record’s explicit algebraic counterexample or pointwise sharpness family. Exact searches and Resultary found no prior statement of this algebraic boundary.

### Equivalent formulations

Aliases and equivalent formulations were compared against the closest primary sources; the assessment follows implication rather than title matching.

### Broader coverage

The checked broader theorems do not imply the exact final claim under the same hypotheses.

### Exact database or table

No finite database/table comparison is decisive for this theorem claim.

### Claim versus prior implication

Wu proves the sufficient bound K>1/12 and poses the positive-sectional-curvature versus 3-positivity question for Einstein four-manifolds, but the inspected source does not give the record’s explicit algebraic counterexample or pointwise sharpness family. Exact searches and Resultary found no prior statement of this algebraic boundary.

## Value

**PASS** — The result isolates a genuine boundary of a published rigidity criterion and shows that any solution of the corresponding closed Einstein-manifold question must use differential/global input beyond pointwise algebraic curvature. That is a motivated structural obstruction, not an arbitrary tensor example.

## Source inspections

- Curvature decompositions on Einstein four-manifolds — https://arxiv.org/abs/1903.11817 — PARTIAL_COVERAGE: Supplies the sufficient threshold and global question, but not the algebraic sharpness family.
- Einstein four-manifolds of three-nonnegative curvature operator — http://pi.math.cornell.edu/~cao/3nonnegative.pdf — NOT_COVERING: Addresses geometric consequences of 3-nonnegativity rather than the pointwise converse/sharpness witness.
- Published-results semantic search — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE044 — NO_STRONGER_MATCH_FOUND: No distinct published SCOPE result covered the same pointwise sharpness statement.

## Residual risks

- Literature search is best-of-knowledge and cannot exclude an obscure or unindexed source.
- The audit credits only inspected proofs, source material, and fresh computations described above.

## Disposition

PASSED
