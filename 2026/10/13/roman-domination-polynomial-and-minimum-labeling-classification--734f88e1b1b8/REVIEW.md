# Scientific review: Roman-domination polynomial of triangular graphs

## Correctness — PASS

The characterization is exact: with the label-two set \(F\) fixed, the edges not touching any member of \(F\) are precisely the edges between unused ground vertices, and those edges must receive label one. All remaining non-two edges independently receive zero or one. Inclusion-exclusion counts the two-edge-support graphs with no isolated vertex, including the empty support boundary. The resulting polynomial is a finite identity for all \(n\ge3\). The minimum-weight proof reduces to a sharp edge-cover inequality and determines every equality case, hence every minimum-labeling count. Direct brute-force enumeration of 59,805 possible labelings across orders three to five and a separate all-support enumeration through order six agree with the formulas. Risk: finite checking alone does not prove the general result, but the unrestricted combinatorial argument does.

## Originality — PASS, with stated residual risk

Zec (2023), Theorem 2.1, proves the exact minimum value \(n-1\) and gives parity-dependent witnesses on the **same** triangular graphs. That value and those example constructions are credited rather than claimed. The full text examined does not give the cardinality-by-weight polynomial, does not enumerate all minimum functions, and does not assert their exact multiplicities. The founding Roman-polynomial article of Gangabylaiah et al. (2021) provides formulas for complete graphs, stars, wheels, complete bipartite graphs and graph operations, not the line graph of a complete graph. Related Roman-polynomial results for complete multipartite and chain graphs concern other adjacency classes and do not dominate the stated result. Edge Roman domination of \(K_n\) is an equivalent interpretation considered in the searches. Residual risk: another full enumeration under that name or an unindexed coefficient table might exist. The available evidence supports originality but cannot establish absolute priority.

## Value — PASS

The triangular graph is the first nontrivial Johnson family, and the already known minimum Roman weight leaves the number and weight distribution of feasible configurations unresolved. The polynomial supplies every labeled configuration count, while the equality-case theorem explains the exact parity-dependent number of optimum deployments by a natural perfect-matching correspondence. This is a complete all-order invariant and a structural classification; it is not the isolated recomputation of the known optimum or an arbitrary finite slice. It gives exact enumerative input for probability, sampling, and optimization studies on the family, without claiming any unproved downstream theorem.

## Closest primary literature and limitations

Zec (2023), *Filomat* 37, 2067–2075, DOI 10.2298/FIL2307067Z, is the closest same-graph source. Gangabylaiah et al. (2021), *Bull. Int. Math. Virtual Inst.* 11, 355–365, DOI 10.7251/BIMVI2102355G, is the closest polynomial-framework source. Chambers et al. (2009), DOI 10.1137/070699688, provides the earlier extremal Roman-domination framework. Some equivalent formulations may be indexed under edge Roman domination. Results count labeled functions, not automorphism orbits, and do not address higher Johnson graphs. Independent mathematical verification is not provided.

Self-review: passed. Independent audit: not yet performed.
