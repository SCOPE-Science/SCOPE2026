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

The included `verify.py` carries out exact full-state SymPy stationary and Poisson calculations for the four-state and six-state continuous-time generators. It reconstructs the stated dimensionless capacity formulas independently of the reflection-orbit proof and verifies the polynomial derivative identities and threshold constants. Numerical checks use a temperature increment of \(10^{-4}\), five parameter pairs for each channel size, stationary-response finite differences, and separate time-integrated matrix-exponential transient heat-flux tests.

Run `python verify.py` with SymPy, NumPy and SciPy. The check returned the expected completion messages for both exact rational identities, derivative factorization, ten perturbation/quadrature comparisons, and critical constants. The tests do not establish novelty, infinite-volume limits, or independent validation; those require separate assessment. The closest motivating paper's full text was not available for a conclusive comparison.
