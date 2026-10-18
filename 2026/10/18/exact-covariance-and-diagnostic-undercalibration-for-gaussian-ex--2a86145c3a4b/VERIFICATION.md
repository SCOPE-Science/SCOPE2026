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
# Reproduction checks

Run `python verify.py` with Python 3.10+ and NumPy. The executed program returned:

`PASS {'exact': 3240, 'matrix': 528, 'sampling': 750000}`

The exact tests use rational numbers for beta moments, expected pair covariance, mean-square variance and the dispersion calibration ratio across integer dimensions and probe counts. Direct small-matrix Gaussian examples evaluate the Nyström/FLEXTRACE formula independently of the rank-one residual simplification and cover both \(k\leq n\) and \(k=n+1\). The Gaussian simulations compare empirical joint moments of paired projection residuals with the analytic covariance in five dimensions; their threshold is statistical, not exact.

The analytical proof in `RESULT.md` is necessary for the all-dimension claim; no amount of finite random testing could prove it. No proof-assistant formalization or independent audit has been performed. Exact arithmetic is assumed for the mathematical result, whereas the reproduction program necessarily uses floating-point matrices for its direct examples.
