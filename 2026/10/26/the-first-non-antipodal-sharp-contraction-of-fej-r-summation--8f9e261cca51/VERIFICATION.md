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

The proof uses exact polynomial factorization, exact antiderivatives, and exact Bernstein-basis sign coefficients. The accompanying standard-library `CHECK.py` was executed and returned `CHECK_OK c=0.338107185334656 angle=2.451782841069228 delta=0.883882377829197`.

The checker reproduces rational sign certificates and the algebraic root numerical enclosure. Its midpoint quadratures independently corroborate several kernel separations, but no finite sampling of shifts certifies the universal supremum; the analytic three-branch argument in `RESULT.md` does that. Results apply to real oscillation for Fejér orders two through four. No independent audit is claimed.
