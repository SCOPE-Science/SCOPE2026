# Scientific review

## Correctness: PASS

An exact bijection records selected original vertices, forces all edge-nodes wholly outside them, and forces one chosen boundary edge-node per selected original vertex that has an outside neighbor. The only remaining maximality obstruction is the condition that every outside original vertex of residual degree at most one be hit by a boundary choice. The inverse construction is verified pointwise. Independence of the two bipartite shores gives the Stirling-number double sum; a separate three-case enumeration of the two-vertex shore yields the four-term specialization and exact gaps. The standard-library checker directly tests maximality and all small-case coefficients, not merely a formula-to-formula comparison.

## Originality: PASS (publication priority provisional)

The closest inspected primary source, Tu–Li–Du, arXiv:2103.01402v1, proves global extremal bounds on counts of maximal dissociation sets for arbitrary and triangle-free graphs, not all-size coefficients or exact subdivision-family formulas. Orlovich–Dolgui–Finke–Gordon–Werner (2011) address hardness and algorithmic questions for maximal dissociation, without a covering formula in the accessible sections; full-text comparison is an acknowledged residual risk. Indexed related findings on complete multipartite graphs, fan graphs, and generalized windmills concern different underlying graphs. The equivalent complement formulation as inclusion-minimal 3-path vertex covers was searched for stronger implications without an identified encompassing result. The available evidence supports an original structural correspondence and explicit natural-family gap theorem, but cannot establish exhaustive publication priority.

## Mathematical value: PASS

The structural formula covers every finite base graph, including isolated vertices, and distinguishes a genuine maximality condition from ordinary dissociation feasibility. The family \(S(K_{2,b})\) is connected, sparse, bipartite, and 2-degenerate; its complete polynomial and unbounded missing-cardinality intervals therefore give a natural quantitative phenomenon, rather than an arbitrary finite subcase or minor parameter increment. The complement formulation connects exact enumeration to minimal 3-path vertex covers.

## Limits

The result is for exactly one subdivision per edge. The distinct-four-support statement requires \(b\ge5\), although the polynomial holds from \(b=2\). Direct enumeration is corroborative and finite. Two relevant complexity and structural papers were not fully accessible; hidden or unindexed coverage remains possible. No external independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
