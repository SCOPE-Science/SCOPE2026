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

# Reproduction and mathematical checks

Run `python verification/verify_algebra.py` to independently substitute the two finite-state generators into the claimed Poisson solutions and check the exact variance and maximum-rate identities symbolically. This program uses SymPy; its assertions compare rational expressions identically, not at sampled parameters. It checks identities needed for the proof but does not mechanically establish general martingale central-limit theory.

For an independent experiment, compile and run `verification/check_event_driven.cpp` with a C++17 compiler. It simulates exponential switching and exact deterministic motion between switches, with a stationary-approximation burn-in of forty inverse trap rates. With 50,000 trajectories per model at \(k=1,v=1.4\) and \(g\in\{0.35,1,3\}\), the six observed work-variance rates agree to within approximately 1.2% of their proved asymptotic values, subject to finite-time and sampling errors. It is not an exhaustive or infinite-time numerical certificate.

The probabilistic proof additionally uses irreducibility of each finite-state drive, contractivity of the harmonic coordinate, bounded support under stationarity, the stationary ergodic theorem for predictable jump brackets, and the bounded-jump martingale central limit theorem. These standard analytical steps are justified in the result but are not replaced by the symbolic scripts.

Independent audit status: not performed.
