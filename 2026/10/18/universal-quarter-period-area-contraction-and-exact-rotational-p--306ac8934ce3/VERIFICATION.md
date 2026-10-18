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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program prints `VERIFY_OK` after checking the exact formula against an independently evaluated curvature-support mixed-area integral for odd orders 3, 5, 7, 11 and 25 and two widths, including interior and boundary rotations. It tests the complementary identity, sample nonuniversal angles, exact Fourier factors on a smooth strictly convex two-frequency family, and the uniform scaled limit for several large odd orders. The numerical checks are reproducibility tests; they do not replace the all-angle analytical classification or infinite-order asymptotics proved in RESULT.md.

Scientific limits: the Reuleaux triangle is a previously established instance of the explicit profile, not a claimed new result; no arbitrary-body area monotonicity or unequal-weight averaging theorem is asserted. Unavailable full text in relevant historical literature leaves a residual priority risk. Independent verification has not been performed.
