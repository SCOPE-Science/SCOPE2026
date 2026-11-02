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

Execute `python3 CHECK.py` with no external libraries. The check file performs 773 assertions in the final tested version. It computes exact rational finite-sum identities from the piecewise-linear hat for fifteen odd values of the denominator and checks the analytic derivative discriminant identity; it independently reconstructs four sample \(2\times q\) Zibulski–Zeevi Zak matrices and their Hermitian eigenvalues at selected fibers, including limiting extremizers.

The theorem for infinitely many odd denominators is proved symbolically in `RESULT.md` using locally finite Walnut sums, a unitary two-periodic fiber decomposition, and a globally positive derivative discriminant. Finite checks alone would not establish the theorem, uniqueness of the extrema, or the universal uniform conditioning bound. No independent mathematical audit has been performed.
