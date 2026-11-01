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
# Reproducible verification

Run `python3 cycle_ind2_dihedral_check.py` in the extracted document directory. It checks by direct subset-orbit enumeration all dihedral characters for each integer \(4\le n\le16\), totaling \(260\) group elements, and validates the exact four-state transfer identity and quotient invariant dimensions. Expected marker: `CYCLE_IND2_DIHEDRAL_CHARACTER_EXACT_CHECK_OK`. The uniform proof is in RESULT.md, relying for homological concentration only on the identified published Theorem 4.6. These are finite corroborations and do not independently certify infinite universality.
