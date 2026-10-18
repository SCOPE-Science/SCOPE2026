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

# Reproduction and limits

The standalone `check_distribution.py` uses Python 3, NumPy and SciPy. Execute `python check_distribution.py` in the directory containing that file. It seeds a local Gaussian generator deterministically, uses the same normal increment for Euler and Heun, and checks the resulting discrepancy identity against the explicit affine-normal formula.

For four dimensions and four thresholds, it compares Monte Carlo tail frequencies to `scipy.stats.ncx2.cdf`; for the same dimensions and three larger thresholds, it tests the noncentral chi-square lower-tail coefficient in the inverse-power asymptotic. It also checks clipped support and computes central chi-square large-deviation rates for increasing dimension. Expected terminal message: `PASS: 16 Gaussian conditional CDF checks, 4 Heun identities, 12 tail asymptotic checks`.

Proof-critical steps needing no code are: the exact common-increment algebra, the noncentral chi-square law, monotonic survival transformation, Poisson–gamma small-ball expansion, layer-cake moment criterion and the Gaussian-square log-moment generating function with Cramér's theorem. Finite simulation is not a proof of any general-dimension or limiting result. In particular, a numerically printed near-zero clipping probability should not be interpreted as mathematical probability zero. No independent audit has been performed.
