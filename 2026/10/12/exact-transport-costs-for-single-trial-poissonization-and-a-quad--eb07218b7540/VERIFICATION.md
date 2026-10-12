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

# Reproducible verification
Run \(\texttt{python verify.py}\) with Python, NumPy, SciPy and SymPy. The deterministic script evaluates the exact Poisson maximum-tail series at \(d\in\{1,2,3,5,10,30,100,300\}\), confirms positivity against \(2/e\) with numerical tolerances, solves finite truncated coupling programs at \(d=1,2,3\), compares them to the symmetric maximal-coordinate coupling, and checks the two Poisson tail-series coefficients and their resulting \(7/12\) combination by symbolic rational arithmetic.

Truncation at low counts changes the Poisson distribution, and HiGHS linear programming uses a finite feasibility tolerance; accordingly, the script explicitly permits small discrepancies. Its successful output is a consistency check, not a completeness or infinite-dimensional certificate. The proof in RESULT.md relies instead on pointwise transport lower bounds, permutation symmetry, Poisson factorial moments and a rigorous tail remainder. Independent audit has not been performed.
