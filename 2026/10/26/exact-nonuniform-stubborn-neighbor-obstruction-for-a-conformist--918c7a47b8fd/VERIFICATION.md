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
The accompanying `verify.py` computes the payoffs for every action pair directly and verifies that the predicted local obstruction is equivalent to the absence of simultaneous pure best responses. It compares all \(7,371\) pairs of stubborn-count vectors over \(\{0,1,2\}^m\) for \(m=2,3,4\) and all \(1,024\) pairs over \(\{0,1\}^5\), using exact integer arithmetic. Every nonobstructed profile also has its constructive equilibrium witness checked. For \(m=2,3,4\), the observed obstructed-profile counts are respectively \(9,63,501\).

The argument in RESULT.md is an independent symbolic proof for every \(m\ge2\) and all nonnegative integer counts. The finite test does not establish the theorem by itself. No claim is made about mixed equilibria or equilibrium dynamics. Run from the same directory using `python verify.py`. Independent external review has not been performed.
