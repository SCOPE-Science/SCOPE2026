# Six vertices are the sharp fixed-order-and-size reversal boundary for adjacency and nonbacktracking spectral radii
## Finding
For a connected finite simple undirected graph \(G\), let
\[
\rho_A(G)
\]
be the spectral radius of its adjacency matrix, and let
\[
\rho_B(G)
\]
be the spectral radius of its Hashimoto nonbacktracking matrix.

Compare graphs only when they have the same order \(n\) and the same size \(m\). Then no pair with
\[
n\le5
\]
has opposite strict rankings under \(\rho_A\) and \(\rho_B\).

The bound is sharp. At
\[
n=6,\qquad m=7,
\]
let \(G\) have edge set
\[
E(G)=\{01,02,03,04,05,23,45\}.
\]
Equivalently, \(G\) consists of two triangles sharing a common hub, together with one pendant leaf attached to that hub.

Let \(H\) have edge set
\[
E(H)=\{04,05,13,14,23,24,34\}.
\]
Equivalently, \(H\) is obtained from \(K_4\) minus one edge by attaching a pendant path of length two to a degree-three vertex of that core.

Their adjacency spectral radii satisfy
\[
\rho_A(G)\approx2.709275359436925
>
2.705586727307842\approx\rho_A(H).
\]

Their nonbacktracking spectral radii satisfy
\[
\rho_B(G)=\sqrt[3]{3}\approx1.442249570307409
<
1.521379706804568\approx\rho_B(H),
\]
where \(\rho_B(H)\) is the positive root of
\[
x^3-x-2=0.
\]

Thus the two spectral quantities reverse their strict ranking on graphs with exactly the same vertex count and edge count.

In threshold language, an adjacency-based inverse spectral surrogate
\[
\tau_A=\frac1{\rho_A}
\]
ranks \(G\) as having the lower threshold, while the nonbacktracking/message-passing surrogate
\[
\tau_B=\frac1{\rho_B}
\]
ranks \(H\) as having the lower threshold.

## Assumptions and scope
Graphs are finite, connected, simple, and undirected.

The comparison fixes both order and size, so the reversal is not caused by changing network population or edge density.

The theorem is a statement about two graph spectral quantities and their inverse threshold surrogates. It does not identify them as two exact thresholds for one universal epidemic model. Adjacency-based thresholds arise under epidemic mean-field approximations, whereas the nonbacktracking threshold arises exactly for locally tree-like percolation/message-passing models and is a bound or approximation more generally.

Trees have
\[
\rho_B=0,
\]
and connected unicyclic graphs have
\[
\rho_B=1.
\]
These degenerate lower-cycle-rank cases are included in the exhaustive lower-order verification.

## Proof
For each
\[
2\le n\le5,
\]
the verifier enumerates every labeled simple graph, filters for connectivity, and quotients by all vertex permutations. It recovers exactly
\[
1,\ 2,\ 6,\ 21
\]
connected unlabeled graphs on
\[
2,\ 3,\ 4,\ 5
\]
vertices.

For each isomorphism class, it computes the adjacency characteristic polynomial
\[
\det(\lambda I-A).
\]
The Perron root is isolated exactly with a Sturm sequence over rational polynomials.

For the nonbacktracking spectral radius, the computation uses the Ihara--Bass determinant relation. If \(D\) is the degree matrix, the nontrivial nonbacktracking eigenvalues are encoded by
\[
\det\!\left(\lambda^2 I-\lambda A+D-I\right).
\]
For connected trees and unicyclic graphs, the known values \(0\) and \(1\) are used directly. In every multicyclic lower-order comparison, the dominant positive roots are isolated by exact rational Sturm intervals; if intervals overlap, a polynomial greatest-common-divisor test distinguishes genuine equality from unresolved numerical proximity.

The graph classes are grouped by the same pair
\[
(n,m),
\]
and every unordered pair is checked. No opposite strict ordering occurs through five vertices.

For the six-vertex witness, the adjacency characteristic polynomials are
\[
\chi_G(\lambda)
=
(\lambda-1)(\lambda+1)^2
(\lambda^3-\lambda^2-5\lambda+1)
\]
and
\[
\chi_H(\lambda)
=
\lambda(\lambda^5-7\lambda^3-4\lambda^2+7\lambda+4).
\]
Exact Sturm isolation gives disjoint Perron-root intervals proving
\[
\rho_A(G)>\rho_A(H).
\]

For \(G\), the dominant nonbacktracking root satisfies
\[
\lambda^3-3=0,
\]
so
\[
\rho_B(G)=\sqrt[3]{3}.
\]
For \(H\), the dominant nonbacktracking root satisfies
\[
\lambda^3-\lambda-2=0.
\]
Exact Sturm isolation gives
\[
\rho_B(G)<\rho_B(H).
\]
Therefore six vertices are sufficient, while the exhaustive lower-order census proves they are necessary.

## Verification
The embedded `verify_adjacency_nonbacktracking_boundary.py` uses only the Python standard library.

It implements exact polynomial arithmetic over rational numbers, determinant expansion, polynomial greatest common divisors, squarefree reduction, Sturm root counting, graph connectivity, and graph canonicalization under vertex relabeling.

Run:

`python3 verify_adjacency_nonbacktracking_boundary.py`

The output must include the connected-unlabeled counts
\[
1,\ 2,\ 6,\ 21,
\]
the marker `NO_REVERSAL_THROUGH_5`, the certified six-vertex witness intervals, and finally `VERIFY_OK`.

The proof does not infer an infinite statement from a partial random search: the lower-order domain is finite and exhaustively enumerated.

## Relationship to prior work
Wang, Chakrabarti, Wang, and Faloutsos connected an epidemic-threshold approximation on a network to the largest adjacency eigenvalue. This supplies the epidemiological meaning of the adjacency spectral surrogate.

Karrer, Newman, and Zdeborová derived the nonbacktracking matrix from message passing for network percolation and showed that, on locally tree-like networks, the critical occupation probability is the reciprocal of its leading eigenvalue. They also compare adjacency- and nonbacktracking-based bounds.

Lin and Zhou study the graph-theoretic relationship between adjacency and nonbacktracking spectral radii, including inequalities and extremal families. Their discussion makes clear that the two radii need not have a simple graph-by-graph relationship.

The present result is narrower and finite: after controlling both graph order and graph size, it identifies the exact first order at which the two spectral radii can rank two connected graphs in opposite strict directions. Targeted searches for ranking reversals, fixed-edge comparisons, exact small witnesses, and adjacency-versus-Hashimoto ordering did not locate this six-vertex boundary.

## Limitations
The theorem compares spectral surrogates, not observed epidemic sizes or exact thresholds for every stochastic epidemic process.

The nonbacktracking matrix is especially natural for locally tree-like percolation and message-passing approximations; short loops can change the quality of that approximation.

The result proves the first order at which a reversal is possible but does not classify all reversing pairs on six or more vertices.

A small witness could occur in unindexed computational material even though the sharp fixed-order-and-size boundary was not located in the checked literature.

## References
1. Y. Wang, D. Chakrabarti, C. Wang, and C. Faloutsos, “Epidemic Spreading in Real Networks: An Eigenvalue Viewpoint,” *22nd Symposium on Reliable Distributed Systems*, 25–34, 6–8 October 2003. DOI: 10.1109/RELDIS.2003.1238052.
2. B. Karrer, M. E. J. Newman, and L. Zdeborová, “Percolation on sparse networks,” arXiv:1405.0483, first submitted 2 May 2014; later *Physical Review Letters* 113, 208702. DOI: 10.1103/PhysRevLett.113.208702.
3. H. Lin and B. Zhou, “On the non-backtracking spectral radius of graphs,” *Electronic Journal of Linear Algebra* 38, 254–265, 2022. DOI: 10.13001/ela.2022.6507.
