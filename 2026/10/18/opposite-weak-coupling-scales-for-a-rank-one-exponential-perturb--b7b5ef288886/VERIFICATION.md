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

# Numerical reproduction and analytic scope

The standard-library checker `check_carleman.py` was executed at its actual package source path and returned:

`PASS: 83 independent finite numerical consistency assertions`

It independently integrated the angular resolvent at 16 exterior spectral parameters, tested signed monotonicity at seven ordered pairs, reproduced the two exact coupling landmarks, solved 16 implicit spectral equations by numerical bisection, tested two weak-coupling limits, and checked vector normalization and the strong-coupling moment. The numerical results test identities and constants only.

The analytical proof in `RESULT.md` separately establishes the Mellin spectral multiplier, the exact Stieltjes transform, the strict one-eigenvalue classification, exclusion of all embedded/endpoint eigenvalues, and the two sharp asymptotic scales. The numeric tests do **not** establish infinite-dimensional completeness or historical originality. Other perturbation vectors and nonreal couplings are outside the claim.
