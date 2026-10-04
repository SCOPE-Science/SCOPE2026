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

The final claim was replayed from its definitions rather than from numerical logs.

For unit vectors, set \(a=\|x+y\|_p\) and \(b=\|x-y\|_p\). The P-angle expression is exactly \((a^2+b^2-4)/(2ab)\). Clarkson yields the correct power-sum constraint with exponent \(m=p\) for \(p\ge2\) and \(m=p'\) for \(1<p\le2\). At a fixed ratio \(a/b\), the expression is strictly increasing in common scale, so only the boundary \(a^m+b^m=2^m\) matters.

The remaining scalar bound was checked algebraically. With \(\alpha=2/m\), \(u=t^m\), and \(v=(u-1)/(u+1)\), the sign condition for monotonicity becomes
\[
(1+v)^\alpha-(1-v)^\alpha\le2^\alpha v.
\]
The left side is a convex function of \(v\in[0,1]\) joining \(0\) to \(2^\alpha\), so it lies below that endpoint chord. This proves the global upper bound, not merely a sampled bound.

Attainment was checked directly using disjoint coordinate vectors for \(1\le p\le2\), the two-coordinate Hanner pair for \(2\le p<\infty\), and its unscaled endpoint version for \(p=\infty\). The formulas agree at \(p=2\) and give \(1/2\) at \(p=1,\infty\).

No numerical experiment, finite search, external proof assistant, or unpublished certificate is required. The unproved limits are only bibliographic: the search cannot rule out an obscure independent prior derivation, and the theorem does not classify all extremizers.
