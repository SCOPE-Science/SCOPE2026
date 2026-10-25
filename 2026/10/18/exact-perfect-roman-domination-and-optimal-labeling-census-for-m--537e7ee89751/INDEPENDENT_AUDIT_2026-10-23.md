# Independent mathematical audit

## correctness

PASS

For H_n=M(K2,n), 3n+2 vertices arranged as row vertices plus n column triangles, fixing the set T of label-2 vertices forces a unique cheapest valid completion: label zeros exactly at vertices outside T with exactly one T-neighbor, ones elsewhere. Set p_i as # row edge providers plus indicator for row original. If (p1,p2)!=(1,1), a column triangle of total weight 1 would force both edge vertices zero and hence p1=p2=1; thus all columns weigh >=2 and the row originals jointly >=1, so weight >=2n+1. If p1=p2=1, chosen row providers each exactly one among a_i,e_ij, no optimal column-2 vertices, and exact column accounting gives uniform weight n+4 with (n+1)^2 choices. Equality in nonregular lower bound entails, up to row swap, exactly one selected edge e_ij (no other 2s), yielding 2n exceptional labelings of weight 2n+1. Compare cases: n1 two singleton edge minima of weight3, n2 four minima of weight5, n3 16+6=22 minima weight7, n>=4 only (n+1)^2 regular minima weight n+4. Independent graph implementation and direct exhaustive 2-support enumeration n1..5 verified (3,2),(5,4),(7,22),(8,25),(9,36), including boundary n3. This is full graph-theoretic proof for every n, not finite extrapolation.

## originality

PASS

The 2021 full text by Kim actually poses this complete-bipartite middle-graph calculation as an open problem and establishes paths/cycles/Kneser families instead. Kim's 2024 work treats ordinary Roman, Italian and 2-rainbow rather than the exactly-one-defender perfect Roman condition. Resultary hits on perfect Roman crown graphs, ordinary complete multipartite graphs and their weight polynomials are on the ORIGINAL graph, not its middle graph, and are not a dominating parameter identity. No later K2,n middle-graph solution located in targeted searches; this is best-of-knowledge, not a certification that the 2021 problem was never solved elsewhere.

## value

PASS

Kim 2021 explicitly posed the minimum perfect Roman domination number of the middle graph of a complete bipartite K_{m,n} (Problem 2.1). The two-row subfamily K_{2,n} is a natural first non-star slice, and classifying all minimum functions adds a previously missing exact enumeration to its scalar open question. The tight transition at n=3 is structurally motivated, not an arbitrary finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
