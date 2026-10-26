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

The standalone `verify.py` counts distinct scattered subsequences by independently constructing their complete sets, including the empty word. Exact rational word probabilities are used for five biases and all lengths through ten. The verifier compares complete enumerations against first moments and second moments from the theorem's matrix and scalar recurrence. It also checks the cubic characteristic polynomial using SymPy when available.

Proof-critical identities are in RESULT.md, including the letter-update bijection, first- and second-moment transformations, exact initial values, characteristic polynomial, positive Perron projection, and a uniform strict inequality for all interior bias parameters. Finite enumeration is not claimed as a substitute for these arguments. No independent external audit is asserted.
