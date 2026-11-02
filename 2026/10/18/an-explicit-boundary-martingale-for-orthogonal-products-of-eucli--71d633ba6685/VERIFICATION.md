---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For K=∏ a_i B_2^{d_i}, codimension-one disjoint boundary strata have Hausdorff area V d_i/a_i, hence q_i=(d_i/a_i)/H with H=∑d_i/a_i. Conditional on uniform interior U and independently selected J=i, the two-point kernel ±a_i Θ_i with probabilities (1±R_i/a_i)/2 has exact barycenter U_i. Since Θ_i is uniform and independent of R_i, signed Θ_i has uniform sphere marginal; all other blocks retain their independent uniform ball laws. This explicitly yields normalized Euclidean boundary measure (not cone measure). Conditional Jensen implies all convex f and, by iterative independence, separately convex F on arbitrarily many independent points, including norm^p chords for p≥1. For d_i≥2 with positive q_i, conditioning both copies on selecting that block gives four positive-mass sign pairs with noncollinear projected differences, ensuring strict Euclidean Jensen even at p=1. Block covariance: q_i[a_i²/d_i−a_i²/(d_i+2)]I=2a_i/[H(d_i+2)]I. Cross blocks vanish by sign symmetry; twice the trace gives 4/H∑d_i a_i/(d_i+2) exactly. The d_i=1 endpoints, all-segment products, m=1 and positivity of a_i are handled. Independent rational checks ran 240 configurations of dimensions/radii and explicit strictness witnesses, corroborating but not replacing the infinite proof.

## originality

PASS

Qualified best-of-knowledge originality of the explicit normalized Euclidean-surface-law martingale for all orthogonal products of Euclidean balls and its blockwise covariance increment. The closest convex-order theorem has, in the accessible abstract, only planar centroid-alignment and centered circumscribed-polytope hypotheses; Shen and Kukushkin prove planar distance inequalities, while high-dimensional counterexamples of Shen/Lotnikov do not imply this positive family. The full Tokmachev paper remained inaccessible: the remaining priority risk is named, not represented as a disproof. Neither Resultary query nor directly read two published related SCOPE results establishes an equivalent or stronger assertion.

## value

PASS

The natural infinite geometric family of orthogonal ball products includes nonpolyhedral cylinders in ambient dimension three where blanket symmetric-body claims fail. The explicit law-level martingale is strictly stronger than the motivating scalar distance inequality and uniformly supplies all separately convex observables, all chord p-moments, and an exact covariance gain for freely varying dimensions/radii. Surface weights are geometrically nontrivial for nonsmooth product boundaries; the theorem solves a motivated positive-subclass question rather than a numerical small-case exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
