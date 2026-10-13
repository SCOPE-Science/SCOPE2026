# Scientific review: complete metric bases of Tutte's eight-cage

## Correctness — PASS

The incidence construction of the 30-vertex graph is explicit. The pair-distance lemma is independently checked against graph-theoretic breadth-first searches for all pairs. Every opposite-side vertex pair is automatically distinguished by parity, and all 210 same-side pairs produce finite hitting constraints. There are exactly 142,506 candidate five-sets and 593,775 six-sets; full enumeration finds no five-set resolving and precisely 32,460 six-set resolving. Monotonicity excludes smaller sizes. A separately implemented C++ program applies the *direct* distance-signature definition to all those candidates and obtains the same answer. The complete group order 1,440 is justified by a checked duality and the six-star rigidity of the line graph of the complete graph on six symbols. Its 34 orbits are partitioned without omission, and their sizes add to the total. Scope is finite and no theorem for arbitrary-order generalized quadrangles is inferred.

## Originality — PASS, with stated priority risk

Bailey's arXiv:1312.4973v1 already records the metric dimension as 6; that previously known scalar is not a novelty claim. Bailey's arXiv:1312.4971 treats imprimitive distance-regular graphs and cites that specific value. Bartoli–Héger–Kiss–Takáts arXiv:1706.06583 studies incidence geometry and metric-dimension bounds, but its generalized-quadrangle analysis does not tabulate or classify all 30-vertex Tutte-cage metric bases. Searches for alternative names, graph incidence dualities, base counts 32,460 and 34 orbits, and related result registries returned no stronger statement implying the optimum multiplicity or symmetry partition. An unindexed enumeration, appendix or database could still contain equivalent results. This review does not claim exhaustive knowledge of unpublished work.

## Value — PASS

The Tutte eight-cage is the unique 30-vertex cubic graph of girth eight and a natural small generalized-quadrangle incidence graph. The earlier scalar metric dimension does not distinguish feasible optimal landmark placements. The result completely enumerates them, gives the full symmetry reduction into 34 inequivalent placements, and records their induced adjacency and two-side allocations. That invariant and classification are natural for the graph, not an arbitrary parameter slice; they make the known minimum reproducible and supply explicit inequivalent extremal configurations.

## Closest literature, verification, and limitations

The main closest source is Bailey, *The metric dimension of small distance-regular and strongly regular graphs* (arXiv:1312.4973), whose existing minimum-size claim is fully credited. Other inspected primary texts include Bailey arXiv:1312.4971 and Bartoli et al. arXiv:1706.06583. Both exact-source verifiers and all orbit representatives are supplied. The finite count and group action are complete only for this graph, and an earlier equivalent classification not found in the inspected material remains a priority risk. The review is not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
