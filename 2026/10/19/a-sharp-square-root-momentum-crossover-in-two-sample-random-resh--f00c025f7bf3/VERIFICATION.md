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

# Reproduction and verification

The mathematical claim concerns the unique stationary **phase-resolved** covariance of a two-component scalar heavy-ball random-reshuffling recursion. Its proof establishes strict stability by the Schur/Jury criterion, derives an affine epoch recursion with independent equiprobable signs, and solves the resulting three-entry discrete Lyapunov system. The infinite sum converges geometrically in the stated parameter interval; this—not a finite experiment—proves the infinite-time statement.

Run `python verification/check.py` with Python 3 and packages pinned in `verification/requirements.txt`. The script reconstructs the one-step and two-step matrices from the algorithm rather than reading precomputed matrices; verifies every entry in the symmetric two-by-two symbolic Lyapunov identity; verifies the iid comparator and its asymptotic ratios; and checks both the fixed-positive-momentum and the joint small-momentum limits.

As independent finite corroboration, the script enumerates both component orders for each of six consecutive epochs at five exact-rational parameter pairs, comparing the complete path-average second-moment matrix at every epoch with direct covariance recurrences (30 exact path-moment comparisons). It also iterates five numerical covariance recurrences and compares their limits with the closed form. The archived `verification/observed-output.txt` was produced by running this exact script with the specified dependencies.

**Unproved by the computation alone:** any general-dimensional extension, almost-sure convergence of fixed-step iterates to one point, and universal optimizer performance. The stated proof makes no assertion about these extensions. At a fixed positive stepsize the invariant law is typically nondegenerate, so pointwise convergence of the random iteration is not claimed.
