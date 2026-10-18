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
# Verification scope

Run `python3 verify.py` with Python 3. The checker uses only standard-library rational and floating-point arithmetic. It checks an exact identity that connects the Dirichlet-polynomial recurrence to the decaying-tail representation, an exactly solvable positive bound state, numerical root monotonicity, the threshold, and the predicted exponential leading coefficient. The exact rational checks certify only the sampled algebraic instances. Numerical roots certify only finite test cases. The proof of the general claim rests on spectral reduction, resolvent monotonicity, and a uniform-derivative/mean-value limiting argument in `RESULT.md`.

The cited 2015 determinantal-polynomial article's abstract and bibliographic metadata were accessible, but its full text was not obtained. The 2015 ELA paper was read in full and compared by mathematical implication. The self-review does not constitute an independent audit or external validation.
