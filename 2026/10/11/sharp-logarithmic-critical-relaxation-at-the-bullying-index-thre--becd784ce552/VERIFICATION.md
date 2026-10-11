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

The proof uses exact symbolic identities plus an analytic variation-of-constants argument.

The packaged `verify.py` checks, with symbolic parameters, that at the critical relation \(\alpha A=c\beta\):

1. the stated Lyapunov function has derivative \(-\beta(x-c/\alpha)^2/x\);
2. the first defect \(r=q+(b/\beta)y\) obeys its exact stable linear equation;
3. the second defect \(s=q+(b/\beta)y-b^2(\beta-c)y^2/\beta^3\) obeys the displayed stable equation with cubic and quartic forcing;
4. the reciprocal logarithmic coefficient simplifies exactly to \(b(c-\beta)/\beta^2\).

The analytic proof then uses the Lyapunov identity to obtain \(q,y\to0\), and variation of constants to show \(r/y\to0\) and \(s/y^2\to0\). These are infinite-time analytic deductions, not conclusions from finite computation.

A numerical trajectory at one parameter set was used only as a stress test of signs and constants; it is not an exhaustive computation and is not used to certify the asymptotic theorem.
