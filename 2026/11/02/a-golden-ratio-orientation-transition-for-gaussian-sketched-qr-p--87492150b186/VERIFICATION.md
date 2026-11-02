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

# Verification and reproducibility

Run `python verify.py` using a standard Python 3 interpreter. The code uses only standard-library modules (`decimal`, `math`, `random`) and needs no external package.

The program independently checks the golden-ratio algebra at high decimal precision, the equality of two analytic expressions at the transition, the sharp upper bound over a grid of 14,007 orientations, a numerical integration of the independent exponential-density event in 16 parameter settings, and seeded Gaussian-sketch simulations for four spectra. It printed `VERIFY_OK 14027 deterministic bounds / integral / sampling checks` in the completed-package preparation. These finite verifications do not certify the universal result; the independent analytical proof is in `RESULT.md`.

The proof uses the exact distribution of an indefinite quadratic form of independent standard Gaussian rows, the exact \(\chi^2_2\) exponential law, and the derivative of a rational function on a closed interval. It does not require matrix dimension enumeration or a numerical limiting argument. The claim has not been independently audited, and no precision or finite-sample performance claim beyond the listed checks is made.
