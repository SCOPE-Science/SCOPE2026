# Independent mathematical audit

## correctness

PASS

Individual plant-loss Pr(L_i)=q^{d_i}; joint Pr(L_i∩L_j)=q^{d_i+d_j-c_ij} recover the labelled row degrees d_i and intersections c_ij for q in (0,1). For a<=3 plants these plus pollinator degree multiset determine counts of each exact nonempty pollinator neighborhood: triple-degree columns fix N_123; pair counts subtract triple; singleton counts subtract double/triple. Remaining guild sizes with a+b<=8 are finitely exhaustive: enumerate every nonzero row mask (2^b-1)^a, keep connected incidences, signature (d_i,c_ij,sorted col degrees), calculate rank-sum h_k=Σ_{|S|=k} matching(G[S]) by exact dynamic programming. Independently reimplemented the exhaustive finite test for all 28 guild-size splits a,b>=1 a+b<=8, including 4x4 connected matrix count 36317, 1986 signature groups, with identical h vectors in each signature. For 4x5 witness G rows (25,6,5,3), H rows (22,9,5,3), checks give equal signatures and h_G=(0,5,19,27,17,4), h_H=(0,5,20,30,20,4), matching(H[S])-matching(G[S]) exactly one for seven subsets, otherwise zero, so gap = q(1-q)^2(3-3q+q^2)>0. This is a finite exhaustive minimality certificate to eight total species and an explicit direct nine-vertex witness; it does not extrapolate to all larger networks.

## originality

PASS

The result distinguishes topological plant loss marginals/pairs from an optimized post-removal bipartite matching rank function, and pins down an exact minimum nine-species obstruction. Memmott–Waser–Price (2004) analyses persistence of plants with at least one pollinator, not one-to-one matching capacity; Bock–Rautenbach studies static matching with prescribed degrees, not expected matroid rank under random deletion conditional on all pairwise loss data. Actual Resultary search did not return this separation; residual priority risk lies in transversal-matroid rank reliability/equivalent configuration matrices.

## value

PASS

The distinction between pairwise plant loss predictions and capacity-constrained service assignments is mathematically motivated: pair statistics measure incidences up to order two, whereas Hall/matching capacity responds to higher-order overlap. The nine-species minimal witness, exact positive gap for every q in (0,1), and pointwise dominance give a sharp identifiable boundary under a clearly stated idealized allocation model. It provides a natural negative identifiability theorem, not an arbitrary tiny graph fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
