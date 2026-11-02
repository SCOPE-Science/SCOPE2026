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

# Verification record

The attached `verify_spin_factor_invertible.py` uses only the Python standard library. Run with `python3 verify_spin_factor_invertible.py`. It checks actual skew-adjoint endomorphisms against the invertible-value condition by enumerating each nonzero image vector, not merely checking preselected rank-two candidates. It builds \(\mathbb F_9\) as a quadratic extension of \(\mathbb F_3\), and distinguishes the two binary quadratic-form types. Actual output is embedded in `verification_output.txt`. The exact terminal success marker is `SPIN_FACTOR_IV_DERIVATIONS_OK 12`.

This bounded exhaustive enumeration covers twelve configurations, including dimensions two, three, four, five and fields of orders 3, 5, 7, 9; it is not an exhaustive proof over all dimensions or all fields. The mathematical proof independently uses skew-adjointness, finite-field anisotropy, orthogonal-stabilizer orders, and Witt extension. No outside audit or independent publication-priority certification is asserted.
