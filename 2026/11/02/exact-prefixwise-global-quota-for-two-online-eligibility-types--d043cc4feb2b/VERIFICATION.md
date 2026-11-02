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
# Verification procedure

Execute `python3 verify.py` in a directory containing the embedded standalone verifier. The exact-integer test enumerates all \(1\le s\le t\le30\), all intersection sizes, all positions assigned to shared agents, and every pair of counter residues. It verifies that the paired position mapping is injective, its phase inequalities hold, and the rounded proportional-share inequalities hold. The observed result is:

```
VERIFY_OK cases= 5425 residue_checks= 19027800
```

The analytical proof covers all positive finite cardinalities and all possible arrival histories. The computation checks finite ranges only. The proposed exact result depends on two fixed, known eligibility types with unit items; its extension to more types or varying values is unproved. No independent scientific audit is asserted.
