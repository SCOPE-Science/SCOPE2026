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

For an adapted orthonormal basis
\[
A=X+Z,\qquad B=Y+W,
\]
put
\[
p=|X|^2,\qquad q=|Y|^2.
\]
The H-type relations and orthogonality give
\[
|j(W)X|^2=p(1-q),
\]
\[
|j(Z)Y|^2=q(1-p),
\]
\[
|[X,Y]|^2=pq.
\]
The two mixed terms are bounded by the common product
\[
\sqrt{pq(1-p)(1-q)}.
\]
Hence
\[
K\le
\frac14(p+q)-\frac54pq
+\frac32\sqrt{pq(1-p)(1-q)}.
\]

Set
\[
u=\sqrt{pq},
\qquad
v=\sqrt{(1-p)(1-q)}.
\]
Then
\[
u+v\le1
\]
and
\[
4F=1-4u^2-v^2+6uv.
\]
For \(u\le1/4\), the right-hand side is at most \(21/16<16/11\). For \(u\ge1/4\), it is at most
\[
8u-11u^2\le\frac{16}{11},
\]
with equality only at
\[
u=\frac4{11},
\qquad
v=\frac7{11}.
\]
Equality in \(u+v\le1\) then forces
\[
p=q=\frac4{11}.
\]

The packaged checker verifies these identities symbolically and reconstructs the \(j\)-maps from the six Lie brackets. It verifies that the plane displayed in the source satisfies
\[
j(Z_2)X_4=j(Z_1)X_3,
\qquad
j(Z_2)X_3=-j(Z_1)X_4,
\]
which are precisely the normalized mixed-term equality conditions.

No numerical experiment is used as proof.
