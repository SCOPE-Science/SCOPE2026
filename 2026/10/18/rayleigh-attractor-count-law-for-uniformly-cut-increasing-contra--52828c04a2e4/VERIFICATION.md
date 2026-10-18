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

# Verification

The packaged `verify.py` is executable with Python's standard library. Running `python verify.py` prints `VERIFY_OK` after exact exhaustive enumeration of all multinomial occupancy vectors for every integer from 2 through 8, comparison of every falling-factorial moment against the independent positive-composition formula, and checking the all-fixed maximal event.

These checks are finite demonstrations. The proof for all branch counts depends instead on strict monotonicity, the exact multinomial identity, uniform Stirling estimates, the integrable Dirichlet simplex limit, and moment determinacy of the Rayleigh law as supplied in `RESULT.md`. No external or independent audit has been performed.
