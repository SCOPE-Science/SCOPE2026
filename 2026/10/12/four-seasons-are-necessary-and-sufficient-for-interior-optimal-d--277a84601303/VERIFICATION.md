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

Run `python verify_mixing.py` with a standard Python 3 interpreter in the directory containing this file and the checker. The script uses `fractions.Fraction` and `itertools` from the standard library only. It performs 750 exact-rational identity and endpoint-characteristic checks for two- and three-phase fitness profiles and computes a separate exact four-phase strict witness at \(d=24/25\). Successful output is:

`VERIFY_OK exact_traces_determinants_endpoint_characteristic=750 witness_negative_polynomial=1`

The code does not enumerate an infinite parameter family and its sample grid is not an exhaustive proof. The universal statement is justified by the characteristic-polynomial inequalities in `RESULT.md`; the exact rational witness provides a sufficient counterexample at four phases. The spectral radius is the principal eigenvalue of the product of the four seasonal 2-by-2 nonnegative matrices. Independent replication or external audit has not been performed.
