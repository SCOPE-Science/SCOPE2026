---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independent enumeration of unordered two-sums yields 15 fibers, six with two representations: three corner-pair versus doubled-midpoint fibers and three corner-plus-opposite-midpoint versus midpoint-pair fibers. Their extra terms have coefficients 4 and 8 respectively, on top of 2T² minus the sum of fourth powers. Completing squares gives the stated two-mass bound; Cauchy–Schwarz and AM–GM attain it at uniform positive magnitudes within each orbit, and equality for positive masses forces those magnitudes. The pure-orbit boundary is strictly suboptimal. The derivative in the ratio variable has exactly the stated cubic factor, with a single positive root; numerical substitution agrees with the printed values. At the optimum three necessary phase comparisons fix the affine-character form, which is also sufficient in every fiber. Modulo m,n ≥5 all two-sum fibers remain distinct; at (4,4) positive extremizing coefficients give a strict surplus from the (0,0), (4,0), (0,4) collision.

## originality

PASS

The strongest earlier result uses the identical support but fixes all six magnitudes at one. Its phase rigidity and nonaliasing grid transfer overlap, but neither gives the unrestricted constant, the nonflat optimizing ratio, nor the strict order-four excess at that constant. The inspected broader sources do not supply the missing optimization.

## value

PASS

This is the first quadratic simplex in two variables, a natural small test of exact Fourier synthesis bounds. The orbitwise equalization is not a consequence of symmetry alone; the result identifies the nonflat magnitudes that actually win over the phase-only optimum, and resolves all equality cases and the sharp square sampling cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
