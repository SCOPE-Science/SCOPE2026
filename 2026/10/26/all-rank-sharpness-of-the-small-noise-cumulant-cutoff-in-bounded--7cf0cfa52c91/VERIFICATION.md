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
The embedded file `verify_cumulant_towers.py` is run with `python verify_cumulant_towers.py`. It passes 107 exact rational comparisons between partition-inversion coefficients and independently enumerated labelled-tree weights in ranks 2 through 6, for four fixed symmetric matrices in dimensions 1, 2, and 3. No random seeds or third-party Python modules are needed.

The code verifies only a finite sample of coefficients. The proof of the all-rank assertion is the exact moment identity, the connected-graph inversion, and the pathwise cutoff plus exponentially small exit probability, as described in `RESULT.md`. The analytic constants may depend on fixed rank, dimension, covariance and time horizon. Independent audit has not been performed.
