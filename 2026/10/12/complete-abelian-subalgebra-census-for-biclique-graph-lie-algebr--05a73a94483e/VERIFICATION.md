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

# Verification of the abelian-subalgebra census

Run `python3 verify.py` with Python 3.8 or newer and no additional dependencies. The script constructs all row-reduced echelon linear subspaces and tests bracket vanishing directly, without implementing the structural classification. It compares the complete dimension distributions for \((a,b,q)=(1,1,2),(1,1,3),(1,1,5),(1,2,2),(1,2,3),(2,2,2)\) against the closed formula. A separate horizontal-space enumeration tests maximality by matrix-rank containment.

Executed checks returned `VERIFY_OK`. The observed \((2,2,2)\) abelian-subalgebra dimension counts were `1,255,2347,4035,1571,135,2,0,0` and its maximal-abelian subspaces had dimensions \(5\) (nine) and \(6\) (two). All-dimensional field-independent correctness rests on the mathematical proof, not these finite tests. Prime powers beyond prime fields were not enumerated; arbitrary fields were not exhausted. Independent audit has not been performed.
