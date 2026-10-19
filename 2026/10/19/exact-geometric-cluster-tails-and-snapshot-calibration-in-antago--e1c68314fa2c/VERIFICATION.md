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

# Reproducibility and verification

Execute `python verify.py` with Python 3.10 or later from the folder containing the checker. No third-party packages or private assets are required.

The checker passed 1,854 assertions. It checks the half-line linear differential equations, independent numerical integrations of the known one-site density, the all-length geometric formulas and inverse ratios over a parameter grid, and an independently implemented finite-chain dynamic program that averages all proposal times/marks/orders. The finite-chain comparisons include explicit finite buffers on either side of target blocks.

Finite-size experiments and numerical quadrature support, but do not establish, the infinite-lattice identities. The independent mathematical proof is given in `RESULT.md`, including the two independent exterior half-lines, inclusion–exclusion, covariance sign, and ergodic inverse identification. No independent audit or external verification has been performed.
