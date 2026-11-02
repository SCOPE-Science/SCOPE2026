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
# Verification of four-round Moore-graph classes

`python3 moore_verify.py` constructs the three known graphs independently of any graph software library: a five-cycle, the Petersen graph on two-subsets of five points, and the 50-vertex Hoffman–Singleton graph as five pentagons joined to five pentagrams. It checks degree and all common-neighbor counts, enumerates every unordered triple and every fourth-vertex adjacency mask, and uses exact recursive ordered-tuple first-order types (including repetitions) to distinguish the three rank-four theories. Recorded standard output: `moore_verify.out`. The type routine examines all fourth moves and requires no probabilistic approximation.

`python3 support_formula.py` checks all symbolic cell sizes and their sums against the total of unselected vertices, for degrees 3, 4, 7 and 57. The degree-57 calculation tests only conditional arithmetic; no graph of that degree was generated. Recorded standard output: `support_formula.out`.

The proof of equivalence for all eligible degrees is the symbolic Ehrenfeucht–Fraïssé argument in `RESULT.md`. Experiments on the known graphs are consistency checks, not substitutes for the infinite claim. Neither script certifies the novelty of the theorem or the existence of a degree-57 Moore graph. Independent audit has not been performed.
