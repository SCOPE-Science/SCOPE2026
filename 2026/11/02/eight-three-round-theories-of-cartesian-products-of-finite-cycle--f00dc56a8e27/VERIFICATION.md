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

# Reproducibility and verification

The exact proof is in `RESULT.md`; these computations are additional finite checks, not an induction or substitute for the all-dimension argument.

Run `python3 torus_types.py` to enumerate two-point extension profiles and test 76 undirected cycle products across dimensions one through five. The script compares each computed set with the eight table entries. Its terminal output is in `torus_types_output.txt`. The vertex list includes every product vertex; the third-vertex loop excludes the two already selected vertices and checks all four adjacency patterns.

Run `python3 direct_rank3.py` to compute full quantifier-rank-three sentence types of 21 finite product graphs by canonical recursive atomic types. It includes all equality patterns, all third-vertex choices, all second-vertex choices and all first-vertex choices, without assuming vertex transitivity. The resulting eight classes and per-graph groups are recorded in `direct_rank3_output.txt`.

No external dependencies are required beyond Python 3. Counts and files were replayed from the actual packaged bytes. Exhaustive finite tests alone cannot imply stabilization in unbounded dimension; that conclusion uses the graph-theoretic lemmas proved in `RESULT.md`. No assertion is made regarding independently performed audit.
