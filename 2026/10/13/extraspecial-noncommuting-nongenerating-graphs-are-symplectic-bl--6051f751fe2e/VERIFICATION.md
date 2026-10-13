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
The infinite-family proof is symbolic.

The packaged checker `artifacts/verify.py` constructs the standard extraspecial group
\[
H_n(p)=\mathbf F_p^n\times\mathbf F_p^n\times\mathbf F_p
\]
with multiplication
\[
(x,y,z)(x',y',z')
=
(x+x',y+y',z+z'+x\cdot y').
\]

For
\[
(p,n)=(2,1)
\quad\text{and}\quad
(3,1),
\]
it enumerates every noncentral pair and verifies directly that every noncommuting pair generates the whole group. Hence the rank-one \(\Xi\)-graph is edgeless.

For
\[
(p,n)=(2,2),
\]
it constructs the full \(\Xi\)-graph directly from group commutators, verifies that no pair generates, and checks the predicted projective blow-up. The graph has \(30\) vertices and degree \(16\).

For
\[
(p,n)=(2,2)
\quad\text{and}\quad
(3,2),
\]
it independently constructs the projective symplectic base graph and verifies
\[
k=p^{2n-1},
\qquad
\lambda=\mu=p^{2n-2}(p-1),
\]
together with the adjacency-matrix identity
\[
A^2=(k-\mu)I+\mu J.
\]
This identity forces the nonprincipal base eigenvalues
\[
\pm p^{n-1}.
\]

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the general theorem.
