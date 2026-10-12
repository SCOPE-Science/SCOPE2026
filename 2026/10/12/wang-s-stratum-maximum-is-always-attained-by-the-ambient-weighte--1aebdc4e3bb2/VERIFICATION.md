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

The initiating arXiv source was inspected in full text.

Its weighted-projective setup assumes a well-formed \(\mathbf P(a_0,\ldots,a_n)\) of dimension \(n\ge3\) with isolated singularities. It records
\[
k=\prod_{i=0}^{n}a_i
\]
and uses
\[
H=f^*\mathcal O_{\mathbf P}(k)
\]
on a toric resolution.

Proposition 3.11 states that
\[
m>n-2+\frac{\sum_i a_i}{\prod_i a_i}
\]
implies algebraic hyperbolicity outside the toric boundary.

Proposition 3.17 defines
\[
\Theta=
\max_{\substack{I\subseteq\{0,\ldots,n\}\\ |I|\ge4}}
\frac{1}{\prod_{i\notin I}a_i}
\left(
\frac{\sum_{i\in I}a_i}{\prod_{i\in I}a_i}+|I|-3
\right)
\]
and states that \(m>\Theta\) implies global algebraic hyperbolicity for a very general hypersurface.

Let
\[
P=\prod_i a_i,\qquad
S=\sum_i a_i.
\]
For each \(I\), with
\[
S_I=\sum_{i\in I}a_i,\qquad
q_I=\prod_{i\notin I}a_i,
\]
the printed term simplifies to
\[
\theta_I=\frac{S_I}{P}+\frac{|I|-3}{q_I}.
\]
For the full set,
\[
\theta_A=\frac{S}{P}+n-2.
\]
For a proper set,
\[
S_I<S,\qquad
\frac{|I|-3}{q_I}\le |I|-3\le n-3,
\]
so
\[
\theta_I<\theta_A.
\]
This proves the unique-maximizer and exact-\(\Theta\) statements with no case split beyond full versus proper subsets.

The convention that the full set is allowed was checked against the source itself: Proposition 3.17 applies in dimension \(3\), where a strict proper subset cannot have four elements, and Corollary 3.18 explicitly computes \(\Theta\) in the family \(\mathbf P(1,\ldots,1,r)\) at the ambient value.

For \(\mathbf P(1,1,2,3,5)\),
\[
n=4,\qquad
S=12,\qquad
P=30,
\]
so
\[
\Theta=2+\frac{12}{30}=\frac{12}{5},
\]
and integer \(m>\Theta\) is equivalent to \(m\ge3\).

No computation beyond exact integer and rational arithmetic is needed. No necessity or optimality statement is claimed.
