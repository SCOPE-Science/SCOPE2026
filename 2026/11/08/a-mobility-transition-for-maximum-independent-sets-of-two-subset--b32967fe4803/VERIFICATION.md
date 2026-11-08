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

# Reproducibility

Using Python 3, run `python prism_direct.py` and `python prism_check.py` in a directory containing these standalone scripts. The first independently constructs the exact graph adjacency and exhaustively checks every candidate bitmask at the claimed optimum sizes at \(n=3,4,5\). It checks counts, legal token slides, component sizes, degrees, edge totals and all-pairs breadth-first diameter. The second starts from pairwise-intersecting ground-edge families, constructs pairs of disjoint families, and enumerates all one-vertex replacements at \(n=5,6,7\). The resulting logs are `prism_direct.out` and `prism_check.out`. The actual script outputs were observed; they agree on the order-five graph.

Scope: exhaustive finite checks are not a substitute for the proof that works for every \(n\ge6\). Source searches cannot prove absolute historical priority. Independent audit has not been performed.
