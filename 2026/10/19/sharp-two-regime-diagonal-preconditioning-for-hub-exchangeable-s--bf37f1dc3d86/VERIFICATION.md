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

# Verification details

The standalone `verify.py` was executed with Python and NumPy. It passed **8,468 checks**. They comprise exact fractional identities for a six-dimensional example and a rational transition boundary, and constructed full-matrix eigenvalue checks for \(m=3,\ldots,11\), seven within-clique couplings and seven hub couplings per size. The script compares every constructed spectrum with the independent direct-sum eigenvalue formula, checks the closed optimum and neighboring symmetric scalings, and tests sampled asymmetric diagonal competitors. It also verifies the homogeneous Jacobi line for \(3\le m\le29\).

The full global proof is the matrix-inequality averaging argument and scalar eigenvalue optimization in `RESULT.md`; the finite tests cannot establish global minimization for a continuum of admissible scalings or infinitely many matrix sizes. No independent audit has been performed.
