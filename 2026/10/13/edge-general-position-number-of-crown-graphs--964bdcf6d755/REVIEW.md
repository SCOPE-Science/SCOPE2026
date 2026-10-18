# Independent mathematical audit

## correctness

PASS

In Cr_n=K_{n,n}-M, n>=3, the diameter-three geodesics are exactly a_i-b_j-a_k-b_i for distinct i,j,k. Map the edge a_i b_j to the arc i->j. The selected three edges on each such geodesic map bijectively to a directed transitive triangle (ordered k->i->j with shortcut k->j). For every selected arc u->v of a T3-free loopless digraph the out-neighborhoods of u,v are disjoint and so are their in-neighborhoods. Summing their cardinalities over arcs gives sum_w(d+(w)+d-(w))^2 <= 2mn where m is the arc count; Cauchy-Schwarz gives 4m²/n<=2mn and m<=n²/2. A bidirected cut with balanced index parts has 2floor(n/2)ceil(n/2)=floor(n²/2) arcs and is triangle-free. Independent literal geodesic/arc triple enumeration checked all 64, 4096, and 1,048,576 candidate edge subsets for n=3,4,5; their maxima were 4,8,12. Finite checking is not the proof.

## originality

PASS

The 2021 founding paper proves edge-general-position extrema for cycles/trees/hypercubes/grids; Cr_3=C6 and Cr_4=Q3 are known, but not the whole deleted-matching family. The 2024 extremal and 2025 diameter-three articles cover other regimes and block graphs, not a growing quadratic crown formula. Semantic Resultary hits for crown metrics and neighborhood coloring concern different invariants. No covering all-n edge-geodesic theorem or directed-T3 extremal implication was identified.

## value

PASS

The crown graph is a natural dense, symmetry-rich graph formed by a single perfect matching deletion; its geodesics change drastically from those of complete bipartite graphs. Determining gp_e for all n resolves a motivated graph parameter, and its sharp translation to transitive-triangle-free digraphs is a reusable structural extremal method rather than a computed small graph table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
