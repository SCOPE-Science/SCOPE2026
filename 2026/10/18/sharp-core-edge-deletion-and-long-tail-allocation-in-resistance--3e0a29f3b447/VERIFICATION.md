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

# Reproducibility and limits

Use Python 3 with `numpy` and `sympy` installed and execute `python verify.py` in a directory containing the embedded `verify.py`. On this run the program printed `PASS 7437 checks` after validating symbolic relations, prices on both sides of and at the threshold, three budgets, direct Laplacian spectra, and independently perturbed feasible conductance assignments. Every finite test is corroborating evidence only. The analytical derivation of the all-order and all-positive-real-parameter theorem is in `RESULT.md`.

No independent external audit has been performed.
