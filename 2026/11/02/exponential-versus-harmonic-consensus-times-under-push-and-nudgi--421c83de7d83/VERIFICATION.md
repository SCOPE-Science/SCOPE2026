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

# Reproducibility and limits

Execute `python verify_media.py` using a standard Python interpreter. The standalone script uses `fractions.Fraction` to calculate the exact count-chain transition rates and expected hitting times; it solves the original finite first-step systems separately using rational Gaussian elimination. It also reconstructs the update probabilities from individual configurations rather than assuming exchangeability, verifies the finite harmonic inequalities, and checks numerical trends toward the logarithmic rate.

Recorded executed checks: 352 rational hitting-time-system comparisons; 2952 configuration-level transition comparisons; 1232 harmonic inequalities; and 24 numerical large-population logarithmic-rate trend comparisons. The code and all dependencies are embedded in the same research record.

Proof of the infinite-\(N\) statement is analytical: the double-product representation is sandwiched between one exponential term and at most polynomially many terms controlled by its positive logarithmic increments. A finite run cannot certify an infinite theorem or establish priority. No independent external audit has been performed.
