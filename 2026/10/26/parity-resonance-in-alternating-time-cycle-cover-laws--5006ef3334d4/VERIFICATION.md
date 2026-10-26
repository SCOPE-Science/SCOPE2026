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

# Reproduction
Run `python3 verify.py` with Python 3 standard library. The script uses exact fractions and a time-phase/neighbor-mask absorbing-chain formulation independent of the analytic resistance derivation. It passes 60 exact comparisons over orders 3 through 7 and probabilities 1/3, 2/5 and 3/4; the Gaussian eliminations span 690 transient states. It also checks odd-cycle exact total variation for orders 3, 5, 7, 11 and 29, and even-order convergence for 20, 40, 80, 160 and 320. The complete arbitrary-order proof is in RESULT.md; finite tests alone cannot certify it. Source priority concerning some older inaccessible literature and independent scientific validation remain open.
