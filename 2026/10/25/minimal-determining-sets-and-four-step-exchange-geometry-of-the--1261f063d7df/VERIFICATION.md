---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python3 verify_action.py` and `python3 verify_profiles.py` in a standard Python 3 environment, each in a fresh process with no external dependencies. Compare their stdout to `verify_action.out` and `verify_profiles.out` respectively. Each produces one JSON object followed by a newline.

`verify_action.py` constructs \(1920\) candidate automorphisms (translations and permutations of five directions), checks adjacency preservation for every ordered vertex pair, tests pointwise stabilizers of all \(2^{16}\) vertex subsets, classifies inclusion-minimal determining sets, verifies automorphism orbits, and conducts full exchange-graph breadth-first searches.

`verify_profiles.py` uses an independent five-column signature characterization and all-subset scan. It checks both directions of the four- and five-set geometric criteria, constructs exchange adjacencies by pairwise set intersections, and independently performs full all-source shortest-path searches. The two verifiers recover the same \(560\) optimal bases, \(192\) additional inclusion-minimal five-sets, \(5920\) exchange edges, and diameter \(4\).

The graph has sixteen vertices. This is an exhaustive finite calculation, not a proof of corresponding results for an infinite family. Prior-art search does not prove worldwide novelty. Independent external scientific validation was not performed.
