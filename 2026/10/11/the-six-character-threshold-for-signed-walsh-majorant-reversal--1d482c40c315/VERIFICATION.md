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

The proof uses characteristic-two affine dependencies, exact enumeration of canonical sign polynomials, Walsh orthogonality, and a convex-chord bound. These steps establish the result for every dimension, rather than extrapolating from tests.

Standalone reproducibility: execute `python checker.py` with a standard Python 3 interpreter. This was actually run and passed all assertions. It exhausts 255 nonempty supports and all signings in the three-bit cube; 1,941 nonempty zero-containing supports of sizes at most five in the four-bit cube and their normalized signings; and all 3,003 zero-containing six-point supports with 32 normalized signings each. It verifies the six-circuit criterion, 168 reversing support masks, 2,688 reversing normalized signings, and exact normalized moments \(21\) and \(24\). Arithmetic uses integers throughout (the cube-wide expectation is applied only after integer accumulation).

Checks do not address unrestricted coefficient magnitudes, arbitrary complex phases, or higher exponents. The program is finite corroboration of, not an alternative to, the general algebraic argument. Independent external audit has not been performed.
