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

# Reproducible verification

The theorem has an unrestricted analytic proof based on an exact tensor-product heat kernel and signed electrical currents. Its only nontrivial finite algebraic certificate is a rational-polynomial identity and a Sturm root count for a 24th-degree polynomial. The standalone `check.py` evaluates those identities exactly and verifies \(\gcd(F,F')=1\).

## Checks actually executed

From the package containing this file, run `python check.py` with SymPy 1.14.0. It constructs eight separate positively weighted Boolean cubes, forms the square-root-weighted signed incidence matrices, inverts their grounded Laplacians over the rationals, and checks *every* projection column and diagonal against the formulas (188 columns altogether). Graph checks include geometric ratios \(3/2\), \(2\), and \(10\), as well as non-geometric profiles. The checker separately recomputes the exact four-coordinate symbolic difference of cycle columns and proves the factorization by reducing it to zero.

For the polynomial phase count it forms the entire Sturm sequence using exact rational polynomial operations and verifies that the sign variations at \(1\), \(181/100\), \(183/100\), \(2\), \(321/100\), \(323/100\), \(4\), and positive infinity are respectively \(13,13,12,12,12,11,11,11\). The code confirms that the polynomial and its derivative are coprime and that the numerical phase witnesses give the asserted maximizing directions.

The successful execution printed:

`ANISOTROPIC_CUBE_EXACT_OK graphs=8 grounded_columns=188 sturm_variations=[13, 13, 12, 12, 12, 11, 11, 11] phase_roots=2`

## Limits of the checks

Exact finite graph reconstructions do not establish infinitely many conductance cases; the separate heat-kernel proof does. Sturm is a finite exact algebraic root-count procedure, not a floating-point extrapolation. The scientific argument does not determine the maximizing cycle direction for general dimension beyond the explicit finite maximum formula. No external independent mathematical audit has been performed.
