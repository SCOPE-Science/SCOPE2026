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

The exact verifier constructs
\[
Q=A^{\mathsf T}(AA^{\mathsf T})^{-1}A
\]
from
\[
A=
\begin{pmatrix}
0&-1&-2&0&-2&3\\
0&-3&-1&-1&-2&-1
\end{pmatrix}
\]
and checks
\[
Q^2=Q,\qquad Q^{\mathsf T}=Q,\qquad
\operatorname{rank}(Q)=2,\qquad
\operatorname{trace}(Q)=2.
\]

It derives the ruling-curve objective and verifies that its critical numerator is a nonzero scalar multiple of
\[
4t^6+23t^5+32t^4-238t^3-142t-12.
\]
The discriminant is checked exactly and is nonzero.

The verifier also computes
\[
\det(B(t)QB(t)^{\mathsf T})
=
\frac{t^2(5t^3+12t^2-2t+1)^2}{252}
\]
and verifies a nonzero resultant between the critical polynomial and the cut-locus factor. A second nonzero resultant excludes the projection-model poles \(1+t^2+t^4=0\).

After changing coordinate to \(u=1/t\), the derivative at \(u=0\) is checked to equal
\[
\frac{4}{63},
\]
so infinity is not critical.

The replay output ends in `VERIFY_OK`.
