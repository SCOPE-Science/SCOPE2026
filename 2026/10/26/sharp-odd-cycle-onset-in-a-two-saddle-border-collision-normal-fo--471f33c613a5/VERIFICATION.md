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

The delivered `verify.py` reconstructs \(M=A_RA_L^2\), \(J_\pm\), the unique affine \(LLR\) branch cycle, the feasibility polynomial and the derivative of the threshold objective using exact symbolic arithmetic. It verifies a concrete rational witness and the quartic rational isolating signs. To reproduce, execute `python verify.py` with SymPy installed. Symbolic checks do not independently audit the quantifier or literature comparison; those arguments are written in `RESULT.md`.
