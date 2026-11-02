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

# Verification of the mathematical result

Use `python3 verify_pal_binary.py` with the Python standard library. This program checks the exact endpoint partition against a separate interval dynamic program for all \(131{,}071\) binary words of lengths \(0\) through \(16\), checks literal sets of scattered palindromic patterns for all \(1{,}023\) binary words through length \(9\), verifies the maxima and exact equality-word classifications at every length through \(16\), checks \(4{,}000\) deterministic random longer inputs, and evaluates the explicit extremizing constructions at lengths \(17\) through \(999\).

Expected output begins `VERIFY_OK` and reports the test domains. This finite checker does not replace the all-length proof in `RESULT.md` and does not provide an independent scientific audit. Verification is limited to the declared finite parameter ranges; correctness for all lengths comes from the outer-letter partition and inductive inequalities.
