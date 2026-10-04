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

The proof was checked symbolically from the defining identities.

For a rank-one operator \(T=f\otimes x\), direct composition gives \(T^2=f(x)T\). If \(f(x)\ne0\), then \(P=T/f(x)\) satisfies \(P^2=P\) and \(T^2=f(x)^2P\). Since the scalar field is real, \(f(x)^2>0\).

The scale-propagation lemma was checked in both regimes. For \(0<t\le1\),
\[
I+\sigma P=(I+\sigma tP)+\sigma(1-t)P.
\]
For \(t\ge1\),
\[
I+\sigma P=t^{-1}(I+\sigma tP)+(1-t^{-1})I.
\]
In each case, the assumed equality at \(t=1\) plus the triangle inequality gives the sharp lower bound \(1+t\|P\|\), while the ordinary triangle inequality gives the same upper bound.

The only non-elementary input is Langemets's theorem that, for a real Banach space of dimension greater than one, either signed square Daugavet identity for all rank-one operators is equivalent to the Daugavet property. The inspected arXiv record states this theorem and lists Primary MSC 46B20.

No numerical experiment, finite enumeration, or computer algebra certificate is used. No complex-scalar analogue is claimed from the same fixed-sign hypothesis.
