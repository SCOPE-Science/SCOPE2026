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

# Finite-field verification

Run `python verify_rank_one_idempotent_commutators.py` in the directory containing this file and the checker. The code scans all matrices, directly tests rank-one idempotence, forms both matrix products, and classifies the commutator independently of the counting parametrization. The field with four elements is constructed with the irreducible polynomial \(X^2+X+1\).

The exact tested cases are \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2)\). The recorded output reports 348,853 examined matrices and 669 rank-one idempotents; each similarity-type multiplicity agrees with the theorem. It verifies the cubic identity, nilpotency indices and rank classification in each enumerated case.

The verification is finite; it is not an exhaustive proof for untested orders or dimensions and does not establish novelty. The general proof relies on the rank-one vector/covector parametrization and exact pairing counts, not on this enumeration. Independent audit is not performed.
