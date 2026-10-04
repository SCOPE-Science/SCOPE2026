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

The mathematical claim was replayed symbolically from the defining maximum norm.

1. Each of the three defining branches is bounded above by the Euclidean norm, so \(N\le E\).
2. After reducing to \(a\ge b\ge0\) and \(t=b/a\), the ratio \(N/E\) is decreasing until \(t=\sqrt2-1\) and increasing afterwards. Hence its exact minimum is \(\cos(\pi/8)\).
3. Euclidean Ptolemy and the two-sided norm comparison imply \(C_{\mathrm{Pt}}\le\sec^2(\pi/8)=4-2\sqrt2\).
4. For \(s=\sqrt2-1\), the triple \(x=(-1,s)\), \(y=(s,-1)\), \(z=(-2,-2)\) satisfies
\[
N(x)=N(y)=1,\quad N(x-y)=2,\quad N(z)=2\sqrt2,\quad N(x-z)=N(z-y)=1+\sqrt2.
\]
Its ratio is exactly \(4-2\sqrt2\).
5. The symbolic identities \((1+(\sqrt2-1)^2)^{-1}=(2+\sqrt2)/4\) and \(((2+\sqrt2)/4)^{-1}=4-2\sqrt2\) were independently recomputed.

No numerical optimization, finite enumeration, or inaccessible lemma is used in the proof. The only unresolved item concerns literature coverage, not correctness.
