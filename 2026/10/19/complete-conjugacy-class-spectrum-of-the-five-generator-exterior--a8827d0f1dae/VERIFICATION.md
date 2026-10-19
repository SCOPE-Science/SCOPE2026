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

# Reproducible checks and scope

Run `python3 verify.py` with Python 3.9 or later from the extracted directory. The program imports only the Python standard library and prints `VERIFY_OK` on success.

It reconstructs exterior multiplication for five generators from squarefree bit masks, independently row-reduces the odd-to-even multiplication maps, completely enumerates the \(3^{10}\) ternary alternating-form parameters, performs seeded sample calculations of unit inverses and group commutators over prime fields, and verifies the polynomial's weighted sum equals the group order for the stated odd sample fields. Full enumeration of every element of the order-\(q^{31}\) group is not attempted or claimed. Finite checks do not prove the universal formula, which rests on the proof in `RESULT.md`.

The public review is limited to the self-review recorded in `REVIEW.md` and `AUDIT.json`. No external audit or independent validation has been performed.
