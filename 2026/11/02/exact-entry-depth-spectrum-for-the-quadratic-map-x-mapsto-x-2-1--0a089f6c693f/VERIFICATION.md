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
# Mathematical verification

The independent enumeration script `verify.py` constructs the complete two-adic residue functional graph at each level from 3 to 14, finds the periodic points, computes the first-entry depth of every residue, and compares the entire cumulative spectrum against the formula. It also checks the exact maximizing residue class and the two periodic points. The script printed `VERIFY_OK exact_all_residues_levels=3..14` in the completed check.

The unrestricted proof is the valuation argument in `RESULT.md`. The script establishes only the finite levels stated. Independent auditing has not been performed.
