---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Beta integration with the probability weight gives m_n=n!Γ(β)/Γ(n+β). The normalized monomial outputs have distinct angular frequencies n−2; projection subtracts the analytic component only for n≥2, giving λ_n=m_(n+2)/m_n−1_(n≥2)m_n/m_(n−2). In particular λ₁/λ₀=3β/(β+2)>1. For n≥1 the displayed rational channel follows on a common denominator, including n=1. Writing A_n=2βn+β+2n²−2, the difference numerator after removing 2(β−1) is (β+n−2)(A_(n+1)−A_n)−4A_n=2[β²−(n+3)β−2n²−3n+2]. All denominators are positive and the single positive root is B_n. These roots increase without bound, starting at B₁=2+√7; for fixed β the sign of the difference switches at most once. Channel squares tend to zero, so the global maximizers are the claimed single degree or adjacent pair, and orthogonality gives precisely their span as the equality space. B_n=2n+3+O(1/n) puts any winning degree at β/2+O(1), yielding 16/(27β)+O(β^−2). The linear symbol has decreasing squares (β−1)/((n+β)(n+β−1)) from 1/β at n=0. Below β=2 the peak is n=1 and the signed difference is −(β−1)(β−2)/(β(β+1)(β+2)). At β≥2 the n=0 channel is below 1/β. For n≥1, setting u=β−2, x=n−1, w=u+x, clearing denominators in 1/β−λ_n gives (w+1)(w+2)(w+3)(w+4)−2(u+2)(u+1)(2ux+3u+2x²+8x+6). Expansion gives the nonnegative polynomial in the record, zero only at u=x=0. The asymptotic proof's distance-to-real-root observation should be understood for large β (the index range starts at 1); this does not affect the result. Uploaded code was not executed.

## originality

PASS

The supported distinctive claim is the exact all-weight upper envelope of the quadratic-symbol channels and its complete norming-mode staircase, not channel diagonalization, the isolated unweighted norm, or the idea of an edge-to-bulk transition.

## value

PASS

The quadratic symbol is the first monomial with weight-dependent maximizing degree. The infinite sharp-norm optimization determines exact two-mode degeneracies, identifies every equality input, and gives a clean benchmark for weighted commutator norms, including reversal relative to the linear symbol and movement of the maximizer at high weight. These finite-weight data are more informative than a standard compactness result or a diagonal channel list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
