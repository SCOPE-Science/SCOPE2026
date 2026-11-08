---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For c>1, L=log c and h_a(t)=a^-1 exp(-t/a)1_(t>0), ψ_c=h_c-h_1 has squared norm N²=(c-1)²/[2c(c+1)]. Direct <h_a,h_b>=1/(a+b) expands to Gram g_k=2(c+1)² c^(3k/2)/[(c+c^k)(1+c^k)(1+c^(k+1))]. The unitary x=log t map converts L²-normalized dilates to translations by jL. The Mellin transform gives Gamma(1/2-iξ)(c^(-1/2-iξ)-1)/N, and |Gamma(1/2+iξ)|²=pi/cosh(pi ξ), producing the periodic positive Gram symbol G_c(theta)=pi(1+q²-2q cos theta)/(L N²) sum_m sech[pi(theta+2pi m)/L], q=c^-1/2. Its continuous positive minimum/maximum are sharp two-sided and one-sided Riesz bounds via Fejér concentration; positivity of all g_k gives maximum at 0. For L->0, the nearest two antipodal aliases give P_L(pi)~4 exp(-pi²/L), D_L(pi)/N²~16/L²; uniform two-range comparison excludes shifted smaller values and yields A~64pi L^-3 exp(-pi²/L), B~pi/L, B/A~L² exp(pi²/L)/64. Independent numerical Mellin symbol checks at L=.5,.3,.2 gave A_symbol(pi)/asymptotic ≈1.02606,1.00938,1.00417, while B_symbol(0)/asymptotic ≈1.01546,1.00560,1.00250. These finite numbers corroborate but do not prove infinite Gram and uniform minimization.

## originality

PASS

Direct statement-level comparison with relevant original primary research and semantic published-finding records did not identify an equivalent or dominating fully checked result. Known premises are attributed; nontrivial new specific quantitative conclusions assessed at qualified best-of-knowledge level. Inaccessible and incompletely inspected papers remain explicit residual priority risks.

## value

PASS

Dense sampling of natural causal exponential-difference scale channels creates a concrete coefficient-recovery conditioning problem. The exact Riesz Gram symbol proves stability at every finite ratio and quantifies exponentially catastrophic deterioration in the dense-scale limit with the sharp non-obvious 64pi and 1/64 constants. This is a motivated spectral stability classification not reducible to single-channel response energy; no translated filterbank claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
