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

# Reproducibility and verification

The analytic proof uses the path eigenbasis, algebraic integrality of doubled cyclotomic cosines, an elementary algebraic-integer norm lemma and the PBH eigenspace rank criterion. Every step applies to the stated infinite rational family. No finite computation is used as a substitute for those arguments.

The supplied `verify.py` constructs the scaled Laplacian with integer entries for each rational rung conductance, independently forms the full one-input Kalman matrix and computes rank over a large prime field. Exactly 504 predicted-versus-computed ranks were compared for 19 ladder lengths, seven rational rung strengths and selected vertices. All 504 matched when this package was checked.

Run `python verify.py` in Python 3 with NumPy installed. The program prints a PASS count on success or raises an assertion with the failing graph, site, weight and two rank values.

The modular tests are finite and can only corroborate instances; the proof, not this test, establishes the all-size real-rank formula. The controls are unconstrained scalar inputs and the theorem does not bound actuation energy or conditioning. There has been no independent mathematical audit.
