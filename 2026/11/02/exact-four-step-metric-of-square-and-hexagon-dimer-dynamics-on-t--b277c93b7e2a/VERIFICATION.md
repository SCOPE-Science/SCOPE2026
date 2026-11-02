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

From the same directory as the three complete supplied files, run:

```
python3 verify_cycle.py certificate.json
python3 verify_bipartite.py certificate.json
```

Both programs use only the Python standard library. The first recomputes every perfect matching, all simple 4- and 6-cycles, legal flips and all-source BFS distances from first principles, then reconstructs `certificate.json` byte-for-byte. The second independently generates perfect matchings through even-to-odd bipartite assignments, computes legality from all matching-pair symmetric differences, and conducts independent all-source BFSs. The tests check full adjacency equality, 272 states, 768 four-cycle edges, 1,216 six-cycle edges, connectedness, eccentricity four at every state, and unordered pair distances 1,984/10,784/19,568/4,520.

These are finite exhaustive computer-assisted mathematical checks. They establish no general formula for larger hypercubes. Literature searches and these two implementations are not an independent scholarly audit.
