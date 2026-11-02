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

The exact finite-state checker in `verify.py` constructs rational transition matrices and solves their invariant probability vectors. Tested dimensions are 2, 3, and 4, with several rational Euler diffusion numbers including the checkerboard point and the two-cell anticorrelation regime. It verifies site means, every checked off-diagonal sign, parity-block factorization, the closed two-site covariance, and the three-site same-parity correlation. Run `python verify.py` after `pip install -r requirements.txt`.

The script neither proves uniqueness for arbitrary grid sizes nor an infinite parameter range. Those facts follow from the Perron-weighted coupling and exact covariance-series and kernel-factorization arguments in RESULT.md. The statement concerns idealized complete-step fixed-level stochastic rounding, not floating-point hardware.
