---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The monomial weights are Γ(alpha+2)Γ(2n+1)/Γ(2n+alpha+2). The even binomial expansion gives K_alpha(u)=[(1−sqrt(u))^(−s)+(1+sqrt(u))^(−s)]/2, s=alpha+2. For a zero, the Cayley transform w=(1+sqrt u)/(1−sqrt u) has Re w>0, and s Log w is an odd multiple of pi i; the strip |arg w|<pi/2 gives precisely negative simple roots at tan² angles and strict 4j<alpha boundary. Transfer f(z)=F(z²) to the induced coefficient-weighted space, equivalent as a set to ordinary weighted Bergman, where B_a acts as (w−a)/(1−aw) and the range consists of functions vanishing at a. The orthogonal wandering line is therefore the evaluation kernel K_alpha(aw). Since the disk automorphism is a uniform functional transformation of w and conversely, B_a-cyclicity is multiplication-by-polynomial cyclicity of the wandering vector; any interior zero blocks cyclicity, while zeros only on boundary are cyclic because ||w^N||→0 and a nonzero analytic factor remains invertible. Independent even-binomial evaluations and negative-zero checks corroborate, without replacing the analytic complete zero argument.

## originality

PASS

Gallardo-Gutiérrez–Partington–Seco prove existence of an *equivalent renorming* making a given finite Blaschke multiplier wandering, with certain special monomial cases in the original norm; renorming does not imply the original-norm sharp family classification. Lin–Xu–Yu and Xu–Yu study global weighted Bergman shift/finite Blaschke wandering existence; their published descriptions do not assert the exact one-parameter degree-two/E2 zero staircase, but relevant 2026 full text was inaccessible here, a material best-of-knowledge risk. The published Resultary Lu Qi-Keng disk kernel concerns a different boundary-distance weight and cannot directly imply this norm-specific criterion.

## value

PASS

The full zero census and exact boundary cyclicity transition for a minimal nontrivial degree-two Blaschke action on a canonical invariant subspace give a natural, exact operator-theoretic phase diagram. This is more informative than a single arbitrary finite zero computation and distinguishes original-norm wandering from the known equivalent-renorming result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
