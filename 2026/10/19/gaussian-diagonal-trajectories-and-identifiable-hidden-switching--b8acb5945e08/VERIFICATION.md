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

# Verification record

The mathematical proof is in `RESULT.md`; run `python VERIFY.py` with SymPy installed for independently constructed symbolic checks. The checker derives stationary polynomial moments from the full Markov-switching generator, rather than copying the conditional-beta fourth-moment derivation. It checks exact positive fourth and negative eighth cumulants, zero sixth cumulant, two exact Gaussian projection directions, mixed fourth-moment anticorrelation, and a separate covariance differential-equation/repeated-root computation. All rates in the proof range over all positive real admissible values; finite symbolic checks corroborate the analytic arguments and are not alone a proof.

There has been no independent audit or external certification. Some originality risk remains because Markov-modulated OU transform/moment theory covers the broad family, and a pre-existing specialized classification may be unlocated.
