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

The standalone file `verify.py` constructs the exact 64-state finite automaton from the edge-local constraints, checks the 102 transitions, the 14-state open-boundary reduction, and the two cyclic components (a loop and a directed six-cycle). The 14-state adjacency table is explicitly given in RESULT.md and proves the unrestricted formulas by path and closed-walk decomposition.

The verifier also independently enumerates all candidate selected-edge subsets on actual graph edges for open ladders with one through six rungs and circular ladders with three through six rungs. Its direct subset test does not use the state automaton. Transfer calculations cover open ladders with one through seven rungs and circular ladders with three through sixteen rungs.

Run `python verify.py` with Python 3 standard library. The expected deterministic output is recorded in `verify_output.txt`. These finite checks support, but do not replace, the all-order state-reduction proof. An independent mathematical audit has not been performed.
