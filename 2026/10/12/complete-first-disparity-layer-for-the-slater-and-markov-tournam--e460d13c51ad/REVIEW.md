# Independent mathematical audit

## correctness

PASS

The Markov transition matrix is column stochastic because outdegree at j plus incoming wins against j equals n-1, and stationary solution exists uniquely in the tournament setting. The Slater criterion maximizes arcs consistent with a linear order. Independently rebuilt all labeled tournaments n=1,…,5 and computed Slater maxima by direct all n! ordering enumeration, and exact Markov winners by rational Gaussian elimination; the original source additionally supplies independent subset-DP and matrix-tree-cofactor implementations, each inspected. The exact discrepancy counts are 0 through n=4, and 240 at n=5 of 1024, with the 240 all satisfying MA⊊SL; the two strict size layers (3,1) and (2,1) each comprise 120 labeled cases. Independently canonicalized these under all 120 relabelings to find two size-120 isomorphism classes, so automorphism order one; rational stationary vectors (9,3,1,13,17)/43 and (1/4,1/12,1/6,1/8,3/8) have the asserted unique maxima. Enumeration is complete for n≤5 only, not larger tournaments.

## originality

PASS

Brandt–Dau–Seedig original 2015 article already computes the first difference threshold d(SL,MA)=5 and first disjointness threshold s(SL,MA)=6, in an exhaustive survey of tournaments of order ≤10; these thresholds are explicitly prior. However its printed comparison table reports onset indices, not all 240 labeled five-vertex mismatch instances, universal MA⊊SL containment, two sizes and exact two isomorphism classes. A separation threshold of six implies only nonempty intersection at order five, substantially weaker than universal strict containment. Related published Resultary five-alternative disparity classifications concern different pairs of tournament rules and do not imply the Slater–Markov special case.

## value

PASS

A complete structural description of the very first disagreement between a global minimum-feedback order and stationary tournament rule is a natural motivated boundary, clarifying why disparity at five precedes separation at six. The two exact asymmetric classes and universal nesting are informative independent of the already-known thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
