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

Run `python verify.py` with `sympy==1.14.0` installed as recorded in `requirements.txt`. The checker constructs the five Weyl reflection matrices, enumerates the 1920 distinct elements, classifies eighteen conjugacy classes, computes the integral fixed lattices via elementary unimodular transformations, determines the torsion Smith factors of all line-orbit trace maps and enumerates all arithmetic effective and nef cone extremal rays using rational hyperplane intersections. It verifies the entire eighteen-row invariant table against an embedded fingerprint, including the uniqueness of index \(16\).

An additional exact pass over all eighteen saved trace matrices recomputed the Smith invariant factors directly and confirmed the index multiset \(\{1^{12},2^3,4^2,16\}\). This verifies the internal finite computation; the general theorem still uses classical del Pezzo geometry, integral descent and finite-field Brauer vanishing. An exhaustive finite group computation is not a proof that no equivalent result was previously published, nor is it an independent audit.
