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

# Verification and limits

The exact proof of uniqueness, one-sided derivative inequality, and end-event law appears in `RESULT.md`. The external first-order cut-time limit [1, Theorem 1.2] is a cited input, not rederived or certified here. No finite computation substitutes for this limit.

Reproduce the independent arithmetic and finite-state consistency checks using the Python standard library: `python3 verify.py`. The actual captured output is supplied in `verification_output.txt`. The script confirms the two rational inequalities bracketing the unique root, validates identities at gap ratios 1 and 2, enumerates all 36 permitted transitions for four distinguishable types and checks the speed-reflection involution, then computes the unique nested stationary-point/root solution with Decimal bisection. Root digits and one-sided slopes are numerical illustrations supported by the analytic uniqueness and derivative proof.

The check on 24 states is not an exhaustive verification for growing populations; the generator-level reflection identity proves symmetry for arbitrary equal-size classes. Claim scope excludes the exactly critical final-interchange probabilities.
