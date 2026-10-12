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

The exact checker `verification/verify.py` uses symbolic polynomial arithmetic modulo \(2\). It verifies:

1. the normalization map lands on \(C\);
2. the displayed dense-chart rational inverse recovers the normalization parameter;
3. the characteristic-two partial derivative formulas;
4. for a general normalization matrix, the \(u^{2}v^{2}\) coefficient is \((ad+bc)(ab+cd)\);
5. after fixing \([1:1]\), the remaining equality of the \(u^{3}v\) and \(uv^{3}\) coefficients is automatic;
6. invertibility eliminates one factor of \((a+c)(b+c)=0\), leaving exactly \(b=c\) and \(d=a\);
7. the normalized one-parameter matrices induce the stated \(T_{\lambda}\);
8. \(T_{\lambda}\) preserves \(y^{4}+xz^{3}+x^{3}z\) identically;
9. \(T_{\lambda}T_{\mu}=T_{\lambda+\mu}\);
10. on the normalization complement of the singular preimage, \(r=v/(u+v)\) transforms as \(r\mapsto r+\lambda\).

The checker is an algebraic identity verification. It does not infer an infinite-field theorem from a finite sample. The geometric steps that a projective curve automorphism lifts to the normalization and preserves the pulled-back hyperplane linear series are standard normalization/linear-series facts and are stated explicitly in the proof.

The verification does not test, and the claim does not address, infinitesimal nonreduced structure of the stabilizer group scheme.
