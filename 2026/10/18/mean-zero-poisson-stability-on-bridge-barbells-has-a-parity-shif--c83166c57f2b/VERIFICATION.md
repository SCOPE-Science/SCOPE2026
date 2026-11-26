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

Independent Poisson derivation: for zero-sum f let T=∑_A f, and let μ_A,μ_B denote solution clique means. Summing over A gives bridge drop T. At ordinary vertices the correction to the clique mean is f_i divided by the clique size, and the endpoint corrections are (f_A0−T)/a and (f_B0+T)/b. Thus μ_A−μ_B=T(1+1/a+1/b)−f_A0/a+f_B0/b, and aμ_A+bμ_B=0. In an ordinary A evaluation row, n times the coefficients, before centering, are b+1 at A0, b+1+b/a on ordinary A vertices with extra n/a at the evaluation vertex, 1 at B0, and 0 elsewhere. The sum is D=ab+n+2. The A0 row instead has b+1 at A0, b on ordinary A vertices, and the same opposite-clique coefficients, for sum ab+2. Center both rows and swap cliques for the remaining rows: same-clique entries are positive and cross entries negative. The absolute row sum (the row functional's induced norm, not the largest entry) is twice the own-clique sum. Endpoint gaps are 2b/n and 2a/n; the A-versus-B ordinary gap is 2(b−a)D/n². For mean-zero inputs, the sorted upper-half minus lower-half sum is the absolute deviation from a median, attained by the stated balanced sign forcing. In the raw ordinary A row the median can be 1 for b=a, is 1 for b=a+1, and can be 0 for b≥a+2; the deviations sum to D−2, D−1 and D respectively. The other three row values are W(A_i)−1, (a/b)W(A_i) and a²/n, with strict loss at endpoints and in the larger clique if sizes differ. In the b−a≥2 branch, ab increases strictly toward balance at fixed n. Direct comparison with the final balanced or near-balanced candidate gives the strict parity-dependent maxima, with gains 1/n at the decisive comparison and the unique n=4 split. Expansion of the exact formulas uniformly gives the two limiting polynomials with maxima 8/27 at 1/3 and 1/4 at 1/2, and fixed-a limits 2(a+1) and a+1. Fresh exact checks verified projected Poisson columns, maximizing row types, median forcing, and all fixed-order comparisons for 121 splits with 4≤n≤24.

## originality

PASS

Pass for the exact pair of sharp norms, evaluation-vertex classification and compatibility-dependent geometry, especially the finite-order shift. The clique/bridge Green matrix and median duality are established ingredients. The strongest inspected inverse formula supplies entries but not the sorted-row comparisons, equality cases, or maximization over sizes. The strongest catalog overlaps optimize a different observable on barbells or a different norm on trees.

## value

PASS

Provides exact worst-case Poisson amplification under two natural forcing constraints, including constructive extremizers. The normalization is identical in both, yet the unconstrained and compatible asymptotic worst proportions differ, extreme-imbalance amplification drops by a factor of two, and exact even-order compatibility favors a one-vertex shift from equality. The latter behavior cannot be read off from the limiting coefficient alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
