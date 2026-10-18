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

The self-contained analytical proof is in `RESULT.md`. A standalone `check_primepower_cubic.py` computes cyclic chirp correlations by finite Fourier transform independently of the claimed congruence spectrum. It separately constructs and diagonalizes the complete projector Gram matrix at dimensions at most sixteen. The recorded output in `checker_output.txt` covers 21 prime-power moduli, including characteristic two through exponent eight and characteristic three through exponent five, and compares the entire ambiguity array, ranks, spectral levels and Moyal sum.

The finite checks do not certify the infinite-parameter proof. Floating-point errors below machine-scale numerical tolerances do not establish symbolic equality. The normal operator is not globally invertible; its reported condition number is for its identifiable subspace.
