# Scientific review

## Correctness — PASS

The three rooted-domination states distinguish selected root, root dominated by a child, and root awaiting domination by a parent. Their recurrences are exact because child subtrees are disjoint, with a necessary at-least-one-selected-child condition for the second state. A simultaneous induction on cost gaps and optimum counts yields a strict selected/child-dominated phase and a three-way boundary phase every three levels. It proves **all** minimum vertex sets, not just a cardinality estimate. A separate verifier checks all optimal vertex sets on 313 small-tree instances and the exact minimum/count on 788 further profiles or irregular instances. Finite tests are not treated as proof; the induction covers every permitted height and branching profile. Risk: there is no independent mathematical assessment.

## Originality — PASS (best knowledge)

Closest source: Allagan et al. (arXiv:2601.03485, Theorems 10 and 14), whose full accessible text was inspected. Their binary-tree period-three case is recovered, but their general tree DP does not assert the structural rigidity on arbitrary nonuniform full-depth trees or the optimizer classification. Livingston–Stout (1994), full PDF text inspected, gives a general fixed-arity, fixed-factor algorithm and remarks on possible counting extensions; no formula covering irregular per-vertex degrees was located. Petr–Portier–Versteegen (arXiv:2206.13182), accessible full article inspected, prove general forest extremal bounds, not this subclass equality characterization. Targeted published-finding corpus and web searches using equivalent descriptions, branch profiles and the period-three law did not identify an equivalent or dominating statement. Searches cannot prove priority; this is a best-knowledge assessment with residual risk of less-visible specialized literature.

## Value — PASS

The result is stronger than merely substituting a larger constant arity into a known binary-tree calculation. It identifies **every** minimizer on the entire family of irregular full-depth trees, allowing arbitrary degree changes even within a level, and shows all deeper branching vanishes from the exact multiplicity. The phase classification supplies closed optimum sizes from level cardinalities and a complete rigidity-versus-root-choice dichotomy without executing the general tree dynamic program. These are natural structural questions about the diversity of optimum placements, directly motivated by the recent binary-tree dominion theorem.

## Limitations

No extension to trees with unary branching or unequal leaf depths is claimed. The general minimum-dominating-set DP and binary special case are prior art. Definitive priority and external mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
