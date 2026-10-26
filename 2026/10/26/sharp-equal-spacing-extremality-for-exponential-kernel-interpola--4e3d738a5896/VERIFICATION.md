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

# Reproducible verification
Run `python check.py` using Python 3.9 or later. The script uses only the standard library. The checker reports 1,942 configurations passed, comprising 1,890 exact inverse/monotonicity comparisons and 52 Toeplitz spectral boundary checks. Tests compare the exact rational inverse \(Q\) against the Gram matrix and check sign-conjugated inverse entries, while a self-contained Jacobi eigensolver evaluates finite spectral examples. Re-run the extracted file rather than relying on a prior textual log.

The proof is analytical: the innovation-factorized inverse, Perron–Frobenius strict order, finite Fourier Rayleigh inequality, and limit of constant/alternating Rayleigh quotients establish its infinite and all-size statements. Finite tests do not certify spectral monotonicity in every dimension or novel publication priority. At the equality separation threshold the guarantee holds for every finite matrix, while the best dimension-free constant is approached only as matrix size increases.
