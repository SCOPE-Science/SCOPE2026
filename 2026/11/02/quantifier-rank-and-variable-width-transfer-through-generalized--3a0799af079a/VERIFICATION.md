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

# Verification record

The proof is a structural formula induction rather than a finite enumeration. Steps independently checked algebraically: multiplication in both parity cases; reflection-coset squares; qf kernel formula; existential and universal case splitting; no new bound variable symbols; preservation of rank by qf relativization; sharp equality of least distinguishing ranks in every finite-variable fragment.

`python check_transfer_atoms.py` produced the companion `check_transfer_output.txt`. This tests atomic identities for examples of orders 3, 5 and 9 and is explicitly not a proof for arbitrary groups.

Unproved limits: no claim on function-language quantifier depth, on groups with nonzero two-torsion in the reverse direction, or on independent priority/certification. The 2000 Koponen–Luosto manuscript cited by Gomaa was inaccessible; its possible coverage is an originality risk.
