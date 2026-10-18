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

The theorem has an integral chain-level proof in `RESULT.md`; the checker is corroborating evidence, not a substitute for a proof of the universal quantifier.

Run `python3 verify.py` with Python 3 and the standard library. It enumerates the normalized cubical chain groups up to degree three for a one-edge graph, a three-vertex path, a triangle, a four-vertex path, a four-cycle, a complete four-vertex graph, and two disjoint edges. It computes signed boundaries and mod-two ranks, and it checks all single-edge cone identities through degree three exactly over the integers.

Expected concluding line:

`VERIFY_OK: 7 graphs, 232 exact signed single-edge contraction tests`

Checks: edge-square support, boundary-squared zero, predicted homology through degree two over the two-element field for finite cases, integral signed contraction on every test cube. These finite cases cannot prove the all-graph theorem and do not test integral torsion in arbitrary larger graphs; the proof supplies that conclusion.

No independent validation has been performed.
