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

Tracing the downdate gives g_i=||Ae_i||²/d_i, the Rayleigh quotient of A at A^{1/2}e_i. Thus Δ₀≤λ_max and Δ₁=tr(A²)/tr(A). Scaling λ_max to one and writing s for the other positive eigenvalues' sum yields (1+s)/(1+s²/(r−1)), maximized at s=√r−1. Rank one ties identically. The block family J_N/N ⊕ I_{r−1}/(√r+1) has gains 1 on the N-block and 1/(√r+1) on singletons, yielding the asserted limit. In size two the difference is (a−b)(g₁−g₂)/(2(a+b))=(a−b)²(1−|c|²/(ab))/(2(a+b))≥0; in size three J₂/2 ⊕ [2/3] gives 8/9 versus 13/15. For fixed real β>1, B_T has gains T on the m_T-block and one on the singleton; total block weight h_T=T^β m_T^{1−β} satisfies Th_T→0 under the stated q, so the ratio is asymptotic to T. These checks establish one-pivot expectations, not multistep performance. The supplied finite-test script was inspected, not run.

## originality

PASS

The distinct contribution supported by the comparison is the sharp all-rank one-pivot trace-gain envelope and the trace-specific rank-two failure throughout β>1, including the regime 1<β≤4 not covered by the prior Frobenius failure. Neither the power family, the β=1 expected residual identity, nor the two-cluster example shape is new. This is a bounded statement-level assessment, not a priority claim.

## value

PASS

A sharp rank-only bound answers how much uniform sampling can outperform the standard Cholesky pivot rule on the actual expected trace progress, and the rank-two construction shows why that guarantee cannot be transferred to any heavier exponent. The first possible reversal in size three provides a compact diagnostic. The result does not depend on calling the family new or extrapolating to multiple pivots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
