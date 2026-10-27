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

# Computational verification

Execute `python verify.py` in the same directory as `requirements.txt` with Python, NumPy and SciPy installed. The checker tests exact rational feasibility and every nontrivial spectral mode at both endpoints and the midpoint of each claimed optimizer interval for \(2\le p\le15\) and \(2\le q\le60\), with more checks at the transition surfaces. A separately formulated SciPy linear program minimizes the maximum absolute nontrivial eigenvalue across edge weights. Fully assembled stochastic transition matrices are also checked for stochasticity, nonnegativity and eigenvalue agreement.

Observed run: `VERIFY_OK exact_endpoint_and_midpoint_cases=2478 independent_lp_instances=257 full_dense_eigensystems=52 phase_boundary_cases=40`.

The source code and output in this package reproduce these finite checks. The general classification uses the analytical inequalities in `RESULT.md`, not extrapolation from experiments. All assertions about mathematical originality are subject to residual literature risk and are not independently audited.
