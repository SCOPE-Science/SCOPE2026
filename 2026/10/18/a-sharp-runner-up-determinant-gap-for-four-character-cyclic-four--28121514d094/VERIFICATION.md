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

# Verification record

The standalone `verify.py` evaluates all four-subsets on each cyclic order \(N=8,12,\ldots,52\) using independent complex chord and trigonometric-gap calculations. It compares the maximum among nonsquare sets with \(16\cos(\pi/N)\cos(2\pi/N)\), verifies every equality case comes from moving one vertex of a square one grid step, and checks the exact maximum counts \(N/4\) and \(2N\).

The recorded executable output is in `verify_output.txt`, ending `CHECK_OK 825642 configurations; all 12 cyclic orders checked`. The program uses no external dependencies and has no publication-time downloads. It relies on floating-point arithmetic, so finite tests are supporting corroboration, not proof of the theorem for all cyclic orders. The general statement follows from the exact gap factorization, integer/half-integer split, strict cosine inequality and equality conditions in `RESULT.md`.

The complete manuscript and code are self-contained for reproducing the finite tests; no independent mathematical audit has occurred.
