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

The included `verify.py` runs under Python 3 with no dependencies beyond the standard library. Execute `python3 verify.py` alongside this file. It constructs the cyclic edge/triple hypergraph independently of the trace calculation and checks the exact blocked-orientation count against a directed-acyclicity test for every \(4\le n\le12\). It computes the full vertex coordinate and order-cone facet profiles from all \(n!\) coordinate permutations for \(4\le n\le8\), including all 24 orders in the dimension-four base case. It separately checks the all-dimensional symbolic-cover witness in each dimension \(5\le n\le40\). The expected terminal line is `ALL_CYCLE_POLYTOPE_CHECKS_PASS`.

The all-dimensional result is justified by the written proof, not by bounded iteration. No independent external audit has been performed.
