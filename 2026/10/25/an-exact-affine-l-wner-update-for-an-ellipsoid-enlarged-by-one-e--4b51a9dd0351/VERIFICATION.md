---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Affine-normalize original ellipsoid to B2^d and outlier to H e1. Solve dr²+(d−1)Hr=1 with 0<r<1/d; exact factorization of the containment slack is (b^-2−a^-2)(s+r)², verifying the entire ball and unique latitude, while H−c=a. Under candidate normalization, apex plus isotropic latitude orbit with weights 1/(d+1), d/(d+1) has mean zero and covariance I/d. Integrating each competitor gives tr(M^-1)≤d; AM–GM forces det M≥1, equality only at candidate, proving universal optimality and uniqueness. Affine untransform gives Q*. Fixed-H and fixed-d limits follow from root expansion. Independently verified factorization and latitude identities with symbolic algebra.

## originality

PASS

Best-of-knowledge qualified PASS: original special-ellipsoid literature provides a characterization of extremal ellipsoids but inspected studies of cuts, slabs and multi-ellipsoid hulls did not identify the explicit one-outlier rank-one affine update, entire apex-plus-ring contact structure and two sharp limits. A prior geometric optimal-design or polar-dual formulation may remain undiscovered; Todd full text uninspected.

## value

PASS

PASS: adding one outlier to a full ellipsoid is a canonical exact extremal-geometry update problem. Explicit global minimum-volume solution, entire contact-orbit classification and sharp volume limits give useful closed forms not supplied by routine numerical MVEE algorithms. It does not address multiple points or simultaneous limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
