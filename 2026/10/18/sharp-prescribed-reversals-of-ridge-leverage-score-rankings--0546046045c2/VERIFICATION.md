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

# Verification and limits

Reproduce with `python verify.py` after installing the packages declared by `requirements.txt` in a clean directory containing these two files. The executable uses exact SymPy rational polynomial residues to test the partial-fraction identity and computes actual real orthonormal-column matrices by positive definite square roots. It independently evaluates both original row scores through the full regularized normal equations. The packaged script passed **540 assertions** covering the explicit crossings at \(1\) and \(4\) and multiple distinct specified root sets at each dimension \(2\) through \(9\).

The universal proof is algebraic: spectral-projector decomposition bounds the polynomial degree, and positive square-root completion realizes any prescribed root set with a valid common data matrix. The finite checks cannot prove the statement for all dimensions, all singular spectra or all positive regularization parameters. Pairwise crossings do not imply a bound or guarantee for full sorting algorithms.

These checks are same-model calculations only. No independent external scientific audit or priority certification has been performed.
