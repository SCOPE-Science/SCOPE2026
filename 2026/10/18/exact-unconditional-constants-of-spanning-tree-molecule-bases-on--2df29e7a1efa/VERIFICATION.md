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

# Verification of weighted cactus unconditional constants

The proof uses three exact steps: edge-flow quotient duality, the edge-disjoint cycle decomposition, and a weighted absolute-deviation minimum with breakpoints \(-1,0,1\). The NP-hardness reduction maps a nontrivial PARTITION instance of even total \(A\) to a cycle with retained lengths \(2a_i\) and omitted length \(1\), so the discrepancy is either zero or at least four.

`verify_weighted_cycle.py` was run with standard Python. It independently enumerates the dual polytope's extreme points, reconstructs all sign-change operator norms from edge increment linear functionals, and checks 284 exact-rational weighted-cycle cases, unit cycles of lengths three to eight, and selected integer partition witnesses. All checks passed. Its finite range is not a certificate of the theorem for arbitrary cycles or cacti; the generality follows from the analytic argument in RESULT.md.

Independent external audit has not been performed.
