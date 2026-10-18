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

# Finite consistency checks and proof boundaries

Run `python3 check.py` using Python 3's standard library. The program reads no other data files and has a fixed random seed. The locally executed result was `PASS 28170 finite sample/assertion groups`.

The code constructs the separator formula as an explicit syntax tree, counts its box nodes, evaluates all operations by exact rational arithmetic, checks the displayed bounded countervaluation on stars with one through six leaves, and checks finitely many other valuations. It additionally selects one extremum witness for each root-evaluated box in randomly generated nested modal formulas and confirms the root value is preserved after retaining those leaves.

**Limits:** sampled real-valued valuations are not exhaustive over the continuum; sampled formula trees are not an exhaustive collection of all syntax. The infinite theorem and the minimality for every formula follow from the symbolic pigeonhole proof and the modal-witness structural induction in `RESULT.md`. The checker verifies examples of those lemmas rather than certifying their universal quantifiers. Independent audit was not performed.
