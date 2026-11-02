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

# Verification evidence and limits

Run `python verify_census.py` with Python 3 and SymPy. Observed: `CENSUS_OK 279 78 10920 73 75`.

Run `python verify_independent.py` after generating `quartic_joint_census.csv`. Observed: `INDEPENDENT_OK 78 full_profiles 546 extended_examples 4`.

The first script enumerates all 32767 binary quartic equations modulo the exact 168-element projective group and tests algebraic-closure smoothness by three Gröbner ideal-unit conditions. It counts all 78 representatives over extensions of degrees 1, 2 and 3, and enumerates their seven rational line restrictions. The second implements different finite-field arithmetic and line evaluation, reproducing all signatures and extended point counts for the four witnesses through degree 6. A companion CSV provides every input mask and computed invariant. These are deterministic, exact computations, not approximate numerical tests. Independent external auditing was not performed.
