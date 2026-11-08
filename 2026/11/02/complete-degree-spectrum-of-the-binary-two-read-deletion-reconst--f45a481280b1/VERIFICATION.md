---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

By the published Type-A characterization, two binary length-n words have two distinct common one-deletion descendants precisely when they are complementary alternating phases on their unique first-to-last mismatch interval of length>=2. Therefore neighbors of x biject with alternating intervals in x. Maximal 1-runs of the difference string have lengths h_i, contributing binom(h_i+1,2) each. Unique run decomposition yields F(z,u)=2(1+R)/(1-z-zR), R=sum_{h>=1}z^h*u^binom(h+1,2); differentiation at u=1 yields exactly mean n-2+2^(1-n) and variance 6n-30+(2n^2+6n+17)/2^(n-1)-4^(1-n), and limiting degree/n->1 in probability. n=1 has two zero-degree vertices. Independent direct distinct-deletion-ball adjacency over all binary words n=1..8 matched every predicted degree and histogram. The all-n conclusion uses the Type-A theorem and formal combinatorics, not finite tests.

## originality

PASS

Cai et al. established pairwise Type-A characterization and an earlier published Resultary result exactly counts edges and mean degrees for arbitrary alphabet; neither determines the complete degree distribution or the exact variance. The bivariate all-length histogram and per-word formula are strictly more informative than their aggregate counts. Novelty qualified against broader reconstruction-code graph studies.

## value

PASS

The full degree distribution is a natural, previously missing graph invariant controlling local confusability heterogeneity, and the exact variance gives an independent quantitative law beyond the known edge count. The all-length formal bivariate generating function makes all local degree counts extractable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
