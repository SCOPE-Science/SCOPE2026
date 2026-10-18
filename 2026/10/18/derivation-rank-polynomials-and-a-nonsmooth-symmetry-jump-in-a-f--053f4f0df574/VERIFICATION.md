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

# Reproducible finite-field checks

Run `python3 check.py` using only Python's standard library. The checker enumerates all pairs of images of the two algebra generators for \(q=2,3,4\), constructs the corresponding linear maps from the Leibniz rule, verifies each basis-product identity, and counts operator ranks by elimination. It separately counts automorphisms by checking the defining square-zero relations and invertibility of the full four-dimensional substitution matrix. The reported counts are:

| Field size | Derivation ranks \(0,1,2,3\) | Automorphisms |
|---|---|---:|
| 2 | \((1,9,94,152)\) | 24 |
| 3 | \((1,8,54,18)\) | 72 |
| 4 | \((1,75,5748,59712)\) | 2880 |

All comparisons passed. The full theorem for arbitrary prime powers follows from the symbolic rank-and-trace counting and the coordinate-ring proof; no finite test is claimed as an exhaustive verification of infinitely many fields. The coordinate-ring argument, not the program, verifies group-scheme nonsmoothness. Independent audit has not been performed.
