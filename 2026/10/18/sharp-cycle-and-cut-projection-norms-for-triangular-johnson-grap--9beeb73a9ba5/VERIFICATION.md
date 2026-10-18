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

# Reproduction and mathematical boundaries

Use Python 3 (standard library) and execute `python verify.py` in the directory containing this file. The exact-rational program constructs the triangular graph and the matrix of the cut projection, checks all edge column \(\ell_1\) norms and their complementary cycle-column norms for \(4\le n\le8\), and checks that the cut projector fixes every gradient. For \(4\le n\le7\), it separately reconstructs the matrix by rational inversion of a grounded Laplacian. A successful run prints `ALL_OK checks=24980`.

The general proof is independent of the finite checks. Its nontrivial ingredients are the stabilizer-antisymmetry classification of equivariant gradient columns, the symmetric-matrix uniqueness argument, the two-eigenspace Laplacian inverse on mean-zero vectors, and exhaustive counting of five types of adjacent potential difference. The \(n=4\) sample is a known boundary and is not included in the claimed new parameter domain \(n\ge5\). No unperformed independent audit or exhaustive literature certification is asserted.
