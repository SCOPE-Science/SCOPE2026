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
# Finite verification

Run `python3 grid3_morse_verify_full.py` on standard Python 3. The script enumerates all matching faces for widths 2 to 8, constructs actual toggle pairs, checks acyclicity of the complete directed Hasse diagram, verifies all critical-face dimensions and counts, and computes the eighth-width exact signed Morse boundary. Its execution output is included as `grid3_morse_verify_output.txt`; the final line reads `ALL CERTIFICATES PASSED`.

The method does not extrapolate from finite computations. It proves precisely these seven cases. The complete matching certificate is algorithmic and reproducible rather than a raw output log. The independent audit status remains not performed.
