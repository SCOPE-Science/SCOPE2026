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

# Verification

Execute `python verify_commuting.py` and `python verify_c3.py` from a directory containing their extracted copies. Standard Python 3 suffices. `verification_output.txt` records results.

The first program exhausts all commuting permutation pairs through six points, computes simultaneous-conjugacy isomorphism classes, then groups representatives by the exact collision-profile histogram. The minimum five-point phenomenon is therefore established by a finite exhaustive proof through four and an explicit witness at five. The second program independently computes pair-colour refinement for every isomorphism type of two unrestricted permutations through five points, corroborating the \(C^3\) property in that finite range.

The proofs of the full histogram criterion and all-size three-variable statement are mathematical, not inferred from these experiments. The exact computer checks are reproducible but have not been independently audited by a separate researcher.
