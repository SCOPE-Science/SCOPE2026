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

# Verification notes

The proof's infinite-domain steps use exact Bessel identities, an index-ratio bound derived from a positive power series, concentration of a positive integral kernel, and an exponentially decaying curvature factor. The classic strict Bessel Turán inequality follows from Neumann's product identity, with a positive integral; no finite enumeration substitutes for these analytic arguments.

The included `verify.py` runs on Python 3 using only `fractions.Fraction` and `math.factorial`. Its rational intervals enclose the complete infinite series for three modified Bessel function values in the explicit two-Poisson example, and yield a strict exact-arithmetic inequality. Its remaining finite checks are diagnostic examples of the algebraic estimates, not proof of universal quantifiers.

The sufficient small-product condition is not asserted optimal; no complete finite-index sign-transition classification or independent priority assessment is provided.
