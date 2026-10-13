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

# Mathematical verification

The proof's exact finite-time law follows from affine transformation of coordinate means and centered variables. The law holds for every Borel probability measure with finite second moment; independence of coordinate draws makes marginal visit counts binomial and their normalized values converge almost surely to the positive sampling probabilities. Scalar equioscillation and harmonic equalization complete the infinite-horizon minimax proof. No simulation is used to establish these infinite statements.

## Reproducible checks

Run `python verify.py` with Python 3 and no third-party dependencies. Expected stdout: `VERIFY_OK 1197 exact-rational checks and limiting-regime numerical cross-checks`. The script uses exact `Fraction` arithmetic to verify per-coordinate energy transformations, the equal-magnitude condition, the closed-form decreases, 27 finite-horizon binomial identities, and the annealed equalization. It also checks the logarithmic probability equalization and a sequence approaching the adverse two-coordinate boundary numerically. The latter tests do not prove the limit; the proof computes it analytically.

## Limitations

Only diagonal positive potential and interaction matrices, exact independent-coordinate pushforwards and fixed sampling distributions are covered. Almost-sure exponential factors do not imply finite-iteration tail bounds. No independent audit or external validation has been performed.
