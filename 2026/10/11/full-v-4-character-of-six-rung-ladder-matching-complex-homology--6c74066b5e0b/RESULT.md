# Full \(V_4\)-character of six-rung ladder matching-complex homology
## Finding
Let \(L_6=P_6\mathbin{\square}K_2\) be the six-rung ladder graph. Let \(h\) interchange the two rows and let \(v\) reverse the six columns. Then \(\operatorname{Aut}(L_6)=\langle h,v\rangle\cong C_2\times C_2\), \(\widetilde H_i(\mathcal M(L_6);\mathbb Q)=0\) for \(i\ne3\), and the full automorphism action on degree-three homology has character \(\chi(1,h,v,hv)=(5,-1,1,3)\). Equivalently, if \(\chi_{a,b}\) denotes the one-dimensional rational character with \(\chi_{a,b}(h)=a\) and \(\chi_{a,b}(v)=b\), then \(H_3(\mathcal M(L_6);\mathbb Q)\cong2\chi_{1,1}\oplus\chi_{-1,1}\oplus2\chi_{-1,-1}\).

The nonequivariant consequence is \(\mathcal M(L_6)\simeq\bigvee^5 S^3\), a homotopy type already implied by the published grid-matching recursion. The new assertion is the complete rational representation of the full graph automorphism group on the nonzero reduced homology. In particular, the two natural reflections are distinguished: row interchange has trace \(-1\) on \(H_3\), while column reversal has trace \(+1\).

## Assumptions and scope
The graph \(L_6\) has vertex set \(\{0,1\}\times\{0,1,2,3,4,5\}\). Its edges are the six rungs \(\{(0,j),(1,j)\}\) and the ten rail edges \(\{(r,j),(r,j+1)\}\) for \(r\in\{0,1\}\) and \(0\le j<5\). The matching complex \(\mathcal M(L_6)\) has one simplicial vertex for each graph edge, and its faces are the matchings of \(L_6\). The action considered is the action induced by the full graph automorphism group.

No claim is made here about the integral \(\mathbb Z[C_2\times C_2]\)-lattice structure, about other ladder lengths, or about equivariant simple-homotopy type.

## Proof
There are exactly four graph automorphisms. The four degree-two graph vertices are the corners. Among corner pairs, the two pairs at distance one are exactly the end rungs, so every automorphism permutes these two rungs. Once the image of one end rung and the choice of whether its endpoints are exchanged are fixed, adjacency along the two rails determines every remaining vertex. Thus there are at most four automorphisms, and the identity, row interchange \(h\), column reversal \(v\), and their product \(hv\) realize all four. Hence \(\operatorname{Aut}(L_6)=\langle h,v\rangle\cong C_2\times C_2\).

An exhaustive enumeration of \(\mathcal M(L_6)\) gives \(732\) nonempty faces with face vector
\[
(16,92,234,263,114,13).
\]
A staged element matching on the full face poset pairs \(363\) cover relations. Direct acyclicity verification on all \(2586\) Hasse covers leaves one critical \(0\)-cell and five critical \(3\)-cells, and no other critical cells. Forman's discrete Morse theorem therefore gives
\[
\mathcal M(L_6)\simeq\bigvee^5 S^3.
\]
In particular, over \(\mathbb Q\), the only nonzero reduced homology is \(H_3\cong\mathbb Q^5\).

For a graph automorphism \(g\), orient every simplex by increasing edge index. The signed traces of \(g\) on the simplicial chain groups \(C_0,\ldots,C_5\) are obtained by summing the orientation sign over the setwise fixed simplices. In the order \(1,h,v,hv\), these six-tuples are
\[
\begin{aligned}
1 &: (16,92,234,263,114,13),\\
h &: (6,10,0,-9,-2,1),\\
v &: (2,-6,-10,7,8,-1),\\
hv&: (0,-8,0,15,0,-5).
\end{aligned}
\]
Therefore the Lefschetz numbers \(\sum_d(-1)^d\operatorname{tr}(g\mid C_d)\) are \((-4,2,0,-2)\). The Hopf trace formula identifies these with the alternating homology traces. Since \(H_0\) is the trivial one-dimensional representation and reduced homology is concentrated in degree \(3\),
\[
\operatorname{tr}(g\mid H_3)=1-L(g),
\]
which gives \((5,-1,1,3)\). Taking inner products with the four characters of \(C_2\times C_2\) gives multiplicities \(2,0,1,2\) for \(\chi_{1,1},\chi_{1,-1},\chi_{-1,1},\chi_{-1,-1}\), respectively.

## Verification
The accompanying `verify.py` reconstructs the graph and matching complex from definitions, enumerates every face and every Hasse cover, replays the discrete-Morse matching and checks acyclicity, enumerates the full graph automorphism group by exact backtracking, computes all signed chain traces, applies the Hopf trace identity, and checks the character decomposition. It also independently computes simplicial homology over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\); all three give Betti vector \((1,0,0,5,0,0)\). Running the script produces `VERIFY_OK` and the numerical certificate recorded in `verification_output.txt`.

## Relationship to prior work
Braun and Hough studied matching complexes of \(2\times n\) grids and obtained Morse-theoretic homology information. Matsushita subsequently determined the homotopy types of these grid matching complexes recursively; his recurrence directly covers the nonequivariant homotopy type of \(\mathcal M(L_6)\), so the wedge-of-five-spheres statement is not claimed as new. Matsushita's later polygonal-line-tiling paper, whose primary MSC2020 classification is \(55P10\), places ladders in a broader topology-led family.

Li studies the graded permutation representations on sets of graph matchings and proves equivariant log-concavity. That representation is not the homology representation computed here. Li explicitly notes that matching-complex homology supplies natural differentials on the graded matching spaces and points to further interactions between these representation-theoretic objects. The present calculation is an exact instance of that interface: it determines the full automorphism character on topological homology, and it distinguishes the two reflection classes even though both are involutions.

Targeted searches for the six-rung ladder, the \(2\times6\) grid, matching-complex homology characters, row interchange, column reversal, and equivariant matching-complex homology did not locate this character or an implication determining it. The closest sources determine the nonequivariant homotopy type or the permutation representations of matchings, not this homology representation.

## Limitations
The result concerns one natural finite member of the ladder family. The computation does not classify the integral representation lattice and does not establish a formula for arbitrary ladder length. The literature comparison is bounded by the sources and searches listed in `AUDIT.json`; a previously unindexed table of explicit automorphism characters remains a residual novelty risk.

## References
1. T. Matsushita, *Matching complexes of polygonal line tilings*, Hokkaido Mathematical Journal 51 (2022), 339–359. arXiv:1910.00186; DOI:10.14492/hokmj/2019-213. Primary MSC2020: 55P10.
2. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26(3) (2019), #P3.1. arXiv:1812.11000; DOI:10.37236/8480.
3. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, Electronic Journal of Combinatorics 24(4) (2017), #P4.18. arXiv:1606.01204; DOI:10.37236/6212.
4. S. Li, *Equivariant log-concavity of graph matchings*, Algebraic Combinatorics 6(3) (2023), 615–622. arXiv:2202.08828; DOI:10.5802/alco.284.
5. M. Bayer, M. Jelić Milutinović, and J. Vega, *General polygonal line tilings and their matching complexes*, Discrete Mathematics 346(7) (2023), 113428. DOI:10.1016/j.disc.2023.113428.
