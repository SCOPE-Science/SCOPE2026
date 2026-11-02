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

Run `python verify.py` with Python 3. The script constructs truncated monomial bases, multiplies polynomial coefficient vectors, and computes powers without importing any formula from the proof. It exhaustively counts automorphisms in three two-variable cases and all admissible individual images in one three-variable case. It also performs seeded finite tests in three larger truncations. The expected output ends with `VERIFY_OK prime-power and successor monomial complete intersections`. The checks are finite and do not establish the theorem for all parameters; the proof supplies that assertion. No independent mathematical audit has been performed.
