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

# Reproducibility and logical boundaries

Run `python verify.py` from the folder containing this file; no external Python libraries are required. The script validates the nonnegative four-cell algebraic certificate for 256 small integer quadruples and separately enumerates acyclic forests on weighted cycles (orders three through seven) and three cactus host topologies, checking 839 event-pair and marginal conditions, for 1,095 exact assertions in total. It uses rational fugacities and exact integer/rational products.

The proof of the infinite theorem does **not** depend on this enumeration. Its critical steps are (i) the factorization of the forest law over cactus blocks, (ii) the exact two-partition cycle covariance identity with nonnegative certificate, (iii) the positive-diagonal combinatorial lemma for two nontrivial bipartitions, and (iv) multiplication of local expectations along independent block paths. No statement is made for noncactus graphs or zero/infinite weights.
