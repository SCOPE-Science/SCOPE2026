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

# Reproducing the integral homotopy classification

The graph has vertices `0..13` and undirected edges `(i,7+j)` exactly when `(i-j) % 7` belongs to `{0,1,3}`. All code uses only the Python standard library and contains its full dependencies.

Run from the directory containing these files:

```sh
python3 verify_morse.py
python3 verify_homology.py
```

`verify_morse.py` enumerates every one of the 16,383 nonempty subsets, rejects cycles by union/find, applies the degree constraint for each of the four stages, then constructs a deterministic coordinate-toggle matching on each full nonempty face poset. It checks all covering relations, that every matched edge is a face cover and used at most once, and that the directed graph obtained by reversing matched face-cover edges is a DAG. The exact number of matchings/critical cells is recorded in `morse_output.txt`. A complete acyclic matching gives a homotopy-equivalent Morse CW complex with only one zero-cell and cells of one higher dimension, proving the integral sphere-wedge homotopy types.

`verify_homology.py` independently checks the forest predicate by counting connected components and induced edges, enumerates the faces, forms each complete simplicial boundary matrix, and reduces over the field with two elements. Its complete boundary ranks are recorded in `homology_output.txt` and agree with the integral homotopy conclusions. Field calculations alone would not prove torsion-freeness; the complete acyclic matching supplies that stronger conclusion.

The barcode follows from dimension separation: all nonzero reduced groups at the four stages lie in four distinct dimensions, so the homology maps at strict stage transitions are zero. All stages are connected, and the filtration stabilizes when the maximum allowed degree reaches three.

This is a finite exact proof for the stated labeled graph only. Independent mathematical validation has not been performed.
