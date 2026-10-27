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

The proof computes finite symplectic-group orbit sizes and classifies both possible homogeneous degrees of the central line. The finite checker does not assume this classification: it exhaustively generates subspaces and tests all Lie-bracket grading inclusions on all pairs of their vectors. Command: `python check.py`; expected final marker: `ALL_HEISENBERG_PARITY_GRADING_CHECKS_PASSED`. Exhaustive cases are dimension three over fields of orders two and three, and dimension five over field order two. General field orders and arbitrary dimensions follow from the written algebraic proof. The asymptotic uses dominated convergence with summable discrete-Gaussian weights; the checker does not certify infinite limits. Independent audit has not been performed.
