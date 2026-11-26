---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Run `python verify_angle.py` with Python 3.10 or later (`int.bit_count` is required). No nonstandard dependencies are needed. The exact rational cases test mixed finite difference normalizations for monomial degrees up to six, Boolean-degree cancellations and coefficient counts. Floating-point tests compare nonempty exponential coefficient factorizations and finite-resolution derivative norms. The constant coefficient of the exponential example is established analytically by evaluation at the zero bit vector, not by these tests. The recorded final line is `PASS: 2644 total checks after leading-bit and angular-range tests`. The proof of infinite-resolution assertions is analytic: iterated fundamental theorem of calculus, uniform continuity, Boolean degree annihilation, and a sharp alternating-sign minimax witness. Finite experiments do not certify the infinite claims. The result is restricted to smooth principal-branch angles, fixed degree, and dyadic samples; alternative oracle encodings are not excluded.
