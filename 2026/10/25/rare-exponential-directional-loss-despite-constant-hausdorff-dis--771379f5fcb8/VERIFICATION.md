---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Verified n≥3, intrinsic 2n−2 dimensional Euclidean normalization and Exp(2) rate convention. The transportation/Hall constraints p_i+q_i≤1 are necessary for singleton rows and sufficient since any ≥2 rows reach every column. Uniform-simplex Beta(1,n−1) marginals give Pr(p_i+q_i>1)=1/binom(2n−2,n−1); two strict violations cannot coexist, proving exact volume ratio. For deleted (e_i,e_i), Cauchy–Schwarz yields min squared distance n/[2(n−1)] with an explicit equal-weight Q coupling; convexity of distance(Q,.) forces a P vertex to be farthest, proving Hausdorff. Centered independent Gaussians divided by R∼χ_{2n−2} give uniform intrinsic spherical direction. Direct support maxima over i≠j prove Δ=[1_{I+}min(top gaps)+1_{I−}min(bottom gaps)]/R. Independent uniform ranking permutations give Pr(I+)=Pr(I−)=1/n and Pr(I+∩I−)=1/[n(n−1)], independent of gaps and R; hence exact positive probability 2/n−1/[n(n−1)]. With b_n=Φ^{-1}(1−1/n)>0, the Gaussian tail ratio shows b_n times each top gap converges to Exp(1), and the minimum of two independent limits is Exp(2). The double-coincidence case has conditional probability 1/(2n−3)→0, while R/√(2n)→1. Gaussian increasing hazard and a superpolynomial small lower-second-maximum exceptional event supply uniform integrability of first two scaled-gap moments; inverse χ moments of R supply the normalizer control. The positive part contributes EΔ∼1/[n b_n√(2n)] and EΔ²∼1/[2 n² b_n²]; subtracting (EΔ)² preserves the variance equivalent. Independent implementation: n=3,4,5 intrinsic ConvexHull ratios 0.5,0.8,13/14 and squared distance n/[2(n−1)]; 3900 fresh support identities, exact-permutation rarity simulations n=8,20,50,100,200; one-event scaled-gap moments n=30,100,500 show slow convergence but expected trend. Computations are corroboration, not all-n proof.

## originality

PASS

The natural sign-reversed bipartite root-polytope realization is indeed covered as an OBJECT by Almousa–Dochtermann–Smith, but their theorem family is tropical subdivisions, type ideals and toric edge-ring invariants (arXiv:2209.09851, §§1.1, 4.5, 5). The Ohsugi–Tsuchiya PQ adjacency polytope includes every diagonal vertex by definition (arXiv:2103.15045, p.1, §1), so its Ehrhart/normalized-volume formulas are for another hull and do not imply this diagonal-deleted random-width law. A published crown-graph symmetric-edge inball theorem uses the centrally symmetrized ± root hull, and proves radius/contact-facet phases rather than the one-sided P/Q directional width defect. Standard Gaussian extreme-order spacing is an acknowledged ingredient; the specific combination of exact volume, Hausdorff, Gaussian ranking event and conditional Exp(2) law has no dominating prior theorem in the inspected texts or Resultary results. This is best-of-knowledge and does not assert absolute novelty.

## value

PASS

The crown root polytope Q_n is a canonical naturally defined deletion of a perfect matching of n vertices from the n²-vertex product Δ_{n−1}×Δ_{n−1}. Comparing three non-equivalent and motivated quantitative notions of geometric stability is useful: relative volume loss is exponentially small, Hausdorff gap tends to 1/√2, while random-direction width deficit appears with only Θ(1/n) probability and has a sharp conditional nondegenerate exponential scale. The exact objectwise formula and infinite-n limiting distribution form a self-contained structural separation, not a routine one-parameter renaming, arbitrary tiny table entry or unsupported numerical curiosity. Even if the elementary volume coefficient had been previously tabulated, the matching of exact rare-angle probability to extreme-order-statistic geometry is a motivated independent invariant with likely use in stability and random support-function comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
