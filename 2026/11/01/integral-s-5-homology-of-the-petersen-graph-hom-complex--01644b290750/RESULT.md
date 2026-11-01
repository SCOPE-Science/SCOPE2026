# Integral \(S_5\)-homology of the Petersen graph Hom complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, whose vertices are two-element subsets of \([5]\), adjacent when disjoint. Let \(X=\operatorname{Hom}(K_2,P)\) be the standard graph-homomorphism polyhedral complex, with the natural \(S_5\)-action induced by permutations of \([5]\). The complex is connected and
\[
\widetilde H_i(X;\mathbb Z)=0\ (i\ne1),\qquad H_1(X;\mathbb Z)\cong\mathbb Z^{11}.
\]
There is a canonical description of the **integral** \(S_5\)-module. Define the bipartite graph \(D\) with vertices \((A,0),(A,1)\) for \(A\in\binom{[5]}2\), and edges oriented from \((A,0)\) to \((B,1)\) when \(A\cap B=\varnothing\). Its oriented edge set comprises the 30 ordered disjoint pairs \((A,B)\). Then
\[
H_1(X;\mathbb Z)\cong_{\mathbb Z[S_5]}
\ker\left(\partial:\mathbb Z^{\{(A,B):A\cap B=\varnothing\}}\longrightarrow
\mathbb Z^{\binom{[5]}2\times\{0,1\}}\right),
\quad \partial[A,B]=[B,1]-[A,0].
\]
The complete rational decomposition is the multiplicity-free representation
\[
\boxed{H_1(X;\mathbb Q)\cong_{\mathbb Q[S_5]}S^{(3,1,1)}\oplus S^{(2,2,1)}},
\]
of dimensions six and five. On the conjugacy types \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), respectively, its character is \((11,-1,-1,-1,-1,1,1)\).

## Assumptions and scope
The graph \(K_2\) has two *distinguished* adjacent vertices (the assertion concerns target automorphisms \(S_5\), not the source-coordinate swap). For finite loopless graphs, a cell of \(\operatorname{Hom}(K_2,P)\) is a pair of nonempty vertex subsets \((A,B)\) for which every vertex of \(A\) is adjacent to every vertex of \(B\), ordered by coordinatewise inclusion. The Hom complex is the geometric realization of the resulting regular polyhedral cell complex. The integral module statement is an explicit cycle-lattice description, not a claim that the two rational summands split as integral \(S_5\)-lattices.

## Proof
**1. Exact cover and its nerve.** The Petersen graph is triangle-free and has no four-cycle. Indeed its vertices are two-subsets of five points; two distinct such subsets have at most one common disjoint two-subset. If a Hom cell had both coordinates of size at least two, the graph would contain a four-cycle, impossible. Thus every cell lies in one of the twenty subcomplexes
\[
U_u^0=\{\{u\}\}\times\Delta(N_P(u)),\qquad
U_v^1=\Delta(N_P(v))\times\{\{v\}\},
\]
indexed by a Petersen vertex \(u\) or \(v\) and a color \(0\) or \(1\). Each is a simplex (a triangle because the degree is three). Same-color distinct pieces are disjoint; two opposite-color pieces meet precisely in the Hom vertex \((u,v)\) if \(u\sim v\), and are otherwise disjoint. There are no triple intersections. All nonempty intersections are contractible. Consequently the ordinary nerve lemma gives \(X\simeq |D|\), where the nerve \(D\) is the canonical bipartite double cover of \(P\). The cover and its intersections are permuted by \(S_5\); the natural equivariant Cech/Mayer–Vietoris double complex, using augmented chains of the pieces and intersections, yields a canonical \(\mathbb Z[S_5]\)-homology identification with \(D\). This claim is about homology, so no unproved equivariant collapse is required.

**2. Integral homology.** The Petersen graph is connected and nonbipartite, since it contains a five-cycle (for example, the ordered pairs \(12,34,15,23,45\) form a cycle). Hence its bipartite double cover \(D\) is connected. This graph has twenty vertices and thirty edges. Its cellular chain complex has differential \(\partial[A,B]=[B,1]-[A,0]\). Connectivity implies that \(\operatorname{rank}\partial=19\). Therefore its integral first homology is the free rank-eleven kernel of \(\partial\); its higher homology vanishes, proving the integral assertions and the exact natural \(S_5\)-action.

**3. Irreducible rational decomposition.** Let \(M^{\lambda}\) denote the rational Young permutation module induced from the stabilizer of an ordered set partition of shape \(\lambda\). The edge permutation module of \(D\) is \(M^{(2,2,1)}\); the vertex module is \(2M^{(3,2)}\). Since the cover is connected, the equivariant graph chain complex gives, in the Grothendieck group,
\[
[H_1(D;\mathbb Q)]=[M^{(2,2,1)}]-2[M^{(3,2)}]+[S^{(5)}].
\]
By two applications of the Pieri rule (equivalently Young's rule),
\[
M^{(2,2,1)}\cong S^{(5)}\oplus2S^{(4,1)}\oplus2S^{(3,2)}\oplus S^{(3,1,1)}\oplus S^{(2,2,1)},
\]
\[
M^{(3,2)}\cong S^{(5)}\oplus S^{(4,1)}\oplus S^{(3,2)}.
\]
The first three constituents cancel as claimed. Maschke semisimplicity over \(\mathbb Q\) upgrades this equality of virtual characters to the asserted actual module isomorphism. The dimensions \(6+5=11\) agree with the integral rank. The character values follow either from these Specht summands or directly from \(\chi(g)=\#\operatorname{Fix}_D(E;g)-\#\operatorname{Fix}_D(V;g)+1\), with edges oriented from color zero to one, so no hidden orientation sign occurs.

## Verification
The standalone `verify.py` independently enumerates the 10 Petersen vertices and 30 ordered-disjoint-pair edges, checks nonexistence of four-cycles, connectivity of the twenty-vertex cover, and checks all 120 point permutations. It computes the seven class characters directly from fixed vertices and edges and checks them against the displayed values. It also enumerates Hom cells and verifies that each lies in one of the twenty simplices and that their intersections have the stated nerve. The proof above is uniform and exact for the one specified complex; the executable is an independent finite reconstruction.

## Relationship to prior work
Matsushita's *Hom complexes of graphs whose codomains are square-free* (arXiv:2412.19144, publicly posted December 26, 2024), Theorem 1.2, classifies **ordinary component homotopy types** for all square-free targets, but does not determine the natural integral \(S_5\)-module or its two Specht constituents for \(P\). The related Kneser neighborhood-complex calculation on six underlying points studies \(\operatorname{KG}(6,2)\), a different graph and a different rational \(S_6\)-module. The unordered two-particle configuration space of the Petersen graph has separately computed \(S_5\)-homology modules with these same two Specht *types in distinct degrees*, but is not the graph Hom complex; that result neither supplies the Hom cycle lattice nor identifies this action. This coincidence is not asserted to arise from a canonical map.

## Limitations
The decomposition of the free integral module into irreducible rational constituents does **not** assert an integral splitting. Source-coordinate exchange on \(K_2\), geometric fixed sets, quotient integral homology, and general Kneser graphs are outside the claim. Coincidental equivalence to an unindexed representation computation remains a literature risk; independent mathematical auditing has not occurred.

## References
1. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144v1 (first publicly available 2024-12-26), https://arxiv.org/abs/2412.19144. Theorem 1.2 and the discussion of graph-Hom topology.
2. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, J. Combin. Theory A 25 (1978), 319–324.
3. C. Schultz, *The equivariant topology of stable Kneser graphs*, J. Combin. Theory A 118 (2011), 2291–2318; the stable Kneser construction differs from \(\operatorname{KG}(5,2)\).
