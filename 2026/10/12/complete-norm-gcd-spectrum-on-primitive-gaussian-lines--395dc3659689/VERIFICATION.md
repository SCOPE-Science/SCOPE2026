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
Run `python3 verify.py` from the extracted artifact directory. The script uses only the Python standard library and reproduces `verification_output.txt`. It verifies \(6260\) primitive Gaussian affine descriptions and \(194060\) direct adjacent-gcd comparisons and tests the three-consecutive norm gcd. It also checks exact counts for the period \(325\). The finite scope is explicit and does not certify all inputs; the general proof appears in `RESULT.md`.
