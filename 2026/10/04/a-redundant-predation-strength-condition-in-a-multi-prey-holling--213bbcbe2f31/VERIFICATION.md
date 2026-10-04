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
The analytic verification checks the exact predator per-capita growth inequality under \(c_i\le b_i\), the induced bound \(R_0<1\), and the comparison constants used in the proof.

`verify.py` also integrates a two-prey instance in which both source inequalities \(p_i^2<4a_i\) fail strongly while \(c_i\le b_i\) holds. The computed trajectory approaches the predator-free equilibrium and respects the derived exponential predator bound. This finite computation is a stress test only; the accepted theorem is established analytically in RESULT.md.

The verification does not claim necessity of the criterion and does not cover boundary prey initial data, delayed systems, stochastic models, or modified functional responses.
