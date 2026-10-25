---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For bidirected G=K1 join disjoint union of clique C_i, each peripheral vertex has outdegree s_i and the hub has sum s_i. Every majority-stable set contains at most b_i=floor(s_i/2)+1 vertices from hub∪C_i: without hub select <=b_i, with hub select <=a_i=floor(s_i/2). Summed fractional cover inequalities yield W≥max_i(s_i+1)/b_i. For the reverse inequality, mix H-sets consisting of hub plus independent uniform a_i-subsets with weight 1 and B-sets consisting of uniform b_i-subsets without hub with weight L−1. Every sample is majority-stable including hub constraint sum a_i≤(sum s_i)/2, and every peripheral vertex gets (L b_i−1)/s_i≥1 while hub gets 1. This proves exact all t,s_i including t=1,s_i=1. Independently checked rational values (1)->2, (2)->3/2, (3)->2, (2,4)->5/3, (2,2,2)->3/2 and the literal supplied verify.py definition; did not independently rerun uploaded SciPy LP census.

## originality

PASS

PASS best of knowledge. Ben-Ameur–Maddaloni arXiv:2610.11997 (HTML full text) establishes general universal 523/140 and complexity/approximation results, no clique-bouquet exact formula; Anastos et al. 2019 fractional majority relaxations likewise differ. Other Resultary majority C-coloring and strong-majority edge-coloring have different feasibility predicates, so cannot dominate the invariant.

## value

PASS

The explicit optimal fractional covering for all unequal clique bouquets is a motivated exact classification of a genuine digraph coloring relaxation. The independence from the number of cliques despite the changing hub degree and the odd/even sharp transition give a structural theorem useful for clique-sum model classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
