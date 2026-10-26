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
# Verification notes

Run the standalone, standard-library Python 3 checker with `python check.py`. It uses exact rational arithmetic for finite \(K\), \(t\), and fugacity to reproduce the stationary generating-polynomial identity, deformed-occupation expectation, and optimal current. It enumerates complete fixed-particle configuration spaces on several small rings and checks each configuration's weighted master-equation balance. It then performs floating-point tests of the capacity-normalized current and limiting curvature on both sides of \(\pm\log3\). The tests report `ALL CHECKS PASSED` when successful.

These finite tests do not establish the infinite-volume or large-capacity limits. The analytic proof uses positivity of all one-site weights, the finite-support local central limit theorem for fixed capacity and interior density, monotone inversion of a Riemann-sum density, and an explicit second-derivative sign calculation. The source factorization is also verified algebraically through the finite master equation. No outside audit has been performed.
