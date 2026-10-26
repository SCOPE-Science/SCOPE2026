# Review of strict-quorum successor rigidity

## Correctness

PASS. The quorum condition and partial-function property give unique outgoing and incoming adjacency by disjoint-support pigeonholing. A union containing a spanning directed path and obeying both degree bounds can only be that path or the arc joining its last vertex to its first. In the cycle case every named spanning successor relation omits exactly one arc; the quorum translates to a bound on omission multiplicities. Exact labelled allocations then prove both the census and the diversity formula. Explicit small counterexamples prove the strict-majority boundary is sharp. `checker.py` exhaustively corroborates the claimed finite cases; universal correctness rests on the proof, not extrapolation.

## Originality

PASS within the inspected primary literature and mathematical-record comparisons. Michaliszyn--Witkowski (arXiv:2610.09758v1, Section 7) study budgets for lost reference adjacencies and provide an illustrative three-block cyclic rotation; that example is prior art. Jeż--Michaliszyn--Witkowski (arXiv:2610.19943) count unrestricted local-profile realisations in a decision procedure. Neither inspected text claims the all-quorum model classification or its exact diversity distribution. Targeted searches for majority adjacency aggregation, cyclic cuts of paths, equivalence under permutation rotations, exact tables, and stronger results located no decisive implication. Absence of a search result is not a uniqueness proof; an older permutation-consensus formulation remains a risk.

## Value

PASS. The new condition is a natural two-variable first-order way to require local consensus across arbitrarily many successor orders. Unlike a generic decidability bound, the theorem completely classifies its finite models: at strict majority, every nontrivial model has a single cyclic scaffold, all distinct successor relations differ in exactly one adjacency replacement, diversity two is impossible, and every larger allowable diversity has a closed multiplicity formula. It identifies the exact minimum world count for a nontrivial model and shows the quorum boundary cannot be lowered. These structural and quantitative facts are useful when separating local overlap constraints from global spanning-path conditions.

## Sources and risk

Relevant primary texts: arXiv:2610.09758v1, introduction, Section 7 and conclusion; arXiv:2610.19943, introduction, Sections 3--6 and quantitative recurrence appendix. Closest mathematical-record analogues concern pairwise-order majorities, common-block decomposition and successor-path quantifier ranks, not the stated strict quorum. An older adjacency-consensus paper could conceivably state a dominating result. The general-complexity statements from the sources and the standard combinatorial identities are not claimed as new.

Self-review: passed. Independent audit: not yet performed.
