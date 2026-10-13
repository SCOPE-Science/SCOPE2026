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
# Verification summary

The exact proof is in `RESULT.md`. A standalone finite cross-check is embedded at `verify_cycles.py`; it requires only Python 3 and the standard library.

Run `python3 verify_cycles.py` after extracting these package entries. A successful run prints:

`VERIFY_OK cycles=3..12 all_binary_subsets=8184 marginal_grid=101 exact_profiles_and_orbit_achievability=1`

The checker verifies each deterministically enumerated cyclic failure set in the declared finite range, cardinality-wise minima, equal-marginal symmetrization via rotations, and equality between the closed formula and all candidate two-cardinality interpolations on the rational test grid. This finite set of tests does not establish the theorem for larger networks or all real marginal probabilities. Those statements are established by the unrestricted convex-minorant, automorphism and boundary arguments in `RESULT.md`.

No independent audit has been performed. The published literature comparison remains subject to the specifically disclosed coverage risk.
