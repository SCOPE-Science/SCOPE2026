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

`verify.py` uses only the Python standard library. Execute `python verify.py` from the extracted package. It enumerates all seven-tuples for field orders \(2,3,4,5,7\), calculates the determinants by direct Gaussian elimination, and compares each target-fiber distribution with the predicted expression. The extension field of order four is represented as \(\mathbb F_2[X]/(X^2+X+1)\). The checked fiber arrays are displayed by the script, followed by `VERIFY_OK` if all assertions pass.

Mathematical proof is the exhaustive symbolic leading-block stratification in `RESULT.md`; checking these small finite fields does not certify all finite fields or higher Hankel sizes. Source comparison is documented separately; no independent review or external audit has been performed.
