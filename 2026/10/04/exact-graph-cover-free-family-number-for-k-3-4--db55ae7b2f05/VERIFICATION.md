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

The claim is finite and is checked by `verify.py`, which uses only exact integer operations and the Python standard library.  The verifier reconstructs the necessary-and-sufficient row-witness requirements for a graph cover-free family, enumerates all binary row types, removes only strictly coverage-dominated types, and performs complete branching.  It proves that five rows cannot realize the requirements for \(K_{3,4}\), finds a six-row realization, and directly checks the displayed block family.

The same verifier establishes \(t(K_{2,2})=4\), \(t(K_{2,3})=5\), \(t(K_{2,4})=6\), and \(t(K_{3,3})=6\), which are exactly the smaller complete bipartite graphs needed for the minimum-order strictness claim.

The computation proves only these finite statements.  It does not extrapolate a formula for arbitrary \(K_{a,b}\).
