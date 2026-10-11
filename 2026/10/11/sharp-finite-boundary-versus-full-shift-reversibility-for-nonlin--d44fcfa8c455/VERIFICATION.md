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

Run `python3 verify.py` from the extracted package, using Python 3.9 or newer and no third-party libraries. The expected exact output is `VERIFIED 19733 exact finite assertions`. The program tests all admissible rules at moduli 2 and 4 with finite-null-boundary lengths up to three, additional seeded composite-state rules, prime-periodic collisions, and digitwise inverse reconstructions. It also evaluates the least-radius witness coefficient in several moduli.

These tests are not a certificate over all integers or all bi-infinite configurations. Global correctness uses the exact prime-power induction, explicit collision, and nilpotent polynomial inverse written in the proof. The reconstructed finite-null-boundary fact is an input context from the primary 2026 paper, and its linear specialization has pre-existing literature. Full text of two earlier additive papers was not accessible for an exhaustive priority comparison.

Same-model review: passed. Independent audit: not yet performed.
