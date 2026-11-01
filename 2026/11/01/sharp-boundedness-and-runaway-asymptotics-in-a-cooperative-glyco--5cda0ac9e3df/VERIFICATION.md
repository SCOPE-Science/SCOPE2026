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

# Reproducibility and limits

The theoretical proof is contained in `RESULT.md` and depends only on positivity and elementary scalar ODE comparison, an exact flux-cancellation identity, uniform saturation estimates, and dominated convergence. Reproduce symbolic and illustrative numerical checks with `python verify.py` (requires Python, SymPy, and SciPy).

The standalone script checks four exact identities symbolically and evaluates sample trajectories for zero, negative, and positive net removal. For the critical sample it also checks the exact weighted-mass linear law at finite times. Those finite trajectories do not establish the universal or infinite-time claims, which follow from the written proof. The strictly positive limit \(C>0\) is proved using an eventual comparison lower bound, not numerical fitting.

The theorem is restricted to positive initial data, Hill exponent \(n\ge1\), and conversion capacity \(\sigma>\nu+\sigma_i\). Independent audit: not performed.
