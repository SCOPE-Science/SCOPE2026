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

# Reproducibility and scope of verification

Run `python3 verification.py` using Python 3 and its standard library. The deterministic program, seed 20261024, completed successfully with the line `PASS: 5742 independent finite checks; seed=20261024.` The checks cover (i) the exact decomposition of the quartic functional into a maximized one-variable polynomial plus three nonnegative deficits; (ii) global energy lower bounds on randomly sampled complex normalized states; (iii) the exact minimizing families across parameter regimes including the \(U=2g\) boundary; (iv) the quadratic energy onset; and (v) the co-rotating-frame Bogoliubov matrix derived by differentiating the original nonlinear ODE to first order.

The actual proof for all normalized complex amplitudes is algebraic, uses positive deficits and strict convexity, and is reproduced in `RESULT.md`. The linear instability follows from the closed characteristic polynomial. Finite tests check calculations but do not establish universal quantifiers by exhaustion. No independent external verification or auditing has been performed. The specialization does not resolve the full infinite-site ground-state problem, thermodynamic scaling, or nonlinear stability.
