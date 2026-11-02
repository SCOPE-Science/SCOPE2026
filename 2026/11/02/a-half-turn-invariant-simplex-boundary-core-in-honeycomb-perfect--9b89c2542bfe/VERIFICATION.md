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

# Exact checks and limitations

The accompanying Python 3 file `check_honeycomb_core.py` reconstructs perfect-matching facets directly from the published plane-partition edge rules, verifies half-turn permutation of all facets, enumerates all simplices for \(n=2,3,4\), checks that the chosen \(n+1\)-vertex core is precisely \(\partial\Delta^n\), verifies that every non-core face is paired and that pairs never cross the core boundary, and checks the orientation parity formula. For \(n=2,3\), it also builds the entire relative directed Hasse graph and verifies acyclicity by topological sorting.

Expected output is:

```
n=2 facets=6 complex_faces=1347 core_faces=7 outside_pairs=670 half_turn_degree=-1 acyclicity_checked=True
n=3 facets=10 complex_faces=17487 core_faces=15 outside_pairs=8736 half_turn_degree=1 acyclicity_checked=True
n=4 facets=15 complex_faces=206127 core_faces=31 outside_pairs=103048 half_turn_degree=1 acyclicity_checked=False
HONEYCOMB_INVARIANT_SPHERE_CORE_CHECKS_OK
```

The `acyclicity_checked=False` field for \(n=4\) denotes an intentionally omitted *separate graph sort*, not failed acyclicity. For all \(n\ge2\), the theoretical acyclicity of the two-toggle matching is proved using the sequential matching theorem cited in RESULT.md. The finite enumeration alone does not establish the theorem for general \(n\). No independent validation has been performed.
