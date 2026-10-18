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

# Reproduction and limitations

Use Python 3.10 or newer and execute `python verification.py` with the included standalone file. No third-party packages or network access are required.

The program tests the probability formula against a separately enumerated list of all \(2^{nm}\) possible approval matrices on six small parameter configurations; for each matrix the JR condition is checked directly over every voter subset with at least \(n/k\) members and a nonempty intersection of approvals. It compares every size-\(k\) committee to the top-\(k\) selection in exact rational arithmetic, including tied, zero, and unit probabilities. It separately checks the exact example \(1042685/1048576\), the universal single-candidate maximizer on a finite parameter grid, and convergence of a binomial-tail log rate for several committee sizes. Expected output ends with `verification assertions: 81`.

These finite exercises do not establish the general optimizer or the sharp exponent; the analytic proof in RESULT.md supplies the infinite and universal steps. No independent audit has been performed.
