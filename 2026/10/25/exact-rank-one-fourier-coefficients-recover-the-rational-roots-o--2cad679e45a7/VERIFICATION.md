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

# Verification and limitations

Execute `python3 check_rankone.py` with a standard Python 3 interpreter. This checks exactly, in cyclotomic integer coordinates, each squarefree characteristic-polynomial fibre and each nonzero rank-one frequency with first column vector fixed to a basis vector over prime fields in dimensions \((q,n)=(2,3),(3,2),(5,2)\). Conjugation invariance makes the fixed-vector check representative of all such vectors in these finite examples. The recorded final output is `CERTIFICATE_OK total_probes=556`, with per-case counts 28, 48, and 480.

The infinite-field-family theorem is not deduced from these checks. Its proof follows from transitivity of the vector stabilizer, exact eigenvector double-counting for squarefree characteristic polynomials, and finite-field additive character orthogonality. The script is not an independent proof or independent audit. No nonsquarefree or higher-rank formula is claimed.
