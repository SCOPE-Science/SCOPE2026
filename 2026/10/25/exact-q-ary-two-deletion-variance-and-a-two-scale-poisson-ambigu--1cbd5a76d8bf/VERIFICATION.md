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
# Reproducibility and limits

Run `python3 verify.py` with Python's standard library. The verifier enumerates every distinct double-deletion descendant directly and compares it against the derived local formula; it also computes exact rational population moments and counts full-volume centers for multiple alphabets and word lengths. It prints `TOTAL_WORDS 39669` and ends with `VERIFY_OK` on success. See `verification_output.txt` for the actual recorded output.

The finite tests exercise the local formula and moment arithmetic. The infinite limits are analytic consequences of the factorial-moment proof. No independent audit or external validation has been performed.
