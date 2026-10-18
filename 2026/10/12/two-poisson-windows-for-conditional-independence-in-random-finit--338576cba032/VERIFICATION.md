---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each fixed z the recombination semantics x⊥_z y is equivalent to the fiber being empty or precisely A×B for its row/column projections. These rectangles are disjoint events under independent Bernoulli cell inclusion and give exact Q_{r,s}(p); the k fibers are independent, giving Q^k. In the sparse regime p=O(n^-5/2), two edges in different rows and columns dominate fiber failures: d_n=2 C(n,2)^2 p²(1-p)^(n²−2)+O(n^-3/2), hence n d_n→a²/2; the failure count is Bin(n,d_n)→Pois(a²/2). In the dense regime, successful nonfull rectangles require an empty row or column, probability ≤2n²(1-p)^n globally, so probability of all-full fibers p^(n³) gives e^-b, with analogous Poisson failure count. For intermediate α,β→∞: p≥1/2 yields exp(-β)+o(1); p≤1/2 and λ=n²p≤1 has ≥c λ² per-fiber failure from nonmeeting edge pairs; for λ≥1 opposite diagonal blocks independently contain edges with positive probability and their cross cells have ≥3/4 missing probability. Thus zero-success asymptotic is proved without extrapolating finite checks. Independent rectangularity enumeration checked n=2,3 and relevant finite coefficients.

## originality

PASS

The random Bernoulli model samples ordinary unweighted relational teams, not probabilistic-team independence. Hannula–Kontinen–Virtema defines the recombination atom; Hella–Luosto–Väänänen examines combinatorial dimensions of independence-satisfying teams and rectangular family counting; neither inspected mathematical statement gives the two Poisson windows n^-5/2 and n^-3 or the uniform intervening regime. The exact unweighted count is treated as known background. Semantic and web comparisons found no equivalent random-database Bernoulli limit theorem, but terminology-alias risk remains.

## value

PASS

A familiar nonmonotone relational dependency has two sharply distinct probabilistic satisfaction transitions, rather than one threshold. Identifying both Poisson intensity constants, their different scaling powers, and the full intermediate failure regime is a motivated probabilistic structural theorem linking logic and random database relations, not just computing a finite reliability polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
