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

# Verification instructions

Run `python3 verify.py` from the extracted package directory. The program uses the Python standard library only. It prints `VERIFY_OK` after checking the exact quadrilateral diagonal formulas on rational normals, global diameter bounds on a separate rational grid, the local maximizing chord against all section vertex pairs for 2,200 deterministic pseudorandom nearby orientations, and deterministic approximations of both leading spherical-area constants.

All verification inputs are constructed within the program; no missing external source data, network download, or previously generated artifact is needed. The analytically proved theorem is in `RESULT.md`; these finite calculations check important algebra and asymptotic normalization, but finite tests cannot certify a universal geometric identity or a probability limit. No independent scientific audit has been performed.
