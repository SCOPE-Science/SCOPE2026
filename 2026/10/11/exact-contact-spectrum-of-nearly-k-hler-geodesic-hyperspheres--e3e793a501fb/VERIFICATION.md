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

Let
\[
k=\cot r.
\]
On the four-dimensional horizontal distribution, choose matrices \(J\) and \(G\) representing \(\phi\) and \(G_N\) with
\[
J^2=G^2=-I,
\qquad
JG+GJ=0.
\]
The horizontal skew operator of \(d\eta\) is
\[
K=2(kJ-G).
\]
Therefore
\[
K^2
=
-4(k^2+1)I.
\]
Since \(K\) is skew-adjoint,
\[
K^\ast K=4(k^2+1)I,
\]
so its two skew singular values are both
\[
2\sqrt{k^2+1}=2\csc r.
\]

In an adapted oriented orthonormal basis the Pfaffian magnitude is
\[
4(k^2+1),
\]
hence
\[
\|(d\eta)^2\|
=
8(k^2+1)
=
8\csc^2r.
\]
Because \(\eta\) has unit norm and the two-form is horizontal,
\[
\|\eta\wedge(d\eta)^2\|
=
8\csc^2r.
\]

The packaged checker verifies these matrix identities exactly. The proof separately verifies
\[
d\eta(\xi,\cdot)=0,
\]
so \(\xi\) is the contact Reeb field.

No finite rank sampling is used to prove the theorem.
