# Integral hexagon-torus bases and full symmetry character for Desargues two-particle configurations

## Finding

Let \(G\) be the twenty-vertex Desargues graph, with vertices all two-element and three-element subsets of \([5]\), and edges joining a two-set to a three-set precisely when the former is contained in the latter. This is also the generalized Petersen graph \(\operatorname{GP}(10,3)\). Set \(X=\operatorname{UConf}_2(|G|)\), the space of unordered distinct points on its geometric realization.

The reduced integral homology is concentrated in degrees one and two, with
\[
H_1(X;\mathbb Z)\cong\mathbb Z^{11}\oplus\mathbb Z/2,\qquad
H_2(X;\mathbb Z)\cong\mathbb Z^{35}.
\]
The graph has exactly twenty simple six-cycles, its girth is six, and precisely seventy unordered pairs of those cycles have disjoint vertex sets. Each such pair produces an embedded product torus and an integral second-homology class. The automorphism group \(\operatorname{Aut}(G)\cong S_5\times C_2\) has exactly two orbits on these seventy tori, of cardinalities sixty and ten. **The sixty-element orbit integrally generates all of \(H_2(X;\mathbb Z)\)**: thirty-five of its members form an integral basis. The ten-element orbit independently spans a primitive rank-ten sublattice.

Write \(\varepsilon\) for the nontrivial rational character of the central complement involution \(C_2\), and \(S^\lambda\) for the rational irreducible Specht representation of \(S_5\) indexed by \(\lambda\vdash5\). The complete rational second-homology representation is
\[
\begin{aligned}
H_2(X;\mathbb Q)\cong{}&
\big(S^{(2,1,1,1)}\oplus S^{(2,2,1)}\oplus S^{(3,1,1)}\big)\boxtimes\mathbf1\\
&\oplus\big(S^{(4,1)}\oplus S^{(3,2)}\oplus S^{(2,2,1)}\oplus S^{(3,1,1)}\big)\boxtimes\varepsilon.
\end{aligned}
\]
In particular, the central involution has \(+1\) and \(-1\) eigenspaces of dimensions fifteen and twenty, hence trace \(-5\), and no nonzero second-homology vector is fixed by the whole automorphism group.

## Assumptions and scope

All homology groups are singular homology of the indicated topological configuration space; all integral lattices use ordinary \(\mathbb Z\) coefficients. The graph \(G\) is exactly the subset-incidence graph above, with no multiple edges. The automorphism group acts by moving the underlying graph; \(S_5\) relabels \([5]\), and the central involution complements each subset. An unordered product torus is the image of a product of oriented geometric simple cycles with disjoint vertex sets, where the two particles run independently. Signs depend on chosen cycle orientations but generation, ranks, and orbits do not.

The result concerns two particles on this single graph. No uniform theorem for other generalized Petersen graphs, or higher-particle configurations, is asserted.

## Proof

**1. Finite cubical model.** The equivariant deleted-product deformation retraction in Barnett–Farber, Lemma 1.1 [1], descends under the free particle-swap involution. Thus \(X\) is homotopy equivalent to the unordered cubical complex \(Y\) whose zero-cells are unordered distinct graph vertices, one-cells are pairs of an edge and a nonincident vertex, and two-cells are unordered pairs of vertex-disjoint edges. In the lexicographically oriented bases specified below, the ranks of the cellular chain groups in degrees zero, one, and two are respectively \(190,540,375\); there are no higher cells.

**2. Integer cellular boundaries and rank.** Number the graph vertices \(0,\ldots,9\) by lexicographically sorted two-subsets of \(\{0,1,2,3,4\}\), and \(10,\ldots,19\) by lexicographically sorted three-subsets. Sort each edge \(e=(a,b)\) with \(a<b\), and sort all edges lexicographically. Orient a one-cell \((e,v)\) by the increasing orientation of \(e\), and a two-cell \((e,f)\), \(e<f\), by the product orientation. For disjoint edges \(e=(a,b)\) and \(f=(c,d)\), the cellular boundary is
\[
\partial_2[(e,f)]=[(f,b)]-[(f,a)]-[(e,d)]+[(e,c)].
\]
The signed one-cell boundary is the endpoint difference. The supplied verifier constructs both integer matrices and confirms \(\partial_1\partial_2=0\). Its exact Gaussian elimination modulo \(101\) gives \(\operatorname{rank}_{\mathbb F_{101}}\partial_2=340\), hence \(\operatorname{rank}_{\mathbb Q}\partial_2\ge340\). The thirty-five cycles constructed below show the reverse inequality.

**3. Exhaustive shortest-torus certificate.** The verifier enumerates every simple six-cycle by a depth-six path search, requiring the least vertex first and the second vertex smaller than the last; it finds exactly twenty. It checks all unordered pairs, finding seventy vertex-disjoint pairs. For oriented cycles \(a=(a_0,\ldots,a_5)\) and \(b=(b_0,\ldots,b_5)\), the product chain is the sum of the thirty-six product two-cells, with signs from each oriented edge and from exchanging their factors into increasing edge order. Each such chain has zero integral boundary.

The verifier orders the seventy pairs lexicographically under this cycle convention. Within the sixty-element symmetry orbit, the zero-based pair-column indices

`[0,1,2,3,4,7,8,9,10,11,14,15,16,17,18,21,22,23,24,26,28,29,30,31,33,35,36,39,40,42,43,45,49,50,56]`

have an exact \(35\)-by-\(35\) coefficient minor with determinant \(-1\), taking zero-based two-cell row indices

`[0,2,3,5,6,8,11,14,25,26,28,31,34,36,39,75,76,78,79,84,87,98,100,104,107,110,142,143,146,151,162,166,202,205,219]`.

A nonzero unit minor proves that these thirty-five cycles are linearly independent and span a *primitive* sublattice of \(\mathbb Z^{375}\). Their independence bounds the boundary rank by \(340\), completing the rank equality. The kernel of an integer map is itself saturated in the ambient free lattice. As the primitive span of these thirty-five cycles sits inside that kernel and has the same rank, the two coincide. This proves that the selected product tori are an **integral basis**, without inferring an infinite statement from numerical sampling.

**4. The second orbit.** Directly applying all \(120\) five-letter permutations and independent complementation to six-cycle pairs gives precisely two orbits of sizes sixty and ten. In the ten-element orbit, its ten columns have a coefficient minor with determinant \(+1\), in two-cell rows `[3,6,11,14,26,34,75,78,104,142]`. Hence this orbit generates a primitive rank-ten sublattice of the full homology.

**5. First homology.** The one-cell boundary has rank \(189\); it is the ordinary incidence map of a connected one-skeleton and has torsion-free cokernel. Exact Smith normal form of the \(540\)-by-\(375\) integer two-cell boundary has \(339\) unit factors and one factor equal to \(2\). Since \(\operatorname{im}\partial_2\subseteq\ker\partial_1\) and \(\operatorname{im}\partial_1\) is free, the integral torsion subgroup of \(H_1\) is \(\mathbb Z/2\), while its free rank is \(540-189-340=11\). There are no other reduced homology degrees.

**6. Full automorphism character.** The graph has \(240\) automorphisms, exhaustively counted by graph isomorphism backtracking; the \(240\) explicit subset-permutation/complementation actions are distinct and therefore all automorphisms. The signed action on a two-cell is the product of the two edge-orientation signs and a minus sign if the two edge factors exchange order. Conjugating this action into the integral torus basis using its unit minor yields the exact traces below. For each cycle type of \(S_5\), the two columns give the trace without and with the central complement, respectively.

| Cycle type in \(S_5\) | No complement | With complement |
|---|---:|---:|
| \((1,1,1,1,1)\) | 35 | -5 |
| \((2,1,1,1)\) | -1 | -5 |
| \((2,2,1)\) | -1 | -1 |
| \((3,1,1)\) | -1 | 1 |
| \((3,2)\) | -1 | 1 |
| \((4,1)\) | 1 | 1 |
| \((5)\) | 0 | 0 |

The supplied program checks the induced matrices on *all* \(375\) two-cell coordinates, not just on the determinant rows. Orthogonality with the seven irreducible characters of \(S_5\), evaluated using fixed-point and two-cycle counts, gives precisely the claimed Specht decomposition. This finishes the proof.

## Verification

Run `python verify.py` after installing dependencies from `requirements.txt`. The verifier reconstructs the graph, checks its isomorphism with \(\operatorname{GP}(10,3)\) and its \(240\)-element automorphism group, exhausts all length-six cycles and disjoint pairs, builds integer cellular boundaries and torus classes, checks both unimodular determinant certificates, computes the Smith form and full symmetry character, and independently verifies every transformed basis chain in the original cellular basis. No precomputed matrix file, external database, or network connection is needed.

The verification result includes `VERIFY_OK_DESARGUES_SHORTEST_HEXAGON_INTEGRAL_S5C2`. Matrix indices in the two determinant certificates are specified exactly above and also embedded in the program. The calculation is finite and exhaustive for this graph; it is not presented as independent expert review.

## Relationship to prior work

Barnett–Farber [1] supplies the deleted-product model and general graph-cycle intersection methods. Farber–Hanbury [2] gives general formulas through the intersection form and mature-graph criteria. Such general tools can determine Betti ranks, but neither consulted theorem selects the two shortest-hexagon-torus orbits, proves that the larger orbit contains a unimodular integral basis, or states the complete \(S_5\times C_2\) character for this graph. An–Knudsen [3] proves a general degree-two generation theorem for *planar* graph braid groups and exhibits nonplanar exceptions; the present graph is nonplanar, so its theorem cannot imply the asserted shortest-torus basis. The Desargues graph is the bipartite double cover of the Petersen graph, but this graph covering does not induce a two-particle configuration map: distinct points in the cover can project to the same point. Previously studied Petersen and dodecahedral two-particle representations concern different graphs and do not determine this one.

## Limitations

The work determines the *integral abelian homology* and *rational* automorphism character. It does not classify the full integral \(\mathbb Z[S_5\times C_2]\)-module beyond its explicit geometric basis and integral action algorithm. It does not determine cup products, the fundamental group, higher-particle homology, or other generalized Petersen families. Bibliographic uniqueness beyond the inspected primary works and targeted search is not certified; equivalent specialized calculations could occur in inaccessible or unindexed literature. No independent scientific audit has been performed.

## References

[1] K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (public 12 March 2009), especially Lemma 1.1 and Sections 1–2.

[2] M. Farber and E. Hanbury, *Topology of Configuration Space of Two Particles on a Graph, II*, arXiv:1005.2300v1 (public 13 May 2010), especially Section 2.

[3] B. H. An and B. Knudsen, *On the Second Homology of Planar Graph Braid Groups*, arXiv:2008.10371 (first posted 24 August 2020), Theorem 1.1 and Example 6.8.

[4] I. N. Kagno, *Desargues' and Pappus' graphs and their groups*, and classical Desargues-graph incidence and generalized-Petersen descriptions, for standard graph terminology only; graph identity and automorphisms are independently recomputed in `verify.py`.
