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
H=\ell^2(\mathbb N),\qquad
Ke_n=\frac1n e_n,\qquad
f_n=g_n=n e_n.
\]
Then
\[
Kf_n=Kg_n=e_n.
\]
For every \(h=(h_n)\in H\),
\[
\sum_n|\langle h,Kf_n\rangle|^2
=
\|h\|^2
\]
and
\[
\|K^*h\|^2
=
\sum_n\frac{|h_n|^2}{n^2}
\le\|h\|^2.
\]
Thus every transformed weave is a \(K\)-frame with bounds \(1,1\).

For
\[
x_N=Ke_N=\frac1N e_N,
\]
the original weaving energy is
\[
\sum_n|\langle x_N,n e_n\rangle|^2=1,
\]
while
\[
\|x_N\|^2=\frac1{N^2}.
\]
Hence no finite upper frame bound exists on \(R(K^*)\).

Nonclosed range can be checked directly. The vector
\[
y=\left(1,\frac12,\frac13,\ldots\right)
\]
belongs to \(\ell^2\) but not to \(R(K)\), since its only coordinatewise preimage is \((1,1,1,\ldots)\notin\ell^2\). Finite truncations of \(y\) lie in \(R(K)\) and converge to \(y\).

For the repair, if \(K\) has closed range and \(x\in R(K^*)\), take
\[
h=(K^*)^\dagger x.
\]
Then
\[
K^*h=x,\qquad
\|h\|\le\|K^\dagger\|\|x\|.
\]
Substitution into the \(K\)-woven inequalities gives the lower bound \(C\) and upper bound \(D\|K^\dagger\|^2\) for the original weave. Substituting \(x=K^*h\) in the opposite direction gives bounds \(A\) and \(B\|K\|^2\) for the image weave.

The primary open PDF was inspected at the full proposition and proof. No numerical approximation or finite truncation is used to establish the infinite statement.
