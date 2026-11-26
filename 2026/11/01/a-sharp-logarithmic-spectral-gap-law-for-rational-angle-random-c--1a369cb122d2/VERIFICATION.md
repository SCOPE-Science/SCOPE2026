---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The primary angular law reduces on the half-offset class to a reversible weighted cycle on 1,…,n−2 with two leaves. In the interior the branch factor is sinθ·uα(θ)=sin(θ+α)/(2cosα); at the left truncation the weight to the leaf is sin(α/2) and the remainder gives the bridge sin(α/2)/(2cosα), using sin(3α/2)=(1+2cosα)sin(α/2). Reflection handles the other end. Normalizing by Sₙ=csc(α/2) gives the stated Dirichlet energy without a factor of two. In each arm, each step-two strand contributes 2α⁻² log n+O(α⁻²) by the reciprocal sine sum, while the bridge contributes O(α⁻²). The two arms therefore give conductance Gₙ∼α²/(2 log n). Same-parity paths to the middle have resistance bounded by Cα⁻²(1+|log sinθ|). Weighted Cauchy–Schwarz followed by summation against the sine masses bounds the squared deviations from parity anchors by O(α⁻²) times the energy. The harmonic test function with anchors ±1 gives the upper bound 4Gₙ(1+o(1)); the upper bound in turn forces the normalized second eigenfunction to concentrate at its anchors. The parity masses tend to 1/2, so the squared anchor difference tends to 4, and the minimum energy at those anchor values gives the matching lower bound. Substituting α=π/n gives 2π²; laziness halves the gap. At even n the core is an even cycle and the leaves preserve bipartiteness, so the algebraic gap must not be confused with an absolute gap for Pₙ.

## originality

PASS

The angular model, the selected weighted graph's topology and sine invariant law, and its periodicity have prior coverage. The supported distinct contribution is the leading-constant logarithmic algebraic gap for this orbit and the equivalent lazy relaxation law. No inspected statement supplies that rate or makes it a direct corollary under the given hypotheses.

## value

PASS

This is a quantitative relaxation law for a naturally specified invariant family in a standard random billiard. The logarithmic penalty is not the diffusive n² scale suggested by the interior cycle alone. Identifying it with two grazing-angle resistance arms and proving the leading constant distinguish a meaningful dynamical effect from a small finite spectrum computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
