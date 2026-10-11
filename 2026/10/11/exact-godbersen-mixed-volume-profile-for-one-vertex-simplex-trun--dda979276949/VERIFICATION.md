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

# Verification of the exact simplex-truncation mixed-volume profile

The analytic proof consists of the four-inequality membership criterion for the Minkowski difference, all sign-orthant integrals, two beta-integral evaluations, an alternating-binomial sum, and extraction of the unique Minkowski-polynomial coefficients. These steps establish the identity for **all** integers \(n\ge2\), \(1\le m\le n-1\), and all real \(0<t<1\); the proof does not rely on numerical interpolation.

The bundled `verify.py` uses Python's standard-library `Fraction` and directly sums the orthant contributions. It ran successfully and emitted `VERIFY_OK exact orthant coefficients: 748; n=2..18; 4 rational t samples`. The test covers four depth fractions, all polynomial coefficients (including endpoints), reflection symmetry, coefficient positivity and the even-dimensional central reduction.

A separate geometric check constructed the convex hull of the pairwise vertex differences of the truncated simplex and compared its Euclidean volume with the analytic polynomial, for dimensions 2 through 5, three depths, and three scale choices. All 36 tested instances agreed to within \(3\times10^{-7}\). That secondary geometric check used floating-point convex-hull calculations and is not needed to prove an infinite statement; it is not bundled as a dependency.

Only the seven included source files are needed to reproduce the exact-rational check. No external compiler, internet access, or unpublished datasets are required. Limitation: exhaustive testing over finite dimensions and depths cannot by itself certify the general theorem; the analytic orthant proof supplies the universal quantifiers.
