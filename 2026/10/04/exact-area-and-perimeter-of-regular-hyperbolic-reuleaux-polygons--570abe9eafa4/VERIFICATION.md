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

Let \(t=\pi/n\) and \(u=\sinh^2(d/2)\). The proof first obtains
\[
\sinh^2\rho=\frac{\cosh d-1}{1+\cos t},\qquad
\cosh s=1+\sinh^2\rho(1-\cos2t).
\]
The radius-\(d\) arc triangle then gives
\[
\cosh s=\cosh^2d-\sinh^2d\cos\alpha,
\]
which simplifies to
\[
\cos\alpha=\frac{u+\cos t}{1+u}.
\]
The polar metric gives \(L=n\alpha\sinh d\); Gauss–Bonnet gives \(A=n\alpha(1+\cosh d)-2\pi\).

The embedded `verify.py` was replayed from its actual package path. It reconstructs \(\rho\), \(s\), and \(\alpha\) from the unsimplified cosine laws for many odd \(n\) and positive \(d\), checks the perimeter-area identity, the Euclidean small-width limit, and the fixed-width disk limit. It returned:

`VERIFY_OK regular hyperbolic Reuleaux profile`

The finite replay is only a consistency check; the analytic proof supplies the all-\(n\), all-\(d\) result.
