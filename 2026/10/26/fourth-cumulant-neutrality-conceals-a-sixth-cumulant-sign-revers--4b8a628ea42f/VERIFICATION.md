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

# Reproduction and scope

Run `python checker.py` with Python 3, NumPy, SciPy and SymPy installed. The checker printed `PASS: 33 symbolic/numerical checks; sample sixth-cumulant zero at t=0.898364443` on the inspected copy. It builds the symbolic tilted matrix and, separately, an eight-order differential system for finite-time moments; the latter is not based on differentiating the leading eigenvalue. It checks the analytic growth formulas against independent finite-time evaluations.

The universal sign statements and the existence of a sixth-cumulant crossing are proved analytically in `RESULT.md`; tests at finitely many parameters and observation times cannot establish them alone. The threshold does not imply that there are no crossings below it or exactly one crossing above it. For each fixed parameter vector satisfying the assumptions, the stationary Markov spectral gap gives existence of all fixed-order growth limits. The independent audit channel has not been performed.
