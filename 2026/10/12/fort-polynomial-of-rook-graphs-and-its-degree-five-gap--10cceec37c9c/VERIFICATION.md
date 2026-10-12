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
# Verification details

The included self-contained `verify.py` runs with Python 3 standard library. Its `direct` function uses the original graph adjacency relation and tests each nonempty vertex subset, rejecting subsets if any omitted vertex has exactly one selected neighbor. Its `fort_polynomial` function independently implements the occupied-support classification and the state-polynomial recurrence.

Checks completed:
- Complete comparison of their coefficient dictionaries on twenty-one labeled rook graphs, totaling 1,423,541 enumerated nonempty vertex subsets.
- Direct lower-boundary comparisons on five small rook-graph parameters.
- Degree-four counts and five/six gap checks for side lengths five through eight, with the explicit degree-six formula tested when both sides are at least seven.
- Boundary checks giving 120 five-element forts in the five-by-five rook graph and 3,720 six-element forts in the six-by-six rook graph.

The proof in `RESULT.md`, rather than these finite tests, establishes the theorem for every positive side length. Arithmetic costs are counted as operations on exact integers; there is no claim of polynomial bit complexity. The literature assessment is based on cited sources and is not independent validation.
