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
# Verification

The symbolic proof classifies every dominating set of a connected chain graph by its boundary indices. The finite checker is auxiliary regression evidence, not an exhaustive proof of the infinite family.

`verify.py` constructs canonical chain graphs from twin-class sizes and compares the displayed formula with direct subset enumeration for every instance satisfying \(1\le p\le4\), \(\alpha_i,\beta_i\in\{1,2,3\}\), and total order at most \(11\). It additionally verifies the closed formula for \(D(G;1)\) and explicit \(K_2\) and star boundaries.

Expected successful output:

`VERIFY_OK graph_types=540 subset_checks=687124 coefficient_checks=5836 max_order=11`

Limits: no finite replay establishes the unrestricted theorem by itself; orders above \(11\) are covered by the proof, not by enumeration. The checker uses ordinary domination, where a selected vertex need not have a selected neighbor.
