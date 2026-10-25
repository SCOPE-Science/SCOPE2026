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

# Reproducibility and verification limits

Run `python verify.py` with Python 3 and NumPy installed. The checker constructs the claimed six-label transition matrices, checks their involution and order-three identities, verifies exact core submatrices and no-leakage blocks for generator macros and sample concatenated words, and compares dimension and macro-length constants. It tests both permutation and unitary tuples for dimensions 2–4 and alphabet sizes 2–5. The bundled `verification_output.txt` ends in `VERIFY_OK`.

These computations are finite sanity checks, not a proof of the universal quantifiers. The symbolic proof is in RESULT.md. The sharp asymptotic lower and upper bounds require Zhao's cited four-letter theorems. No numerical test can replace that published premise or verify absolute literature uniqueness.
