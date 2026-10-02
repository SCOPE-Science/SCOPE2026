# Independent audit — 2026-10-01

## Record

A finite-template first-obstruction dichotomy at the first-zero LPO degree

## Final claim

For every fixed finite nonempty relational template \(\mathbf B\) over a finite positive-arity relational signature, the first failing finite-prefix homomorphism problem is identically zero exactly when \(\mathbf B\) has a point on every relation diagonal; otherwise it is strongly Weihrauch-equivalent to the first-zero problem \(\mathrm{LPO}_{\min}\), and their parallelizations are Weihrauch-equivalent.

## Correctness

**PASS** — Both strong Weihrauch reductions reconstruct directly. The upper map computes the monotone decidable sequence recording whether each finite prefix maps to \(\mathbf B\); its first zero is exactly the first failing prefix. For the lower map, a zero at index \(n\) is encoded by putting only the diagonal tuple \((n,\ldots,n)\) into every relation. Before the first zero every finite prefix has empty relations and maps to nonempty \(B\); at and after the first zero a homomorphism would require one image point lying on every relation diagonal, contrary to the nontrivial-branch hypothesis. Both postprocessors are the identity, so the reductions are strong. In the remaining branch a common diagonal point gives a constant homomorphism from every input. The argument also handles the empty signature vacuously.

Risk: No correctness gap was found. The theorem depends on unrestricted input tuples; promised irreflexive or otherwise tuple-restricted classes are outside the claim.

## Originality

**PASS** — The primary BeMent–Hirst–Wallace paper was inspected in its first-zero \(\mathrm{LPO}\) and local fixed-color graph section. It proves the graph-specific local-coloring Weihrauch equivalence using clique obstructions, not the finite-template homomorphism dichotomy, the common-diagonal-point criterion, or the unrestricted diagonal one-vertex obstruction. Resultary semantic searches for fixed-template CSP/homomorphism first-obstruction aliases returned the audited record as the direct match and no earlier stronger SCOPE finding. General CSP search results found no theorem implying this exact strong-Weihrauch classification.

Risk: A semantically equivalent result under computable-structure or CSP terminology could be poorly indexed; unsuccessful search is not novelty proof.

### Equivalent formulations

The graph theorem and the audited relational-template theorem have different object classes and obstruction mechanisms; no equivalence or reduction from a broader prior theorem was found.

### Broader coverage

The prior graph theorem is narrower, and no stronger template theorem was located.

### Exact database or table

This is a theorem-classification question, not a table lookup.

### Claim versus prior implication

No inspected prior statement implies the full final claim.

## Value

**PASS** — This is a natural complete classification over all finite relational templates of a first-obstruction problem, with a sharp computable/noncomputable boundary given by an intrinsic template property and an exact strong Weihrauch degree on the nontrivial side. It is broader than a single gadget calculation and is reusable for comparing promised and unrestricted local CSP representations.

Risk: Its value is representation-sensitive and does not automatically transfer to promised graph classes or alternative encodings.

## Source inspections

- **Reverse mathematics and Weihrauch analysis motivated by finite complexity theory** (arXiv:2105.01719v1): Primary PDF section defining the first-zero LPO variant and proving the local fixed-colouring reduction, including the clique lower-bound construction Assessment: PARTIAL_COVERAGE. Evidence: The paper treats simple graph local k-colouring and ordinary Weihrauch equivalence; it does not state the finite relational-template common-diagonal dichotomy or its strong Weihrauch form.

## Residual risks

- Equivalent work under computable-structure, finite-template CSP, or alternative Weihrauch terminology could be missed.

## Disposition

Passed: the claim survives all three axes.
