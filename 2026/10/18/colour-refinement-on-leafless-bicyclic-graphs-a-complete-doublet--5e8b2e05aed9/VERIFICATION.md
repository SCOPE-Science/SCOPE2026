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

The unrestricted classification is established by the graph-core decomposition, a rooted-universal-cover necessary invariant, and an explicit balanced equitable partition for the exceptional pairs. The two attached Python programs are independent finite corroborations, not proofs of the unbounded quantifier.

Run `python check_small.py` and `python check_core.py` in a directory containing the attached files, with Python 3.9+ and NetworkX 2.6+ available. Compare their standard output to `check_small.out` and `check_core.out`. The first program enumerates labelled small-order graphs and checks precise isomorphisms; the second enumerates parameterized leafless bicyclic cores through seventeen vertices and checks 9,619 unordered pairs. Neither program claims to exhaust graphs beyond its stated domain or to perform an independent audit.

Known restrictions: connected, simple, minimum degree at least two, exactly one more edge than vertex; only equivalence *within that class* is classified. Priority relative to all unpublished or inaccessible literature has not been certified.
