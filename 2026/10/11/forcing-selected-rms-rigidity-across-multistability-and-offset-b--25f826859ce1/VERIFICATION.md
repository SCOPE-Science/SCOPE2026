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

The bundled `verify.py` uses dependency-free exact polynomial arithmetic over rational coefficients.

It checks the core cancellation
\[
xy-b-x(y-x)=x^2-b,
\]
which is equivalent to differentiating
\[
Q=z-\frac{x^2}{2a}
\]
along the printed equations. Because the offset parameter enters only the \(\dot y\) equation, the checked identity also applies to the offset-boosted family.

It also checks the algebra behind the activity defect,
\[
(y-x)^2=y^2-2xy+x^2,
\]
and the published specialization
\[
a=31,\qquad b=25,\qquad a^2=961,\qquad \sqrt b=5.
\]

Run `python verify.py`; successful replay prints `VERIFY_OK`.

The script verifies the exact algebra and numerical specialization only. The infinite-time conclusions are analytic: boundedness makes \((Q(T)-Q(0))/T\to0\), and invariant-measure identities follow from integrating Lie derivatives against a compactly supported invariant measure. Strictness of the \(y\)-moment bound uses invariance and compactness of the support. No finite simulation is used to certify asymptotic dynamics.
