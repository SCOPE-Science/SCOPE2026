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

The proof is in `RESULT.md`; the self-contained exact-arithmetic consistency checker is `verify.py`, executable using `python3 verify.py` with no third-party dependencies.

Checks include 72 feasible positive-parameter substitutions for the equilibrium, invasion and Lyapunov identities; exhaustive enumeration of all 16 active-species subsets at \(d=5/4\) and \(d=7/4\) identifying nine nonnegative equilibria at each parameter; enumeration of eight unique proper-support solutions at \(d=3/2\), including the two nonisolated endpoints of a critical segment (the other six are isolated equilibria); and exact verification of five points of that segment. Every finite support check solves the active per-capita linear equations by rational Gaussian elimination and verifies all four original nonlinear stationary equations.

The all-parameter stability and existence assertions are analytical results, not extrapolations from the finite rational tests. No global basin, cycle-exclusion, or finite-time convergence claim is made. Independent audit has not been performed.
