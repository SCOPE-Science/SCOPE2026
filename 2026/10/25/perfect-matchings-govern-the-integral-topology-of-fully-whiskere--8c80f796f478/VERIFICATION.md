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

# Reproducibility checks

The standalone `whiskered_matching_check.py` executes with the Python standard library and prints JSON. The included `verification_output.json` is its actual output.

The finite independent checks establish: 190 verified directed acyclic face-poset matchings with perfect-base-matching critical simplices; 162 complete reduced homology computations over a field; 54 signed simplicial Lefschetz traces agreeing with the determinant-line prediction. These are finite validations only: the universal topological and integral claims follow from the written all-graphs proof. Endpoint-independence and integrality follow from explicit chain identities, rather than modular experiments.

No independent mathematical audit or human verification is asserted.
