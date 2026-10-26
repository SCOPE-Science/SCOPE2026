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

# Reproducibility

Run `python verify.py` from this package with Python 3, NumPy and SymPy. The checker reconstructs the two-particle full-state exclusion generator independently, solves the reset-resolvent linear system, compares exact \(K_{2,m}\) covariance for positive integer \(m\le7\) across eight rates, solves the lumped three-state probabilities symbolically for \(1\le m\le9\), and verifies the six-state four-cycle closed formula. It passed 251 symbolic and numerical checks.

The general finite-graph high-rate coefficient rests on the analytical two-jump enumeration in RESULT.md, not on exhaustive graph enumeration. The all-\(m\) threshold is a symbolic rational identity and sign check; enumerated sizes corroborate but do not establish it. The full-state computations use column generator convention and rate-one exchanges on undirected occupied-vacant edges. The no-reset stationary covariance and \(r\to\infty\) limits use fixed finite graph size. All scholarly-priority comparisons are provisional, not independent audits.
