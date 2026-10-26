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

# Reproducibility and limits

Run `python verify.py` with Python 3, NumPy and SciPy. Actual execution returned `PASS: 90 independent finite checks of fidelity, Haar law, and asymptotics`. Checks include optimizing Pauli-matrix pulse products over phase angles for one- and two-tilt architectures, comparing numerically integrated Haar infidelity with the closed form, testing Haar-quaternion samples against the exact cumulative law, and examining the fourth-order asymptotic coefficient. The fixed random seed makes the finite tests reproducible.

No numerical grid, finite Monte Carlo simulation or optimizer run proves the global all-target result or originality. The proof in RESULT.md is analytic and gives a cap equality for every permitted angle and depth, an exact matrix identity for trace fidelity, and an elementary integral for the Haar distribution. This package makes no claim of independent validation, external certification or proof assistant verification.
