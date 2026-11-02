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

# Reproducibility checks and limitations

The bundled `verify.py` is standalone source, reproducible using Python 3 with NumPy and SymPy; Numba enables additional direct physical-time Monte Carlo checks. Its symbolic stage computes the stationary embedded-chain variance and the full martingale second moment, simplifies the analytic expression to the stated closed form, verifies the strictly positive coefficient of refractory-time variance and the complete-reset boundary, and independently compares an exponential-refractory two-state Markov-Poisson calculation.

Nine sampled cycle-martingale comparisons use three parameter sets crossed with deterministic, exponential, and two-point refractory clocks (650,000 samples per comparison); all relative errors were below \(0.7\%\). An independent path-integral simulator computes the actual \(\int_0^T X_t\,dt\) over a finite time horizon of \(T=4000\) with incomplete final cycles included, across 2,400 replicas per refractory clock type; its variance-rate estimates differed from predictions by \(1.21\%\), \(1.04\%\), and \(0.56\%\), respectively.

Run `python verify.py` in an environment supporting the documented Python dependencies. The exact theorem is proved analytically by a stationary cycle-martingale decomposition, ergodic renewal-time change and finite-moment boundary estimates; sampling checks do **not** prove its infinite-time or all-distributions statement. The paper's original exact stationary one-time law is credited as prior work. No independent scientific audit or independent validation has been performed.
