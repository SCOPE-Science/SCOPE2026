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

# Reproducibility and limits

Invoke `python3 tree_hypercube_checker.py` using the bundled standalone file. It imports only Python standard-library modules and checks 16 labelled trees and 27 integer nodes per tree, reconstructing all normalized simplex determinants directly. It reports `TREE_HYPERCUBE_OK trees=16 grid_per_tree=27 subsets=4368 nonzero=3008` when all exact assertions hold. The proof supplies independent evenness and degree bounds, allowing interpolation from the grid to a genuine identity for all real parameters; the finite checker alone cannot certify properties of arbitrary real weights without that argument. Differentiation proves strict correlation monotonicity. No formal proof-assistant check or independent external scientific audit was carried out.
