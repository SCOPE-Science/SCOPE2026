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

The defining identities were checked algebraically:
- \(g(x)-g(y)=(x-y)(x+y)(x^2+y^2-2\lambda)\).
- \(f(\beta+u)-\alpha=u(2\beta+u)\).
- \(g(\beta+u)-\beta=u[4\alpha\beta+(6\beta^2-2\lambda)u+4\beta u^2+u^3]\).

For \(v_2(u)=k\ge3\), the leading coefficient \(4\alpha\beta\) has valuation \(3\), and the remaining terms in the bracket have valuation strictly greater than \(3\). This verifies the exact \(k+3\) increment without cancellation. The one-step increment is exactly \(k+2\). The tail-time expression follows by taking the first even or odd iterate whose error valuation is at least \(N\). The global formula then checks the possible time-zero and time-one hits before using the basin-entry tail formula.

No computational enumeration or finite experiment is used to infer the infinite statement. The result does not provide a histogram of preperiod counts over all residues, and no independent audit has been performed.
