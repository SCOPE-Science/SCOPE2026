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

Run `python verify.py` with NumPy and SciPy. It independently solves a four-dimensional linear stationary moment system and evaluates the two-time matrix exponential, checking 80 combinations of bath friction, reset rate, and lag; it numerically integrates the time covariance at 16 parameter points and tests six strong-reset asymptotic cases. Observed maximum absolute matrix comparison error: \(1.91\times10^{-11}\).

Run `python simulate.py` with NumPy to perform direct Euler–Maruyama and Poisson-reset trajectory sampling. For \(\gamma=3\), \(r=1.7\), the four observed time-lag covariance discrepancies were below \(0.019\) absolute (sampling and discretization error). These tests confirm finite sets of numerical cases only; the all-parameter statement rests on the algebraic proof. The stationary one-time moments originate in the motivating literature, and the new claim concerns the two-time and integrated observables.
