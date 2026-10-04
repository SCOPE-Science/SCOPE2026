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
# Verification

The analytic proof is self-contained. For each three-point set, translation reduces the character matrix to columns indexed by a map into \(\mathbb F_2^2\); direct determinant expansion gives determinant \(\pm4\) for any three distinct column types and zero for a repetition. The combined map has rank \(r=\dim(U_1+U_2)\) and equal fibers of size \(2^{{d-r}}\). Its image is a subdirect bipartite graph with three-edge matching counts \(4\), \(16\), and \(96\) for ranks \(2\), \(3\), and \(4\), respectively. This proves the universal formula without finite extrapolation.

`verify.py` was executed from the packaged path. It returned:

`VERIFY_OK canonical_cases=12 all_d3_pairs=1596 all_d4_plane_pairs=630`

The script uses only Python standard-library integer arithmetic. It checks the determinant criterion against the projection criterion, canonical rank cases through dimension \(6\), every unordered pair of three-point sets in \(\mathbb F_2^3\), and every unordered pair of two-planes in \(\mathbb F_2^4\). These computations are replay checks, not the proof for arbitrary dimension.
