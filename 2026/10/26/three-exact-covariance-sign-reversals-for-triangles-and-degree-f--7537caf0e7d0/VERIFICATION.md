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

Use `python verify.py` in a Python 3 installation with no third-party dependencies. The script enumerates every labelled graph with \(n-1\) edges for \(n=4,5,6,7\) and compares the covariance of triangle count with each degree-bin count to the conditional expectation identity in `RESULT.md`, using exact `fractions.Fraction` arithmetic. It checks \(22\) degree-index identities exactly, then checks every degree-bin sign for \(14\le n\le120\) and the boundary at \(n=13\). This direct enumeration is finite corroboration, not an infinite proof; the latter is established by the cubic root count and positive-shift polynomial certificates in `RESULT.md`.

The checks executed successfully. Independent audit has not been performed. Historical priority is not established exhaustively, because the most relevant broad papers were available as abstracts but not inspected in full.
