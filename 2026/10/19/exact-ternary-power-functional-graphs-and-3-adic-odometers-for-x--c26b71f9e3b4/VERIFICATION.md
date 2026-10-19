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

# Reproducibility and scientific limits
Run `python3 verify.py` with the standard Python library. It exhaustively enumerates every state modulo \(3^n\) for \(1\le n\le8\), checking periodic cycle sizes, return-to-cycle depths, a bijection from depth-one vertices to cycles, all square-root branching counts and total state count. It separately checks the valuation induction on selected ternary integers at finite precision \(3^{22}\), without claiming exhaustive infinite verification. Expected output is `VERIFY_OK`.

Proof of the infinite result is the integral-polynomial displacement induction, the exact finite digit-lifting argument, and the Hensel root count in `RESULT.md`. The checker is a finite corroboration, not a replacement for those arguments. Historical-priority assessment relies on the literature comparisons in `AUDIT.json` and acknowledges incomplete access to a plausible later general source.
