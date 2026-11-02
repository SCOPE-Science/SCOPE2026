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

The exact symbolic verifier `verify_cycle.py` uses SymPy and runs with `python verify_cycle.py` after installing `requirements.txt`. It rebuilds the paired complex-polynomial numerators from the partial-fraction identity, proves the row-sum numerator identity, and checks four independently inverted exact rational matrices for every dimension from two to eight.

The verifier also evaluates exact Sturm variation pairs at zero and positive infinity, proves the stated number of positive roots, verifies rational root-isolation brackets, and confirms positive coefficients for the remaining polynomials. Observed output from the delivered source was `VERIFY_OK 188 exact assertions; dimensions 2..8; root intervals certified`.

The finite symbolic proof applies exactly to dimensions up to eight and all real nonnegative timesteps. Numerical root decimals are informative, not proof. No statement about larger dimensions, internal stages, nonuniform rates or numerical accuracy is verified. Independent mathematical audit has not been performed.
