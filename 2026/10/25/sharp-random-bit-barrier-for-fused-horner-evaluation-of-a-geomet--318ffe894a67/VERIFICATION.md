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

# Reproducibility and scope

Run `python verify_fma_horner.py` with Python 3. The script uses only the standard-library `fractions`, `collections`, and `random` modules. It checks every reachable state and transition using exact rational arithmetic for 224 parameter triples, the final predecessor's upward probability, and one reproducible trajectory. The expected successful output is `PASS: 224 distinct parameter triples; max 2382 reachable states; sample absorption 245 steps, terminal 193/2`.

These finite checks are not an exhaustive proof for arbitrary bit widths. The proof in `RESULT.md` establishes the universal claim by monotonicity, the exact binary precision-grid threshold, and almost-sure absorption of a finite-state chain. The implementation does not emulate finite exponent bounds, subnormals, actual fused hardware timing, or alternative rounding modes.
