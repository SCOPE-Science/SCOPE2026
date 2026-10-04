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

`verify_desargues_matching.py` reconstructs the Desargues graph from the generalized-Petersen definition, checks \(30\) edges, enumerates every matching, and forms every mod-2 boundary map.

Expected matching counts for cardinalities \(0\) through \(10\):
\[
(1,30,375,2540,10155,24486,34945,27840,11040,1720,60).
\]
Expected boundary ranks for cardinalities \(1\) through \(10\):
\[
(1,29,346,2194,7961,16525,18415,9380,1660,60).
\]
The reduced Betti numbers are \(5\) in degree \(5\), \(45\) in degree \(6\), and zero otherwise. The Euler check is \(\chi=41\) and \(\widetilde\chi=40=-5+45\).

The script uses exact bitwise Gaussian elimination over \(\mathbb F_2\) and prints `DESARGUES_MATCHING_VERIFY_OK` only after all assertions pass. This verifies only the finite mod-2 homology calculation; it does not determine integral torsion or the complete homotopy type.
