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

# Reproducibility

Run `python3 klein_q9_certificate.py` using Python 3 and no external packages. The run checks a primitive quotient-field multiplication table, enumerates all 605242 RREF two-planes, tests all four coefficients of the cubic restriction, and computes the full exact graph by Gaussian elimination over nine field elements. The observed output was:

```
RREF_Grassmannian=605242
contained_F9_lines=82
F9_incidence_edges=350
F9_degree_distribution=[(4, 5), (6, 20), (8, 15), (10, 32), (12, 10)]
F9_incidence_triangles=190
F9_incidence_graph_connected=True
F3_fixed_lines=10; induced_graph=C5_disjoint_union_5K1
C5_coordinate_shift_fixed_F9_lines=2; swapped_by_Frobenius=True; disjoint=True; degree=10
VERIFY_OK
```

**Checks actually performed:** Complete deterministic field/RREF exhaustion; all exact line-containment coefficients; exact adjacency and triangle census; connectedness; Frobenius and cyclic coordinate-action checks, including automorphism preservation of the full graph. Mathematical verification of the semisimple representation lemma is given in RESULT.md.

**Unproved scope:** The calculations certify this finite graph only; they do not prove any statement about every finite extension or preclude every unpublished equivalent incidence table. Independent audit and independent validation have not been performed.
