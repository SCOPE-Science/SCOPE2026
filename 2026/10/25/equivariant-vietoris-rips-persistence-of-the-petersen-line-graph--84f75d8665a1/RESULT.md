# Equivariant Vietoris–Rips persistence of the Petersen line graph

## Finding
Let \(P=KG(5,2)\) be the Petersen graph and let \(L=L(P)\) be its fifteen-vertex line graph, equipped with the shortest-path metric. Write \(X_r=\operatorname{VR}_{\le r}(L)\) for the inclusive finite Vietoris–Rips complex. The integer-radius homotopy types are
\[
X_0\simeq\{15\text{ points}\},\qquad
X_1\simeq\bigvee^6 S^1,\qquad
X_2\simeq\bigvee^{32}S^4,\qquad
X_r\simeq\{\mathrm{pt}\}\ (r\ge3).
\]
The **positive-degree rational persistent homology with its natural \(S_5=\operatorname{Aut}(L)\) action** consists of precisely two intervals of representation-valued multiplicity: in degree one the interval \([1,2)\) carries \(S^{(3,1,1)}\) (dimension six), while in degree four the interval \([2,3)\) carries
\[
2S^{(5)}\oplus2S^{(1,1,1,1,1)}\oplus S^{(4,1)}\oplus S^{(2,1,1,1)}
\oplus2S^{(3,2)}\oplus2S^{(2,2,1)}.
\]
Here \(S^{\lambda}\) denotes the irreducible rational \(S_5\)-representation indexed by the partition \(\lambda\) of five. In the conjugacy-class order \((1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)\), the degree-one and degree-four characters are, respectively,
\[
\chi_1=(6,0,-2,0,0,0,1),\qquad
\chi_4=(32,0,8,2,0,0,2).
\]
Thus degree-one homology is irreducible and has no invariant vector; degree-four homology has an invariant subspace of dimension **two**. All these homology groups are torsion-free integrally, but the displayed irreducible direct sums are assertions over \(\mathbb Q\), not integral splittings. The reduced degree-zero barcode consists of fourteen intervals \([0,1)\).

## Assumptions and scope
The Petersen vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\); two vertices are adjacent when disjoint. Vertices of \(L\) are the fifteen edges of \(P\). Simplices of \(X_r\) are sets of distinct vertices at pairwise distance at most \(r\), not metric-geometric realizations of the graph. The filtration parameter \(r\) is real and nonnegative; no changes occur except at integer radii zero, one, two and three. The natural \(S_5\)-action permutes the underlying five symbols and hence preserves graph distance and the filtration.

## Proof
**1. The distance-three fibers.** Each Petersen edge is an unordered pair \(\{A,B\}\) of disjoint two-sets. It is uniquely encoded by an unused symbol \(i\in\{0,1,2,3,4\}\) and a partition of the remaining four symbols into two unordered pairs. For each \(i\), let \(F_i\) be its three possible pair-partitions. These are five disjoint three-element subsets of \(V(L)\).

Two distinct edges of the Petersen graph have distance at most two in its line graph precisely when at least one endpoint of the first edge is disjoint from one endpoint of the second. For edges in the same \(F_i\), their pairings are distinct and each block of either pairing meets both blocks of the other, so the line-graph distance is greater than two. It is exactly three: given \(A\sqcup B=C\sqcup D\) with the two partitions distinct, choose intersecting blocks \(A,C\); the complementary two-set \(E\) in the full five-symbol set is disjoint from both, giving a length-three line-graph path through the edges \(\{A,E\}\) and \(\{C,E\}\).

For edges in different fibers, take an endpoint block of the second edge containing the first edge's unused symbol \(i\). This block meets only one of the two disjoint blocks of the first edge, so it is disjoint from the other, giving line-graph distance at most two. Therefore
\[
\bigl(L\bigr)^2=K_{3,3,3,3,3},
\]
where the parts are exactly the \(F_i\); \(L\) has diameter three. (Here the square joins vertices at graph distance at most two.)

**2. The four homotopy stages.** At radius zero there are fifteen isolated points. Because \(P\) is triangle-free and cubic, \(X_1=\operatorname{Cl}(L)\) is covered by the ten closed triangles comprising the edges incident to each Petersen vertex; their nonempty intersections are single vertices, and their nerve is \(P\). Thus \(X_1\simeq P\simeq\bigvee^6S^1\), since \(|E(P)|-|V(P)|+1=15-10+1=6\). The nerve equivalence is natural with respect to the \(S_5\)-action. From the squared-graph identity,
\[
X_2=F_0*F_1*F_2*F_3*F_4,
\]
where each \(F_i\) is regarded as a discrete three-point simplicial complex. Iterated reduced join and Künneth give only \(\widetilde H_4(X_2;\mathbb Z)\cong\mathbb Z^{2^5}\); the join of finite nonempty zero-dimensional spaces is homotopy equivalent to a wedge of \(2^5\) four-spheres (iteratively join with a discrete triple, equivalently wedge two suspensions). At radius three the full fifteen-vertex simplex appears.

**3. The degree-four character.** Set \(W_i=\widetilde H_0(F_i;\mathbb Q)=\ker(\mathbb Q[F_i]\to\mathbb Q)\), a two-dimensional augmentation module. The oriented join gives \(\widetilde H_4(X_2;\mathbb Q)\cong\bigotimes_{i=0}^4 W_i\) as vector spaces, with a sign whenever two zero-dimensional join factors are interchanged. Let \(\sigma\in S_5\). For each cycle \(C\) of \(\sigma\) on the five symbols, choose \(i_C\in C\), write \(\ell_C=|C|\), and let \(f_C\) be the number of the three pair-partitions in \(F_{i_C}\) fixed by \(\sigma^{\ell_C}\). The cyclic tensor-trace identity then yields the exact formula
\[
\operatorname{tr}(\sigma\mid\widetilde H_4(X_2;\mathbb Q))
=\operatorname{sgn}(\sigma)\prod_C(f_C-1).
\]
Evaluating this for the seven conjugacy types gives \(\chi_4\) above. Inner products with the seven rational irreducible characters of \(S_5\) give multiplicities \((2,2,1,1,2,2,0)\) in the order \((5),(1^5),(4,1),(2,1^3),(3,2),(2,2,1),(3,1,1)\). Averaging the character over all 120 elements gives \(\dim\widetilde H_4(X_2;\mathbb Q)^{S_5}=2\).

**4. The degree-one character.** By the natural nerve identification, \(H_1(X_1;\mathbb Q)\cong H_1(P;\mathbb Q)\). Since \(P\) is connected, its oriented cellular chains give
\[
\chi_1(\sigma)=1-\operatorname{tr}(\sigma\mid C_0(P;\mathbb Q))
+\operatorname{tr}(\sigma\mid C_1(P;\mathbb Q)),
\]
where each preserved but orientation-reversed edge contributes \(-1\) to the last trace. Direct counting of the ten two-sets and fifteen unordered disjoint-pair edges gives \(\chi_1=(6,0,-2,0,0,0,1)\). Its inner product with itself is one, and comparison with the standard \(S_5\) character table identifies the irreducible \(S^{(3,1,1)}\). Distinct nonzero homology degrees at adjacent filtration stages force all positive-degree persistence maps across radius two to vanish. Radius three kills the degree-four group. These facts establish the stated representation-valued barcode.

## Verification
Run `python3 verify.py` using Python 3 and no external packages. The program builds the Petersen graph from disjoint two-subsets and its line graph independently of the fiber formula, checks all 105 unordered line-graph vertex pairs, enumerates all 56 faces at radius one and all 1024 faces (including the empty face) at radius two, and computes reduced mod-two chain ranks. It checks both character formulas against oriented fixed-simplex Lefschetz traces for **all 120 permutations**, verifies both rational irreducible decompositions, and checks the invariant multiplicity. Its expected final line is `PETERSEN_LINE_RIPS_EQUIVARIANT_CHECKS_OK r1_faces 56 r2_faces 1024 permutations 120`. These finite calculations are corroboration; the integral homotopy claims and group trace formulas follow from the explicit structural proof above.

## Relationship to prior work
Goyal, Shukla and Singh prove that for a triangle-free graph \(G\), \(\operatorname{Cl}(L(G))\simeq G\), giving the *radius-one* stage here. The distance-regular graph reference already records that \(L(P)\) has fifteen vertices, diameter three, antipodal fibers and automorphism group \(S_5\). Those properties, together with standard join topology, already imply the **nonequivariant radius-two sphere count**; this count is not asserted to be independently novel. Chachólski and collaborators provide general homotopical decompositions of Rips complexes. The distinct contribution here is the **explicit full equivariant rational persistence** for this graph, including the two nonzero character tables, the six-dimensional irreducible group at radius one, the irreducible decomposition at radius two, and the two-dimensional invariant fourth-homology subspace. No located source states or implies this character decomposition without additional symmetry-action computation.

## Limitations
This is the graph-shortest-path metric on fifteen vertices, not the geodesic metric of a continuously realized graph. Rational semisimple representation decompositions do not specify integral \(S_5\)-lattice splitting or an equivariant wedge decomposition. The proof is for this one graph, not all antipodal covers. Prior literature and graph tables determine part of the combinatorial geometry; unindexed equivalent symmetry calculations remain a possible originality risk. No independent audit is claimed.

## References
1. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, first public arXiv posting 2020-09-25, arXiv:2009.12130, especially Lemma 3.2 and Corollary 3.3. https://arxiv.org/abs/2009.12130
2. *Line graph of Petersen graph*, DistanceRegular.org, https://www.math.mun.ca/distanceregular/graphs/line-petersen.html (graph data and antipodality).
3. W. Chachólski, A. Jin, M. Scolamiero and F. Tombari, *Homotopical decompositions of simplicial and Vietoris Rips complexes*, Journal of Applied and Computational Topology (2021), DOI:10.1007/s41468-021-00066-2. https://link.springer.com/article/10.1007/s41468-021-00066-2
