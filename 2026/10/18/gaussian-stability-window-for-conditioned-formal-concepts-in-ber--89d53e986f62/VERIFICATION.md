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

Execute `python3 verify_stability.py` with the included source code and Python 3 standard library. The verification enumerates all binary incidence matrices of sizes at most 3 by 3, with three exact rational incidence probabilities; it checks every admissible nonempty candidate extent and intent having at least one outside attribute. The expected completion line is `VERIFY_OK 264 exact full-matrix conditional checks`.

The checker confirms the finite concept-event probability, conditional first moment, and conditional second moment using explicit enumeration rather than calling the closed formulas to compute the observed moments. This test is a finite cross-check, not a proof of the asymptotic Gaussian statement. The latter rests on the conditioning decomposition, elementary exponential bounds, binomial anti-concentration, and normal approximation in RESULT.md. No independent external audit or certification has been performed.
