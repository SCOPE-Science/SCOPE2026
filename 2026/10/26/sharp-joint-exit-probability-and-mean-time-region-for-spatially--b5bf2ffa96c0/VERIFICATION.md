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

The analytic proof uses the exact two-state backward generators with absorbing *outgoing* endpoint states and verifies that the expected lifetime is finite. The image of the rate-to-observable map follows from strict spatial centroid positivity and a smooth exponential tilt whose mean is strictly increasing and ranges over the whole open interval. Identifiability failure is certified by cosine perturbations with exactly zero zeroth and first spatial moments.

As a separate stochastic check, `check_simulation.py` simulates 12,000 trajectories for each of four positive profiles at \(L=1.7\), \(v=1.4\), \(K=2.2\), with deterministic random seed 1850744. The predicted right-exit probability is \(0.3125000\) in each case. The simulated values are approximately \(0.3170833\), \(0.3184167\), \(0.3070833\), and \(0.3179167\). The exact predicted unconditional mean times are \(1.2142857\), \(1.5092250\), \(0.9193464\), and \(1.2142857\), while simulated values are approximately \(1.2209925\), \(1.5098492\), \(0.9074149\), and \(1.2067839\), respectively. This finite stochastic experiment is a consistency check, not a proof, and some statistical fluctuations remain. The formulas and limiting feasible region are established by the exact backward-equation proof alone.

Independent audit has not been performed.
