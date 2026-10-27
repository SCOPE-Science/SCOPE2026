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

Run `python3 verify.py` from a directory containing this file and `verify.py`. The program constructs every digit-choice support for \(k=1,2,3,4,5\), independently evaluates the integer pair counts for every shift, confirms each value against the balanced-base-seven formula, verifies the full histogram, confirms the number of distinct supports and classes under reflection, and checks the multiplicative order of two modulo each involved power of seven. For depths one through four, it independently computes the sixth Fourier moment as the squared coefficient norm of the cubed support polynomial, then compares this with the exact recurrence. A successful run ends with `VERIFY_OK`.

The verified finite range is not an exhaustive check of arbitrary depth. The proof for all \(k\ge1\) requires cyclotomic irreducibility, support-product uniqueness, and unique balanced-base-seven digit differences, as established in RESULT.md. No independent audit has been performed. The full text of the older Inglis--Wiseman paper was not available for priority comparison.
