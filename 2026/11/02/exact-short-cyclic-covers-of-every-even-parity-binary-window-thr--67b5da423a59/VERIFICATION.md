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

# Reproducibility

Run `python3 verify.py` and `python3 crosscheck_small.py` in a directory containing all three supplied artifact files `verify.py`, `crosscheck_small.py`, and `witnesses.json`. The expected final lines are `VERIFY_OK` and `CROSSCHECK_OK`, respectively.

The main verifier reconstructs the complete even-weight one-in/one-out arc system in the de Bruijn digraph, canonically enumerates every simple directed cycle through the feasible augmentation budgets, computes the minimum hypergraph connection cost by exact bitmask dynamic programming, checks a circular witness for each order, and exhaustively computes the more restricted odd-only augmentation costs. There is no numerical solver or floating-point rounding. The separate cross-check directly enumerates all binary circular words at the three smallest orders, without using the cycle or hypergraph reduction.

This establishes the stated finite values conditional only on the proved complete enumeration and graph-to-word equivalences. It does not verify lengths outside the declared range or establish historical priority against inaccessible literature. Independent scientific audit has not been performed.
