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

# Computational verification

Run `python check.py` with Python 3 and SymPy. The supplied program checks the full cubic population mean identity, the lower-front cubic drift, the lower and upper critical variance polynomials, 24 exact finite-population variance calculations, a full six-agent triplet-partition enumeration, and the exact six-agent spin-complement transition-kernel conjugacy for all seven possible incoming and outgoing opinion counts. All assertions succeeded.

The conditional covariance of disjoint triplet compositions is derived analytically from the falling-factorial six-hypergeometric law. The bounded-differences fourth-moment estimate, compact containment, and diffusion martingale-problem limit are mathematical steps described in `RESULT.md`, not numerically certified as statements for every population size. No Lean, independent audit, or finite-chain stationary-distribution claim is made.
