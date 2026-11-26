---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The zero- and one-one images contribute two types. For a window with at least three ones, the distance between the first two retained ones uniquely identifies the original first-one index, and their offset recovers the window start. Thus counting triple-window starts is valid. For exactly two ones at a_j,a_{j+1}, intersect the start conditions t>=0, t>a_{j-1} when present, t>=a_{j+1}-n+1, t<=a_j, and t<=a_{j+2}-n. The retained position a_{j+1}-t-1 is the sole image parameter. On scales C=d_k to D=d_{k+1}, k>=2, the initial triple windows cover 0 through a_{k-2} because a_{j+2}-a_{j-1}<=C for 1<=j<=k-2 and a_2<C. Put A=d_{k-2}, B=d_{k-1}. The new triple windows contribute the truncation of n-B-C to [0,A]; the earlier active two-one interval contributes its complement in A. The other active two-one interval contributes min(B,n-C) and is disjoint since A+B<=C. This gives 2+b^{k-2}+A+min(B,n-C), and b^{k-2}+A=b^{k-1}. At k=1 the single start t=0 switches from a two-one to a triple window just after d_0+d_1; the other interval contributes min(d_0,n-d_1). For n<b there is no pair; for b<=n<=d_1 only the initial pair fits. This includes b=2 and all shared endpoints. The rising and constant segments have diverging lengths, and evaluating P_b(n)/n at the eventual local minima d_k and maxima d_k+d_{k-1} gives the claimed liminf and limsup.

## originality

PASS

The inspected earlier work does not give or imply this exact all-radix image complexity. A later indexed record has a genuinely equivalent binary formula but does not cover the all-radix result. This is a bounded literature judgment, not an assertion of priority over unindexed sources.

## value

PASS

Geometric gaps are a canonical sparse, unbounded-gap test case for an established transformed-factor invariant whose bounded-gap theorem does not apply. The exact interval collision count exhibits long rising runs and plateaus and yields two distinct normalized limits, making visible behavior that a linear-growth estimate or ordinary factor count cannot resolve. The all-radix formula and collision method give a meaningful exact benchmark for other unbounded-gap words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
