---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The north-east convention agrees with the rank of the specified permutation matrix in Fink–Rajchgot–Sullivant. Congruence by the diagonal cocharacter of exponents 3^a preserves each rank condition and separates the coordinate lines by base-three uniqueness. For a<b, the smallest rank-one and rank-two corners for E_ab+E_ba are (a,b) and (b,a); rank monotonicity gives the asserted two inequalities. Among the b entries of the prefix, at most a−1 can exceed n+1−a, so in fact R_w(b,a)≥b−a+1≥2 automatically. The same argument with b=a gives R_w(a,a)≥1 for every diagonal point. Therefore the formula is correct and can be simplified to n+Σ_a(n+1−a−m_a); no second order statistic is actually needed. Euler localization counts these points even in the singular case. Every summand is nonnegative, and their simultaneous vanishing requires the reverse permutation by induction on a. The ambient maximum requires the (1,n) point to survive when n≥2, hence w(1)=1, which conversely suffices; for n=1 the sole point attains both bounds. The all-size argument is symbolic; the finite checker described in VERIFICATION.md was not rerun.

## originality

PASS

The strongest inspected overlap counts the same types of ambient fixed points but under an overall rank cutoff. Prior symmetric Schubert results establish the convention, ideals and patch geometry; no inspected statement gives the global projective fixed-point census for these permutation-indexed north-east conditions or its sharp equality cases. The supported distinction is the permutation-dependent count, not the localization method, and the second statistic adds no independent information.

## value

PASS

The result gives a readily usable exact topological invariant and both extremal classifications for an established permutation-indexed family. It identifies the rank-zero corner pattern, equivalently the prefix minima, as sufficient despite the higher minors defining these varieties. That simplification, not novelty of the localization technique or a purported independent role for two statistics, gives the formula value when comparing different permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
