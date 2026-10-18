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

Run `python3 verify_cograph_cr.py` in Python 3 with no nonstandard packages. The verifier enumerates unique reduced cotrees, builds exact adjacency bitmasks, assigns colour signatures globally across the graph population, and checks all assert statements for orders \(1\) through \(12\). Successful output prints `NAMED_WITNESSES_VERIFIED`, terminates in `CENSUS_VERIFIED`, and explicitly prints the degrees and complement-component multisets of the three threshold pairs.

The execution checks the entire enumerated finite domain rather than a random sample. Cotree uniqueness and the finite colour-refinement stabilization argument, described in `RESULT.md`, connect the computation to the mathematical claim. The published connected-cograph population counts provide an independent count cross-check but not an independent audit of the complete collision classification.

No external independent validation or audit has been performed. The result does not extend beyond \(12\) vertices, and unseen literature remains a residual novelty risk.
