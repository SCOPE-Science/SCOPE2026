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

For independent uniform labeled spanning trees of K_n, the Cayley forest-extension count yields P(H subset T)=n^(−|H|) product(component sizes) for any host forest, with exact one-edge probability 2/n and two-edge probabilities 3/n² or 4/n². Peeling a leaf of a *tree-index* forest, conditionally on the other trees, gives E[X_ab|T_b]=2(n−1)/n=μ independent of T_b; hence all distinct-index forest product moments factor and their mixed cumulants vanish. The two-edge inclusion kernel on host K_n edges has line-graph spectrum μ (one), 1/n (n−1) and 2(n−1)/n² (n(n−3)/2). Traces give the stated exact positive cycle cumulant (n−1)/n^ell+[n(n−3)/2]*(2(n−1)/n²)^ell. Independent exact SymPy traces confirmed n=3..8, ell=3,4,5. For each fixed pair-index factorial multiindex, vertex-disjoint distinct host-edge assignments contribute 2^R+O(1/n); intersecting hosts are O(1/n), and repeated hosts across different pair classes demand ≥3 distinct trees and contribute O(1/n). This establishes mixed factorial moments and fixed-q joint independent Poisson(2) convergence, not finite-sample independence.

## originality

PASS

Best-of-knowledge comparison of statements rather than titles: close primary results supply tools, partial parameter regimes or weaker scalar/qualitative conclusions but do not directly cover this particular exact claim. Inaccessible plausible broader results are named and retained as specific historical-priority risks, not treated as automatic failure.

## value

PASS

Overlaps between many independent trees form a natural network of correlated combinatorial statistics. Pairwise overlaps are exactly uncorrelated despite strictly positive cycle-index higher cumulants; asymptotic independent Poisson coordinates then reveal the decay of those dependencies. Explicit exact dependence at every finite n combined with a complete fixed-q limit is a motivated structural result beyond a scalar two-tree overlap law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
