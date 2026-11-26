---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Assessed the corrected complete RESULT.md in /workspace/repairs/1/. The frozen §3's exact count of active leaves is false: a directed triangle has k=0 and all its divergences zero. The corrected proof uses at most 2r−k, since each extreme-hub triangle contributes one active leaf, and each mixed-hub triangle contributes either two (transitive) or zero (cyclic). Its hub moment bound follows from |b_0|≤2k and k^q≤r^(q−1)k. Averaging over the leaf-symmetry group and applying the concavity of x^(1/q) gives the stated Jensen upper bound. The explicit witness uses hub extremes of common sign with probability 2/3, making each leaf active half the time in that branch, and transitive mixed-hub triangles with probability 1/3, making all leaves active in that branch. This realizes both the upper hub moment and the leaf moments exactly. The statement of the theorem is unchanged. For the general formula the free-lattice weak p constraint reduces to independent coordinate bounds, the nonnegative ℓ_q dual coefficients allow replacing each graph variation by its independently maximizing orientation, and coordinate-wise Hölder followed by grouping the coefficient q-powers gives the simplex formula both ways. At infinity the optimum is a point mass of maximum ℓ₁ divergence; at one the lattice triangle inequality and single-coordinate probes match. Attaining the sum of degrees forces uniform source/sink behavior at each nonisolated vertex in every positive-mass orientation, equivalent to bipartiteness. A maximizing moment is on a proper face in the full-dimensional case by strict coordinate monotonicity, or the hull already has affine dimension at most n−1; Carathéodory gives the at-most-n support. The cycle signs change an even number of times and attain the largest allowed even count; complete-graph partial score sums are bounded by k(n−k), the transitive bound. Vertex transitivity and convexity then establish the two additional formulas at all stated exponents. The packaged finite code already uses the correct inequality (verify.py:77); it was inspected and not executed, and no verification-file correction is needed.

## originality

PASS

The verified distinction is the graph-specific norm analysis: a divergence-moment formulation for graph variation on the real ℓ₁ base, its equality distinction, and especially the sharp all-exponent friendship-graph evaluation. The free-lattice representation, summing-norm/factorization framework, orientation zonotope, and convexity tools are existing inputs. Correcting the pointwise leaf bound does not change the stated scope or comparisons.

## value

PASS

The invariant is the norm of the natural graph total-variation element, not an arbitrary parameter instance. The equality result makes the norm detect bipartiteness for every p>1, and the windmill computation gives a sharp size-independent relative deficit for a non-vertex-transitive family and a concrete common norming design. Those are reasonably useful exact tests for any later treatment of graph variation or incidence summing norms. The repaired leaf bound retains that mathematical content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
