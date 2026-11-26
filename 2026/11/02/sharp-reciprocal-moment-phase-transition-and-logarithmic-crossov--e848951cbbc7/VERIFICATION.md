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

For interior k, the two nonnegative mass-recurrence coefficients sum to 1−p/n≤(n/(n+1))^p, and the endpoint probability p^(n−1) is absorbed in a uniform C_p n^−p bound. The mass at 1 is a_n=Γ(n−p)/(Γ(n)Γ(1−p)). For any fixed k≥2 the ratio h_{n,k}/a_n is an average of its previous value and the ratio at k−1, with weight p(k−1)/(n−p) on the latter. The weight lies in (0,1) for n≥k, has divergent sum, and hence forces convergence to 1 by induction on k. This proves n^p h_{n,k}→1/Γ(1−p) for each fixed k. Conditional recursion for g_u(k)=Γ(k−u)/Γ(k) multiplies its expectation by 1−pu/n. For 0<u<1 the summable approximation error against the uniform mass bound is O(n^−p), negligible at scale n^−pu. For u>1, summable domination of the fixed-k limits gives exactly ζ(u)/Γ(1−p). At u=1, subtract the exact atom a_nΓ(s) from the transform at u=1−s before sending s to zero. With R_n(s)=Γ(n−p+ps)/(Γ(n)Γ(1−p+ps)), the result for the shifted reciprocal sum is R'_n(0)=p a_n[ψ(n−p)−ψ(1−p)]. To replace (k−1)^−1 by k^−1, the correction Σ_{k≥2}h_{n,k}/[k(k−1)] equals a_n+o(n^−p) by fixed-k convergence and domination, so the critical finite part is as stated. The pole-subtracted identity extends to both signs of s near zero; the difference between its summands and k^−1+s is uniformly O(k^−2+δ) for k≥2 and |s|≤δ<1/2. At s=b/log n, R_n(s)/R_n(0)→exp(pb), and Γ(s)/log n→1/b for b≠0, yielding the claimed crossover; b=0 follows from the fixed critical expansion. This checks signs, constants and critical cancellation without inferring unbounded moments from weak convergence. Frozen exact and numerical check evidence was inspected, not rerun.

## originality

PASS

The movement clock, its scaling limit, Liang's exact gamma transform and uniform mass bound, the three orders, and the direct subcritical gamma-ratio coefficient implication receive prior credit. The distinct contribution supported by this audit is the sharp small-count-controlled side and the critical finite part, together with an explicit moving-exponent law across the boundary. Existing transform and point-mass bounds are important inputs here; the reviewed results did not establish the critical correction to the shifted reciprocal or the complete sharp transition for actual reciprocal powers.

## value

PASS

Inverse powers measure the effect of paths with very few movements, information lost under the usual clock scaling limit. The zeta factor identifies the discrete fixed-count contribution, the critical constant distinguishes the actual reciprocal from the convenient gamma-ratio proxy, and the logarithmic window gives a coherent interpolation where estimates at fixed exponents do not apply uniformly. The exact constants and crossover let a reader distinguish typical scaling from rare-count domination, rather than merely restating the known orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
