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

The exact Python 3 verification script `artifacts/verify_shuffle.py` was executed with the original package content and independently replays two finite constructions of the squared diameter: exhaustive sign matrices and vertex coordinate multisets reconstructed from strict interleavings. The latter is a genuinely different combinatorial enumeration and evaluates maximum squared distance by rearrangement.

Command: `python3 artifacts/verify_shuffle.py`
Expected output: `VERIFY_OK sign_matrix_cases=49 independently_reconstructed_vertex_cases=49`.

The script also verifies both deficit inequalities on each enumerated sign matrix and checks subcritical and supercritical cases with exact rational weights. These calculations do not certify unbounded dimensions or real parameter continua; the written inequalities and extrema arguments prove the universal claim. No independent audit or external certification has been performed.
