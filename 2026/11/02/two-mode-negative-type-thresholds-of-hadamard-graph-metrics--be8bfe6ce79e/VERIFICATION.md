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

The analytic certificate is the four-eigenvalue table and the sign-and-concavity argument in `RESULT.md`, not finite enumeration.

The included `check.py`, run in Python with the versions specified by `requirements.txt`, independently constructs the incidence graphs for Hadamard orders \(4,8,12,16,20\), reconstructs their actual shortest-path distances via breadth-first search, and confirms the spectrum of the powered-distance matrix at 30 distinct order/exponent combinations. Observed local output:

```
order=4 roots_rho_sigma=1,1 critical=1
order=8 roots_rho_sigma=0.548266996421,0.472668518614 critical=0.472668518614
order=12 roots_rho_sigma=0.333888133778,0.350055449681 critical=0.333888133778
order=16 roots_rho_sigma=0.240717706899,0.288502592661 critical=0.240717706899
order=20 roots_rho_sigma=0.188335913698,0.250152601662 critical=0.188335913698
HADAMARD_NEGATIVE_TYPE_CHECK_OK cases=30
```

The eigenvalue comparisons are to independently constructed numeric symmetric matrices, not merely re-evaluation of the distance polynomials. Numerical tolerances are \(10^{-8}\), and scalar root bracketing uses the monotonicity/concavity proved in `RESULT.md`. Reproduction command: `python check.py`.

**Scope of this verification:** no exhaustive enumeration of Hadamard matrices or all orders; all-dimensional correctness rests on the analytical distance-regular recurrences and inequalities. The article does not claim an external audit or machine-certified infinite proof. Independent audit: not performed.
