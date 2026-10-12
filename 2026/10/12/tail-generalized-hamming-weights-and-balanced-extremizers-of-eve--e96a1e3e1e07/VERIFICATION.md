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

# Reproducible checks
Execute `python3 verify.py` using Python 3 with the standard library. The script enumerates reduced-row-echelon subspaces and checks simultaneous zero coordinates reconstructed directly from cycle vertices, the bound \(Q^{d+1}\), and the residue-partition extremizer count.

Direct enumeration covers all \(40\) and \(130\) subspaces for \((q,k)=(3,2)\) and \(d=1,2\), all \(156\) and \(806\) subspaces for \((5,2)\), and all \(364\), \(11011\), and \(33880\) subspaces for \((3,3)\), \(d=1,2,3\). The observed maximizing-subspace counts in those seven cases are \((4,6,16,8,16,120,60)\), respectively.

An independent image-based computation enumerates all \(3906\) one-dimensional and \(508431\) two-dimensional subspaces of \(\mathbb F_5^6\), obtaining image maxima \(4\) and \(16\), and extremizer counts \(256\) and \(576\), respectively. The script constructs the predicted \(96\) distinct three-dimensional extremizer planes of \(\mathbb F_5^6\) and checks all torus assignments on each. That last construction verifies attainment, **not exhaustive optimality** for three-dimensional planes. All-parameter assertions follow instead from the classification proof.

The expected terminal line is `VERIFY_OK`. The finite field arithmetic in the executable tests is integer arithmetic modulo the **prime** fields \(\mathbb F_3\) and \(\mathbb F_5\). The proof, which uses only finite-field multiplicative cyclicity and the \(q>2\) additive-sum property, covers all prime powers. These numerical checks are neither infinite proofs nor independently performed audits.
