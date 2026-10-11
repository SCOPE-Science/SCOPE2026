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
# Verification

The proof-critical algebra is reproduced by `verify.py` using exact arithmetic in \(\mathbb Q(\sqrt2)\). The checker verifies the three equality/contact equations, expands the claimed factorization of \(1-Q_*\) coefficient-by-coefficient, and confirms that the residual quadratic has discriminant \(-1\). It then samples \(20001\) angles only as an additional numerical sanity check.

Expected replay output:

`VERIFY_OK exact_factorization=1 contacts=3 discriminant=-1 grid=20001 max_abs=1.000000000000000`

The dense grid is not an exhaustive proof and is not used as one. Global nonnegativity follows from the exact factorization and the sign of its factors on \([-1,1]\). The result does not assert any discretized-grid analogue.
