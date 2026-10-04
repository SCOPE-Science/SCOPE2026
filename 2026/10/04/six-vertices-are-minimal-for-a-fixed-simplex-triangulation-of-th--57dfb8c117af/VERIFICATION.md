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
The packaged checker is `artifacts/verify.py` and uses only the Python standard library.

It verifies that the four displayed complexes are connected closed triangulated two-manifolds with Euler characteristic two and cyclic vertex links. It then verifies the stellar-subdivision description of the successful six-vertex complex, the three explicit fixed-simplex-free automorphisms on the failed low-order types, every one of the \(6^6=46{,}656\) vertex maps of the successful six-vertex complex, and every vertex permutation of that complex.

Expected successful output:
`VERIFY_OK target_endomorphisms=6658 target_bad=0 automorphisms=4 sphere_types_le6=1,1,2 explicit_failures=3`

The enumeration establishes the finite claims about the displayed complexes. The proof of the sharp minimum also uses the symbolic reduction from fixed-simplex-free maps to nonzero-degree automorphisms and the complete structural classification of sphere triangulations through six vertices. No claim about larger vertex counts is inferred from the computation.
