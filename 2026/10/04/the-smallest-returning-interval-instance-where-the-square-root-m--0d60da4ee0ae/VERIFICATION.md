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

The proof uses only finite-dimensional linear algebra. For \(0<r<1\), set \(s=\sqrt{1-r^2}\) and \(D=\sqrt{2+r^2+2s}\). Reflection decomposition of the Gram matrix gives the exact symmetric-block square root \((A+sI)/D\) and antisymmetric square root \(s\). From these expressions one obtains
\[
S_{12}=\frac rD>0,
\qquad
S_{11}-S_{22}=\frac s2\left(1-\frac{1+s}{D}\right)>0,
\]
because \(D^2-(1+s)^2=2r^2\).

The rotated orthonormal measurement in `RESULT.md` has exact derivative
\[
P'(0)=\frac{rs}{3D}\left(1-\frac{1+s}{D}\right)>0.
\]
Thus strict suboptimality is proved for the entire open interval, not inferred from finite sampling.

`artifacts/verify.py` independently evaluates the closed-form matrix entries at representative values of \(r\), squares the resulting matrix, and verifies a small-angle success increase. Its finite checks test implementation and algebra transcription only. They are not an exhaustive proof over \(0<r<1\).
