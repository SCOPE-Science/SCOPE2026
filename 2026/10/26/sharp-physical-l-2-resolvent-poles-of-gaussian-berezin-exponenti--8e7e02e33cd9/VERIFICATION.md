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

Run `python3 gaussian_berezin_jet_verify.py` using the standard library. The verifier prints `VERIFY_OK: 516 exact rational assertions` and `PHYSICAL_L2_VERIFY_OK: 15 exact shifted-Gaussian Gram checks` on successful execution. The first group tests nilpotency/ranks and highest-power coefficients; the second builds Gaussian monomial Gram matrices after the explicit shift and checks exact dual norm values using fraction-preserving linear solves. The checked degrees and real parameter pairs are written in the program; complex-parameter and all-degree validity follow from the proof in RESULT.md. An exact Gram check is not a substitute for the general Hermite orthogonality argument.

The norm is the inherited Gaussian physical-symbol norm, not the unweighted formal coefficient norm. This distinction is essential for comparing pseudospectral constants. No independent scientific audit has been performed.
