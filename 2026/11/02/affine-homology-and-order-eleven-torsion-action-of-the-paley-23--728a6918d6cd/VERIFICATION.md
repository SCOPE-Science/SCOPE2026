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

Execute `python paley23_equivariant_check.py` from the same directory, with Python 3.10 or newer and SymPy. Expected exact output includes `PAL23_AFFINE_FREE_MODULES_AND_23_TORSION_CHARACTER_OK`.

The program checks the exact quadratic-residue tournament, all 5,589 nonempty faces, the 2,681-pair acyclic matching, 22,011 face incidences, the integer Smith invariant factors \(1\) (78 times) and \(23\) (once), and signed invariant subcomplex ranks under the 23 translations, 11 multipliers, and all 253 affine transformations. It additionally computes each order-eleven eigenspace over \(\mathbb F_{23}\), finding a unique torsion-related jump at eigenvalue 12.

The program supplies complete finite enumeration and integer arithmetic; the interpretation as an equivariant torsion character uses the exact universal coefficient theorem, prime-to-23 semisimplicity of \(C_{11}\), and the rational representation decomposition established in `RESULT.md`. This verifies no claim about other tournaments, integral quotient homology, or an equivariant homotopy equivalence.
