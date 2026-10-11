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
# Verification

The proof is analytic and does not depend on a numerical experiment.

1. Define \(y=\phi_p(u')\). At \(\gamma=0\), direct substitution gives \(y'=-a(t)\).
2. Neumann or periodic derivative data imply \(y(T)=y(0)\), hence \(\int_0^T a=0\). For the two-step weight this is exactly \(a_+\tau=a_-(T-\tau)\).
3. In the Neumann case, \(y(0)=0\), so the derivative profile is uniquely \(u'=\phi_q(-A)\).
4. In the periodic case, \(y=c-A\). Position closure is \(\int_0^T\phi_q(c-A(t))dt=0\). Because the two branches of \(A\) each traverse \([0,M]\), this is equivalent to \(|c|^q=|c-M|^q\), whose unique real solution is \(c=M/2\).
5. The oscillation integrals reduce to \(M^q/q\) and \((M/2)^q/q\), multiplied by \(1/a_++1/a_-=T/M\), giving the stated formulas.
6. Adding a constant preserves the equation and both boundary conditions; sufficiently large translates are positive. Since the derivative profile is unique in each boundary problem, these exhaust all positive solutions.

Limits: no statement is made about \(\gamma=p-1\), non-two-step weights, or independent validation.
