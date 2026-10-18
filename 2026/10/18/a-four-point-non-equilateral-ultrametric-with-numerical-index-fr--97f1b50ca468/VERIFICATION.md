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

# Exact reproducibility

From this result folder execute `python3 artifacts/verify.py`. The checker uses only Python standard-library rational arithmetic. Its actual verified output was:

`VERIFY_OK vertices=18 supporting=56 objectives=216 bound=2 radius=1 norm=2`

The program independently enumerates the exact dual unit-ball vertices, rebuilds signed supporting tensor rows, checks each of the 216 rational nonnegative certificates coefficient by coefficient with coefficient sum at most two, and verifies the sharp diagonal operator has operator norm two and numerical radius one. The finite polyhedral reduction in RESULT.md is the argument extending this exhaustive rational check to every linear operator on the fixed three-dimensional space. This proof does not cover other short-edge distances, other metric spaces, or complex scalars. No independent mathematical audit has been performed.
