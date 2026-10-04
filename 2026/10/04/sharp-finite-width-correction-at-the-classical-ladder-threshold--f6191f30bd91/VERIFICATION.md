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

`verify.py` uses symbolic differentiation to reconstruct the zero-width critical orientation after the substitutions \(A=a^{1/3}\), \(B=b^{1/3}\), and \(S=A^2+B^2\). It checks exactly that
\[
G(t_0)=S^{3/2},\qquad H(t_0)=\frac{S}{AB},\qquad G'(t_0)=0,
\]
then computes
\[
G''(t_0)=3S^{3/2},\qquad
H'(t_0)=-\frac{(A^2-B^2)S}{A^2B^2},
\]
and simplifies \(-H'(t_0)^2/G''(t_0)\) to the claimed second derivative. A successful replay prints `VERIFY_OK`.

The checker is algebraic support only. Concavity is proved for the full interval by the infimum-of-affine-functions argument, strictness of the tangent inequality follows from the nonstationarity of the zero-width orientation when \(a\ne b\), and the exact corridor interpretation follows analytically from the equivalence between the source functions \(m\) and \(n\). No finite experiment is used to infer an infinite statement.
