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

# Reproducible checks and limits

Extract `verify_split_super.py` next to this file and run `python3 verify_split_super.py`. The standard-library-only checker reconstructs the \(81\)-state directed local automaton, all \(178\) arcs, and an integer potential by at most \(81\) monotone relaxation rounds. It verifies \(4w-3\le h(t)-h(s)\) on every arc and enumerates every simple tight directed cycle, obtaining exactly three of length eight. It confirms the boundary-state inequalities, all explicit base words, the eight-letter insertion, and all target values through length \(64\). An independently implemented graph-level check exhausts \(174672\) vertex subsets across twelve path/cycle graphs and compares the resulting minima. A separate local-versus-graph equivalence check covers all three-symbol words on small orders.

These checks prove finite lemmas required by the stated mathematical argument. The argument from potential and insertion is necessary for all orders; raw enumeration through length \(64\) is not by itself an infinite proof. A complete external mathematical review has not been performed. The theorem excludes cycles of order three, general graph factors, and minimum-set multiplicities.
