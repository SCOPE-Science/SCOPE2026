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

The prefix at T=t,L=i has r-1 occurrences of i and caps r-1 on every other count. The multinomial weight with the final draw fixed gives (1) and positive mass in every feasible cell. The factorial coefficient sequences have contiguous support and strictly decreasing successive ratios. Their Toeplitz kernels are TP2 in the nonnegative-minor sense. In the convolution log-concavity proof one may remove degree-zero factors as identities; for positive-degree factors the Cauchy–Binet term with intermediate indices s,s+1, s=max(0,k-A), is strictly positive, and the top-degree minor is positive by support. For the marked ratio the analogous s=max(0,k-Q) is always at most r-2 and furnishes a strictly positive product with the determinant x^s y^s(y-x)/(s!(s+1)!), including the m=2 point-mass case. Thus the sign is strict at every adjacent time. Constant and leading coefficients give the two endpoint odds; normalizing the time laws multiplies their ratio by a positive constant, and equal probabilities give equality by symmetry. As a separate finite check, (p_1,p_2,p_3)=(1,2,4)/7 and r=3 give odds 1/8,3/20,9/50,3/10,1/2 for times 3 through 7. The supplied code was inspected, not run; its captured output reports 1,737 profiles and is finite corroboration only.

## originality

PASS

The r=2 specialization, including the endpoint odds, is exactly covered by an earlier Resultary record and is not credited as new. The supported distinct contribution is extension to every common quota r>=3 with strictness at each pair of consecutive feasible times. Inspected repeat-time and competing-pattern results do not cover that extension; final-coupon orderings use the opposite stopping rule.

## value

PASS

This is a natural marked stopping problem, not an arbitrary coefficient comparison: observing a longer race changes the relative identity of the likely winner. Higher quotas allow repeated nonwinning labels, and the sign remains strict at every feasible time with simple sharp endpoint odds. It provides information not captured by the time distribution or unconditional winner probabilities. The reusable strictness argument and the extension to all higher common quotas are the valuable part.

The dated certificate retains the supplied scientific assessment, sources and limitations.
