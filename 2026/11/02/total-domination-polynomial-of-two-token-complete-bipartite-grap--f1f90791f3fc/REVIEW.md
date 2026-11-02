# Review of the total-domination polynomial for two-token complete-bipartite graphs

## Correctness: PASS

The claim concerns all labelled two-token graphs \(F_2(K_{m,n})\) with \(2\le m\le n\). The proof identifies their bipartition into mixed and pure token vertices. Its two necessary-and-sufficient open-neighborhood conditions are checked directly against the token-slide edge definition, including domination of selected vertices themselves. Inclusion–exclusion gives the two polynomial factors. Independent lower bounds on the selected mixed and pure vertices are attained simultaneously. The minimum-set multiplicity counts functions using all but at most one host row and minimum edge covers on one of the two host sides. For odd host size, the minimum edge cover is a single three-vertex path plus disjoint edges. No limiting argument or finite-experiment extrapolation is needed for the universal formula. The standalone verifier compared the entire polynomial against direct token-graph subset enumeration in six small parameter cases and against separate subset enumerations in three further cases; it also checked 56 minimum-coefficient cases.

## Originality: PASS, with historical-priority qualification

The two closest primary preprints (arXiv:2610.28936v1 and arXiv:2610.31557v1) determine the ordinary, closed-neighborhood domination number and discuss the same token graph, but neither states the complete *open-neighborhood* total-domination polynomial or its Stirling-number minimum-set multiplicity. Ordinary domination cannot imply the claimed counting formula: a vertex in the dominating set can satisfy ordinary domination without an external neighbor, and the minimum values differ in the precisely stated exceptional families. Related public mathematical-record results about complete multipartite graphs, chain graphs, and total-domination variants concern other graph families or altered domination constraints. Earlier accessible findings on minimum ordinary domination of \(F_2(K_{3,n})\) and on the adjacency kernel of \(F_2(K_{m,n})\) do not imply total-domination enumeration. Targeted exact-phrase, alias, and structural searches did not identify a covering statement. Residual risk: historical work on symmetric squares or double-vertex graphs might contain an equivalent result under other terminology; independent priority review is not claimed.

## Mathematical value: PASS

Two contemporaneous papers determined the ordinary domination number of this natural token-graph family. The new result gives every total-dominating-set coefficient, not merely a minimum value, and exactly counts the labelled optimal configurations via Stirling numbers and minimum edge-cover multiplicities. The distinction from ordinary domination is concrete: the difference is exactly one in the exceptional ordinary-domination regimes and zero elsewhere. The factorization reflects two structurally distinct coverage mechanisms (mixed-token incidence and pure-token edge covers), and is useful for studying redundancy or uniformly sampled total-dominating sets. This is a natural infinite two-parameter exact enumeration problem rather than an arbitrary finite slice or a numerical restatement of the cited minimum formula.

## Scope and risks

Only two tokens and complete bipartite host graphs with both parts of size at least two are covered. Computational checks are finite corroboration; the written proof supplies the universal quantifiers. The primary literature comparison used relevant full-text definitions, theorems, and proofs, and does not certify exhaustive historical priority.

Self-review: passed. Independent audit: not yet performed.
