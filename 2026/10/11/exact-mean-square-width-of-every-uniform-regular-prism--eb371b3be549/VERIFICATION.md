---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For a right regular n-gon prism, support of a Cartesian product separates: w_P(U)=sqrt(1−Z²)w_B(V)+|Z| with Z uniform [-1,1] and planar V uniform S^1. Spherical integration yields E w_P²=(2/3)E w_B²+1/3+(2/3)E w_B. Cauchy perimeter gives E w_B=n/pi for a unit-edge n-gon. Difference body is a regular n-gon if n even and a regular 2n-gon if odd, of radii 1/sin(pi/n) and 1/(2sin(pi/(2n))), respectively; support-square integration on a normal cone yields both exact formulas. Independently integrated 100,000 planar directions for n=3,4,5,6,7, agreeing at 1e−9; these finite checks supplement the analytic all-n derivation. Cube n=4 equals known 1+4/pi.

## originality

PASS

PASS on explicit all-n regular right-prism second-width moments with parity-dependent closed forms. Finch already has cube (n=4) but not the family; Gaussian-width paper covers other regular polytope classes and generic methods without the target uniform prisms. A known special case does not dominate the full all-n classification, and the prior cube formula is credited.

## value

PASS

Regular right prisms are a canonical infinite geometric family whose directional-width second moment is a natural stochastic-geometric invariant; the even/odd difference-body change yields an explicit nontrivial parity split and recovers a classical cube benchmark. This is a complete motivated natural classification rather than an arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
