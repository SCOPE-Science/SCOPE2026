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

# Reproducibility

Run `python verify_incidence_rank.py` using Python 3 (standard library only) in a folder containing the program. The exact output used for this review is saved as `rank_checks.json`.

The program independently constructs the two prime-field incidence graphs, checks that each has the correct regular degree, recursively computes the complete finite first-order rank types of all ordered tuples through rank four, and verifies that the two uncoloured graphs have the same rank-four type of the empty tuple. It checks that the uncoloured rank-one triple profiles are precisely the 24 geometric categories in the proof and that the rank-two pair types number four. It also confirms agreement of the sort-named graphs at rank three and separation at rank four.

The rank-five uncoloured separator is verified by the exact degree difference. The incidence-axiom proof in RESULT.md, not the finite enumeration, establishes rank-four equivalence for every finite projective plane, including non-Desarguesian instances. No higher-rank exhaustive census is claimed, and no independent validation has been performed.
