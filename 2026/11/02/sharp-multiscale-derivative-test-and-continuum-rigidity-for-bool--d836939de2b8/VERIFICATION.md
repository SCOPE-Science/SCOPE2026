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

# Reproduction and limits

Run `python verify_angle.py` with Python 3.9 or later. No nonstandard dependencies are needed. The exact rational cases test mixed finite difference normalizations for monomial degrees up to six, Boolean-degree cancellations and coefficient counts. Floating-point tests compare exponential coefficient factorizations and finite-resolution derivative norms. The script prints `PASS: 2644 total checks after leading-bit and angular-range tests` when all assertions pass. The proof of infinite-resolution assertions is analytic: iterated fundamental theorem of calculus, uniform continuity, Boolean degree annihilation, and a sharp alternating-sign minimax witness. Finite experiments do not certify the infinite claims. The result is restricted to smooth principal-branch angles, fixed degree, and dyadic samples; alternative oracle encodings are not excluded.
