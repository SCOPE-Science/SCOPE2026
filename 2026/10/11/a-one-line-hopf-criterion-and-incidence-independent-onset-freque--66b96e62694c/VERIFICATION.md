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

The claim was checked directly against the normalized equilibrium relation, Jacobian trace and determinant, and generalized-Hopf reparametrization in arXiv:2609.38874v1.

The critical algebra is:
\[
1+B_H=rac q{q-q_c},\qquad
\det_H=rac r{X_1}(1-p_cX_1)
=rac{rs\widetilde X}{X_1}-1.
\]
Thus \(\det_H>0\) is equivalent to \(\widetilde X>1/(s+1+sr)\). At \(B=B_H\), the source's auxiliary inequality \(q>q_1\) is equivalent to the same condition, so no extra high-\(p\) branch restriction survives.

Differentiating the published trace gives
\[
\left.\partial_B\operatorname{Re}\lambdaight|_{B_H}
=-rac{r(q-q_c)^2}{2q},
\]
which is strictly negative in the stated domain. Substitution of the paper's \((a,m,n,g,D)\) parametrization yields \(X_1=(g+1)/((a+1)(g+1)+aD)\) and \(rs\widetilde X/X_1-1=D\).

An exact rational stress check with \((s,r,\widetilde X,p,q)=(1,3/2,1/3,3,2)\) gives \(B_H=1/5\), \(\omega_H^2=1/2\), and crossing speed \(-25/24\). This check is illustrative only; the proof is symbolic and covers all parameters satisfying the stated strict inequalities.

Limits: no statement is made about Lyapunov coefficients, Hopf criticality, number of cycles, global epidemic dynamics, or codimension-six nonexistence. The originality search cannot rule out inaccessible or differently normalized older derivations.
