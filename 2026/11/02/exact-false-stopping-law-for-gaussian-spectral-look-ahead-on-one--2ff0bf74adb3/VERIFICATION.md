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

The full proof is in `RESULT.md`; the supplied `verify.py` is a standalone finite diagnostic using Python 3, NumPy and SciPy. Executing `python verify.py` on the embedded file yielded `PASS: 1133 deterministic and seeded numerical checks` and `Example false-stop probability: 0.989767987748`.

The script tests the QR-based spectral norm against the rank-one projected-eigenvalue identity and independently checks the one-coordinate Haar scaling identity; it uses normal random matrices of seven sizes and three power counts. It evaluates beta CDF probabilities across increasing column widths, compares seeded independent chi-square-event frequencies with the closed CDF, and checks the explicit finite example and phase-trend signs.

The general proof uses the exact identity for the rank-one compression, the deterministic scaled-subspace projection formula, and Gaussian Haar invariance. The asymptotic assertions use chi-square concentration. Neither finite numerical tests nor a probabilistic fit is an infinite-dimensional proof.

No external independent audit was performed. Bibliographic priority, extensions beyond the one-spike/flat-tail real Gaussian family, and finite-precision robustness remain unverified.
