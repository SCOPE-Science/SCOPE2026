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
The package checks the first-step support structure of the printed AdaLomo matrix recurrence.

`verify.py` exhaustively enumerates every two-by-three gradient matrix with entries in \(\{-1,0,1\}\), excluding only no cases from the support classification. It verifies that both the current normalized factorization and the original unnormalized outer product produce a finite raw quotient exactly when every row and every column contains a nonzero gradient entry.

The script separately checks a nonstationary \(1\)-strongly convex two-by-two quadratic witness, an Adafactor-style positive denominator safeguard, and the positive squared-gradient floor used by the maintained implementation.

Enumeration is a transcription guard only. The all-dimensional iff statement is proved in `RESULT.md`.
