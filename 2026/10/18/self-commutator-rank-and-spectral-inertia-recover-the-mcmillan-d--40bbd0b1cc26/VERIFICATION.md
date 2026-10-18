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

# Verification record

The exact Lyapunov identity, the finite-rank integral-kernel decomposition, Kalman controllability/observability tests, and the coprime annihilating-polynomial argument are proved in `RESULT.md`. The checker `check.py` executes four separately parameterized stable minimal examples. It computes direct scalar-integral quadratures for points on and off the diagonal, compares finite-section self-commutator eigenvalues with those predicted by the reduced parity Gram matrix, tests the trace and determinant identities, and checks a repeated-pole and oscillatory-pole instance. The checks passed when run with NumPy and SciPy. Rerun: `python check.py`.

Limitations: no finite grid verifies a statement over all stable dimensions or all kernels. Analytic proof rather than computation supports generality. Historical priority remains subject to further external review, particularly the complete 2015 Andersson--Carlsson source, which was not accessible. Independent audit not performed.
