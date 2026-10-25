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

# Verification of the finite classification

The standalone `verify_chvatal_higher.py` defines all 24 edges, all twelve vertices, the admissible-face predicate, the deterministic pivot matching, the two specified dihedral generators, and complete finite checks. Execute it using the Python 3 standard library only.

Actual replay of the supplied script produced `CHVATAL_HIGHER_OK`, exactly 424 nonempty simplices with face vector `(12,66,148,142,52,4)`, 211 matched pairs, critical masks `16` (dimension zero) and `232` (dimension three), 1428 directed face-cover incidences, and a topological sort visiting all 424 faces. It exhaustively found eight graph automorphisms and verified generator characters `r: -1` and `s: +1`. Separate simplicial boundary-rank computations over the prime fields of orders 2, 3 and 101 reproduced unreduced homology ranks `(1,0,0,1,0,0)`.

The acyclic matching yields an integral homotopy theorem by Forman's theorem. Finite-field ranks alone do not establish integral torsion-freeness or the homotopy type, and the numerical tests do not claim anything about larger graph families. The homology action is not an equivariant homotopy classification.
