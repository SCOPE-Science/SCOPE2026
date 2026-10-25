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

The analytic proof in `RESULT.md` provides a complete derivation of the local-time normalization, the Neumann heat-kernel covariance identity, the sharp \(2/3\) constant, the almost-sure exposure law, and the smooth pulse counterexample. The deterministic `verify.py` program runs without third-party packages and passed 19 finite assertion groups, checking Basel-sum bounds, spectral finite-time variance, pulse-width summability, and survival-bound arithmetic.

Run from the extracted directory with `python verify.py`. The finite calculations do not replace the heat-kernel argument, the infinite Basel-series identity, Borel--Cantelli, or the limit proofs. An independent mathematical audit was not performed.
