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

# Reproducible integral topology certificate

Run `python3 verify.py` in this directory using Python 3.9 or later; no package installation or network access is needed. The script deterministically reconstructs both Steiner triple systems and all their independence-complex faces. It checks pair uniqueness, the Pasch-trade legality and counts, facet dimensions, signed acyclic discrete-Morse matching, exact boundary minors and independent mod-two chain ranks. The printed `VERIFY_OK` means all of these assertions passed. An actual output record is included as `verification_output.txt`.

The cyclic matching leaves four dimension-three cells and sixteen dimension-four cells, with an integral full-rank four-by-four minor of determinant one. The switched matching leaves two dimension-three cells and nineteen dimension-four cells with an integral full-rank identity minor. The resulting homotopy classification also uses standard Hurewicz and Whitehead theorems as explicitly stated in `RESULT.md`; those infinite-dimensional general theorems are not replaced by finite experimentation. No generalized assertion is made for other Steiner-system orders.

The only representation assertion is the cyclic translation character, checked by enumerating fixed faces and deduced via the reduced Lefschetz formula and homology concentration. Neither the full automorphism group nor noncyclic-design characters are classified. Scientific review was conducted without independent external validation.
