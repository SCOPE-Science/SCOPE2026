---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a fresh P′ the counterexample sentence in RESULT.md lines 15–19 holds precisely on a same-domain pair X⊆Y where truth is lost. For the upper bound, track matched assignments and counts of unused elements by type. With j remaining quantifier levels, matched unused counts agree below j, are both finite at least j, or are both infinite. Choosing an assigned element preserves this comparison, and choosing a fresh element lowers one count and the budget by one. A fresh element of a given type represents all unused elements of that type. An infinity quantifier therefore only needs to look for a satisfying infinite type (or, for the dual, a counterexample infinite type). This proves profile preservation, including empty models, and gives an evaluator with at most n(2^m+r)^r quantifier-choice/Boolean positions up to polynomial bookkeeping, with m,r=O(n). For hardness θ∧∀x ¬P(x) loses truth between ∅ and D exactly if θ has a nonempty model; an empty model cannot witness a strict increase in P. The precise Lewis prefix citation could not be checked in full, but equality-free ordinary monadic satisfiability hardness also follows directly by an exponential computation tableau: use two sets of b unary bit predicates for time and space on a 2^b by 2^b grid; one existential and two ∀x∃y modular increment axioms guarantee every coordinate pair. Coordinate comparisons and binary successor have polynomial-length equality-free bit formulas. Give each cell exactly one unary label and universally equate labels on identical coordinates. For a fixed nondeterministic exponential-time machine, use a finite label alphabet encoding the tape symbol and, at the head, its state and chosen legal transition. For universally quantified cells at successive times (excluding wrap of time), require the next cell label to be an allowed update of the current three-cell neighborhood. The head's recorded choice makes all overlapping updates consistent, with only the next head's new choice left free. Prescribe the initial row, demand an accepting head in the final row, and choose b polynomial in the input length with grid width and height larger than four times the padded time bound; start at the spatial midpoint and make halting states stutter. The circular spatial successor cannot affect the actual run before it halts. The sentence is polynomial in the input and has a nonempty model exactly for accepting runs. The alleged hardness does not depend on the uninspected details of the cited prefix theorem. This is a proof audit, not a mechanization or a fixed-vocabulary classification.

## originality

PASS

The strongest inspected monadic-infinity source gives a semantic/positive-fragment characterization and decidability, expressly leaving complexity unexplored, while the bounded Resultary searches exposed no material match. Credited ingredients include the type-profile theorem and ordinary monadic satisfiability hardness. The distinct claim is the tight combined-complexity classification with a negative-only hardness restriction, not either credited ingredient.

## value

PASS

An exact combined-complexity answer strengthens a qualitative decidability theorem, and its lower bound within a single syntactic polarity identifies where the cost already occurs. The result handles infinite semantics with an explicit finite representation and avoids suggesting the same complexity for a fixed vocabulary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
