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

The theorem is established by the bilinear-pencil and block-norm argument in RESULT.md. The calculations below are supplementary finite crosschecks, not the proof for all fields and orders.

Run `python checker.py` from the directory containing that file, with Python 3 and SymPy installed. Observed result:

```
VERIFY_OK {'base_blowups': 412, 'criterion_yes': 8, 'criterion_no': 404, 'singular_cases': 385, 'exact_witnesses': 6, 'pencil_test': 'pass', 'rational_cube_boundary': 'pass'}
```

The checker enumerates all connected simple graphs on 2–4 vertices with invertible adjacency and sizes \(1\) or \(2\) for each block; it checks algebra products for every constructed rational scalar witness, the determinant factorization for a \(6\)-dimensional triple-blowup, and the field cube boundary for complete bipartite graphs \(K_{2,3}\) and \(K_{1,8}\). The checker does **not** enumerate all invertible matrices or independently establish nonexistence of arbitrary non-diagonal isomorphisms; those exclusions follow from the universal determinant-factorization proof.

Proof-specific checks: the base adjacency is invertible, hence the vectors \(u_i\) are independent; distinct linear factors of the pencil determinant recover blocks and their dimensions; the all-ones block vectors have squared norm \(n_i\neq0\) in characteristic zero; even-walk connectedness yields one coefficient in the nonbipartite case and two in the bipartite case; direct substitution proves sufficiency. The fact that the degree-inverse random-walk multiplication is defined follows from connectedness and nonzero positive degrees in characteristic zero.

Scientific limits: no claim for characteristic \(p>0\), singular base adjacency, or unexamined historical literature. Independent audit has not been performed.
