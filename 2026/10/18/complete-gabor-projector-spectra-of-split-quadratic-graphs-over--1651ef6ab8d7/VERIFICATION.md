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
# Verification and reproducibility

Run `python3 checks/verify_graph.py` with Python 3 and NumPy. The script constructs the graph points, their overlap after each translation, the field characters for each modulation, and the resulting complete ambiguity-magnitude histogram. It checks the histograms against the closed multiplicity formulas using numerical tolerance \(10^{-8}\), not as an exact-integer certificate for character cancellations. It covers \((q,r)=(2,1),(3,1),(4,1),(5,1),(2,2),(3,2)\); the \(r=1\) cases additionally exercise the formulas outside their stated main range and reveal occasional coincident eigenvalue levels. Every evaluated case passed. The \(\mathbb F_4\) field operations and trace-character computation are explicit.

Direct projector-matrix check: in dimension \(D=8\), forming all \(64\) Weyl-translated vectors and diagonalizing their projector Gram matrix gives eigenvalues \(0,2,8\), with multiplicities \(35,28,1\). This is an independent normalization check of \(D|A|^2\).

The general theorem is proved by finite-field character orthogonality and Gauss-sum identities. Finite checks alone cannot certify all finite fields or all ranks \(r\).
