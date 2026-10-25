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

The proof supplies a complete symbolic derivation of the three commutation equations and their solution count. The standalone `verify.py` replays the direct group-enumeration test over prime fields for \((q,b)=(2,1),(2,2),(2,3),(3,1)\) and a distinct diagonal-stratification check for \((2,4),(3,2),(3,3),(4,2),(5,1),(5,2)\). The latter only uses whether pairs of nonzero diagonal labels are equal and therefore also applies to the size-four prime-power case; it does not pretend that modular arithmetic on four symbols is \(\mathbb F_4\). The script must output `ALL_CHECKS_OK` without external dependencies. The general formula is an algebraic proof, not an experimental extrapolation. The main originality risk is an unrecognized classical class-number formula for this exact poset family. No independent audit or independent validation has been performed.
