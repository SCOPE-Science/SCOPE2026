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
# Reproducibility and verification

Run `python3 check_multiscale.py` using Python 3 with the standard library only. The program performs 341 exact-rational assertions: triangle-kernel integrals across an eight-by-eight length grid, symmetry and positivity checks, samplewise equality of the direct sliding-arc integral to its pair-kernel expansion for sample sizes 2–6, and exact positive pivots for a five-length covariance matrix. It prints `PASS: 341 exact rational checks; universal proof is analytical`.

The analytical argument in `RESULT.md` verifies arbitrary real arc lengths and every integer sample size at least 2, whereas these exact finite checks are auxiliary consistency tests. Nothing here represents an independent external audit.
