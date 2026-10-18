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
The proof is a finite permutation-counting identity. The attached `verify.py` enumerates labeled tree parent maps for sizes at most six and compares the weighted last-rank masses with the same mass obtained from uniform input-permutation fibers. The equivalence is then checked with an exact factorial/leaf-count computation. Exhaustive bounded tests cannot prove the theorem for arbitrary sizes; the general argument is in RESULT.md. No independent audit has been performed.
