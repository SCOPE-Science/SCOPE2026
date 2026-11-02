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

# Reproducibility and limits

Run `python verify.py` with Python 3. The code is standalone and needs no external data or dependencies. It checks the exact maximum-marker formula for integer bases two through six and lengths one through thirty, explicit witnesses and critical patterns, finite samples of progressions at bases two through five and lengths one through twenty-three, the quadratic counting inequality on those samples, and the normalized power-gcd identity for hundreds of exponent triples.

Observed output: `VERIFY_OK 639077 assertions; finite tests only`.

The arithmetic progression scan is finite in both start and step. No claim that it exhausts all factors for an unbounded range is made. The infinity statements are established by the standalone mathematical proof in RESULT.md. These are ordinary reproducibility checks and do not constitute independent scientific auditing.
