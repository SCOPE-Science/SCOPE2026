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

# Reproducibility
Run `python3 CHECK.py` with the Python standard library. The checker prints `VERIFY_OK` on success. It independently verifies an exact Chebyshev identity for all indices below ten; over \(\mathbb F_3\) and \(\mathbb F_5\), it enumerates all projective symmetric Toeplitz matrices for \(n=4,5,6\) and checks equality of the rank-at-most-two locus and the predicted two projective curve components. These finite tests cannot prove the characteristic-zero, arbitrary-dimensional theorem: the exact proof is in RESULT.md.

No external independent audit or mathematical certification has been performed.
