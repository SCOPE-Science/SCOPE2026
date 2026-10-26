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

# Checks and limits

The positive semidefinite matrices in the proof are certified by exact analytic decompositions, not numerical eigenvalue estimates. The trace-class lower bound uses an explicit normalized rank-one matrix and the exact eigenvalues of its image. `CHECK.py` uses only Python standard-library rational arithmetic and checks these equalities at 26 finite sizes; all 26 cases pass. Finite checking is corroborative, not exhaustive, and does not prove the universal or infinite-star statement. The publication date of the motivating source was checked against the arXiv version-one posting of 2026-10-11. Relevant literature was compared at the implication level; possible unindexed historical equivalence remains. Independent scientific validation has not been performed.
