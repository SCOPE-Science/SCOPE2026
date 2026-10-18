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

# Reproduction and scope

Run `python verify_2conn_bipartite_outerplanar.py`, `python verify_independent.py`, and `python verify_family.py` in one directory. Python 3 and NetworkX are required for the independent graph-matcher implementation; the primary enumeration and the family checker use the standard library. The second program enumerates full graph automorphisms rather than reusing the primary program's dihedral-orbit routine. Compare standard output with `primary_output.txt`, `independent_output.txt`, and `family_output.txt`.

The two exact finite programs enumerate 1, 4, 21, 126 and 818 noncrossing bipartite polygon dissections (before isomorphism), yielding 1, 2, 4, 13 and 48 isomorphism types at even orders 4 through 12. Both find exactly one orbit-refinement failure at order 12, with diagonals (0,3) and (6,9) and colour/orbit sizes 4+8 versus 4+4+4. The group-theoretic proof explains exhaustiveness of canonicalization. The independent program's graph-isomorphism checks are separate from the primary dihedral implementation.

The family test exercises odd arc lengths 3 to 81, validating all observed colour counts, orbit counts, refinement depths and orbit sizes. These finite tests are checks, not certificates of the universal statement, which follows from the equitable distance-shell proof and chord-preserving automorphism classification.

No independent scientific audit, publication priority judgment, or external expert certification has been performed.
