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

The exact source vector field was checked in the lawful open-access full text of the 2018 article. The proof uses only polynomial generator identities for that vector field.

`artifacts/verify_stationary_gap.py` is a standalone Python script using only the standard library. It implements multivariate polynomials over exact rational coefficients and verifies:
\[
L\!\left(\frac{x^2}{2}\right)=xz,
\]
\[
L\!\left(\frac{(x+y)^2}{2}\right)=-x(x+y),
\]
\[
L(xy)=yz-x^2-xz,
\]
and, for
\[
G=z+\frac12(x+y)^2+\frac{11}{10}x+\frac{1}{10}y+\frac{3}{20}x^2,
\]
\[
LG=a+5y-x^2.
\]
The script was executed from the packaged path; its output is embedded as `artifacts/verification_output.txt`.

The equality case in the variance bound is not delegated to computation. If \(\operatorname{Var}(x+y)=0\), invariance of the support and \(d(x+y)/dt=-x\) force \(x=0\), then \(z=0\), then \(y=-a/5\).

A finite-time numerical trajectory may be used only as a sanity check and is not evidence for the exact theorem, compactness of the reported attractor, or originality.
