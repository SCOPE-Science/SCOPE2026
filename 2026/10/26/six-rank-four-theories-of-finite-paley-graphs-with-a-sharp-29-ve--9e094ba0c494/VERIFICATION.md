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
# Reproducible checks

Run `python3 verify.py` with Python 3 and no dependencies. The direct finite-field constructions use the irreducible polynomial \(u^2-2\) for extensions of \(\mathbb F_3\) and \(\mathbb F_5\). The program verifies the six pairwise distinct recursive rank-four theories, truth values of five explicit rank-four sentences, normalized common-nonneighbor tables in orders 13 and 17, the diamond, clique and non-extension witnesses, and three-existential closure of the order-29 example. Recorded exact output: `verification_output.txt`.

The verification cannot establish Weil's character-sum bound for all prime powers; the manuscript proves that universal step mathematically. Independent scientific audit has not been performed.
