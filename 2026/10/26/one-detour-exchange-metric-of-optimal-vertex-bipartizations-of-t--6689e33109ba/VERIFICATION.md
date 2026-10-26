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

Run `python verify_a.py > check_a.json` and `python verify_b.py > check_b.json` using Python 3.10 or later. Check byte-exact agreement of those outputs with the included `verify_a.json` and `verify_b.json`, respectively. Both checks completed successfully at preparation time. Both programs assert their own complete tests; the independent LCF representation includes a checked vertex-isomorphism to the stated generalized Petersen graph.

The certified finite domain is 20 graph vertices, all deletion masks through size six, all 3,240 optimum masks and all 10,497,600 ordered pairs. BFS from every state is exact for unit-length exchanges. The crosscheck shares the mathematical specification but not the enumeration or adjacency-construction algorithm; agreement is supporting evidence, not an independent external audit. Other graph orders and unpublished parallel analyses are not verified.
