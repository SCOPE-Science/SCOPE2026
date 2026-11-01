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

Run `python3 verify.py` with Python 3.9 or later; no third-party dependencies. The executable constructs all directed matching-pair vertices for the friendship graph, enumerates the complete set of vertex filtrations for the first four cases, computes the induced full strong matching complex, and compares every face against the independent join-plus-cones construction. It also forms the mod-two simplicial boundary matrices directly and computes their ranks.

Observed successful output:

```text
EXHAUSTIVE_OK m= 1 vertex_orders= 6 directed_pairs= 6 faces= 6 f_vector= (6,) reduced_mod2_betti= [5]
EXHAUSTIVE_OK m= 2 vertex_orders= 120 directed_pairs= 12 faces= 36 f_vector= (12, 24) reduced_mod2_betti= [0, 13]
EXHAUSTIVE_OK m= 3 vertex_orders= 5040 directed_pairs= 18 faces= 178 f_vector= (18, 72, 88) reduced_mod2_betti= [0, 0, 33]
EXHAUSTIVE_OK m= 4 vertex_orders= 362880 directed_pairs= 24 faces= 840 f_vector= (24, 144, 352, 320) reduced_mod2_betti= [0, 0, 0, 89]
ALL_VERIFY_OK
```

These are exhaustive checks only for those four finite instances. The universal integral homotopy statement depends on the separately reconstructed symbolic proof in `RESULT.md`, in particular the exact facet classification and the explicit nullhomotopies of the cone bases. Mod-two Betti ranks alone would not establish the integral homotopy equivalence. Independent mathematical audit has not been performed.
