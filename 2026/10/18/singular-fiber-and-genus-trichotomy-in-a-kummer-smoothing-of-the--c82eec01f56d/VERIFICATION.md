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

The mathematical proof is in `RESULT.md`. The associated `verify_ceva_pencil.py` is reproducible with Python 3 and SymPy installed; it checks the exact rational identities for the critical locus of the cubic quotient, the exceptional cubic node and Hessian, and the Gröbner-elimination parameter factor. The checker also enumerates all projective points over the finite field of order 13 for exponents two and three at four distinct parameter values. Executing this exact script returned `VERIFY_OK`.

The finite-field checks do not imply a characteristic-zero infinite-family theorem. Integrality for every exponent is established by the valuation/Kummer argument, and genus by the plane-curve delta formula, independently of the finite experiments. No independent audit or external validation has been conducted.
