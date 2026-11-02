# Scientific review

## Correctness — PASS

The complete proof reconstructs the closed-neighbor and outside-neighbor conditions directly. The two incidence obstructions are necessary and sufficient, and the key intersection fact—that a full omitted row and a full omitted column force every present incidence edge into a nontrivial connected component—is verified explicitly in the argument. Inclusion--exclusion independently counts each obstruction and subtracts the second from the isolate-free class. The three probability laws follow from exact factorial moments and vanishing exceptional-event bounds, not finite extrapolation. The standalone program independently tested the original predicate and polynomial on \(70{,}480\) selected subsets over six labeled board sizes. The infinity claims are proved symbolically; computation is finite corroboration.

## Originality — PASS, with residual priority uncertainty

The 2014 general Cartesian-product characterization by Canoy is the closest structural predecessor. It covers the general notion of product restrained domination and can imply the feasibility condition after specialization, but it neither supplies the closed rook-graph polynomial nor proves the three square-board probability laws. The 2021 Paul--Chauhan--Swain full text concerns cycle enumerators; even its cycle generating-function method does not imply the bipartite-incidence intersection count. Searches for rook-graph, line-graph, incidence-graph, and reliability aliases in published mathematical records identified no equivalent enumerator or limit theorem. The nearest indexed items address restrained domination on crown graphs and chain graphs or different rook-graph invariants, so there is no demonstrated dominating coverage. General Poisson limit methods are known and not claimed as original. Residual risk: an unindexed equivalent reformulation in random bipartite graph or specialized line-graph literature could exist.

## Mathematical value — PASS

The all-cardinality polynomial gives precise counts of guard-placement configurations for arbitrary rectangular dimensions. The three asymptotic regimes reveal two qualitatively different obstructions (uncovered row/column crosses versus isolated omitted cells) and a nonmonotone transition near fully selected configurations. These results concern the naturally motivated reliability of restrained placement rather than a narrow arbitrary coefficient or an unsupported scalar gain.

## Closest literature and limits

Sources inspected: Canoy, *Restrained Domination in Graphs Under Some Binary Operations* (2014), Cartesian-product Theorem 3.1 and its proof, and Paul--Chauhan--Swain, arXiv:2111.11140 (2021), abstract, introduction, cycle enumeration theorems and conclusion. This is a self-review only; an independent literature audit has not been performed. The standalone finite checker cannot establish infinite cases or publication priority.

Self-review: passed. Independent audit: not yet performed.
