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

# Reproducibility and verification

Run `python verify.py` from the directory containing the standalone checker. No nonstandard Python packages are needed. The checker constructs the graph neighborhoods directly from ordered nonempty part-size profiles. For every profile, it enumerates all subsets and computes both approximations from the same reflexive symmetric neighborhood relation; separately constructs the claimed exact family of rough pairs; builds the induced coordinatewise poset; verifies every meet and join exists uniquely; checks modularity, distributivity, and the order-reversing complement swap.

Observed output:

```text
VERIFY_OK multipartite_profiles= 134  all_rough_pairs=PASS coordinate_order_lattice=PASS self_duality=PASS modular_distributive_boundaries=PASS
```

The finite search ranges over all ordered multipartite part profiles of total vertex count between two and seven, and selected profiles with eight vertices. It is an independent cross-check of the exact formulas and lattice-identity classifications within that range, not an exhaustive proof for unbounded parameters. The all-profile proof is given in `RESULT.md`. The group decomposition and inverse classification are proved there by the connected components of the comparability graph of the interior of the Boolean horizontal sum; the checker does not enumerate these potentially large permutation groups.

Independent external assessment: not performed.
