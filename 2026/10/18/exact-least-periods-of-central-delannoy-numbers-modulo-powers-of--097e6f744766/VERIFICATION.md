---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The theorem quantifies every r≥1 and every starting index n≥0. For s≥2, Vandermonde applied to Δ_k=binom(n+2^s,k)−binom(n,k), together with exact ν₂binom(2^s,j)=s−ν₂(j), yields ν₂(Δ_k)≥s−⌊log₂k⌋ for low k. Splitting 2^k[(a+Δ)^2−a²] into linear/quadratic terms gives divisibility by 2^(s+2) for each low k; high k are killed by 2^k. Thus 2^s is a pure period modulo 2^(s+2). Mod 2 all terms are odd; mod 4 D_n≡1+2n; D₂−D₀=12 excludes half-periods for r=3,4; D₅−D₁=1680 excludes r=5. For r=t+3≥6, the k=1 difference at n=1 has ν₂ exactly t+2, while binom(2^t+1,k) has ν₂=t−ν₂(k(k−1)) and each k≥2 term has ν₂≥2t≥t+3, excluding the candidate half-period. Every least positive period divides the demonstrated power-of-two period, so all smaller periods are excluded. Independent standard-library modular arithmetic replayed exact periods r=1..12 (up to 520 starts per r), and sharp half-period valuations for t=3..12. These bounded tests corroborate, not replace, the all-r proof.

## originality

PASS

Best-of-knowledge primary-text comparison: the same sequence is also P_n(3)=T_n(3,2), but inspected published results concern selected-index 2-adic valuations, prime congruences, automaticity, or different triangle-array directions. No inspected source states or implies the all-n least pure period P(r) for every 2-power modulus. This is qualified by an inaccessible related article and potential unindexed general 2-adic continuity results.

## value

PASS

The least pure modular period is a standard and naturally motivated arithmetic invariant of a classical lattice-path counting sequence. The result fully classifies all dyadic moduli, detects a genuine r=3,4 plateau, and proves sharp eventual period doubling with explicit witnesses and no preperiod. The exact lengths are useful in reducing infinite-index residue questions and modular Delannoy computations to finite cycles. They are not an arbitrary small-parameter tabulation or a renamed existing result; the complete all-r statement requires separate uniform divisibility and minimality arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
