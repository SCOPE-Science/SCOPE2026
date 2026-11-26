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

Each subdivided cycle flow is constant along each consistently oriented path. With replication U, UᵀU=diag(r), so the ordinary Euclidean cycle projector is UHUᵀ with H=B(Bᵀdiag(r)B)⁻¹Bᵀ. For subedge f the cycle column norm is A_f=Σ_g r_g|H_gf|, and the cut column norm is 1+A_f−2H_ff because only one diagonal entry changes sign convention and 0≤H_ff≤1. Vary one length t. The Gram update is rank one; H_gf has an affine numerator over the common positive affine d=1+(t−1)H_ee(1). When g=e, the numerator is constant H_ef(1), so multiplying by the varying multiplicity t does not create a quadratic numerator. After clearing d, each cycle or cut column norm has a convex numerator (absolute values of affine expressions plus affine terms). A convex numerator over a positive affine denominator is bounded between length endpoints by the larger endpoint ratio: interpolate the numerator and weight the endpoint ratios by their positive denominators. Maximizing over columns then repeating over coordinates proves the corner inequality. Forests use H=0; a bridge has a zero cycle-basis row; degenerate intervals require no interpolation. Symmetry gives equality of the induced ℓ₁ and ℓ∞ norms. The real-length claim is for the displayed extension, not fractional graphs. Independent exact-rational diamond replay for k=1,…,25 gave the two stated cycle-column functions; they cross at k=2 and have opposite strict slopes. The diamond's cut norm instead is 2−1/(k+1). The frozen verifier was inspected, not run; neither its recorded PASS nor the separate diamond replay proves the universal inequality.

## originality

PASS

The identical pointwise nonuniform-subdivision formulas are prior; only the cross-length optimization theorem and its interpretation are credited here. The inspected work does not supply a stronger multi-length extremum statement. The key new comparison uses the cancellation of the varying row's denominator-cleared coefficient against the varying multiplicity; an exact pointwise formula alone does not state that comparison. The diamond values can be computed directly from prior formulas, and are a witness rather than a separate originality basis.

## value

PASS

A universal corner maximum reduces the worst-case independent-budget search from every allowable subdivision vector to endpoints. It works for both complementary canonical projectors even though the cycle norm can have an interior dip, as the diamond shows. This is a useful optimization distinction, not a claim of monotonicity, a polynomial-time algorithm, or a result about optimal nonorthogonal projections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
