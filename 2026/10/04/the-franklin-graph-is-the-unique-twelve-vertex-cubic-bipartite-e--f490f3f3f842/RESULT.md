# The Franklin graph is the unique twelve-vertex cubic bipartite equality graph for paired domination
## Finding
Among connected finite simple cubic bipartite graphs \(G\) on exactly \(12\) vertices,
\[
\gamma_{\mathrm{pr}}(G)=
\begin{cases}
6,&G\cong F_{12},\\
4,&G\not\cong F_{12},
\end{cases}
\]
where \(F_{12}\) is the Franklin graph. Hence the Franklin graph is the unique twelve-vertex equality case for
\[
\gamma_{\mathrm{pr}}(G)\le 2\left\lfloor\frac{|V(G)|}{4}\right\rfloor.
\]
There are exactly five connected simple cubic bipartite isomorphism classes on twelve vertices; four admit a dominating matching of size two, while the Franklin graph requires a dominating matching of size three.

## Assumptions and scope
All graphs are finite, simple, undirected, connected, cubic, and bipartite unless stated otherwise. A paired dominating set is a dominating vertex set whose induced subgraph contains a perfect matching. Its minimum cardinality is \(\gamma_{\mathrm{pr}}(G)\). Equivalently, \(\gamma_{\mathrm{pr}}(G)\) is twice the minimum size of a matching whose endpoints dominate the graph.

The claim concerns exactly order twelve. It does not classify equality for larger cubic bipartite graphs.

## Proof
Let \(G=(X,Y;E)\) be cubic bipartite of order twelve. Degree counting gives \(|X|=|Y|=6\). Encode \(G\) by a \(6\times6\) zero-one incidence matrix \(A\), whose row and column sums are all three.

The finite classification is exhaustive. There are twenty possible row masks of weight three. Enumerating nondecreasing six-tuples of those masks subject to column sums three gives exactly \(550\) semilabeled matrices. Disconnected matrices are discarded. For each connected matrix, isomorphism is quotiented exactly under row permutations, column permutations, and exchange of the two bipartition classes. For a fixed row order, sorting the six column bitstrings gives the canonical representative under column permutations; taking the minimum over all \(6!\) row orders, and then also over the transpose, gives a complete canonical form. Exactly five connected canonical forms remain.

For paired domination, a size-two paired dominating set would be the two ends of one edge. In a simple cubic bipartite graph the union of the closed neighborhoods of adjacent vertices contains exactly six vertices: the two endpoints, the two other neighbors of the first endpoint, and the two other neighbors of the second. Therefore no twelve-vertex cubic bipartite graph has paired domination number two, so every graph in the census has \(\gamma_{\mathrm{pr}}(G)\ge4\).

For four canonical classes, the verifier exhibits two disjoint edges whose four endpoints dominate all twelve vertices. Thus those four classes have \(\gamma_{\mathrm{pr}}(G)=4\).

For the fifth class, represented by the bipartite neighborhoods
\[
\begin{aligned}
N(x_0)&=\{y_0,y_1,y_3\},&N(x_1)&=\{y_0,y_2,y_3\},\\
N(x_2)&=\{y_1,y_2,y_4\},&N(x_3)&=\{y_0,y_4,y_5\},\\
N(x_4)&=\{y_1,y_2,y_5\},&N(x_5)&=\{y_3,y_4,y_5\},
\end{aligned}
\]
the verifier checks every two-edge matching and finds that none dominates. It also exhibits the dominating matching \(\{x_0y_0,x_1y_2,x_3y_4\}\), so this class has \(\gamma_{\mathrm{pr}}=6\).

Finally, the verifier constructs the standard Hamiltonian LCF graph \([5,-5]^6\), canonically bipartition-encodes it, and obtains exactly the fifth canonical form. The LCF graph \([5,-5]^6\) is the Franklin graph. Hence the unique class with paired domination number six is the Franklin graph.

## Verification
The standalone verifier `verify.py` uses only the Python standard library. It performs the complete matrix enumeration, exact canonicalization, connectivity test, exhaustive dominating-matching search, and the Franklin LCF identification. Its recorded output is in `verification_output.txt` and begins with `ALL CHECKS PASSED`.

The run enumerates \(550\) semilabeled regular matrices and obtains exactly five connected isomorphism classes, matching the independent cubic-bipartite graph count tabulated by House of Graphs for order twelve. The five paired-domination values are \(4,4,4,4,6\).

## Relationship to prior work
Lu and Wu proved on September 24, 2026 that every finite simple cubic bipartite graph satisfies \(\gamma_{\mathrm{pr}}(G)\le 2\lfloor |V(G)|/4\rfloor\). Their full text notes \(K_{3,3}\) and the cube \(Q_3\) as equality witnesses but does not classify the twelve-vertex equality cases. Their Proposition 2.2 also records the dominating-matching formulation used here.

The Franklin graph is a standard twelve-vertex cubic bipartite graph; standard references identify it with the LCF graph \([5,-5]^6\). The present finding determines its paired domination number and places it uniquely among all five twelve-vertex connected cubic bipartite graphs.

## Limitations
This is an exact finite classification at order twelve, not an infinite equality characterization. The completeness proof depends on the embedded exhaustive enumerator, although the enumeration is small, deterministic, integer-only, and independently corroborated at the level of the five-class count by the House of Graphs table. The literature search found no prior exact paired-domination classification for the Franklin graph or for all twelve-vertex cubic bipartite graphs, but bibliographic searches cannot exclude every unindexed source.

## References
1. C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs*, arXiv:2609.30152v1, first public 2026-09-24.
2. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks 32 (1998), 199--206.
3. House of Graphs, cubic bipartite graph census table; the order-twelve row lists five connected cubic bipartite graphs.
4. E. W. Weisstein, *Franklin Graph*, MathWorld; identifies the Franklin graph with LCF notation \([5,-5]^6\).
