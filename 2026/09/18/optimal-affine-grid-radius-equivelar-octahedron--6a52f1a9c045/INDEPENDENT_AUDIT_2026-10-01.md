---
audit_date: 2026-10-01
status: repaired
---

# Scientific audit

## Final claim

For Mizhaev's published 24-vertex genus-three \(\{9,3\}\) integer realization, among affine integer copies for which the conjugated published \(C_4\) generator remains a Euclidean isometry, the sharp centered \(\ell_\infty\) grid radius is \(90\). An explicit radius-\(90\) copy attains the bound. The previously claimed unrestricted affine radius \(84\) is removed as a new claim because it had already been publicly established.

## Correctness — PASS

The assigned exact certificate was independently reconstructed. The difference lattice has index \(60\), so every coordinate row of an affine integer copy is a dual-lattice covector \(q^TA\). The exact short-width bound reduces every row of any hypothetical radius-below-\(90\) copy to five projective integer directions with widths \(156\) or \(168\). There are exactly eight linearly independent unordered triples of those directions; exact rational conjugation of the published generator \(T(x,y,z)=(y,-x,-z)\) is non-orthogonal for every triple. Row signs and permutations preserve that conclusion. The displayed linear map \(C\) sends all vertices to integers, has radius \(90\), commutes with \(T\), and therefore attains the lower bound.

**Checked sources.** Assigned RESULT.md and artifacts/verify.py at source tree d5dbba8010eb32096bd768b9eeb6127654114b33; R. Mizhaev, Integer Realization of an Equivelar Octahedron of Genus 3, arXiv:2609.17700; Earlier public record Affine-integer grid radius 84 for Mizhaev's genus-3 equivelar octahedron, dated 2026-09-17

**Residual risks.** The older 2020 precursor to Mizhaev's construction was not read in full; no accessible evidence found there states a symmetry-preserving affine-radius theorem.

## Originality — PASS

The original package's unrestricted radius-\(84\) theorem is directly covered by a public record dated 2026-09-17 and is therefore removed from the repaired claim. Searches did not locate a prior theorem for the additional Euclidean-\(C_4\)-preserving radius constraint or the sharp value \(90\).

### Equivalent formulations

The repaired claim is the constrained optimization problem in which the conjugated source symmetry must remain Euclidean; that condition is absent from the prior radius-84 theorem.

### Broader coverage

The Euclidean-conjugacy constraint is genuinely additional and requires checking orthogonality for the short dual-lattice bases.

### Exact database or table

This finite exact invariant is not present in a standard external table; the relevant database comparison is the published record corpus.

### Claim versus prior implication

Neither prior implication yields the value \(90\); the extra finite classification is load-bearing.

**Checked sources.** https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-affine-grid-optimal-equivelar-octahedron--5ecb04caa0a4; https://arxiv.org/abs/2609.17700; https://doi.org/10.31219/osf.io/hvtey

**Residual risks.** The 2020 precursor was not available in full during this audit; it remains a limited historical-risk source, but accessible metadata did not indicate the affine-symmetry optimum.

## Scientific value — PASS

The repaired theorem isolates the exact coordinate cost of preserving a natural geometric structure already emphasized by the source: its order-four Euclidean symmetry. The jump from the known unrestricted optimum \(84\) to the constrained optimum \(90\) is a sharp boundary proved by a complete finite dual-lattice classification, not an arbitrary coordinate tweak.

**Residual risks.** The result is specific to one affine orbit and one distinguished symmetry generator.

## Limitations

- The radius \(90\) is optimal only inside the affine-integer orbit of Mizhaev's specific realization and under the requirement that the published order-four generator remain Euclidean after conjugation.
- The result does not assert global coordinate minimality among non-affinely-equivalent realizations of the abstract surface.

## Disposition

REPAIRED. Acceptance requires all three scientific axes to pass.
