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

`verify.py` reconstructs the exact ball from the published nineteen tetrahedra of \(S_{32}\) and the seven removed tetrahedra. It checks the resulting face vector \((8,25,30,12)\).

For non-evasiveness, the checker uses the standard recursive definition with a nonempty simplex as the successful base case and the empty complex as unsuccessful. It verifies, for every vertex \(v\in\{0,1,\ldots,7\}\), that both \(B-v\) and \(\operatorname{lk}_B(v)\) are non-evasive.

For pure vertex-decomposability, the checker verifies purity, the shedding condition, and recursive vertex-decomposability of deletion and link. It finds exactly one first root, \(5\). The deletion-maximal-face profiles are checked exactly; every other vertex leaves at least one maximal triangle together with tetrahedra, so its deletion is non-pure.

The computation is finite and exact. It does not prove any statement about other triangulated balls or classify all later decision trees.
