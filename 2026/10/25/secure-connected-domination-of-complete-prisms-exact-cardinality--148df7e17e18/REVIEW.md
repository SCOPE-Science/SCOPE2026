# Scientific assessment: complete-prism secure connected domination

## Correctness

**PASS.** The result uses the original single-vertex defender definition. A connected dominating selection in both clique layers must contain a matching edge, and a one-layer selection cannot be secure under replacement. With at least two vertices in each layer, any omitted vertex can replace a same-layer selected vertex without erasing the final selected matching edge. If one layer has only one selected vertex, all vertices of the other layer are necessary and sufficient. These arguments establish the exhaustive classification. Disjoint-pair subtraction yields the bivariate and univariate polynomials, while inclusion-minimality reduces to intersecting two-by-two pairs and one-layer-singleton/opposite-layer-full sets. The independent graph-definition checker agrees on all 87,360 vertex subsets for clique orders three through eight. The infinite statement is proved symbolically, not inferred from the census.

## Originality

**PASS, with publication-priority uncertainty.** The original 2014 single-replacement secure connected domination work gives the definition, general criteria, and formulas for paths, cycles, joins and coronas; the 2015 follow-up treats joins and lexicographic compositions. The 2020 algorithmic paper treats an ordinary ladder \(P_n\square K_2\), not \(K_n\square K_2\). No inspected result specializes directly to this exact set classification, cardinality polynomial, or inclusion-minimal census. The 2013 secure-set literature and a 2026 similarly titled connected-secure polynomial use the different secure-alliance condition rather than the single-replacement criterion. General indexed results on complete multipartite graphs concern nonisomorphic graph families or different domination predicates. No dominating equivalent was found in the queried resources, but an unindexed or differently named formula remains possible. An independent priority investigation has not been performed.

## Mathematical value

**PASS.** The graph is a natural, connected and regular Cartesian product. Every admissible one-attack repair configuration is counted, refined by occupation of its two cliques, and every inclusion-minimal configuration is characterized. The constant optimum of four masks an arbitrarily large difference from the largest irredundant configuration, namely \(n-3\), with exact multiplicities. Such a distinction matters when monitoring sets are assembled greedily rather than globally optimized. This is a finite-graph structural theorem for an infinite family, not an arbitrary small numerical slice.

## Limits and closest literature

The theorem addresses secure connected domination as defined by permitted single-vertex replacements, not eternal security, secure defensive alliances, or secure *total* domination. It does not classify partial matchings or general Cartesian products. Closest primary literature: Cabaro–Canoy–Aniversario (2014), Cabaro–Canoy (2015), and Pavan Kumar–Venkata Subba Reddy–Arumugam (2019/2020). The similarly named Andoyo–Rulete (2026) polynomial uses a distinct secure-alliance property. Targeted full-text and published-record comparisons are documented in AUDIT.json; exhaustive publication uniqueness is not established.

Self-review: passed. Independent audit: not yet performed.
