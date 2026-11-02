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

Run `python3 verify.py` from the directory containing this document and the script. The code has no third-party dependencies. It checks the first 65536 fixed-point symbols against an independently implemented valuation formula, verifies the exact factor languages for lengths 1–192, tests the predicted all-rotation class counts and compares all even-length classes with the corresponding morphic images.

The factor-set computation uses the mathematically justified bound \(\mu^{m+4}(0)\) for windows of length at most \(2^m\). Because every adjacent letter pair in the fixed point occurs in \(\mu^4(0)\), this finite prefix contains every possible length-\(n\) factor for such \(n\). This makes the finite checks exhaustive for their stated range.

Expected stdout begins with `VERIFY_OK`. The finite checks do not certify arbitrary lengths on their own; the all-length result is established by the parity obstruction and morphic class bijection in `RESULT.md`. No external proof certification or independent scientific review is claimed.
