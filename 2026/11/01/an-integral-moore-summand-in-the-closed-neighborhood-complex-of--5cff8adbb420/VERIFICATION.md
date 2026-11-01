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

# Reproduction and limits

The file `verify.py` is a standalone exact checker. From a Python environment with `sympy` installed (compatible version stated in `requirements.txt`), run:

```bash
python verify.py
```

It reconstructs the 13 Paley closed neighborhoods directly from quadratic residues modulo 13, enumerates all 1,171 faces, and performs a deterministic vertex-toggle matching with 579 pairs. It orients every incidence in the complete face-poset Hasse graph, verifies acyclicity with a complete topological sort, computes the full signed integral 6-by-7 Morse differential and its exact Smith diagonal, and independently calculates original augmented simplicial boundary ranks over three prime fields.

Expected terminal output includes:

```text
FACES_OK (1, 13, 78, 286, 416, 273, 91, 13)
MATCHING_OK 579 critical {'two': 6, 'three': 7}
ACYCLIC_OK 1171 4693
INTEGRAL_MORSE_OK [1, 1, 1, 1, 2, 0]
RAW_FIELD_HOMOLOGY_OK {2: (2, 3), 3: (1, 2), 5: (1, 2)}
HOMOTOPY_OK Moore(Z/2,2) wedge S2 wedge 2*S3
ALL_VERIFY_OK
```

The checker establishes the finite combinatorial and integral chain data. The additional mathematical step upgrading those data to a homotopy equivalence is given in `RESULT.md`: the Morse CW two-skeleton is simply connected and is a wedge of two-spheres, so cellular attaching maps from two-spheres are classified by their degree vectors. An integral Smith reduction therefore represents elementary cell changes, giving a Moore space together with the indicated spheres.

The finite-field calculations alone cannot exclude other torsion or determine homotopy. The exact integral differential and topological attaching-map analysis are essential. No infinite-family theorem, equivariant classification or independent external audit is asserted.
