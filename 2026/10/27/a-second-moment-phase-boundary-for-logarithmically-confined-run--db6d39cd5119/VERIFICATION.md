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

The exact two-state generator acting on \(H_2\) and \(H_4\) was independently expanded symbolically. The polynomial drift signs were checked for \(D_{\mathrm{eff}}<1/3\). The supplied `verify.py` constructs finite upper absorbing levels and computes the first two moments through separate sparse linear equations. These finite cutoffs corroborate the critical logarithmic divergence, but cannot establish an infinite-time or infinite-space statement. The critical step in the proof is the sign of the infinite-domain integrating-factor integral, together with a fourth-degree Lyapunov supersolution.

The source's quadratic first-moment asymptotic is an explicit assumption of the derived second-moment analysis and was checked against its first-order backward equation. The strength, velocity, switching-rate, and starting-position restrictions are stated in `RESULT.md`. No independent audit or experimental verification was performed.
