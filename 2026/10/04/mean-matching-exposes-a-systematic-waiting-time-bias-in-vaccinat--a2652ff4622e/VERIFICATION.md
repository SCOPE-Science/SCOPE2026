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
The general proof is analytic. For an immunization waiting time \(T\) independent of an exponential infection clock of rate \(h>0\), conditioning on \(T\) gives the exact success probability \(\mathbb E[e^{-hT}]\). Strict convexity of \(e^{-ht}\) then proves the deterministic fixed-time extremum at fixed mean.

The standalone `verify.py` replays only consequences that are suitable for finite computation: the fixed and exponential formulas on a deterministic grid, conservation of exit fluxes, ordering of waiting stocks, positivity of the derivative of the relative throughput factor, and several two-point mean-preserving waiting laws. These computations are consistency checks, not a substitute for the Jensen proof over all distributions.

The comparison assumes a common constant breakthrough hazard and constant vaccination-age susceptibility. The steady stock/flux formulas additionally assume constant vaccination inflow. No claim is made about global ordering of the fully coupled epidemic systems.
