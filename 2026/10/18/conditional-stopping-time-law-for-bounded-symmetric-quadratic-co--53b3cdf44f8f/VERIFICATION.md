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
# Verification evidence

Run `python3 verify.py` next to the source files. The program uses integer arithmetic to reconstruct classified terminating seed sets and independently calculate their trajectories, count and total hitting time at every dyadic size \(2^L\) for \(7\le L\le35\).

Actual latest run printed `VERIFY_OK terminal_tests=322 seed_tests=15689 dyadic_L=7..35`. It checked the three exceptional hitting times (12, 20, 80), verified all dyadic polynomial instances in that range, cross-checked the exact short-time formula, and performed three larger finite sharpness checks at \(L=100,400,1600\).

The analytic proof of the infinite census, limiting law and optimal-order convergence rate is in `RESULT.md`; these finite tests do not certify universality or mathematical novelty. The independent-audit channel has not been performed.
