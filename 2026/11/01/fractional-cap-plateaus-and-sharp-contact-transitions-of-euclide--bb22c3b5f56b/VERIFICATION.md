---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run the embedded `verify.py` using `python3 verify.py`. It requires only the Python standard library. The checker independently enumerates all binary and fractional vertices for rational caps and checks, with exact fractions, each vertex's distance against the proposed radius. It also checks that the optimal center coordinate lies in the convex hull of the average coordinates of the contact orbits, which is an independent standard minimal enclosing-ball certificate.

The observed run passed 333 parameter cases, 103,420 exact vertex-distance equalities/inequalities, and 63,032 contact vertices for dimensions 2 through 10. This finite experiment is evidence corroborating the analytic proof and cannot establish the theorem's universal quantifiers.

The mathematical proof independently uses a complete vertex description and minimization of two quadratic branches and proves existence, uniqueness, all boundary cases, and contact criteria for arbitrary real caps. Historical priority and independent mathematical audit are not certified.
