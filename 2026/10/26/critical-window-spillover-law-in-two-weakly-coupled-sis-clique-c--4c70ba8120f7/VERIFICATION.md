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

# Reproduction and scope

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses exact `Fraction` coefficients and 72-digit `Decimal` bisection without network access. It checks 53 rational Taylor identities and 15 asymptotic spot comparisons and prints `PASS: 53 exact coefficient identities and 15 numerical asymptotic comparisons`.

The finite checks reproduce exact coefficients and small-parameter instances; they do not replace the existence, uniqueness, global-convergence or asymptotic proofs in `RESULT.md`. The positive fixed point is a deterministic mean-field endemic solution, not an invariant probability measure for a finite stochastic absorbing epidemic. No independent audit has been performed.
