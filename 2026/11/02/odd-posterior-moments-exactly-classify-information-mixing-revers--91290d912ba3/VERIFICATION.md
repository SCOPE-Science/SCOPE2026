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

# Finite verification and analytical limits

The accompanying `VERIFY.py` uses deterministic exact rational probability vectors, 75-digit standard-library Decimal logarithms and direct Cartesian-product enumeration. Reproduction command: `python3 VERIFY.py` in the package directory (Python 3.11 or later). No network access, additional packages or external data are needed.

The program verifies the exact binary example against both product Jensen–Shannon definitions and the closed logarithm, checks the common-margin correlation formula against the directly enumerated gap on 164 rational pairs, checks the centered posterior score and nonnegativity, verifies the binary sign-symmetry boundary and strictness for a rational grid, and tests the expected sixth-order coefficient for an explicit weak-contrast family. Its recorded output is in `VERIFICATION.log`: 1321 assertions passed.

The infinite identity is established analytically by the conditional-independence information formula, the bounded posterior kernel and a uniformly convergent Taylor series. Equalities use compact-support moment uniqueness. The numerical program does **not** independently prove convergence, full equality classification or the global theorem. Independent audit has not been performed.
