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

The finite exact-rational checker is `CHECK.py`; execute `python3 CHECK.py` using Python 3.9 or later, with no third-party packages. It enumerates 48 positive integer weight profiles with between three and eight generators, checking 1,328 proposed facets for exact affine rank and 3,936 distinct projected sign-corner vertices. It verifies all facet inequalities on enumerated vertices, exact circumradius identities, the active edge graph, and the full predicted dimension of feasible inball centers by constructing linearly independent feasible examples.

The checker has been executed successfully on the embedded source before acceptance. These finite checks do not certify the result for arbitrary real weights or arbitrarily many generators; those cases are addressed by the analytical facet and center-locus proof in `RESULT.md`. The exact partition-complexity implication is a standard reduction, not an experimentally established hardness result. Independent audit is not performed.
