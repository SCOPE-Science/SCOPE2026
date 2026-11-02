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

## Exact and finite checks

`python check.py` verified symbolically the average birth and capture rates, their differences, the weighted logarithmic invariant, and the strict Lyapunov derivative. For \(r=2\), \(\delta=1\), \(K=2\), \(\beta=1\), \(g=2/5\), numerical integration at \(e=3/10,3/5,9/10\) checked the time-dependent identity at 35 time points in each regime. The neutral case converged to \(x_\infty\approx0.2880580664\), while the two other cases approached opposite prey-boundary states. The finite integration is corroborative, not a proof of a universal statement. The analytical proof in `RESULT.md` establishes the global theorem with LaSalle and an exact integration.

**Known limits:** This verifies a special balanced-payoff subclass and depends on positive predator persistence. Independent validation of scientific priority and correctness has not been performed.
