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

Execute the standard-library-only checker `python3 verify_two_variable.py` from this directory. Its output in `verification_output.txt` records six distinct classes among the tested finite structures, with full enumeration of atomic diagrams using zero, equality and all ordered ternary-addition triples, and both possible single-variable replacement repertoires. Failed expectations cause an assertion error.

The computational check is finite, whereas the result is for every prime, all positive dimensions and arbitrarily nested two-variable formulas. The uniform proof is the five-exceptional-slope case analysis followed by an explicit invariant two-pebble back-and-forth. The distinction among the six classes is witnessed by rank-two existential diagrams. Independent mathematical audit and exhaustive historical priority checking have not been performed.
