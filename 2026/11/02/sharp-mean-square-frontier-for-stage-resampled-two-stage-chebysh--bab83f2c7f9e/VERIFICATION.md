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

# Reproducible checks and limits

Run `python verify.py` with the version-compatible dependency in `requirements.txt`. The standalone checker recomputes the stage multiplier and verifies its mean/variance factorization symbolically. It then executes 245 exact two-client probability configurations, 480 further exact finite-support cases, and the complete ordered-pair rational certificate for the clients with curvatures \(1\) and \(6\). It checks the exact mean, second moment, shared-batch second moment, and four-outcome absolute product underlying the iid strong-law exponent.

The exact distribution-free statement follows from independence, moment algebra, and a factor sign classification. The almost-sure statement follows from the classical strong law on a four-atom nonzero multiplier distribution. These analytical arguments are required: finite checks cannot establish a universal infinite-horizon theorem. The check does not validate nonlinear or floating-point behavior, earlier priority, or the source method at other damping parameters. Independent mathematical audit has not been performed.
