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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 standard library from the directory containing this file. The script enumerates all partition-respecting maps for ten small \((r,m)\) pairs and directly tests each map for idempotence, records its character and image rank, and compares with the independent product-sum count. Verified pairs: (1,1), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3), (4,1), (4,2). Notable total/constant-character counts: (3,3) gives 9028 / 3348 and (4,2) gives 2073 / 264. The finite character formulas and additional stable logarithmic calculations at block sizes 250, 1000 and 5000 passed. Output ends with `VERIFY_OK`.

The infinite conclusions require the analytic proof in `RESULT.md`: uniformly controlled logarithmic Laplace estimates and a strict entropy gap between character-basin compositions. The finite tests cannot certify the infinite limit. No external independent audit has been performed.
