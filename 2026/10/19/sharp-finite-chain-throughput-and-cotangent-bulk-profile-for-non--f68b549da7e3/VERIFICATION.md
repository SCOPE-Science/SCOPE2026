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

The exact edge equilibrium equations are reduced to the scalar shooting map \(F_J(x)=J/(1-x^r)\), checked against the cited stationary balance equation (2.6). The singular passage-time coefficient uses \(h''(s_r)=-r/s_r\), \(a=(r+1)/r\), and \(b=(r+1)/(2s_r)\). Passage-time integral comparisons prove the infinite-length limits. Run `python3 check.py` for finite-chain diagnostics; these are not certificates of the asymptotic theorem. The current theorem excludes endpoints of the bulk profile and unbounded power parameter. External independent validation has not been performed.
