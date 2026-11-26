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

# Exact palindrome saturation certificate

Run `python3 verify.py` with the Python 3 standard library. The program reconstructs the known 37-palindrome catalogue from the four level-three pair images, confirms the length spectrum through the two empty terminal lengths 24 and 25, and tests every length-172 window in the four level-four pair images. Their lengths allow a window to meet at most two consecutive level-four blocks, so the tests cover every length-172 factor of the infinite word. It also checks a length-171 factor lacking a specified palindrome, which establishes sharpness. The expected line is:

`palindromes=37; window counts=1329,1079,1079,829; witness=00:325:171; threshold=172`
