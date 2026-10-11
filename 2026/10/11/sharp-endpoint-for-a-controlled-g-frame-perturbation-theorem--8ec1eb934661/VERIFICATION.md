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

The counterexample was checked from the defining series. For \(f=(f_n)\in\ell^2(\mathbb N)\),
\[
\sum_n|\Lambda_nf|^2=\|f\|^2,
\qquad
\sum_n|\Gamma_nf|^2=\sum_n\frac{|f_n|^2}{n^2}\le\|f\|^2.
\]
For \(f=e_N\), the second quantity is \(N^{-2}\), proving that no positive lower frame bound exists. The mixed operator is
\[
D=\operatorname{diag}(1,1/2,1/3,\ldots),
\]
and
\[
\|D-I\|=\sup_{n\ge1}|1/n-1|=1.
\]
The inverse diagonal \(\operatorname{diag}(1,2,3,\ldots)\) is unbounded, so \(D\) is not invertible as a bounded operator.

For the repaired theorem, when \(\lambda<A\), both the mixed operator and its adjoint have minimum modulus at least \(A-\lambda>0\). The operator therefore has closed range and is injective; the adjoint lower bound makes the range dense. Hence the range is all of \(H\), and bounded invertibility follows. Substitution into the source's Cauchy--Schwarz estimate gives the controlled lower bound \((A-\lambda)^2/B\).

The verification does not claim that all controlled-g-frame perturbations are classified, and it does not treat an inaccessible source as evidence of absence.
