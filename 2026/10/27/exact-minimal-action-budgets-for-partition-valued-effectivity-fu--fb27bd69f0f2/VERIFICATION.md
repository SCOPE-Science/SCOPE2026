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

# Verification of the exact action-budget theorem

Run `python3 checker.py` using Python 3's standard library. Expected terminal line: `ALL_CHECKS_OK`.

The checker enumerates all partition tuples over labelled outcome carriers for (number of agents, maximum carrier size) equal to (2,6), (3,5), and (4,4). It filters for the stated all-cells-inhabited hypothesis, constructs the uniform cyclic-difference outcome maps, and tests every action's actual range. For two agents it separately constructs unequal optimal block multiplicities and verifies every action's range. It also checks the lower-bound inequalities on the enumerated instances. In total it checks 1,655 admissible partition tuples.

These are finite instance checks, not certification of all cases. The general proof is symbolic: fixing one action restricts every possible outcome in a cell to completions within the other prescribed blocks; the difference map is a bijection on every one-coordinate slice; and modular addition covers all symbols of a cell in both directions when both dimensions are at least the cell size.

Independent auditing and independent validation have not been performed.
