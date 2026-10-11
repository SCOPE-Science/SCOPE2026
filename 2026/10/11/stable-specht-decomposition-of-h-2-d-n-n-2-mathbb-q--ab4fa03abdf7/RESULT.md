# Stable Specht decomposition of \(H_2(D_{n,n-2};\mathbb Q)\)

## Finding
Let \(D_{n,n-2}\) be the simplicial complex of labeled graphs on \(n\) vertices with domination number at least \(n-2\). Relabeling vertices defines a natural \(S_n\)-action. For every integer \(n\ge6\), its only nonzero reduced rational homology representation is
\[
\widetilde H_2(D_{n,n-2};\mathbb Q)\cong
S^{(n-2,1,1)}\oplus S^{(n-3,2,1)}
\oplus 2S^{(n-3,1,1,1)}\oplus2S^{(n-4,2,1,1)}.
\]
Here \(S^\lambda\) is the irreducible rational Specht module indexed by the partition \(\lambda\vdash n\); a coefficient \(2\) means two copies. At the two smaller noncontractible cases the same uniform chain-character formula gives
\[
\widetilde H_2(D_{4,2};\mathbb Q)\cong S^{(2,1,1)},
\qquad
\widetilde H_2(D_{5,3};\mathbb Q)\cong
S^{(3,1,1)}\oplus S^{(2,2,1)}\oplus2S^{(2,1,1,1)}.
\]
All other reduced rational homology vanishes for every \(n\ge4\). In particular, there is no trivial \(S_n\)-summand in degree two. This is an equivariant refinement of a previously established, nonequivariant homotopy classification, not a new assertion of that classification.

## Assumptions and scope
Fix an integer \(n\ge4\). A graph is finite, simple and undirected on the labeled vertex set \([n]=\{1,\dots,n\}\), including its isolated vertices. Its domination number \(\gamma(G)\) is the minimum cardinality of a vertex set \(T\) such that every vertex outside \(T\) is adjacent to some vertex in \(T\). The vertices of \(D_{n,n-2}\) are edges of the complete graph \(K_n\); a nonempty edge set \(E\) is a simplex precisely when \(\gamma(([n],E))\ge n-2\). A simplex with \(k\) graph edges is a \((k-1)\)-simplex. The symmetric group \(S_n\) acts by permuting graph vertices and hence by signed permutations of oriented simplicial chains over \(\mathbb Q\). The Specht-module notation uses the usual partition parametrization; \(h_j,e_j,s_\lambda\) denote complete, elementary and Schur symmetric functions, with \(h_0=1\).

## Proof
**1. Homology concentration and simplex types.** González and Hoekstra-Mendoza, Theorem 1.1, prove for every \(n\ge4\) that \(D_{n,n-2}\) is homotopy equivalent to a wedge of two-spheres. In particular the rational chain complex has reduced homology in degree two only. Their Section 4 establishes the following exhaustive graph types. Every one-edge or two-edge graph is a simplex. The three-edge simplices are exactly triangles \(C_3\) and four-vertex paths \(P_4\), with all other graph vertices isolated. The four-edge simplices are exactly four-cycles \(C_4\), again with the remaining vertices isolated; there are no simplices with more than four graph edges. These assertions can also be checked directly from the definition of domination number. The orbit types and oriented stabilizer actions below depend only on at most four graph vertices, so the formulas apply to all \(n\ge4\).

**2. Signed chain representations.** Denote the rational oriented simplicial chain group in degree \(j\) by \(C_j\), and use \(\operatorname{ch}\) for the Frobenius characteristic of an \(S_n\)-representation. A single graph edge is a two-element subset and gives
\[\operatorname{ch}(C_0)=h_{n-2}h_2.\]
The oriented two-edge subsets split into adjacent pairs on three graph vertices and disjoint pairs on four vertices. Interchanging the two graph edges reverses simplex orientation. An adjacent pair therefore has local signed representation \(\operatorname{Ind}_{S_2}^{S_3}(\mathrm{sgn})\), with characteristic \(h_1e_2\); a disjoint pair has local characteristic \(s_{(3,1)}\). Consequently
\[\operatorname{ch}(C_1)=h_{n-3}h_1e_2+h_{n-4}s_{(3,1)}.\]
The triangle orbit of oriented three-edge simplices carries the vertex-permutation sign representation of \(S_3\), while the signed \(S_4\)-module on the twelve \(P_4\) edge sets is \(2S^{(3,1)}\oplus2S^{(2,1,1)}\). Thus
\[\operatorname{ch}(C_2)=h_{n-3}e_3+h_{n-4}(2s_{(3,1)}+2s_{(2,1,1)}).\]
The signed module on the three \(C_4\) edge sets is \(S^{(3,1)}\), so
\[\operatorname{ch}(C_3)=h_{n-4}s_{(3,1)}.\]
For completeness, the two local signed \(S_4\)-orbits on disjoint edge pairs and four-cycles both have character values \((3,1,-1,0,-1)\) on the ordered classes \((1^4),(2,1^2),(2^2),(3,1),(4)\), the character of \(S^{(3,1)}\). The twelve oriented paths have character \((12,0,-4,0,0)\), equal to \(2\chi^{(3,1)}+2\chi^{(2,1,1)}\). These equalities follow by fixing each graph-edge subset and taking the sign of its induced permutation of edges, and independently are checked by `verify.py`.

**3. Euler--Poincaré in the representation ring.** The equivariant Euler identity applies to the actual \(S_n\)-chain complex, not just its dimensions. All reduced rational homology except degree two vanishes, and the connected complex has one-dimensional trivial \(H_0\). Therefore
\[
\operatorname{ch}\widetilde H_2
=\operatorname{ch}C_0-\operatorname{ch}C_1
+\operatorname{ch}C_2-\operatorname{ch}C_3-h_n
=h_{n-2}h_2-h_{n-3}s_{(2,1)}
+2h_{n-4}s_{(2,1,1)}-h_n.
\]
The final identity uses \(h_1e_2=e_3+s_{(2,1)}\). This is an equality of genuine characters, not an assumption that the chain groups split compatibly with the boundary: semisimplicity over \(\mathbb Q\) converts the representation-ring identity into the asserted isomorphism.

**4. Irreducible expansion.** Apply Pieri's horizontal-strip rule to the three products. For \(n\ge6\) the expansions are
\[
\begin{aligned}
h_{n-2}h_2&=s_{(n)}+s_{(n-1,1)}+s_{(n-2,2)},\\
h_{n-3}s_{(2,1)}&=s_{(n-1,1)}+s_{(n-2,2)}+s_{(n-2,1,1)}+s_{(n-3,2,1)},\\
h_{n-4}s_{(2,1,1)}&=s_{(n-2,1,1)}+s_{(n-3,2,1)}+s_{(n-3,1,1,1)}+s_{(n-4,2,1,1)}.
\end{aligned}
\]
Subtraction leaves exactly the four partitions in the finding, with multiplicities \(1,1,2,2\). For \(n=4,5\), applying Pieri directly, without using a stable-range expression where partitions coincide or cease to be partitions, gives the two displayed exceptional formulas. All displayed constituents are nontrivial. The sum of their hook-length dimensions equals the known \(\widetilde\beta_2=(n-2)(n-3)(3n^2-7n-2)/12\), including the two exceptional values \(3\) and \(19\).

## Verification
Execute `python3 verify.py` from the extracted package directory using a standard Python interpreter. The script exhaustively constructs the graph-property simplices from the definition of domination number, including a check that no five-edge simplex exists, for \(n=4,5,6,7\). It compares the complete signed simplex traces for representatives of all \(5,7,11,15\) symmetric-group conjugacy classes, respectively, with the claimed character; it also computes the local oriented \(S_4\)-orbit characters independently. Rim-hook recursion verifies the Specht-character identity through \(n=12\). The expected success marker is `VERIFY_OK`. These finite computations check, but do not replace, the uniform proof by equivariant Euler--Poincaré and Pieri's rule.

## Relationship to prior work
González and Hoekstra-Mendoza's Theorem 1.1 (first publicly posted 2019-01-22) already proves the two-sphere wedge homotopy type and the explicit Betti-number formula. Its Section 4 also classifies the necessary face types; those facts are inputs, not claimed novelties. The result here supplies their previously unspecified rational \(S_n\)-homology representation, including the stable constituent multiplicities and small-\(n\) transition. It is not implied by the Betti numbers alone, which cannot determine any nontrivial automorphism trace. Nearby results on \(D_{6,3}\) and \(D_{7,4}\) concern \(D_{n,n-3}\) rather than \(D_{n,n-2}\) and do not give this representation.

## Limitations
The theorem describes rational representations, not the integral \(\mathbb Z[S_n]\)-lattice structure or mod-prime decomposition. It relies on the cited prior nonequivariant homotopy theorem to assert homology concentration; the present argument independently establishes the equivariant character conditional on that published premise. No claim is made about \(D_{n,n-r}\) for \(r\ge3\). Searches of indexed literature do not rule out an equivalent representation result under a different terminology; no independent external audit has been performed.

## References
1. J. González and T. I. Hoekstra-Mendoza, *On the homotopy type of complexes of graphs with bounded domination number*, arXiv:1901.07130 (first posted 2019-01-22), especially Theorem 1.1, Section 4 and Section 7; subsequently published in *Contributions to Discrete Mathematics* 16 (2021), 153–174. https://arxiv.org/abs/1901.07130
