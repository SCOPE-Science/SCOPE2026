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

# Reproducibility and scope

Run `python3 check_translation.py` with Python 3. The program uses only the standard library. It explicitly constructs the Latin-square graphs and clique complexes for the cyclic groups of orders 5, 7, and 9 and the noncyclic group of order 9, enumerates all cliques and all translations, calculates the signed alternating face traces, and verifies the proposed character formula at each translation. It additionally constructs all boundary maps over the field of two elements, obtains their ranks by bit-vector elimination, and confirms the Betti ranks and character multiplicities.

Observed successful cases: `(5,)` had 25 vertices, 515 cliques and second Betti rank 64; `(7,)` had 49 vertices, 2863 cliques and rank 216; `(9,)` and `(3,3)` each had 81 vertices, 14283 cliques and rank 512. Exactly 236 translation traces and 236 multiplicity entries were checked across the four groups. The other positive-degree mod-two Betti ranks vanished for every case. This is a finite consistency test, not an exhaustive search of all odd groups or a proof of the unrestricted theorem.

For all group orders, the proof relies on the established all-field homology theorem for Latin-square clique complexes, the elementary no-intercalate argument for odd-order abelian group tables, the classification of invariant cliques, and the signed Lefschetz trace identity. The conclusion is a rational representation isomorphism, not an assertion about integral representation lattices or equivariant homotopy types.
