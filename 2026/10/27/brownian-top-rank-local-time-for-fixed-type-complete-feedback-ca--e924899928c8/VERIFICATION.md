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

# Verification and scope

Run `python verify.py` with Python 3 and its standard library. The program exhaustively enumerates 4362 distinct finite multiset deck orders for five parameter pairs, checking the exact pathwise rank-regulator identity and compensator expectation equality. It also performs reproducible, low-power seeded simulations for the two-type and three-type limiting means. The calculation does not independently establish the infinite-dimensional or large-m limit; the analytical proof uses a joint martingale bridge FCLT, endpoint estimates, smoothing of the maximizer, and Brownian rank Tanaka. No independent audit has been performed.
