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

After width normalization, the proof reaches
\[
P=\operatorname{conv}\{\pm(1,r),\pm(-s,1)\},
\qquad 0\le r,s<1.
\]
Writing
\[
A=\begin{pmatrix}1&-s\\r&1\end{pmatrix}
\]
gives \(P=A B_1^2\), so
\[
\|(p,q)\|_P
=
\frac{|p+sq|+|q-rp|}{1+rs}.
\]
The sign-split inequalities in the proof show analytically that \(r<s\) leaves only \(\pm e_1\) shortest and \(s<r\) leaves only \(\pm e_2\) shortest. Thus completeness forces \(r=s\).

The embedded `verify.py` uses exact `Fraction` arithmetic to replay this normal-form conclusion for a grid of rational parameter pairs and all lattice vectors in a fixed box. It also checks the exact canonical diameter, the polar vertices, the involution
\[
\psi(x)=\frac{1-x}{1+x},
\qquad
\psi(\psi(x))=x,
\]
and invariance of the diameter profile under \(\psi\). A numerical check of the analytic one-variable minimum confirms the fixed-point value \(4(\sqrt2-1)\).

The script was replayed from its actual package path and returned:

`VERIFY_OK symmetric lattice quadrilateral classification profile`

The rational grid is only a consistency test. No finite enumeration is used to infer the classification over real parameters.
