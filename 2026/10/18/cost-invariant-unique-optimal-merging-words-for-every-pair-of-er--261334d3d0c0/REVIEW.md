# Scientific review

## Correctness — PASS

The pair-potential formula includes all \(n\ge3\), all unordered distinct initial pairs, and all positive real letter costs. The two branch inequalities and their unique equality cases are derived from explicit \(a,b\) actions on pairs; finite descending paths show existence, telescoping gives global optimality, and strictness proves uniqueness. The signed component comparison prevents any cost-ratio crossover. Direct counting by circular gaps yields a bijection between pairs and integer distances \(1,\ldots,\binom n2\). Two genuinely different finite checks reproduce exact distances and action uniqueness through \(n=40\), and forward shortest-word multiplicities through \(n=23\). Numerical checks are not used as an infinite proof.

## Originality — PASS, with documented uncertainty

Vorel (arXiv:1403.3972) studies binary subset-synchronization complexity and growth, rather than an exact pair-by-pair weighted policy. Gusev (arXiv:1404.6731), Section 3, explicitly supplies the Černý pair-state graph for expected synchronization under random input, the closest known antecedent. That **graph** substantially overlaps the present mechanism, and individual unweighted distances could in principle be deduced from it; the inspected material does not assert cost-ratio-invariant **unique** optimum words, simultaneous separate minimization of both action counts, or the bijective full pair-distance spectrum. Ruszil (arXiv:2103.16185) studies generic weighted synchronization complexity/approximation without such a specialized exact theorem. Related prior-record results concern pair avoidance, altered automata, or resetting two entire automata, rather than this claim. Absence of a direct match in available searches does not establish global novelty; possible earlier implicit derivations and unindexed presentations remain risks.

## Value — PASS

This is an exact all-parameter optimal-control policy, not an arbitrarily selected finite table. For a canonical synchronization-hard automaton, it proves there is **no tradeoff whatsoever** between the two control-action counts for resetting any state pair, even with arbitrarily unequal positive costs. The strict policy generates all pair states in a single Hamiltonian shortest-path chain, with a complete, nonrepeating length spectrum. Those structural facts are relevant when one must merge uncertain pairs with asymmetric or uncertain actuator costs and to understanding the classical pair automaton beyond random hitting times.

## Limits

Restricted to the stated state labeling, pair synchronization, positive costs, and standard two-letter Černý family; no general weighted full reset formula. Residual bibliographic uncertainty requires independent assessment before external assertions of priority.

Self-review: passed. Independent audit: not yet performed.
