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

Run `python3 verify.py` from a directory containing the accompanying unmodified standalone `verify.py` program. The verifier independently simulates ordinary zero forcing on every initial coloring of the boards \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\). It tests all 104272 white-edge subsets against a separate acyclicity/degree implementation, uses a component-subset recursion to evaluate the six signed weighted bipartite-tree enumerators coefficient by coefficient, and checks the Stirling-number formula at the minimum set size. The expected final status is `VERIFY_OK boards=8 exhaustive_subsets=104272 six_EGF_terms=passed minimum_count=passed`.

These are exhaustive checks only for the listed finite boards. General correctness is supplied by the leaf-peeling and Prüfer-word proofs in `RESULT.md`; the computational agreement is independent corroboration, not a substitute. All integer operations and forest cycle checks are exact; no timeout or numerical approximation is treated as a mathematical conclusion. This documentation does not claim independent audit or external certification.
