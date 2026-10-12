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

# Reproducible checks

Run `python3 check.py` from the extracted package directory. Python 3 standard library suffices. The script constructs every row from seventeen explicitly listed equal-norm representations and uses fraction-free exact integer elimination; the 17-by-17 complement-column minor is `432`. It also checks that the three template vectors vanish on the rows and are independent on the first three coordinates (determinant `-16`). The exact mathematical proof, not the numerical sampling, establishes the infinite recurrence.

Independent audit has not been performed.
