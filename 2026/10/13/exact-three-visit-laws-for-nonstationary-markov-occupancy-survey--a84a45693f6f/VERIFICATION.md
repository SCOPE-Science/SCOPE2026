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
# Exact verification

Run `python3 verify.py` with Python 3 and its standard library. The program uses `fractions.Fraction` throughout. It independently multiplies a binary Markov chain law conditioned on site occupancy, checks normalization and positivity, reconstructs all parameters from eight probability cells, and verifies the three defining feasibility equations. It tests 625 rational interior quadruples, a constructive two-visit alias with different occupancies, and a positive-law perturbation that violates a defining identity.

Actual output from the file in this package:

`VERIFY_OK exact_parameter_tuples= 625  two_visit_alias=1 three_visit_identification=1 feasibility_constraints=1`

The all-parameter proof is algebraic in `RESULT.md`; 625 checks are not claimed to exhaust the continuum. No finite-data inference accuracy, universal model fitness or independent audit was tested. Models with extra hidden local-detection errors, non-Markov memory, false positive records or boundary transition probabilities are outside this check.
