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

# Verification procedure

The exact source is the included `compute_dimensions.py`; its `SHATTERING_TREES.json` records twelve complete depth-optimal binary query trees, each with a leaf permutation index. The separate `verify_certificates.py` reconstructs all permissible permutations from independent rank-standardization logic, checks every query-answer history against the indicated leaf permutation, confirms distinct witnesses, and independently recomputes nonexistence of depth one greater. Execute `python3 verify_certificates.py` in the directory containing all three files. `verification_output.txt` is the output of that invocation against the packaged files; it is not itself an independent proof. The implementation's exhaustive recurrence and the leaf assertions are the finite mathematical certificates.

The final line of the actual check was:

`PATTERN_CLASS_WITNESS_CHECKS_PASS 12 1596 1608 32941`

The largest nontrivial upper-depth search involved 31,849 states, for eight symbols and forbidden pattern \(132\). For \(n=1,2\), the dimensions are elementary. For larger \(n\), no finite-experiment-based inference is made. The static VC dimension for every \(n\) has an independent mathematical proof in `RESULT.md`.
