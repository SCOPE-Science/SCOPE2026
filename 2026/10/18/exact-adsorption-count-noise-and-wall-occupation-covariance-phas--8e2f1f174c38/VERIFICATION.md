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

Run `python verify.py` using Python, NumPy and SciPy. The script uses event-driven continuous-time run-and-tumble trajectories with orientation reversal and independent bulk resetting, independent exponential wall residence, and a fixed reproducible pseudorandom seed. Its checks compare the theoretical excursion moments, long-horizon Fano and count–bound-time covariance, unique crossover location, and the weak-reset critical-rate limits.

Executed checks: 100,000 exact excursions at each of three reset rates; 2,500 independent time-horizon-750 regenerative trajectories for each of five parameter pairs; four small-reset values; scalar root search. The root was \(r_*=0.5041300402\) at \(v=\alpha=x_0=1\). All programmed tolerance assertions passed. For the five joint tests the empirical count Fano values differed by at most roughly \(0.04\) from the analytic ones, while covariance rates differed by at most approximately \(0.005\). Monte Carlo fluctuations and nonstationary initialization cause finite-sample errors.

Mathematical validity depends on the explicit backward equations, exact resetting transform, regenerative reward identities and the monotonicity argument in `RESULT.md`. Numerical finite-horizon checks cannot certify the full all-parameter or infinite-time statement. No independent external audit has been carried out.
