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
The theorem is mathematically conditional only on the cited published all-exponent strict-descent bound. Independently, the lower-digit convexity argument gives the **exact** maximum at each factorial-block endpoint and a witness for the last allowed block. The proof applies to all integers \(r\ge2\) without a numerical bound on exponent or input.

Run `python3 verify.py`. Two different factoradic digit extraction methods are compared. The script checks all lower-digit endpoint inequalities and each boundary for exponents \(2\le r\le40\), and exhaustively scans every input \(0\le n<(j_r+1)!\) for \(2\le r\le6\). The expected output is `VERIFIED: exact block endpoints, exponents 2..40, exhaustive lower ranges for 2..6`.

Finite checks do not establish the general published theorem or infinite validity by themselves. They supplement the symbolic convexity proof and the cited all-exponent theorem. No independent mathematical audit was performed.
