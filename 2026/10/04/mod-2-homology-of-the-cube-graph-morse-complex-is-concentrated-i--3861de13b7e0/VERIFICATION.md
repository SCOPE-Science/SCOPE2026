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

The standalone verifier constructs the graph \(Q_3\) from the binary XOR rule and then performs the following checks.

1. It recursively enumerates every acyclic partial orientation with each tail used at most once, obtaining the nonempty face vector \((24,240,1296,4080,7488,7424,3072)\).
2. Independently, it loops over all \(3^{12}\) edge states and tests legality and directed acyclicity from scratch; the counts agree exactly.
3. It reconstructs \(t(t+2)^3(t+4)^3(t+6)\) and verifies that the graph-Laplacian generating identity gives the same face vector.
4. It checks that every codimension-one deletion is present and that \(\partial^2=0\) over \(\mathbb F_2\) on every face.
5. For each boundary matrix it computes the exact rank three ways: high-pivot column elimination, low-pivot column elimination, and high-pivot elimination after transposition. The augmented ranks are \((1,23,217,1079,3001,4487,2933)\).
6. It derives \(\widetilde\beta_5=4\), \(\widetilde\beta_6=139\), zero in other degrees, and checks the reduced Euler characteristic \(135\).

The script prints `VERIFY_OK` only after all assertions pass. These checks establish the stated finite mod-\(2\) computation; they do not address integral torsion, cohomology operations, the full homotopy type, or higher-dimensional hypercubes.
