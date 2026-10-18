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

# Verification and limitations

The theorem is proved analytically by a saddle stable-manifold construction, invariant moving barriers, global convergence of the resource/strategy dynamics, parameter comparison for the invariant graph equation, and a scalar differential inequality yielding a uniform rate bound.

Run `python verify_boundary.py` in a Python 3 standard-library environment. The deterministic program integrates the graph in the logit strategy coordinate, compares numerical phase-plane outcomes, and checks 60 seeded admissible parameter pairs, greed-ordering, and the claimed quantitative bound. For the source parameter tuple it returns a threshold approximately \(0.23295910703656\) at initial cooperator frequency \(1/2\), versus linear interpolation \(0.24017936572844\). These numerical tests support, but cannot replace, the infinite-dimensional quantification over all parameter tuples and initial states in the proof.

Scientific limits: strictly bistable parameter range and deterministic well-mixed dynamics only. No formal proof assistant, external certification, or independent audit is claimed.
