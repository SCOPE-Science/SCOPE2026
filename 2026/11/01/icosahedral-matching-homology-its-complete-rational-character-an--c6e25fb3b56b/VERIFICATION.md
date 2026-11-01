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

The two scripts are executable, standalone Python 3 sources, reconstructing rather than loading the simplicial complex. Execute `python3 verify_character.py` (requires `networkx`) and `python3 verify_torsion.py` (standard library only). The archived files `character_output.txt` and `torsion_output.txt` record the actual successful executions, which end with `VERIFY_CHARACTER_OK` and `VERIFY_TORSION_OK`.

The first program verifies 5,887 nonempty simplices, all augmented boundary ranks over the prime 1,000,003, all 120 graph automorphisms, the antipodal central involution, the entire eight-case character table, and the rational irreducible multiplicity calculations. The rational rank conclusion follows mathematically from the chain-complex saturation bounds in RESULT.md rather than treating one modular calculation as automatically equal to characteristic zero.

The second program independently uses an explicit edge list, computes all antipodal eigenspace boundary matrices over the prime three, and confirms that the unique degree-four mod-three homology class is antipodally odd. The action on the integral three-torsion subgroup then uses the natural universal coefficient sequence and the explicitly cited previously established integral homotopy theorem. That integral theorem is not rerun or independently audited in this package.

This is finite exact computation and a written mathematical argument; it is not independent certification, and it does not determine the entire integral automorphism lattice or exclude equivalent unindexed results.
