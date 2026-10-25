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
# Verification and limits

The self-contained `verify.py` reconstructs the exact graph Laplacian and its two-block Gaussian support function; the script checked 320 finite instances covering \(2\le p,q\le9\) with five independent Gaussian trials per pair. Each trial directly compared matrix multiplication with the block formulas and compared the resulting spherical width with the maximum-minus-minimum formula.

At \(n=6000\), 3500 independent samples in each of three imbalance regimes gave approximate upper-part selection frequencies of 0.2643, 0.5049, and 0.7446 for crossover parameters near -1, 0, and 1; the limiting predictions are 0.2682, 0.5000, and 0.7318. The corresponding lower-part frequencies were 0.2703, 0.5037, and 0.7411. These are diagnostics only: finite Gaussian extreme-value centering converges slowly, and the simulated normalized width mean differs visibly from its asymptotic mean at this dimension.

The mathematical proof itself is finite-dimensional linear algebra followed by standard Gaussian-tail extreme-value estimates, a four-variable joint limit, an exponential-race calculation, and a spherical-radius concentration estimate. No finite simulation substitutes for any of these steps. Reproduction: run `python verify.py` in an environment with Python, NumPy and SciPy. Do not interpret a successful run as independent verification, publication, or an automated proof of an infinite limit.
