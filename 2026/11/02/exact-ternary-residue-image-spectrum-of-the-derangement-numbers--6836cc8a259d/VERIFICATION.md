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

# Reproducibility and verification

Execute `python3 verify.py` with the Python standard library. The program performs direct recurrence enumeration at every modulus from three through the ninth power of three, polynomial coefficient calculations modulo nine, 27 and 81, a critical-value calculation, and independent signed-square image counts.

The observed full image sizes are `3, 7, 21, 61, 183, 545, 1633, 4895, 14683`. The terminal output is `VERIFY_OK polynomial_certificates=3 image_indices=59046 signed_square_inputs=3280 limiting_density=725/972`.

The unrestricted theorem is proved analytically, not inferred from these finite checks. The change-of-coordinates argument uses existence and uniqueness of solutions to strict contractions on the complete ring of three-adic integers. No external certificate or independent audit is asserted.
