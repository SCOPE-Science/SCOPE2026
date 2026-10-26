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
The included `checker.py` was executed using Python 3 with only the standard library and returned `ALL_CHECKS_OK`. It checks direct enumeration for seven finite tree configurations and both possible threshold strictness conventions, totalling 132,696 evaluations. It verifies the exact weak/strict complement and odd-branching symmetry for branching factors up to 20 at three depths, and compares the even depth-two probability at six increasing branching factors with the stated normal-limit constant.

Analytical proof obligations independently inspected: the child-subtree independence used by the recursion; endpoint/rounding conventions for \(\ge\) and \(>\); fair-binomial symmetry; the central-binomial Stirling constant; triangular-array binomial normal approximation with a moving success parameter; and Hoeffding propagation for every fixed remaining depth. Exhaustive finite tests do not prove the infinite limits. The modal statement is restricted to independent leaf labels on complete regular directed trees, with fixed depth and ratio.
