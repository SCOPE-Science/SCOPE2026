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

# Reproducible finite checks and proof scope

Run `python3 verify.py` using standard-library Python 3. The checker enumerates all \(q^{2r^2}\) candidate block pairs \((A,C)\) for each declared finite-field case, filters on the defining equations, independently multiplies the full \(2r\)-square matrices, tests the square-zero and twisted-commutation identities, and compares every rank count to the closed formula. The exhaustive cases are \((q,r,\zeta)=(2,1,1),(2,2,1),(3,2,1),(3,2,2),(4,2,2),(4,2,3),(2,3,1)\). The field of four elements is represented as \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). The last printed line must be `TWISTED_SQZERO_MAXRANK_OK 7 complete block enumerations`.

The block form is derived in the paper and is mathematically exhaustive; the checker itself does not enumerate all \(q^{8r^2}\) unconstrained pairs of full matrices. The checks support, but do not replace, the exact proof of the formulas for all prime powers and positive \(r\). No independent review has been performed; publication priority is not certified.
