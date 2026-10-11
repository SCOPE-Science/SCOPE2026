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
# Finite exact verification

Run `python3 verify_icosahedral_character.py` (Python 3.9+, standard library only). Successful output starts `VERIFY_OK` and reports a face vector of `(12, 60, 120, 60, 12)`, boundary ranks `(11, 49, 48, 12)` both modulo two and modulo three, reduced mod-two Betti rank 23 in degree two, all 120 symmetry permutations, and the rational irreducible multiplicities described in `RESULT.md`.

The source independently rebuilds the graph from its six edge families, all faces from open neighborhoods, exact boundary columns, all graph automorphisms by partial-adjacency backtracking, the unique antipodal pairing, the 60-element order-five-generated rotation subgroup, and the signed trace of every automorphism on every chain degree. The table of class traces is compared to fixed expectations. Irreducible multiplicities follow by exact integer character inner products; no floating-point arithmetic or third-party packages are involved.

The finite checker establishes the exhaustive finite identities which, together with the standard universal-coefficient, Euler characteristic, Lefschetz, semisimplicity, and \(A_5\)-character-table arguments in `RESULT.md`, prove the rational module decomposition. It is not a computation of the integral equivariant lattice, a proof about other graphs, or an outside independent audit.
