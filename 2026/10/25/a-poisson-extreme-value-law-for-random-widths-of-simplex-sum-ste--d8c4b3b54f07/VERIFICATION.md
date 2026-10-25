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

The exact Gaussian support identity is proved by counting inclusion subsets by their highest-ranked leaf. A standard-library executable `CHECKER.py` confirms the exact combinatorial identity with rational arithmetic in 72 finite cases. The checker also cross-checks the limiting variance constant from a polylogarithm and a 3,000-term exponential-variance series, and finds strictly positive third cumulant. A seeded Monte Carlo check samples 5,000 terms in each of 900 independent series realizations as a diagnostic.

The infinite-dimensional proof does not depend on these finite experiments: Gaussian quantile/exponential spacing coupling and normal Mills asymptotics give the upper and lower limiting point processes; summable geometric rank weights justify tail truncation; beta-gamma ratios yield the independent-exponential law; and the radial chi normalization converts the Gaussian width to spherical direction width. The exact mean is derived from Gaussian support additivity.

Independent mathematical replication, complete bibliographic exhaustiveness, finite-sample error bounds and independent audit are not claimed.
