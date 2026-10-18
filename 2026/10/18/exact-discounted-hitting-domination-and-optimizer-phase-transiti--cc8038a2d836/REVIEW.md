# Scientific review

## Correctness — PASS

A source-bearing clique with \(s\) pinned peripheral vertices and hub support \(x\) has exactly one unpinned support \(\lambda(x+s)/(q-\lambda(q-s-1))\). Monotonicity yields the tight per-clique source lower bound. When the hub is absent, \(mr\) sources force equal allocation and center support below the floor. At the first feasible hub-free cardinality \(mr+1\), one clique has exactly one extra source, giving a single explicitly solvable hub equation; the other cliques determine the minimum support. Positive marginal discounted hitting support places the new threshold strictly inside each cardinality plateau. Every case, including \(r=0\), \(r=q\), and threshold equality, is included. Exact rational exhaustive replay gives `TOTAL_EXACT_OK 132` from `verify.py`; it is corroboration, not the universal proof.

## Originality — PASS, with residual risk

Allagan–Pereyra–Massey (arXiv:2609.31535v1) provides the invariant, equilibrium representation, and results for spiders, stars, complete graphs and arbitrary-graph algorithms; its graph-specific statements do not give the optimizer census for clique windmills. The Guo–Lin–Wang–Wong–Lin group-hitting paper addresses pointwise target-set queries and ranking, not simultaneous uniform-floor minimum-source placement. A published exact result for complete bipartite graphs is different in both graph class and extremizer formula, and a windmill dissociation polynomial concerns another graph property. Searches for windmill, friendship, clique bouquet, discounted hitting, pinned dynamics, and source placement revealed no stronger implication covering this result. Unindexed mathematics and other terminology remain risks.

## Value — PASS

Clique windmills are natural one-cut-vertex block graphs, intermediate between the stars and complete graphs treated by the initiating paper. The exact cardinality step law, full minimum-set classification, and a genuinely distinct internal threshold for whether high-degree-hub omission is compatible with optimality describe the entire family for every admissible real fidelity and floor. The number of feasible optimum placements can fall discontinuously without changing the optimum budget, an interpretable redundancy transition in discounted network coverage. For example, a nine-vertex windmill with two four-vertex peripheral cliques and \(\lambda=4/5\) changes from 64 to 16 optimum three-source placements precisely at \(\tau=9/17\).

## Primary sources and limitations

Relevant primary source sections were read: Allagan–Pereyra–Massey, Sections 2, 5, 6, 7 and concluding remarks; Guo et al., abstract, definitions and conclusion. Other mathematical records were compared by their stated claims, without claiming that an abstract or indexed summary is a complete full-text inspection. The theorem excludes heterogeneous cliques or discount rates; no external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
