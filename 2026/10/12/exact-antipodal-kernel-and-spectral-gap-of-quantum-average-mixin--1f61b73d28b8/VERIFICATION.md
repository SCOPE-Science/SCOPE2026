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

Run `python3 verify.py` in the directory containing this file. The verifier uses only the Python standard library and exact integer/rational arithmetic. It reconstructs halved-cube vertices and every distance-two adjacency action, groups characters by exact adjacency energy, constructs the Schur-square mixing kernel, and transforms the result back to exact mixing eigenvalues. It separately checks the antipodal symmetry of the kernel, the rank, and the exact minimal positive eigenvalue, and evaluates binomial overlap formulas without enumerating exponentially many arbitrary-dimensional bitstrings.

Observed output on the enclosed verifier:

`VERIFY_OK exact_graph_dimensions=3..10 adjacency_identities=349520 character_modes=1020 binomial_cross_checks=165 d6_rank=16/32 d8_rank=64/128`

The sampled dimensions include odd-dimensional sanity cases and the previously known dimension-four boundary, but the scientific claim concerns even dimensions at least six. Exact arithmetic eliminates numerical-tolerance errors in these finite checks. They are **not** an exhaustive verification of all dimensions; that follows only from the argument in `RESULT.md`. No third-party or independent audit was performed.
