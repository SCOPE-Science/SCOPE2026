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

The included `check_hamming.py` is a self-contained Python-standard-library exact-rational verification program. It constructs the full vertex and edge sets of nine Hamming graphs, assembles the reduced graph Laplacian, inverts it over rational numbers, forms both complete projection matrices, and checks norm formulas, diagonal entries, matrix symmetries, idempotence, and zero divergence. A completed replay reported `CHECK_OK 88858 exact-rational assertions across 9 finite cases`. Its enumeration ranges from \(H(1,3)\) through \(H(4,2)\) and includes \(H(2,5)\) and \(H(3,3)\).

The main theorem requires arbitrary integers \(d\ge2,q\ge3\); finite checking cannot prove it. The analytical argument in RESULT.md supplies the missing universal quantifiers by symmetry averaging and the exact product-heat-kernel integral. The binary and one-coordinate cases are calibration only, not asserted as novel. No external audit or independent validation has been carried out.
