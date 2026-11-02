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

# Verification notes

The general statement is proved by an exact rank-preserving factorization, with an explicit algebraic base-rank computation. The standalone `checker.py` directly constructs binary finite toroidal graph-state cross blocks, toggles one or two actual edges, and checks the formulas with exact bit-vector elimination. Its recorded output is in `verification_output.txt`: 112 pairs and 339 rank comparisons at long circumferences 8, 16, 32. The exact finite cases supplement the proof and are not an exhaustive all-dimensional verification. No independent audit or historical priority certification has been performed.
