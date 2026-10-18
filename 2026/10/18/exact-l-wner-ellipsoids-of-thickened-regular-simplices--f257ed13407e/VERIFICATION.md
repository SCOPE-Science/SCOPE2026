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

Run the standalone `verify.py` with Python 3. It uses only `fractions.Fraction` and checks 510 exact rational triples \((n,k,t)\) and 3,060 exact rational support-function factorization instances. The corresponding nonnegative scale is recovered as \(s=(k-nt^2)/((n-k)t)\) whenever positive.

Expected completion line:

`VERIFY_OK exact_parameter_pairs=510 support_factorizations=3060 dimensions=3..16`

The verifier checks identities but does not exhaust real parameters or arbitrary ambient dimensions. The universal containment, optimality, contact classification, and differentiation statements follow from the proof in `RESULT.md`. Independent audit has not been performed.
