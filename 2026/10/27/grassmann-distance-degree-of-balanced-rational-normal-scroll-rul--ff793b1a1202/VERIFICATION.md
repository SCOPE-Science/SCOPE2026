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

The symbolic checker is self-contained apart from Python 3 and SymPy and can be executed as `python checker.py`. For each \(m\in\{2,3,4,5\}\), it selects two real coefficient vectors, embeds one in each orthogonal block, normalizes them, and therefore constructs a genuine rank-two orthogonal projector. It verifies that the exact derivative numerator has degree \(4m-2\), no repeated roots, no pole roots, and no roots at the explicit cut determinant. These tests are illustrative, not exhaustive over rank-two data or over integers \(m\).

The infinite statement uses the proof in `RESULT.md`: explicit surjectivity of the numerator-map differential, generic squarefreeness by two independent jet constraints, and a Schubert-incidence argument excluding cut-locus critical points. The ED comparison is Theorem 2.2 of arXiv:2610.02018, not a newly claimed ED calculation. No independent audit or third-party certification has been performed.
