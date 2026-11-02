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

Run `python3 verify.py` with the standard Python 3 library. The script checks exact matrix powers, the root of the two-adic interpolation modulo \(2^{22}\), the normalized recurrence valuations for 200,000 positive indices via independently calculated recurrence terms modulo \(2^{32}\), and twenty-eight finite density comparisons. It prints `VERIFY_OK` after all assertions pass. The generating proof in `RESULT.md` establishes the infinite claim; the finite test is an implementation and arithmetic consistency check, not an independent certification or infinite enumeration.
