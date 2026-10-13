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
The checker verifies the two finite combinatorial ingredients used by the proof.

For every
\[
1\le n\le16,
\]
it assigns powers-of-two weights to the first basis vector in each \(\mathbb C^2\)-factor and checks that all subset sums are pairwise distinct. Hence the tested one-parameter subgroups have exactly the tensor-coordinate lines as projective fixed points.

For every
\[
1\le n\le10
\]
and every subset \(I_0\subseteq[n]\), it evaluates the diagonal specialization
\[
\phi(A,B)_I
=
\prod_{i\in I}a_i\prod_{i\notin I}b_i
\]
with
\[
(a_i,b_i)=(1,0)\quad(i\in I_0),
\qquad
(a_i,b_i)=(0,1)\quad(i\notin I_0),
\]
and confirms that exactly coordinate \(I_0\) is nonzero.

Finite checks are regression evidence only. Distinctness for every \(n\) follows from uniqueness of binary expansion, and coordinate containment follows from the displayed exact diagonal formula. The all-parameter Euler statement then follows from the archival group invariance and algebraic \(\mathbb C^*\)-localization.
