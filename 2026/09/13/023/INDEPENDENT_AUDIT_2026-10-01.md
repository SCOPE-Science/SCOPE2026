# Scientific audit — SCOPE-20260913-023

Date: 2026-10-01 UTC

## Final claim

For the equiangular degree-8 single vertex at the fully flat-folded state, among the 112 flat-foldable mountain-valley assignments, a strictly positive first-order unfolding speed exists exactly when both the even and odd crease classes contain both signs; this gives 96 first-order-admittable and 16 obstructed assignments.

## Correctness

**PASS** — Direct differentiation of the eight-factor closure at fold angles plus or minus pi gives two alternating Jacobian column directions. The kernel equations reduce exactly to one signed positive-weight balance on even creases and one on odd creases. Such a balance exists exactly when each parity class has both signs. A fresh combinatorial reconstruction gives 112 Maekawa assignments, 96 satisfying the mixed-parity criterion, 16 obstructed, and ten dihedral orbits with sizes 8,8,8,8,8,8,16,16,16,16.

Residual risk: The conclusion is first-order only at a singular flat state; it does not prove integration to a finite rigid-folding branch.

## Originality

**PASS** — The equal-angle forcing-number theorem and flat-foldability criterion are prior results and are not counted as new. The rigid-origami primary source inspected treats rigid folding from the unfolded state and explicitly separates the fully flat-folded combinatorial singularity; the exact flat-state parity kernel criterion was not found in the compared primary sources or published-results corpus.

Residual risk: A specialized rigid-origami source outside the checked literature could contain an equivalent flat-state Jacobian reduction.

### Equivalent formulations

The inspected rigid-origami source characterizes unfolded-state rigid foldability and does not state this fully flat-folded positive-kernel parity criterion.

### Broader coverage

The published equal-angle forcing result explains the uniform forcing number 5 but does not imply the flat-state rigid-unfolding Jacobian classification.

### Exact database or table

No independent exact published table with the 96/16 first-order split was located in the compared published-results corpus.

### Claim versus prior implication

The unfolded-state bird-foot criterion does not imply the singular flat-state linearized kernel criterion used here.

## Value

**PASS** — This is a structural classification over the complete natural degree-8 equal-angle flat-foldable family, not an arbitrary sample. The parity criterion gives an exact tangent-level boundary between first-order-admittable and obstructed assignments and is useful precisely because flat states are singular configurations where generic unfolded-state criteria do not apply.

Residual risk: Its scope is deliberately narrow: it is a tangent obstruction/classification, not a finite-amplitude rigidity theorem.

## Sources inspected

- Rigid origami vertices: conditions and forcing sets — https://arxiv.org/abs/1507.01644 — NOT_COVERING: The paper treats rigid foldability from the unfolded state and notes completely flat-folded states require separate combinatorial treatment.
- Minimum Forcing Sets for Single-vertex Crease Pattern — https://doi.org/10.2197/ipsjjip.28.800 — PARTIAL_COVERAGE: Covers forcing number 5, which the record expressly treats only as a cross-check, not the retained parity claim.
- Published finding SCOPE023 — https://github.com/Resultary/2026/tree/main/2026/9/13/SCOPE023 — SELF_MATCH_ONLY: The exact matching published-results hit was the record itself; no stronger indexed result was found.

## Disposition

PASSED
