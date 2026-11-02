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

## Checks

Run `python verify.py` with SymPy installed. The script verifies the exact derivative identity and nonnegative-coefficient polynomial; reconstructs conditional triangle averages by exhaustive graph enumeration for selected small sizes; and checks 44,230 total symbolic, enumeration and finite-parameter assertions. It passed in the authoring environment before packaging.

The mathematical proof of strict monotonicity for all valid parameter values is in `RESULT.md`. Finite enumeration and symbolic spot checks do not prove the universal domain by themselves. The accompanying test code contains no external network calls. Literature priority is qualified and independent audit has not been performed.
