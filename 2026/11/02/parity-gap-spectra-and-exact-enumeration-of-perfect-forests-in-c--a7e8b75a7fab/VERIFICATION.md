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

# Verification of the perfect-forest enumerator

The adjacent `verify.py` contains a standalone Python 3 checker with no external dependencies.

Run `python3 verify.py`. In the recorded run its output began:

```
VERIFY_OK direct_graphs=19 edge_subsets=190798 support_pairs=180
```

The verifier performs three independent tests for each edge subset: acyclicity; odd selected degrees at every vertex; and inducedness of each connected component (all ambient edges internal to a component must be selected). It compares exact component-count dictionaries to the labelled-component recurrence and checks the claimed support on 180 further parameter pairs. Its direct tests total 190,798 edge subsets across 19 complete bipartite graphs. Examples include the distributions for \(K_{4,4}\), \(K_{5,5}\), and \(K_{6,6}\).

This check is finite and is not an infinite certificate. The main proof is a component classification followed by a labelled-set bijection and an explicit construction for each admissible component count. Independent external audit has not occurred.
