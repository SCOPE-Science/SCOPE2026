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

# Reproducibility and independent limits

Run `python3 verify.py` using Python 3 and only its standard library. The actual recorded run is contained in `verification_output.txt` and reports 4,898,253 passed assertions.

The verifier exhaustively enumerates every two-predecessor choice history up to \(N=12\), validates the hitting-time/commute-time and longest-run discrepancy identities, and solves independent exact first-step rational linear systems for both directions up to \(N=7\). It also runs deterministic-seed finite-size simulations for \(p\in\{1/4,1/2,3/4\}\). The simulation values are diagnostics and are not certificates of the infinite weak limit.

The analytical limit depends on the exact ancestor renewal representation, the deterministic longest-run bound, a standard inverse-renewal functional central limit theorem, and Brownian integral covariances. These are proved or explicitly invoked with hypotheses in `RESULT.md`. The independent mathematical audit remains unperformed.
