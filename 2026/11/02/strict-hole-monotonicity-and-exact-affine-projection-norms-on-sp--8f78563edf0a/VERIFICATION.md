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

# Reproduction and scope

Run `python verify_annulus.py` with Python 3 and `mpmath>=1.2`. The script sets 48-decimal-digit precision and independently computes the norm by two methods: an incomplete-beta closed formula and direct nested radial/angular quadrature of the positive kernel part. The tested dimensions are 2, 3, 4, 5 and 6, at radii 0, 0.15, 0.5 and 0.81. It also compares strict norm ordering at five radii per dimension, the sphere/ball dimension relation, the exact value for a three-dimensional ball and a two-dimensional sphere, and four small-hole coefficients.

Observed on the packaged `verify_annulus.py`:

`VERIFY_OK: 51 high-precision formula, direct-integration, monotonicity, shell/ball, and small-hole checks`

The proof of strict monotonicity is analytic, using a one-crossing distribution argument, and is not contingent on tests. Numerical quadrature and finite profiles do not certify universal quantifiers, rule out all older equivalent literature, or constitute independent scientific verification. No external audit was performed.
