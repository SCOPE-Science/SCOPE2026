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

# Verification of arithmetic spectral and information formulas

The exact proof in `RESULT.md` establishes all bases and resolutions without relying on exhaustive computation. The standalone `check_arithmetic_binning.py` runs with Python 3 and SymPy; execute it from the containing directory with `python check_arithmetic_binning.py`.

The verifier uses exact rational intersections for 7,100 joint-probability cells, checks exact total variation and chi-square formulas, and obtains 44 complete matrix characteristic polynomials by SymPy symbolic determinants compared with the divisor-order expression. Fourier-character cycle products and the information-asymptotic coefficients in the 7-bin example are also checked.

Observed output: `VERIFY_OK direct_cells= 7100 ; exact_characteristic_polynomials= 44 ; Fourier_cycles=verified; periodic_limits=verified`.

The finite test ranges are not an exhaustive demonstration for arbitrarily large integer parameters. The nonstandard proof steps needed for the general statement are residue enumeration, Fourier-cycle telescoping, and the entropy expansion. Those steps are supplied algebraically in `RESULT.md`. Independent audit has not been performed.
