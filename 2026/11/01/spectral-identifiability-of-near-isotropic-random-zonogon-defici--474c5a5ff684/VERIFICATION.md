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

Run `python verify.py` using Python 3 standard library. It computes pairwise determinant areas, truncated Fourier deficit sums, explicit tail bounds, and numerical checks of the Euler product at multiple positive arguments. It uses reproducible independent accept–reject samples for one nonuniform angular density and compares the sample mean with the exact finite-sample mean. Execution in this package produced `ALL_CHECKS_PASSED`.

For the exact finite Fourier truncation at mode \(M\), the omitted sum is nonnegative and never exceeds \(n/[\pi(2M+1)]\), as used by the checker. These finite tests do **not** establish weak convergence or the inverse theorem; the proof of those assertions is in `RESULT.md` (Steps 3–5). The mathematical argument assumes fixed finite angular Fourier bandwidth, common row density, and independence of directions. Historical priority and independent validation are unperformed.
