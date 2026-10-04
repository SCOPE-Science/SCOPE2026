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

The source theorem supplies an integer \(q\ge1\) satisfying
\[
2q+1<\frac m2
\]
and identifies the endpoint
\[
p_{i-q-1,i+q}
\]
of the homothetic image of side \(i\).

For equally spaced side normals with angular step \(\phi=2\pi/m\), a direct two-line intersection gives
\[
A h_{i-q-1}+B h_{i+q}=\mu D h_i,
\]
where
\[
A=\sin(q\phi),\qquad
B=\sin((q+1)\phi),\qquad
D=\sin((2q+1)\phi).
\]
The source inequality implies \(A,B,D>0\). Summation over \(i\) gives
\[
\mu D=A+B.
\]

For a Fourier root \(z\), a nonzero coefficient would require
\[
A z^{-(q+1)}+Bz^q=A+B.
\]
The triangle inequality is sharp only when both unit complex numbers equal \(1\). Thus \(z^q=z^{q+1}=1\), hence \(z=1\). Only the constant support mode remains.

The embedded `verify.py` was replayed from its packaged path. It checks the nonconstant Fourier-mode obstruction for all admissible \((m,q)\) in a broad finite range and independently reconstructs the sideline intersections for regular support data. It returned:

`VERIFY_OK equiangular illumination-homothety rigidity`

The finite replay is not an infinite proof. The all-parameter conclusion is established by the exact triangle-equality argument above.
