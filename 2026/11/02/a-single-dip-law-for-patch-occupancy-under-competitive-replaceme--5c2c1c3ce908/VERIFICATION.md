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

# Reproduction and limits

The analytical proof in `RESULT.md` gives the arbitrary finite irreducible reversible-chain result. `CHECK.py` uses no nonstandard dependencies. Reproduce with `python3 CHECK.py`.

The checker constructs connected reversible generators, obtains their stationary distributions through an independent exact rational linear solve, and compares the augmented invasion generator's direct stationary solution with the resolvent expression for multiple invasion and extinction rates. It verifies strictly positive first derivative and strictly negative second derivative of the spectral-resolvent scalar, decrease of the derivative-sign function, and the two-state threshold/minimum. Its finite cases are corroborating evidence, not exhaustive proof for arbitrary chain size.

Independent audit: not performed. Historical priority: provisional, especially against unavailable full text of Pakes (1997). No empirical calibration is supplied.
