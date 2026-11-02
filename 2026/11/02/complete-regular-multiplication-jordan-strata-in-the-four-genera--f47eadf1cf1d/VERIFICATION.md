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
Run `python3 exterior4_verify.py` in the directory containing the standalone checker. Its expected output is `exterior4_verify.log`. The checker uses original exterior basis multiplication with explicit finite-field arithmetic and independent row elimination; it does not derive its observed ranks from the claimed normal forms.

The completed run exhausted all \(2^{15}=32768\) positive-degree elements over \(\mathbb F_2\), all \(3^6=729\) and \(4^6=4096\) degree-two forms over \(\mathbb F_3\) and \(\mathbb F_4\), and 557 additional graded sample operators in each of \(\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_9\). The finite-field extension arithmetic is genuine. The expected final output line is `EXTERIOR4_REGULAR_JORDAN_SPECTRUM_OK`.

The exact rank and distribution theorem is proved symbolically in `RESULT.md`. This finite verification does not establish general statements by exhaustive enumeration outside the specified finite ranges and does not independently establish publication priority.
