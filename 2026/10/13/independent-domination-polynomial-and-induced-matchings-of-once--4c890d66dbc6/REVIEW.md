# Scientific review: independent domination of once-subdivided graphs

## Correctness — PASS

The universal claim has an explicit inverse bijection. Starting from an independent dominating set of the full subdivision, the selected original vertices uniquely determine every inserted-edge vertex: it is selected exactly when neither endpoint is. The remaining domination requirement at each unselected original vertex is precisely the absence of an isolated vertex in the induced original-vertex complement. This establishes both directions of the polynomial formula, all cardinalities, and empty and disconnected boundary cases.

The matching step bounds the saving \(|W|-|E(G[W])|\) by the number of tree components, which cannot exceed the induced matching number because one edge from each component forms an induced matching. An induced matching supplies equality, and equality characterizes all minimum-size sets. For forests, the independently stated three-state recurrence tracks the root's own inclusion and need for a supporting parent; the excluded-at-root and included-supported-at-root states close the recursion without leaving unsupported vertices. No infinitary inference is made from enumeration.

Executable evidence: `CHECK.py` and `CHECK_OUTPUT.txt`, including \(3{,}229{,}975\) directly tested subdivision-graph subsets on exhaustive small and sampled larger base graphs, \(201\) nonisomorphic trees, \(640\) additional random forests, and the explicit \(L_3\) check. The universal conclusion rests on the written proofs; the computations independently probe implementation and boundary errors.

## Originality — PASS, with stated uncertainty

Jahari–Alikhani (arXiv:1808.07369, first posted 2018-08-21) study independent domination polynomials for compound graphs and paths, not an induced-subgraph description of every maximal independent set of a complete edge subdivision. Dod (arXiv:1602.08250) provides broad inclusion–exclusion and corona identities, but neither the induced-matching optimization equality nor the subtree recursion follows as an immediate stated special case. The 2021 Babikir–Dettlaff–Henning–Lemańska article studies the *number of edges requiring subdivision to raise a parameter*, not enumeration after every edge is subdivided. The 2017 Tsukuda paper describes homotopy types of independence complexes of edge-incidence graphs; homotopy type cannot in general determine the number of maximal faces at each cardinality.

The especially close 2019 study “Independent Domination in Some Subdivision Graphs” gives scalar results for particular graph families, including a ladder assertion (Theorem 3.4) that differs from direct enumeration at the three-rung ladder. Its formula yields six whereas a concrete independent dominating set of four vertices and all \(8{,}192\) direct subset checks give four. The discrepancy is explicitly disclosed rather than silently treating that source as corroboration. It does not contain the all-graph classification or polynomial and therefore does not imply this claim. A semantic search of published research records found nearby results on independent domination of other constructions and induced-matching gaps, with no same-input same-output coverage; this is not a proof of absolute novelty.

**Residual risks:** an unindexed explicit formula for incidence-graph maximal independent sets could be equivalent; a pre-existing algorithmic or hypergraph formulation may imply this theorem after a nontrivial translation; external review is needed before publication. The 2019 conflicting family-specific assertion should be reconciled by independent readers. These limitations do not introduce a logical dependence into the present self-contained derivation.

## Value — PASS

This is not a renamed scalar equality or a single numerical table. The bijection classifies *every* maximal independent set of the subdivision of any base graph, gives all coefficients, explains the minimum through the induced matching invariant of the original graph, and classifies every minimum-size set through induced forests. The explicit forest recursion turns the all-subsets formula into a polynomial-time exact enumerator for an infinite and structurally general class. The connection is motivated by independent-domination subdivision literature and by the difference between ordinary, induced and dominating induced matchings. The concrete ladder boundary comparison further shows why a structural criterion is useful beyond extrapolating small-family formulas.

Self-review: passed. Independent audit: not yet performed.
