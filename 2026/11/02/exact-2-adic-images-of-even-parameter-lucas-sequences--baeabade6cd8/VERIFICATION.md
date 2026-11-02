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

# Reproducibility

Run `python3 verify.py` with Python 3 and no third-party packages. It exhausts the *entire state cycle* for 18 signed even recurrence parameters and 12 modulus levels, rather than assuming a fixed time cutoff. The completed execution printed `VERIFY_OK modular_image_cases 216 total_modular_states 76816 isometry_pairs 54432 doubling_identities 1080`. The symbolic proof, not these finite checks, supplies all-parameter and all-precision validity. Independent mathematical review has not been performed.
