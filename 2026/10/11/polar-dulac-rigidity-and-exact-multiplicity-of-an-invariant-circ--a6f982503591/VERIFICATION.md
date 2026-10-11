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
The algebraic proof starts from the exact radial reduction. Differentiating \(2U/(sU-V)\) with respect to \(s\) gives \(-2U^2/(sU-V)^2\); converting to \(z=\log|s/(1-s)|\) multiplies by \(s(1-s)\). On a full oriented turn this gives strict multiplier signs whenever \(U\not\equiv0\). A neutral multiplier leads to \(K=\frac12\int A^2h\ne0\), because \(h>0\) and the orientation has a fixed sign. The resulting fixed-point and asymptotic statements are analytic, not numerical extrapolations.

Run \(\texttt{python verify.py}\) with SymPy installed to check the expansion \(dq/d\theta=Aq+(A+A^2/2)q^2+O(q^3)\), the weighted-divergence formula, and exact inequalities for the examples. Successful output is \(\texttt{CHECK_OK}\). The checker is an algebraic sanity check; it does not certify global originality or replace the argument proving return-map uniqueness.

No claim is made about regions with zero or reversing angular velocity. The 1987 earlier paper was not fully available and residual comparison risk is disclosed. Independent audit has not been conducted.
