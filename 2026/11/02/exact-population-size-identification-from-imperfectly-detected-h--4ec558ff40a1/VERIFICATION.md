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

The birth–death model's drift and quadratic generator were derived exactly; the stationary mean, variance, covariance decay and conditional binomial-thinning identities were recombined algebraically. Necessity and sufficiency of the two strict interval bounds were checked separately, including all positive-rate boundary exclusions. The interval has an unbounded upper endpoint exactly when the recovered scaled latent variance satisfies \(s\geq pm\), whenever the data are feasible. The two worked examples were checked using fractions; one yields compatible populations of every integer size at least three, the other exactly size four.

Run `python check.py` using the Python 3 standard library. It reconstructs 1,100 finite stationary laws from detailed balance with rational arithmetic, verifies moments and recovery formulas and both examples, and checks the inverse population-size membership against the predicted strict open interval. The script does not replace the analytical proof for arbitrary population size and parameters. Tests use the exact rational covariance multiplier \(e^{-A\Delta}=1/2\). No external data, probabilistic simulation, independent scientific audit or empirical validation is claimed.

The earliest verified primary publication is Kirman (1993-02-01). Its full technical text was unavailable for direct comparison, leaving historical-priority uncertainty; the 2020 and 2022 technical preprints were inspected materially.
