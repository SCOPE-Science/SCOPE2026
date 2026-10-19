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
# Verification and scope

Run `python3 verify.py` in the package directory (standard Python 3, no external dependencies). The script enumerates 4096 directed, four-vertex, pair-parent hyperedge masks and every subset support, validates the greatest Boolean fixed point and existence of half-density subsolutions when the common infection multiplier is 4 and recovery is 1, and numerically checks a multi-layer no-core five-vertex example against the derived explicit decay bound.

The checker uses exact representable quarters for its subsolution test. The mathematical proof, not enumeration, establishes the result for every finite vertex set and all positive weights, recoveries and allowable steps. No claim is made about stability of a nonzero equilibrium, global convergence when the core is nonempty, or finite stochastic epidemic extinction times.
