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

Let
\[
Y_{a,p}=\operatorname{Bl}_pX_a
\]
and let \(E\) denote its exceptional divisor.

The inspected source gives
\[
H^2(Y_{a,p},\mathbb Z)=\mathbb Z[E]
\]
and
\[
c_1(TY_{a,p})=-2[E].
\]
Thus a biholomorphism of two such blow-ups carries the target exceptional cohomology class to the source class.

If \(D\) is the inverse image of the target exceptional divisor and \(D\ne E\), the defining section of \(D\) restricts nontrivially to \(E\). Since
\[
[D]=[E],
\]
its restriction has the same first Chern class as the normal bundle of \(E\). On
\[
E\simeq\mathbb P^2
\]
this forces
\[
\mathcal O(D)|_E
\simeq
\mathcal O_{\mathbb P^2}(-1),
\]
which has no nonzero holomorphic section. Hence \(D=E\).

The biholomorphism therefore maps exceptional divisor to exceptional divisor and descends through the point blow-downs to a biholomorphism of the bases carrying the centre to the centre. The reverse implication follows by lifting a pointed base biholomorphism.

For fixed \(a\), the source gives
\[
\dim_{\mathbb C}\operatorname{Aut}^0(X_a)=1.
\]
Every full orbit is a countable union of real at-most-two-dimensional immersed submanifolds, hence has zero measure in the real six-manifold \(X_a\). Therefore the point-orbit quotient is uncountable.

No numerical computation or finite enumeration is used.
