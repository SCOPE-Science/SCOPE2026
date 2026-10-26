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

The bundled `CHECK.py` is standard-library-only. Execute `python CHECK.py` to compare exact rational arc-intersection integrals with the Bernoulli-polynomial covariance formula, evaluate selected finite sample sizes exactly, and inspect the predicted leading and logarithmic asymptotic scales. The bundled `CHECK_OUTPUT.txt` records 358 successful checks.

Proof verification is analytical: independent Fourier orthogonality gives the simultaneous time-shift criterion; the periodic Bernoulli series evaluates the surviving kernel; its Lipschitz bound controls the high-shift tail; a logarithmic cutoff extracts the coefficient of \(\log_bN/N\). The numerical tests are not a proof of an infinite-scale assertion.

Scientific boundaries: only independent Haar starting points, fixed \(b\ge2\), fixed \(s>0\), and circular distance are proved. No independent scientific audit has been performed.
