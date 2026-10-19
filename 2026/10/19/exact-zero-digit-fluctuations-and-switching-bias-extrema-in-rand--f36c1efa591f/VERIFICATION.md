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

Run `python3 verify.py` using Python 3 and its standard library only. The successful observed output was `PASS: 434 exact checks (direct interval-affine cylinders, matrix PGF, finite variances, covariances, extrema).`

The script independently propagates the eight actual affine quarter-branches of the endpoint random maps, weighted by each map's selection probability, starting from the stationary piecewise-constant density. Its rational push-forward densities determine exact length-\(N\) zero-count probabilities without assuming the reported two-state matrix. It then compares those probabilities with matrix powers for seven rational probabilities, all lengths \(0\le N\le10\), as well as exact moments and finite-length variances. Additional rational tests check the finite-lag covariance identity for five probabilities through lag ten and the balanced binomial distribution through ten digits.

The script does not independently prove assertions quantified over all real \(p\), all lengths or infinitely long trajectories; those are mathematical consequences of the complete branch partition and Perron/spectral calculations in `RESULT.md`. The differentiable finite-dimensional Perron eigenvalue gives the central limit and large-deviation claims analytically. No independent mathematical audit or historical-priority certification is represented by these tests.
