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

# Reproducible checks

With NumPy, SciPy and SymPy installed as specified in `requirements.txt`, run `python verify.py`. The script constructs the actual full matrices for each finite test, rather than relying on an imported or separately derived spectrum. It verifies the symbolic determinant of the reduced four-state matrix, the decoupled factorization, 720 full-matrix spectral comparisons, 21 onset/asymptotic comparisons, and three third-order Jordan/propagator checks. All tests passed on the bundled source at the time of this review.

The proof is supplied in `RESULT.md`; finite computations do not replace the general rank decomposition, exact characteristic polynomial, or limit argument. No external/infinite formal certification or independent audit has occurred. Possible earlier equivalences require further scholarly inspection.
