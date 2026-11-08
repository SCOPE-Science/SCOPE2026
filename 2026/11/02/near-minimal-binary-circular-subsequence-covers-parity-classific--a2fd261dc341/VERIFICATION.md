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

For a binary linear word, k universal subsequence coverage iff there are k disjoint adjacent unequal pairs (greedy minimal alphabet-covering arches). For n=2k+1 a cyclic rotation has such pairs exactly when the unequal-edge subgraph of the odd cycle has matching number k. Equal-adjacency edges break the cycle into paths; matching size=(n-E)/2, where E is number of even-length unequal paths. Hence exact condition E=1. Counting odd r=2s+1 equal edges and weak compositions gives L=(2k+1)2^k. Each admitted word has multiplicities k and k+1, so is primitive, giving 2^k necklaces. A prescribed dihedral reflection fixes 2^(floor(k/2)+1) admissible words and Burnside yields 2^(k-1)+2^floor(k/2) bracelets. Independent exhaustive checker verified edge parity, arch universality, and orbit counts for every k=1..7, with direct subsequence coverage for k<=5; infinity follows from matching and Burnside, not finite enumeration.

## originality

PASS

Targeted Resultary semantic searches and primary literature comparisons, with specific mathematical implication checks and residual priority risks, support qualified best-of-knowledge originality of the final scoped claim.

## value

PASS

The first nonminimal length 2k+1 of circular binary subsequence universality is a natural fiber of a previously studied combinatorics-on-words notion. An exact parity classification, linear-time criterion and all three orbit counts give a complete structural and enumerative result, beyond merely computing an index for individual words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
