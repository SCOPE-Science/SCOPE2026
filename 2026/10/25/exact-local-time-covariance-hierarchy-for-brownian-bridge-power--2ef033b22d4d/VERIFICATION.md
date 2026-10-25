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

Analytical checks performed:

- Reconstructed the conditional bridge variance for both orders \(t\le s\) and \(s\le t\).
- Evaluated the time integral as \(\operatorname{B}(q+1,q+1)(s^{q+1}+(1-s)^{q+1})\).
- Evaluated \(\mathbb E[L]\), \(\mathbb E[I_q]\), and \(\mathbb E[LI_q]\) under the stated occupation-density normalization.
- Reduced the beta-function expression using the gamma duplication identities and checked the cases \(q=0,1,2\) algebraically.
- Established the strict sign for all integer \(q\ge1\) by a central-binomial inequality, not by finite enumeration or simulation.

Limits: no independent audit or external certification was performed. The related Knight (2000) full text was not available in the inspected sources, so indirect prior coverage remains a stated risk.
