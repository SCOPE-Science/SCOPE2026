# Independent mathematical audit

## correctness

PASS

A 3-cycle of a nonconstant binary triple swaps the unique minority bit with another of the two positions, equivalent exactly to exchanging unequal bits at distance 1 or 2; every such edge can be realized by some length-three window even at n=3. Thus the move graph is the k-token graph of the squared path. For any connected base graph, token-slide distance equals min-cost integral transshipment: a directed acyclic optimum has an occupied→unoccupied positive-flow arc whenever the current set differs from target, and this reduces divergence and flow cost by 1. Integral LP duality gives max signed sum of integer edge-1-Lipschitz potentials. Removing any one vertex from P_n^2 leaves it connected, so sorted potential gaps δ_i∈{0,1} cannot have adjacent ones. Summing k windows of m=n-k gaps gives <=ceil(km/2); integer potentials floor((j-1)/2),ceil((j-1)/2) attain it for extreme initial/final blocks. Independent BFS and min-matching tests confirmed all 66,174 ordered word pairs n=3..9; this is evidence, not proof for arbitrary n.

## originality

PASS

The original 2009 token-graph paper introduces exactly the graph formalism and diameter inequalities k(delta-k+1)<=diam<=k delta, but not this specific P_n^2 formula in its inspected Section 3. The 2021 Gray-code appendix identifies the SAME squared-path token graph for adjacent-distance-one-or-two swaps but addresses Hamiltonian Gray code, not metric diameter. The 2026 cyclic burst paper studies one-error correction, not arbitrary sequential distance. Generic transport duality is classical; combining it with squared-path two-vertex-connectivity yields a new exact formula as far as checked.

## value

PASS

The exact diameter is the natural worst-case number of sequential length-three cyclic-permutation bursts at fixed binary composition, with an explicit diametral pair and a transport proof. This addresses global reachability/metric complexity of a previously motivated burst channel, not a re-run of single-burst code tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
