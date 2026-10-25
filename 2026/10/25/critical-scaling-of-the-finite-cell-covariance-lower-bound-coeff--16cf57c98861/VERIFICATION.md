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

The fixed-temperature coefficient was derived by a cellwise Taylor expansion with a uniform remainder on the compact interval, followed by the midpoint Riemann-sum estimate. The low-temperature law follows by rescaling the neighborhood of the unique zero and using exponential suppression away from that endpoint. The integral defining \(K_z\) is finite and positive for every integer \(z\ge1\).

The included numerical script checks the finite-cell ratio \(M^2S_M/C_E\) for the critical Ising dispersion at several \(M\) values and checks the \(z=2\) coefficient against its defining integral. These finite calculations are consistency checks, not proof of an infinite limit. No claim is made that the physical entropy bound is saturated at finite M or for arbitrary Hamiltonians.
