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

# Reproducible verification

Run `python verify.py` with Python 3 using only the standard library. The script exhaustively generates every uniform recursive tree through nine vertices using all possible independent parent choices. For every tree it computes total path length, total leaf count, and the childless indicator of each eligible birth label. Rational arithmetic verifies the exact leaf probabilities, the conditional total-path-length expectation shift, the labeled covariances, and the full leaf/path-length covariance. It checks the strictly increasing first-difference sequence of the labeled covariance profile for sizes 3 through 499, and approximates the minimizing age fraction for sizes 100, 1000 and 10000.

Observed local run: `PASS: 640 exact/structural assertions; exhaustive recursive trees through 9 vertices`.

These finite checks cannot establish the unrestricted theorem or historical originality; the unrestricted mathematical arguments are supplied in `RESULT.md`. The established variance of total path length and classical leaf-count variance are cited, not recertified independently here.
