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

The proof uses conditional uniformity after deleting a specified leaf, Cayley two-edge forest counts, and exact partition edge-pair combinatorics. Exact rational enumeration by the standalone program `verify_leaf_cut.py` independently checks every labeled tree of orders three through eight and every nontrivial predetermined cut size.

Run `python verify_leaf_cut.py` using Python 3 and its standard library. The successful local execution reports 280391 trees and 27 cut-size parameter cases. Finite checks are not proofs for arbitrary tree size; the analytic argument in RESULT.md is required. Full independent scientific auditing is not performed.
