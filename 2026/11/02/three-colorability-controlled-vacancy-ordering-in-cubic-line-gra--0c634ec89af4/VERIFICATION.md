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

# Checks and limits

The included `checker.py` requires Python 3 and no third-party dependencies. Running `python3 checker.py` checks all \(531441\) cuboctahedral ternary configurations and independently enumerates the same ground states from four disjoint cube-vertex stars. It verifies exact energies, all five degeneracies, occupancy-resolved counts, and magnetization second moments, and also checks all \(19683\) configurations of the line graph of \(K_{3,3}\). In particular, both cube enumerations agree on their complete (occupancy, magnetization) multisets at all five anisotropy values. The supplied local-star analytic proof, not this finite computation, establishes the all-graph statement. No continuous-parameter numerical optimization, external formal certificate, or independent scientific audit is claimed.
