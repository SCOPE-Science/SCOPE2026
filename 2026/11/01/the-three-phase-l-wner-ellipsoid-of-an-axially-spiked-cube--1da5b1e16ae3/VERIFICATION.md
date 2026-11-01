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

The defining quantitative claim is a statement for every integer \(d\ge2\) and every real \(a\ge1\), not only for tested samples. The proof checks the entire generating set of the hull, constructs nonnegative normalized contact weights, shows exact zero transformed mean and covariance \(I_d/d\), and invokes the explicitly proved global Löwner optimality criterion. These steps analytically establish the claimed unique ellipsoid. The volume and \(C^1\)-but-not-\(C^2\) transition assertions are obtained by direct differentiation of its exact semiaxes.

Run `python3 verify.py` in the extracted directory (Python, NumPy, and SciPy are required). The recorded run completed with: `PASS: 989 containment-and-isotropic-certificate cases, 70 independent convex optimizations, maximum log-volume discrepancy 8.82e-12`. The solver cross-check is separately constructed from the convex inverse-semiaxis variables, not by inserting the candidate ellipsoid into its own objective. It is a finite numerical corroboration and cannot prove global optimality beyond the analytical contact arguments, or exclude all other published equivalent derivations. Independent validation and independent audit have not been performed.
