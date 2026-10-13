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

`verify.py` reconstructs the \(q=10\), \(a=6/5\) fixed-point cubic from the published equation using exact rational arithmetic. It checks the exact discriminant factorization, uses Sturm root counts to prove that \(D\) has three positive and one negative real root, certifies each positive root in its stated rational interval, and verifies the nonzero resultant that excludes triple roots at the three endpoints. It also checks the exact \(b=1\) factorization.

The global root-count proof additionally uses these analytic sign facts: \(P_b(0)=1\); the cubic leading coefficient is negative; on every multiple-root region the coefficient of \(u\) is negative while that of \(u^2\) is positive, so \(P_b(-u)>0\) for every \(u>0\). Thus finite numerical sampling is not used to infer the infinite parameter classification.

The verified scope is only the positive-solution count for the scalar translation-invariant equation (3.10). No claim is made about non-translation-invariant Gibbs measures, extremality, or stability.
