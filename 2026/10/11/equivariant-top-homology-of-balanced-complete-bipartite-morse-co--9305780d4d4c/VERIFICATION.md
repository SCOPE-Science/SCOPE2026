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

# Reproducibility and scope
Execute the adjacent dependency-free source file using `python3 verify_equivariant_k44.py`; it prints `VERIFY_OK` after all assertions. The program exhaustively examines all \(5^8=390625\) rooted-orientation assignments on the eight graph vertices, keeps \(140625\) acyclic assignments, and computes signed fixed-face Lefschetz sums on twenty representative automorphisms.

The verified character sequence for fifteen side-preserving classes in the order printed in RESULT.md is:
`7,0,3,3,3,0,0,0,0,63,3,-9,15,-45,5103`.
The five side-exchanging character values are:
`-1,0,3,-1,27`.
The program checks that conjugacy-class sizes sum to \(1152\), their weighted character sum is \(6912\), and the trivial-isotypic multiplicity is \(6\). The diagonal-swap family formula is independently spot-checked by exhaustive enumeration for \(m=2,3,4\), while its proof for every \(m\ge2\) is symbolic and relies on the graph Laplacian forest identity and Jojić's established homology concentration.

All computations use exact integers; no floating-point tolerances, randomized searches, or external libraries enter the certificate. Full character claims for \(m>4\), integral representation-lattice classification and equivariant homotopy types remain unproved. The same-model scientific review is not an independent audit.
