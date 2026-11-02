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

Run `python3 verify.py` from a directory containing this document and `verify.py`. The script implements finite fields by irreducible polynomial quotients and determines squarefreeness by Euclidean polynomial gcd, not by the incidence argument used in the proof. It independently counts, for each selected nonzero constant shift, the monic quartics for which both polynomials are non-squarefree, and compares against the formula.

Observed replay: `VERIFY_OK fields 12 shift_cases 88 quartics 596920`. Fields of orders 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, and 17 have every nonzero shift checked; order 25 has four representative shifts checked. The script verifies finite samples; the theorem for arbitrary prime powers depends on the supplied mathematical proof. No independent audit has been performed.
