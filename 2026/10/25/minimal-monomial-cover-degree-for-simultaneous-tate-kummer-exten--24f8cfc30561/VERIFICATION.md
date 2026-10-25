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

## Checks and limits

- Premises: \(p\) is an odd prime; the coordinate Kummer classes are independent; the exponent matrix is integral; and a monomial cover has a nonsingular integer exponent matrix.
- Pullback check: the class vector transforms by right multiplication, \(\bar A\mapsto\bar A\bar M\).
- Lower-bound check: \(\bar A\bar M=0\) forces \(\operatorname{rank}(\bar M)\le r-\rho\), so at least \(\rho\) Smith invariant factors are divisible by \(p\).
- Attainment check: an adapted unimodular basis followed by multiplication by \(p\) on the \(\rho\) independent directions gives determinant magnitude \(p^\rho\) and zero pulled-back classes.
- Boundary cases: \(\rho=0\) gives degree one; \(\rho=r\) gives degree \(p^r\); the one-dimensional case follows directly.
- Source evidence: Pentland's Example 5.35 explicitly identifies \([p^pT]=[T]\) in \(H^1_{\mathrm{\acute et}}(U_\eta,\mu_p)\) and the associated nonsplit extension.
- Limits: the conclusion is only about monomial covers and the stated independent Kummer classes. Independent audit and external validation have not been performed.
