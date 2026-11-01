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

The monotone equation q_i(a_i+q_i)=kappa b_i^2 and sum q_i^2/b_i^2=1 has exactly one positive solution. Expanding the submitted exact sum-of-squares identity proves every box-plus-ellipsoid point satisfies sum x_i^2/[d(a_i+q_i)^2]<=1; positive a_i forces equality only at the 2^d coordinate-sign contacts. Rescaling these contacts gives mean 0 and covariance I/d. Averaging an arbitrary translated/rotated enclosing ellipsoid inequality and using trace>=d*(det)^(1/d) proves it cannot have lower volume; equality forces the identity shape and zero center. My independently written rational-arithmetic checker verified the identity for 1,088 exact parameter/point cases, not a replacement for the universal proof.

## originality

PASS

Best-of-knowledge PASS, qualified. Classical Loewner/John contact criteria characterize optimality but do not calculate this anisotropic rounded-box family. Halder (2018) computes parameterized MVOE outer approximations for sums of ellipsoids, not the globally optimal enclosing ellipsoid of a nondegenerate box plus a coaxial ellipsoid with all contacts. Courteaux et al. (2025) treat the exact summand type but construct bounding-box-based implicit approximations; the inspected article does not entail the scalar optimum. Resultary hits are Loewner ellipsoids of unrelated rank-selected polytopes/permutohedra, not this set. The general optimality criterion alone is not a prior expression of the new shape without the substantial identity and contact construction.

## value

PASS

PASS: exact global convex-geometric optimization for a natural rounded-orthotope family, reducing arbitrary anisotropy to one monotone scalar parameter and giving a complete active-contact classification and volume. This materially sharpens bounding approximations and the homogeneous rounded-cube special case; neither a parameter substitution nor merely a numeric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
