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

The analytic proof explicitly reduces the constrained two-kernel maximization to two scalar branches, selects the maximizing branch and angle, and certifies the one-variable global maximum by a nonnegative perfect square. Equality and endpoint cases are treated directly.

Run `python3 check_q_berezin.py` with Python 3 standard library. The deterministic script produced `PASS 41440 finite diagnostic assertions`. Tests include the exact overlap constraint, proposed equality kernels, the global square certificate, norm-saturation and relative-defect identities, selected direct Hardy coefficient truncations, and scalar monotonicity checks.

Finite tests cannot prove all-parameter optimality; that conclusion rests on the exact algebraic certificate in `RESULT.md`. No independent audit or external formal certification has been performed.
