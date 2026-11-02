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

# Verification notes

Run `python verify.py` in a standard Python 3.10+ environment. The checker needs no third-party packages or other data files. In the submitted package it prints `PASS: 9369 exact rational checks`.

The checker compares the complete event-chain distribution (retaining current walker position and the full visited-set mask) with its compressed \((N,X)\) distribution over 0–7 events, for two initial sizes and three pairs of positive integer intensities. It independently checks the exact linear and quadratic generator formulas of the imbalance process for extensive integer state and rate grids. It verifies all displayed limiting covariance simplifications by rational arithmetic and strict positive definiteness.

The probability limit requires the analytic proof in `RESULT.md`, especially predictable quadratic-variation convergence, the Gaussian martingale theorem, and the initial-segment removal for the singular limiting drift. Finite checks do not verify an infinite central limit theorem. Source inspections and unresolved historical-access risks are recorded in `AUDIT.json` and `REVIEW.md`. No independent external verification has occurred.
