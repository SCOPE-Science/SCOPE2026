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

The standalone `check.py` reconstructs exact equality/inclusion types for all third selections using four membership cells and checks complete three-round equivalence in finite instances. Execute `python3 check.py` (standard library only) and compare with `check_output.txt`. It directly enumerates all flats in fifteen small models, compares that recursion to the four-cell formula, and checks tens of thousands of finite boundary configurations for the pumping identities used in the proof.

The arbitrary-parameter statement requires the combinatorial pumping argument in `RESULT.md`. Bounded program output alone does not certify universal stabilization. This package does not contain an independent audit or any claim of external certification.
