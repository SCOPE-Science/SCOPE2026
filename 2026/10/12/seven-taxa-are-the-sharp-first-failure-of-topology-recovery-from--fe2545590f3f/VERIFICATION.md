---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Let s_e be the descendant count of edge e and c_s the total length of edges with s leaves. Each edge is absent from a k-tip sample with probability binom(n-s,k)/binom(n,k), so the mean formula holds and the system for k=n-j is triangular with new coefficient c_j=1. Strictly positive edge lengths make the support of c_s for s>=2 exactly the support of proper internal clade sizes. Independently enumerate every unordered rooted binary shape by its unordered pair of child shapes; counts at n=1..7 are 1,1,1,2,3,6,11, with no support collision at n<=6 and the first unique collision at seven. Independently reconstruct both height-4 ultrametric 7-tip witnesses and all 128 subsets: common spectrum (12,3,2,1,0,0), exact mean curve (0,4,51/7,351/35,433/35,101/7,114/7,18), two-tip counts (1,4,4,12) vs (2,2,5,12), and variances 128/147 vs 142/147. Grafting a new root with a single new leaf preserves positive ultrametric lengths, weighted-spectrum equality and different rooted shapes for each n>=7; this induction, not the finite enumeration alone, proves the unrestricted assertion. Only unlabeled rooted topology is recovered below seven, not edge lengths or labelings.

## originality

PASS

Compare full-curve versus weighted clade-size spectrum, rather than confused notions of identical clade-size multiset, leaf-level labels, or phylogenetic-diversity distributions. Nipperess--Matsen already prove general rooted mean and variance rarefaction formulas. Fischer--Hamann--Wicke (2025) analyze clade-size multisets and first multiset collision at nine tips; their invariant retains multiplicities and does not impose or exclude a weighted-edge total collision at seven. Complete shape supports and integer ultrametric witness add a natural exact first-identifiability cutoff not found in inspected primary results or semantic searches. No absolute historical uniqueness is asserted.

## value

PASS

An entire exact mean rarefaction curve is a standard ecologically interpretable observable, so asking whether it reconstructs unlabeled evolutionary tree topology is natural. The first indistinguishable positive-edge ultrametric pair at exactly seven taxa is a sharp information-loss boundary; the explicit variance separation shows what extra distributional information restores. This is a substantive extremal identifiability theorem, not merely a numerically guessed tiny instance; the all-n extension adds a constructive family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
