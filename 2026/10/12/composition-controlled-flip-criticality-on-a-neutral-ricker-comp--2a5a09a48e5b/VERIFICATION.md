---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Direct exponent cancellation proves K invariance. Monotonicity of K y^alpha+alpha y gives the unique leafwise fixed point; lambda=1-R+(alpha-1)y_K decreases through -1 exactly at x+y=2. For lambda<-1, f_K^2(y)-y is positive just above zero and negative just below the equilibrium, proving an actual positive nonconstant two-cycle by IVT. At the crossing the second derivative is -t/y_c and the third derivative is [4+(5-alpha)t]/y_c^2, giving flip cubic c=Q/(12y_c^2); the smooth scalar normal form gives attracting/repelling cycle types on the stated sides. Independently checked rational supercritical and subcritical witnesses by direct finite differences and exact Q arithmetic. The planar fixed point has neutral multiplier one, so no full-plane attraction is asserted.

## originality

PASS

The invariant foliation and nonhyperbolic (1,-1) flip sign boundary are not implied by inspected generic Ricker bifurcation criteria; established scalar flip normal forms are explicitly credited.

## value

PASS

The result resolves a motivated degenerate parameter locus excluded by generic planar flip theory, exhibits every postthreshold leaf having a positive cycle, and sharply partitions supercritical and subcritical behavior by a nontrivial competition-strength threshold; not just a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
