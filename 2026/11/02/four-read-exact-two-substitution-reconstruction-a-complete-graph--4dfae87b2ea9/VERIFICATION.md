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

Both independent finite verifiers use only the Python 3 standard library:

```
python3 verify_spheres.py
python3 verify_graphs.py
```

`verify_spheres.py` represents each radius-two sphere as an arbitrary-precision integer bitset. For every unordered quartet of distinct weight-two error words at each length \(5\) through \(9\), it checks that the intersection contains only the zero source, and it tallies the count and the exceptional length-five stars. This is a direct implementation of the original distance definition, without relying on graph classification.

`verify_graphs.py` independently enumerates all unordered quartets of graph edges. It checks the necessary-and-sufficient structural criterion from the proof (at least five active vertices and no exact two-vertex transversal), and verifies both the closed-form counts and their decomposition by incident-vertex cardinality.

Both outputs are preserved as `verification_spheres.txt` and `verification_graphs.txt`. Their numerical counts for lengths \(5,6,7,8,9\) are \(15,240,1785,8225,28665\). These tests establish the stated finite cases exhaustively; the all-length claim is supported by the separate combinatorial proof and not by a finite extrapolation.

The published exact-error and at-most-error sources concern related but different reconstruction conditions. They do not constitute independent mathematical validation of the new classification. Independent audit is not yet performed.
