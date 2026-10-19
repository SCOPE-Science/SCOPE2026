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
The attached `verify.py` uses only standard Python. Execute `python verify.py` to recheck representative finite fields. It enumerates all projective-line permutations and nonzero line scalings for \((q,n)=(2,2),(3,2),(2,3)\), enumerates the invertible matrices over each prime field and tests the common-witness condition for every pair of algebra elements in dimension two, with representative three-dimensional checks. Expected output contains `CHECK 2 2 ...`, `CHECK 3 2 ...`, `CHECK 2 3 ...`, and `VERIFY_OK`. These computations support the finite examples only; the symbolic classification proves the infinite parameter range. No independent audit has been performed.
