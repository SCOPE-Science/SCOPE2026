# Exact Kempe metric and symmetry strata of the Petersen four-edge-colouring graph

## Finding

Let \(P\) denote the Petersen graph, and let \(\mathcal K_4(P)\) be the graph of proper edge-colourings with four colours, modulo global permutations of the colour names. Two different states are adjacent precisely if a representative of one is obtained from a representative of the other by swapping two colours on one connected component of the corresponding bichromatic edge-induced subgraph.

**Exact result.** \(\mathcal K_4(P)\) has \(2080\) vertices and \(12600\) edges, is connected, has radius \(5\), and has diameter \(7\). Its complete eccentricity profile is
\[
  (\operatorname{ecc}=5:60,\quad \operatorname{ecc}=6:1860,\quad \operatorname{ecc}=7:160).
\]
Its degree profile is \((12:1840,13:240)\). The natural \(120\)-element automorphism group of \(P\) has \(21\) orbits on the colour states. Their complete size–eccentricity multiplicities are
\[
\begin{array}{c|rrrrrrr}
(\text{orbit size},\operatorname{ecc})&(20,6)&(40,6)&(40,7)&(60,5)&(60,6)&(120,6)&(120,7)\\
\text{number of orbits}&1&1&1&1&2&14&1
\end{array}
\]
In particular, the entire centre is one graph-automorphism orbit, whereas the eccentricity-seven states comprise two orbits of sizes \(40\) and \(120\).

## Assumptions and scope

Set \(u_i=i\) and \(v_i=5+i\) for \(0\le i<5\), with subscripts interpreted modulo \(5\). The simple graph \(P\) has outer edges \(u_i u_{i+1}\), spokes \(u_i v_i\), and inner edges \(v_i v_{i+2}\). The edges are ordered lexicographically as unordered endpoint pairs. A proper four-edge-colouring assigns labels from \(\{0,1,2,3\}\) to all \(15\) edges so that adjacent edges have unequal labels. Colours may be renamed globally: all colourings related by \(S_4\) form one state. The Petersen graph is not three-edge-colourable, so every proper four-edge-colouring uses all four colours.

A Kempe move chooses two colours and one connected component of the subgraph of edges bearing those two colours, then exchanges those two colours on every edge in that component. Global colour renaming is subsequently forgotten. Loops and multiple moves to the same neighbour are discarded. Distances are shortest-path distances in this simple quotient graph; eccentricity is the maximum distance from a state, radius the minimum eccentricity, and diameter the maximum.

## Proof

The finite algorithm in `verify.py` is a complete certificate; its termination is evident because all enumerations are over fixed finite sets. The exhaustive domain and all equivalence reductions are justified here.

1. **State enumeration.** Every orbit under global colour renaming has one and only one canonical representative whose sequence of colours, in lexicographic edge order, starts at \(0\) and introduces each previously unused colour as the smallest unused label. A depth-first enumeration allows an existing colour or the next unused colour at each edge; it rejects precisely choices forbidden by an already-coloured incident edge. Each complete branch is a proper colouring and every canonical colouring appears. The resulting list consists of \(2080\) distinct states, each using exactly four colours. An independent enumeration fixes the three colours on the edges at vertex \(u_0\) to \(0,1,2\), then assigns any of four colours to the remaining edges subject to properness. Because all four colours appear, this is another unique representative of each colour-renaming orbit. Its normalized set agrees with the first enumeration and also has size \(2080\).

2. **Kempe adjacency.** For each state, the checker considers all six unordered colour pairs and determines *all* connected components of the resulting two-colour edge subgraph. Flipping each component and canonicalizing gives exactly the neighbours by definition. It constructs components independently by (a) edge adjacencies in the line graph and (b) edge traversal through common endpoints; the resulting neighbour sets agree for every state. Every neighbour belongs to the enumerated set, the graph is undirected with no loops, and the degree counts are \(1840\) vertices of degree \(12\) and \(240\) of degree \(13\), totaling \(12600\) distinct unordered edges.

3. **Exact distances.** Breadth-first search starting from each one of the \(2080\) states visits all \(2080\) states. Since BFS in an unweighted graph gives shortest path length, the maximum distance on each run is precisely that state's eccentricity. The full census gives counts \(60,1860,160\) at eccentricities \(5,6,7\), proving the radius and diameter and not merely bounding them.

4. **Symmetry.** Enumerate all bijections on the ten graph vertices that preserve every edge and nonedge. A backtracking adjacency-preserving test finds exactly \(120\) automorphisms. Each automorphism permutes the ordered edges; applying it to each colouring and canonicalizing yields the group orbit of that state. The checker partitions all \(2080\) states into these orbits, checks that eccentricity is constant on each, and obtains the seven orbit-type multiplicities displayed above. The sizes weighted by their multiplicities sum to \(2080\), and the multiplicities sum to \(21\).

All numerical assertions are integer equality checks over complete finite sets. They do not rely on a solver's timeout, floating-point approximations, or a random sample.

## Verification

Run `python verify.py` with Python 3.9 or later. Only the Python standard library is used. The script contains independent proper-colouring enumeration paths and independently reconstructs Kempe components in two ways, exhaustively verifies every graph adjacency, checks each state's shortest-path eccentricity, and enumerates the complete automorphism action. Every claimed numerical quantity is asserted inside the verifier. The replay terminates after a few seconds on a typical computer.

## Relationship to prior work

McDonald, Mohar, and Scheide prove that **all** proper four-edge-colourings of any subcubic graph are Kempe equivalent [1]. This implies the connectedness of this graph but neither determines shortest Kempe distances nor the exact eccentricity, edge-count, degree, or automorphism-orbit profiles of the colour-name quotient for the Petersen graph. The present finding is a quantified exact refinement for the smallest snark, not a new proof of generic connectedness. The 2014 Belcastro–Haas theory of three-edge-coloured cubic graphs studies a different colour count: a snark cannot be properly three-edge-coloured. General papers about vertex-colouring Kempe diameters also treat a different state space and move model.

## Limitations

The classification concerns one fixed ten-vertex graph, precisely four edge colours, and quotienting by arbitrary global colour-name permutations. It does not assert the same metric for the unquotiented graph of fully labelled colourings, for proper five-edge-colourings, or for other snarks. Search cannot establish logical uniqueness or rule out unpublished or poorly indexed tables. The finite verifier is supplied so every claimed exact count can be reproduced; independent audit has not been performed.

## References

[1] J. McDonald, B. Mohar, and D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248 (first public posting 2010-05-13), later *Journal of Graph Theory*, DOI 10.1002/jgt.20613.

[2] S. M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, *Discrete Mathematics* 325 (2014), 77–84.
