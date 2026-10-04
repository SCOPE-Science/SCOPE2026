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
The proof uses the source-indexed equal-weight Schedule-Free SGD recursion with \(x_1=z_1\). It eliminates the base sequence through \(z_t=t x_t-(t-1)x_{t-1}\), derives the exact differential equation for the generating function, and extracts its coefficients.

`verify.py` checks exact rational resonance cases, direct agreement between simulated iterates and generated coefficients, the noninteger asymptotic constant, the strict stability frontier, and the boundary case in which \(x_t\) can decay while \(z_t\) grows.

The finite numerical checks serve only as transcription and asymptotic guards. The infinite-time statements follow from the exact recurrence and coefficient analysis in `RESULT.md`.
