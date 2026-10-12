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

# Reproduction and verification

Run `python3 verify.py` in an environment with NumPy and SymPy. The verification file uses 3,240 exact rational input/horizon checks, 900 direct orthogonal-polar-factor iterations, 16 attaining parameter instances, and symbolic factorization of the derivative and minimum. Observed outputs: `SYMBOLIC_OK` and `VERIFY_OK 3240 exact rational checks; 900 independent polar-SVD repetitions; equality for 16 horizons`. The proof of all positive real parameters and all positive integer horizons is analytic and recorded in RESULT.md; the script is a finite consistency test, not an infinite certificate. No independent audit has been carried out.
