---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The linear shear sending the coordinate rectangle [0,a]×[0,b] to any parallelogram preserves Euclidean arclength on each edge (the direction vectors are unit) and scales all area by det, hence normalized sampled-hull area depends only on the side lengths. For n≥2 the cap identity for consecutive arclength samples integrates oriented tangent determinants with weight (1-δ/L)^n; adjacent-edge rectangle evaluation gives exact missing area 2[L^{n+2}-(2a+b)^{n+2}-(a+2b)^{n+2}+a^{n+2}+b^{n+2}]/[L^n(n+1)(n+2)], L=2(a+b), and normalized formula as submitted. The expectation equals 2E φ_n(uX+(1-u)Y), φ_n(z)=(1-z/2)^n-((1-z)/2)^n. For n≥3, φ_n is strictly convex on [0,1], so the deficit strictly grows with |u-1/2| by symmetrization, giving exactly rhombus maximizers and explicit sharp thin/equal-side endpoints. Dominated convergence with u_n n→τ gives n(1-Q_n)→8(1-e^{-τ/2})/τ, including limit τ=0 as 4; fixed u gives n²(1-Q_n)→8/[u(1-u)]. An independent exact moment expansion agrees with the formula for 32 rational settings. Finite checks do not prove the strict inequality or boundary-layer limit, which follow analytically.

## originality

PASS

Reitzner–Schütt–Werner (2019/2023) analyze convex hulls from uniform boundary points on simple polytopes and provide asymptotic volume differences for fixed input bodies. Their theorem yields/relates to fixed positive side-ratio behavior, but not an equality for each n or uniformity as one relative side length collapses at n^{-1} scale. Prochno et al. (2024) study Hausdorff distance, not expected missing area. Buchta (1984) exact square formula is for area-uniform interior samples, a mathematically different distribution. The familiar integral cap method is not novelty by itself; the assessed contribution is the exact finite-n aspect-ratio ordering, sharp boundaries and n-dependent thin crossover. A general older boundary polygon finite-sample integral could nevertheless imply this specialization by nontrivial reduction.

## value

PASS

Expected area of a boundary-sampled random polygon is a canonical random-polytope approximation statistic, and parallelograms form the simplest nontrivial two-edge-length shape family. Exact angle-independence, strict rhombus extremality for every n≥3, and recoverability of the unordered side ratio are meaningful structural results, not a numerical fit. The n^{-1} thin-side crossover exposes a genuine failure of fixed-body n^{-2} asymptotics in a natural degenerating regime. The theorem is self-contained and carefully excludes full distributional comparisons and higher dimensions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
