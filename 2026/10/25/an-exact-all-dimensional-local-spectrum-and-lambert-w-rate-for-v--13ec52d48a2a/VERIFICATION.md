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

Execute `python check_polycd_spectrum.py` with the versions specified in `requirements.txt` or compatible NumPy and SymPy. It checks the exact characteristic polynomials for integers \(3\le n\le8\), two exact small-dimensional characteristic polynomials, numerical spectral radii for dimensions \(3,4,6,10,20,40\), and 70 independent finite-difference comparisons with an actual nonlinear PolyCDwA simplex sweep. This verifier was executed and printed `VERIFY_OK exact characteristic polynomials n=3..8 and 70 nonlinear differential checks`.

The symbolic and numerical checks do **not** establish the formula for all integers, simplicity in arbitrary dimension, the tight local linear rate or the Lambert-W limit; those follow from the full proof in `RESULT.md`. The rate does not claim every starting perturbation realizes the maximal eigendirection. Independent audit remains unperformed.
