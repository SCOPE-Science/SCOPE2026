# Independent mathematical audit

## correctness

PASS

The 126 transmitted multisets are weak compositions of 5 into 5 parts; two have a shared deletion descendant iff their L1 distance is two. Thus codes are independent sets in the unit-transfer graph, or size-26 cliques of its complement. Source verify_n5.cpp uses a greedy proper coloring of every candidate subgraph: prefix color numbers give a rigorous upper bound on later clique extension. Independent C++17 code implemented the vertex compositions in reverse lexicographic ordering, edges from L1>2, and a separate coloring-branch enumeration; it visited 93,475,251 nodes, obtained exactly six size-26 cliques, and matched these to the six distinct checksum-zero classes among all 120 label permutations. For each class, independent deletion shadow enumeration found exactly all 70 received profiles. Any clique size>=27 would contain at least 27 distinct 26-subcliques, so the six-class census excludes it. The root-of-unity filter gives |C_f|=(binom(9,4)+4)/5=26. Affine checksum relabeling yields stabilizer size20, S5 orbit size6; exact positive-coordinate profile (5):5,(3,1,1):10,(2,2,1):10,(1^5):1 gives 5+30+30+5=70 shadows. The finite census is exhaustive for q=n=5 only; no other-parameter extrapolation.

## originality

PASS

Same-object and stronger-implication search compared: The complete equality-case classification is compared in multiset-channel, monomial-graph, simplex-packing, perfect deletion-ball and additive-checksum language; none of the inspected statements lists all six maximum sets. Broad optimum-size results dominate the size assertion but not the all-optima theorem. The independently verified exhaustive search is necessary to distinguish other 26-element independent sets, which a sharp upper bound does not automatically identify. Known 26-size bounds plus existence of six checksum codes only show at least six maxima; the independent exhaustive 26-clique enumeration proves no additional maximum exists, and hence perfection and orbit structure for every maximum. A semantic Resultary query was executed for this problem. All source limitations and possible hidden equivalences are retained as residual risks, not misreported as proof of absolute priority.

## value

PASS

At a natural multiset deletion-channel parameter whose extremal size was already known, determining every equality codebook, exact algebraic rigidity, symmetry and perfection is an independently useful complete finite classification. It identifies that no nonadditive maxima exist and supplies a benchmark for multiset-code rigidity, without suggesting a new code rate or arbitrary parameter theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
