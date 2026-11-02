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

# Reproducibility and limits

Run `python3 verify.py` with standard Python. The checker computes an exact derivation system in the original \(e_i\)-basis of the dihedral quandle algebra, comparing rank against the asserted kernel dimension for \(p=3,5,7,11,17\). For \(p=3,5,7,11,17,31\), it tests the complete Leibniz identity for each predicted basis derivation on each ordered pair of truncated monomials, and tests commutators for every pair of predicted basis derivations. The positive marker is `MODULAR_QUANDLE_DERIVATION_OK`.

Checks use prime-field arithmetic and do not enumerate derivations of the full linear space at \(p=31\). The theorem is over **all** characteristic-\(p\) fields, and its universal validity rests on the explicit uniqueness proof in `RESULT.md`, not the finite sample of exact computations. The code performs no mathematical audit by an independent party.
