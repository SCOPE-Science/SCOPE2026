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

The mathematical proof uses exact differential inequalities, an asymptotically stable scalar quotient equation, elementary implicit-function theory and planar dynamics. No infinite-time conclusion is inferred from finite computation.

To reproduce: install `requirements.txt` and run `python verify.py`. The supplied program checks the symbolic formula for \(Z'(0)\), the positivity of \(K\), exact fractions in four response families, and numerical limits along long but finite solutions of the actual two-dimensional ODE. It additionally brackets the unique endemic root for three positive reproduction excesses. Under the documented numerical tolerances all assertions passed on the packaged code at review time. In particular, for \(B(y)=1+y\), \(C(y)=1-y/2\) and equal positive rates, the predicted limits are \(4/7\) and \(-3/14\); the normalized-time \(30{,}000\) calculations gave approximately \(0.571380764\) and \(-0.214270337\). Exact agreement in the limit is proved analytically, not certified by these finite trajectories.

Scientific limits: smooth monotone contact feedback; strictly positive creation; positive initial prevalence; recovery-normalized time; stochastic and multigroup behavior outside scope. Independent audit and independent validation have not been performed.
