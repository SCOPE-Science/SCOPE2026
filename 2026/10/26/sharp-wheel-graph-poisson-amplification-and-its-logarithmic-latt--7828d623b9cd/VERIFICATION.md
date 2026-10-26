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

The standalone `verify.py` uses exact rational Gauss--Jordan elimination on the full wheel Laplacian with its nullspace removed. It checks all entries, zero row sums, vertex-row absolute norms, and a separate circulant-inverse construction for rim sizes 3--17. It compares explicit exponential kernels with direct finite Fourier series up to rim size 65 and tests the uniform second-order asymptotic error through rim size 50,000. A successful run reports 2,336 individual exact-entry and numerical checks.

The infinite-size statement, positivity partition and accumulation interval are proved analytically in `RESULT.md`; finite tests do not prove those quantifiers. No independent mathematical or bibliographic audit was conducted. The exact wheel Green kernel was known previously and is not claimed as new.
