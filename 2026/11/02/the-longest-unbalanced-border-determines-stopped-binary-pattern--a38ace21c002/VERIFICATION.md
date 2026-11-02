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

# Verification record

The analytic proof of the universal statement is in `RESULT.md`. The executable independent checker `verify.py` checks all binary words of lengths 1 through 9 for the sign of the border polynomial at four positive test arguments (4,088 instances). The script compares a numerical integral from the border generating function against an independent automaton dynamic program computing the stopped empirical fraction for seven example words of lengths at most four. It additionally tests two longer mixed-border patterns. The actual successful output is embedded in `verification_output.txt`.

The finite runs are tests, not exhaustive verification of an unbounded theorem. The strict sign and absence of cancellation for every word are proved by the geometric bound in `RESULT.md`. No independent mathematical audit or publisher priority validation has occurred.
