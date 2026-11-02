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

# Reproducible verification and limits

Run `python3 verify_fermat.py` from the directory containing this file and the verifier. The program uses only the Python standard library. A successful run prints:

`FERMAT_CUBIC_FOURFOLD_HEXACODE_405_486_MOD4_AND_INCIDENCE_EXACT_PASS`

It performs exhaustive finite coordinate enumeration of the \(405\) paired planes and \(486\) hexacode monomial images over \(\mathbb F_4\), confirms their Hermitian isotropy and nonoverlap, verifies all four refined intersection distributions, computes rank-nine tangent matrices at both representatives, and checks the entire coefficient identity \(4(u^3+v^3+w^3)+18uvw\) inside \(\mathbb Z[\zeta]/(\zeta^2+\zeta+1)\). It separately checks the isotropic-point counts entering the geometric enumeration of \(891\) planes.

The code does **not** replace the mathematical arguments for algebraic-closure descent, exhaustive classification of maximal isotropic planes, generic-fiber completeness, formal implicit-function elimination over the dyadic ring, or global proper quasi-finite decomposition. These are proved in `RESULT.md`. No independent external audit or validation has been performed.
