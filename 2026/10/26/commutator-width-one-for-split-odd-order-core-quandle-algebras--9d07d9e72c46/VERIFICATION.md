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

The file `verify.py` is self-contained and uses only Python's standard library. Running `python3 verify.py` prints `VERIFY_OK` if and only if every diagnostic check passes. It verifies determinant edge assignments for sampled scalar cycles over five prime fields, constructs Fourier witnesses for split cyclic and product groups, and recomputes commutator coefficients in the original quandle basis instead of relying on the Fourier formula alone. The random generator is seeded and the script records cases/counts. These checks are finite tests; universal validity depends on the written proof and determinant-cycle lemma.

Exact domain: finite abelian group of odd order, field with invertible group order and full character splitting. No finite test is presented as an exhaustive verification over all parameters, and no independent audit or formal certification is claimed.
