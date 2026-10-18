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

# Reproducible verification

Run `python3 verify_shelling.py` followed by `python3 verify_singular_torus.py`, using Python 3 and the standard library alone. Both programs operate on the explicitly defined sixteen-vertex graph and enumerate all faces. The first verifies a complete 80-facet shelling witness; the second evaluates reduced simplicial boundaries over both primes 2 and 3 for representatives of every dihedral face orbit, verifies triangle/edge/vertex membership of the doubled local homology locus and checks the oriented surface cycle over the integers.

The established pure-shellable-complex theorem gives torsion-free top-only link homology, which is necessary to infer integral local homology from the prime-field rank computations. The genus-one conclusion follows from explicit two-triangle-per-edge, six-cycle vertex-link, connectivity, orientability, and Euler characteristic computations. These programs check a finite, exhaustive certificate for the fixed graph; they do not establish general claims for other graphs, and no independent scientific audit has been performed.
