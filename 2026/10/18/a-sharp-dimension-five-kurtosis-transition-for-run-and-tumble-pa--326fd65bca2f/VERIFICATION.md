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

# Verification record

The standalone `rtp_velocity_kurtosis_checks.py` was run using Python 3 standard-library Decimal/Fraction arithmetic and reported `PASS 1136 analytic/Poisson-Dirichlet/symbolic coefficient checks`. It compares independently derived conditional Poisson–Dirichlet fourth moments with the closed formula for multiple dimensions, speed laws, and finite observation times. It checks exponential coefficient cancellation through degree seven and exact positive recurrence through degree 120. It numerically brackets the two explicitly quoted crossover times using 70-digit arithmetic. SymPy was also separately used to verify the exact differentiated-threshold exponential polynomial; SymPy is not required to run the included script.

The analytic proof's induction is necessary for all positive times and all integer dimensions. Finite experiments are not extrapolated to infinite intervals. The findings do not establish priority against every possible result in general velocity-jump and persistent-walk theory. Independent audit has not been performed.
