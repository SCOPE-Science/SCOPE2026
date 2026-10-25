# Five exceptional scale-two Rips homotopy types for \(GP(n,2)\)

## Finding
Let \(K_n=\operatorname{VR}_{\le 2}(V(GP(n,2)),d_{GP(n,2)})\). For exactly the five integers \(8\le n\le12\), its integral homotopy type is
\[
K_n\simeq
\begin{cases}
S^2,&n\in\{8,10\},\\
S^1,&n\in\{9,11\},\\
\bigvee^3 S^2,&n=12.
\end{cases}
\]
Thus the scale-two graph-square clique complex has no integral torsion in these five cases. In particular, the three mod-two degree-two classes at \(n=12\) are integral sphere classes, and \(K_{12}\) is simply connected. The classification is of actual homotopy types, not merely field homology ranks.

## Assumptions and scope
For an integer \(n\ge5\), the generalized Petersen graph \(GP(n,2)\) has outer vertices \(u_i\), inner vertices \(v_i\), and exactly the undirected edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+2}\), with indices modulo \(n\). All graph edges have unit length, and \(d_{GP(n,2)}\) is shortest-path distance between vertices, not Euclidean distance between a chosen realization. The inclusive Vietoris–Rips complex contains a nonempty vertex set precisely when every pair has distance at most two. Equivalently \(K_n=\operatorname{Cl}(GP(n,2)^2)\). The five asserted values are the **entire** domain of the present theorem; neither larger radii nor other Petersen parameters are asserted.

## Proof
The accompanying finite certificate gives an acyclic partial matching of the codimension-one face-incidence graph of each of the five complexes. Here is the fully specified construction and its exact verification criterion.

Number outer vertices \(0,\ldots,n-1\) and inner vertices \(n,\ldots,2n-1\), with \(u_i=i\) and \(v_i=n+i\). Form the three edge families in the preceding definition, compute shortest-path distances by breadth-first search, and enumerate **all** nonempty cliques of the graph in which distance at most two defines adjacency. The face numbers, ordered from dimension zero upward, are

| \(n\) | \(f_0\) | \(f_1\) | \(f_2\) | \(f_3\) | \(f_4\) |
|---:|---:|---:|---:|---:|---:|
| 8 | 16 | 68 | 104 | 58 | 8 |
| 9 | 18 | 81 | 117 | 63 | 9 |
| 10 | 20 | 90 | 140 | 80 | 12 |
| 11 | 22 | 99 | 143 | 77 | 11 |
| 12 | 24 | 108 | 160 | 84 | 12 |

The file `MORSE_CERTIFICATE.json` supplies the explicit pairs \((\sigma,\tau)\), with \(\sigma\) a codimension-one face of \(\tau\), and all unmatched critical faces. The separate checker `verify_gp_small.py` independently reconstructs every simplex and checks that each face appears exactly once, either as one endpoint of a pair or as a critical face. It then constructs the complete directed Hasse diagram, orienting matched incidences upward and every other incidence downward. Its exact topological-sort test visits every face, proving that the directed graph has no cycle; hence the pairs constitute acyclic discrete-Morse matchings.

The resulting critical-cell vectors, indexed by dimension, are
\[
\begin{array}{c|c}
n&\text{critical cells}\\\hline
8&(c_0,c_1,c_2)=(1,0,1)\\
9&(1,1,0)\\
10&(1,0,1)\\
11&(1,1,0)\\
12&(1,0,3).
\end{array}
\]
There are no unmatched cells in dimensions greater than two. Forman's discrete Morse theorem gives a CW complex with exactly those cells in each case. If there is one zero-cell and no one-cells, every attaching map of a two-cell has a one-point target and is constant, giving the stated wedge of two-spheres. If there is one zero-cell and one one-cell, with no higher-dimensional cells, the resulting space is a circle. This proves all five assertions over the integers.

## Verification
Run `python3 verify_gp_small.py` from the same directory as `MORSE_CERTIFICATE.json`; no third-party Python packages are needed. The checker does not trust the certificate's face lists as input: it reconstructs all graph distances and all simplices from the graph definition, validates every matching incidence, checks absence of repeated or omitted faces, and independently confirms acyclicity on the **entire** directed Hasse diagram. Its deterministic conclusion is `GP_SMALL_EXCEPTIONS_EXACT_CERTIFICATE_OK`.

As a separate arithmetic test, the checker builds the full simplicial boundary matrices over \(\mathbb F_2\). The ranks of boundaries in dimensions one through four are, respectively,
\[
\begin{array}{c|c}
n& (\operatorname{rank}\partial_1,\operatorname{rank}\partial_2,
\operatorname{rank}\partial_3,\operatorname{rank}\partial_4)\\\hline
8&(15,53,50,8)\\
9&(17,63,54,9)\\
10&(19,71,68,12)\\
11&(21,77,66,11)\\
12&(23,85,72,12).
\end{array}
\]
These ranks check the Betti numbers but are not used to infer integral homotopy; the matching and discrete-Morse theorem provide that inference.

## Relationship to prior work
Adamaszek's study of clique complexes of graph powers identifies \(\operatorname{Cl}(G^r)\) with discrete graph-metric Rips complexes and gives a collapse theorem under a girth bound. The bound at radius two is at least seven, whereas the graphs here have five-cycles, so that theorem does not yield this five-case classification [1]. Feng and Nukala obtain scale-two sphere-wedge results for selected levels of Boolean-subset metrics, a different class of spaces [2]. Their results do not identify the present graphs' Rips complexes.

The separately published result *A sharp twelve-to-thirteen Rips collapse transition in generalized Petersen graphs* establishes the circle collapse for \(n\ge13\) and three independent mod-two degree-two classes at \(n=12\) [3]. Neither assertion yields these five integral homotopy types: knowing mod-two homology does not establish simple connectivity or identify higher attaching maps. The present calculation provides the complete homotopy behavior in the finite interval immediately preceding that stable range. The \(n=10\) member is also the dodecahedral graph; its inclusion is for the natural exhaustive parameter statement, not a claim that every constituent case was previously unknown.

## Limitations
Only the five listed parameters and the inclusive scale-two vertex metric are certified. No homotopy types are asserted for other scales or for \(GP(n,k)\) with \(k\ne2\). The proof is finite but exhaustive at each specified parameter; it is not an induction over an unbounded family. The available bibliographic search cannot exclude every unindexed equivalent calculation. No independent audit or third-party verification is claimed.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first submitted 2011-04-03), especially the graph-square stability results.

[2] Z. Feng and N. C. P. Nukala, *On Vietoris-Rips complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664 (first submitted 2023-02-28), sections on Boolean-level metrics.

[3] *A sharp twelve-to-thirteen Rips collapse transition in generalized Petersen graphs*, public research record, 2026-10-11; directly comparable range \(n\ge13\) and the reported mod-two boundary at \(n=12\).
