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

# Verification of analytical transverse stability

The theorem follows from exact rotating-frame differentiation, decomposition into neutral and radial directions, the two-dimensional complex collective determinant, and quartic Routh–Hurwitz. The supporting `CHECKER.py` is standalone apart from NumPy and prints `PASS 2283 finite computations` on the included finite suite.

The suite checks \(M=3,4,\ldots,10\), several dissipative and reactive coupling strengths, regular balanced polygons, and a continuum-sampling of the nonregular four-node antipodal-pair family. It constructs the actual \(2M\times2M\) real Jacobian and compares the entire characteristic polynomial and nonneutral roots against the analytic factorization; a separate exact-rational loop checks the critical Hurwitz identity. The four-agent stability boundary is also checked as the exact rational \(13/18\).

Finite testing does not certify the infinite-parameter statement. The printed tests use double precision for the Jacobian comparisons and exact Python fractions for the rational identity. Nonlinear dynamics exactly at the imaginary-eigenvalue boundary and collinear configurations remain unproved by this result. No independent audit has been carried out.
