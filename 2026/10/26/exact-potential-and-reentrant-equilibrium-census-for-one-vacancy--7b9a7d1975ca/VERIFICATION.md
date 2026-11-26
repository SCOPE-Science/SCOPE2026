---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a cross-part move, there is one vacancy outside the part of the mover both before and after, so the two occupied-neighbor denominators are H_i and H_j, both positive. The old same-type count outside i is R_t-x_it and the new one outside j is R_t-x_jt-1. A ±1 difference of the proposed quadratic in x gives these two terms with opposite signs, so the potential increment exactly equals the utility gain; within-part moves change neither. For opposite-color agents in a mixed full part the two present payoffs sum to 1 and their separate counterfactual payoffs to (H_j+1)/H_j: each departure excludes no opposite-type agent from its own numerator. One would strictly improve. With full parts pure, comparing each color's old quotient with its new quotient gives the stated non-strict inequalities at equilibrium. The labeled choices are disjoint, hence the polynomial with the vacancy-location multiplier and binomial coefficient; for equal parts the inequalities are automatic and the denominator of the fraction is hm times 2^(hm-1), allowing zero population of either color. For K_{2,2,b}, adding the inequalities forces b<=5, and the allowed r for b=2,3,4,5 are {0,1}, {1}, empty, {2}, respectively. Independent replay from adjacency, rational utility and pair counts covered 16 graph/type cases, 35,349 states and 243,582 moves; direct equilibrium totals at b=3,4,5 were 68,96,252. Finite replay supports, but does not replace, the proof.

## originality

PASS

There is real existing coverage of regular-graph convergence and a close catalogue result for two parts. Neither establishes the exact h>=3 unequal-part increment and binary classification or the three-part arithmetic example. No novelty is credited merely for convergence on regular graphs.

## value

PASS

The utility is an established strategic model, and finding all binary equilibria at any population is substantially stronger than proving some equilibrium exists. The mixed-full-part obstruction and nonmonotone three-part witness show what vacancy-dependent normalization and integer occupancies change on unequal graphs. The polynomial is a labeled census supported by a structural criterion rather than a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
