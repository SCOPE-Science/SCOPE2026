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

The accompanying `verify.py` uses only the Python standard library. Invoke `python3 verify.py` from a directory containing the file.

It independently constructs all permutation models for dimensions 3, 4, and 5; builds one-round and iterative rule systems; compares both with the direct model-intersection closure on all 64 possible inputs of dimension 3, all 4096 inputs of dimension 4, and 1024 deterministic sampled inputs in dimension 5. It also checks the worst-case directed-cycle round bound for dimensions 3 through 8. The enumeration establishes only the indicated finite instances, not the all-parameter theorem. The general result follows from the separate directed reachability, lower-bound and doubling arguments in `RESULT.md`.

Expected terminal marker: `VERIFY_OK exact_closure=PASS optimal_basis_counts=PASS direct_one_round=PASS logarithmic_depth=PASS`.
