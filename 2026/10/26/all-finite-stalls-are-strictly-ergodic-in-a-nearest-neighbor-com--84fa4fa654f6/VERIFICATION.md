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

For each integer m≥1, F_m(s)=(1−s)(s+s^(−1))^(m−1)−s² has a unique root on (0,1): the ratio (1−s)(s+s^(−1))^(m−1)/s² strictly decreases from infinity to zero. Put λ=s+s^(−1), c=1/(λ−2), h(j)=λ^j for j<m and c+(λ^m−c)s^(j−m) for j≥m, with h(∞)=c. The root equation is equivalent to the interface relation λ^m−c=s(λ^(m−1)−c). Using s+s^(−1)=λ and (λ−2)c=1 verifies Mh=λh at every j and at infinity. The identity c/λ^m=1/[(1−s)(1+s²)]>1 gives 1≤h≤c and positivity; order bounds give r(M)=λ exactly. Writing M=S+K with (Sf)(j)=f(j−1)+f(j+1) for j≥m, S(∞)=2f(∞), S(j<m)=0 gives norm S≤2 and finite-rank K. Hence normalized T=M/λ is quasi-compact (distance ≤2/λ<1 to compact K/λ). Uniform common occurrence of each isolated letter after sufficiently many iterates proves primitivity, so MRW Theorem 6.7 implies minimality and unique ergodicity. The defining root gives δ=1−s=2^(1−m)(1+O(2^(−m))) and λ−2=δ²/s=4^(1−m)(1+O(2^(−m))). The λ^n/c≤|ρ_m^n(0)|≤λ^n bound and exact rational binomial certificate yield the 72000-step crossing at m=7; the 1000-step below-two bound was independently recomputed. Direct independent script checked m=1..16 high-precision eigenfunction residuals, exact finite length 2-stall at n=34, the 7-stall n=1000 bound, and exact rational 72000 binomial bound; none substitutes for the universal proof.

## originality

PASS

Best-of-knowledge originality: Walton 2609.07550 is the exact motivating one-point-compactification family, but its first-version seven-stall non-unique-ergodicity prediction and two/four-stall observations do not entail the new all-finite-stall explicit root, positive eigenfunction, and exact length reversal. The newer v2 primary full text was inaccessible in this run; this is explicitly a live priority risk, not asserted whole-document noncoverage. MRW 2025 supplies only the conditional quasi-compact primitive theorem and a different initial rule, while Frettlöh–Garber–Mañibo 2024 constructs parametrized other substitutions. Relevant published Resultary finding concerns a four-adic expanding map rather than compact-alphabet substitution. No inspected dominating theorem yields this exact classification.

## value

PASS

The result classifies a natural, explicitly studied family of nearest-neighbor compact-alphabet substitutions for every finite stall, resolving a reported seven-stall negative prediction in the opposite direction by a rigorously positive spectral gap. A sharp exponentially small λ_m−2 law mathematically explains a long misleading finite transient, and a rational certificate supplies an explicit cutoff witnessing reversal. Unlike routine PF substitution, the noncompact countable alphabet requires an explicit positive eigenfunction, spectral bound and compact perturbation; the full all-m classification is independently useful and motivated by an existing open spectral question. Limitations to this tail rule and finite stalls are appropriately stated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
