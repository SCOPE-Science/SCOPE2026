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

Run `python verify.py`. It reconstructs the house graph, its \(12\) primitive vector fields, all \(208\) nonempty gradient-field faces, and the face vector \((12,51,90,55)\). It rebuilds all \(592\) Hasse covers, recreates the deterministic \(101\)-pair toggle matching, and checks that reversing exactly the matched covers gives an acyclic directed Hasse graph. The unmatched faces are one \(0\)-simplex and five \(3\)-simplices.

As independent finite checks, exact permutation expansion gives
\[
\det(L+xI)=x^{5}+12x^{4}+51x^{3}+90x^{2}+55x,
\]
and direct boundary calculations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) give ranks \((11,40,50)\) and Betti vector \((1,0,0,5)\).

The exhaustive computation proves only the stated finite case. The field calculations are cross-checks; the homotopy conclusion uses the explicitly verified acyclic Morse matching.
