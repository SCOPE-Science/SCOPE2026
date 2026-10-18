# The icosahedral symmetry representation on dodecahedral independence homology

## Finding
Let \(D=GP(10,2)\) be the dodecahedral graph. Its vertices are \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), and its edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). Write \(K=\operatorname{Ind}(D)\) for the simplicial complex of independent vertex sets. The full automorphism group is the classical icosahedral symmetry group \(G\cong A_5\times C_2\), where the central \(C_2\) is antipodal inversion. Let \(W\) be the four-dimensional rational augmentation module of the natural five-point permutation representation of \(A_5\), and let \(\varepsilon\) be the nontrivial one-dimensional rational character of \(C_2\). Then
\[
\widetilde H_5(K;\mathbb Q)\cong_{\mathbb Q[G]} W\boxtimes\varepsilon,
\qquad \widetilde H_j(K;\mathbb Q)=0\quad(j\ne5).
\]
In particular, the rational top homology representation is absolutely irreducible, and antipodal inversion acts on it by minus the identity. For \((a,z)\in A_5\times C_2\), with \(z\in\{0,1\}\), the complete character is
\[
\chi(a,z)=(-1)^z\bigl(\operatorname{fix}_5(a)-1\bigr),
\]
where \(\operatorname{fix}_5(a)\) is the number of fixed points of the standard five-letter action of \(A_5\).

## Assumptions and scope
The graph is the explicitly labeled 20-vertex, 30-edge simple graph above, not its line graph or its neighborhood complex. Faces of \(K\) are sets containing no graph edge, with the empty face included in the augmented chain complex. The action is by graph automorphisms on oriented simplicial chains, with rational coefficients. We identify the full automorphism group by the standard dodecahedron symmetry identification; computationally the attached scripts independently enumerate exactly 120 automorphisms. No assertion is made about the integral \(G\)-lattice, a \(G\)-equivariant wedge of spheres, or arbitrary generalized Petersen graphs.

## Proof
**(1) Homology concentration.** Exhaustively examining all independent sets in the displayed graph yields 5,828 faces including the empty face. The numbers of nonempty faces in dimensions \(0,\ldots,7\) are
\[
(20,160,660,1510,1912,1240,320,5).
\]
The ranks over \(\mathbb F_2\) of the seven successive nonaugmented simplicial boundary maps \(\partial_1,\ldots,\partial_7\) are
\[
(19,141,519,991,921,315,5).
\]
The reduced augmented boundary in degree zero has rank one. Hence reduced homology over \(\mathbb F_2\) is four-dimensional in degree five and zero elsewhere. Rational ranks are at most the corresponding mod-two ranks, so rational homology vanishes outside degree five and has dimension at most four there. The face counts give reduced Euler characteristic \(-4\); therefore rational degree-five homology has dimension exactly four. The boundary calculations are finite exact bit-vector eliminations, replayed by two separately implemented programs.

**(2) Equivariant Hopf trace calculation.** For any automorphism \(g\) of \(D\), let \(\sigma\) run through its invariant independent subsets, including the empty face. The reduced Lefschetz formula and concentration in odd homological degree five give
\[
\operatorname{tr}(g\mid\widetilde H_5(K;\mathbb Q))
 =\sum_{g\sigma=\sigma}(-1)^{|\sigma|}\operatorname{sgn}(g\mid\sigma).
\]
The empty subset contributes one. An invariant face is a union of vertex cycles of \(g\). Each selected cycle of length \(\ell\) contributes \((-1)^\ell\) from face cardinality and \((-1)^{\ell-1}\) from the orientation permutation, hence exactly \(-1\). Thus the trace is a signed count of compatible collections of vertex cycles, with sign \((-1)^{\text{number of selected cycles}}\). This provides a finite integer computation independent of any choice of basis for homology.

**(3) Exhaustion of the symmetry group.** In the labeling \(u_0,\ldots,u_9,v_0,\ldots,v_9\), the attached first checker lists explicit automorphisms generating a group of size 120. Each generator is checked edge-preserving. The second checker independently enumerates every automorphism by full graph-isomorphism backtracking, again obtaining 120. Both methods compute the character independently. Aggregating by element order and trace gives the following complete multiset:
\[
\begin{array}{c|rrrrrrr}
(\operatorname{ord}(g),\chi(g)) &(1,4)&(2,-4)&(2,0)&(3,1)&(5,-1)&(6,-1)&(10,1)\\\hline
\text{count}&1&1&30&20&24&20&24
\end{array}
\]
The sole nonidentity central element has order two and trace \(-4\); as it acts on a four-dimensional rational representation, its eigenvalues are all \(-1\).

**(4) Character identification and irreducibility.** The rotational symmetry subgroup is \(A_5\), acting on the five cubes inscribed in a dodecahedron. The four-dimensional augmentation character of that five-point action has values \(4,0,1,-1\) on the rotational classes of orders \(1,2,3,5\). The full symmetry group is their direct product with the central inversion. The computed table agrees elementwise with this augmentation character tensored with \(\varepsilon\). Finally, direct summation gives
\[
\frac1{120}\sum_{g\in G}\chi(g)^2=1.
\]
For a rational character this complex character inner product of one implies absolute irreducibility. This completes the identification.

## Verification
Run `python3 verify_character_and_homology.py` (Python standard library) and `python3 verify_signed_traces.py` (Python and NetworkX). Both scripts recompute the graph and every independent face. The first uses recursive branching and lower-face column elimination over \(\mathbb F_2\); it generates the automorphism group from explicit permutations and evaluates invariant-cycle polynomials. The second uses a complete bitmask scan, transposed-row boundary elimination, independently enumerated graph automorphisms, and the actual sign of every invariant oriented face. Both check all 120 group elements, the face vector, mod-two ranks, and the seven displayed order/character classes; successful execution prints `VERIFY_OK`. The finite exhaustive checking proves a fact about this finite graph, without any asymptotic extrapolation.

## Relationship to prior work
A published exact calculation titled *The dodecahedral independence complex is a wedge of four 5-spheres* proves the nonequivariant homotopy equivalence \(\operatorname{Ind}(D)\simeq\bigvee^4S^5\). Its full main proof was inspected; it does not determine the action of the 120 graph automorphisms. That homotopy type and the rank four are not claimed as new. Barmak's triangle-free graph independence-complex methods, Berghoff's spectral-sequence computations for other graphs, and Goyal–Shukla–Singh's graph-family Morse decompositions give relevant background, but no inspected statement identifies this specific equivariant character. The present result distinguishes a nontrivial, absolutely irreducible top homology action from the many other representations of the same dimension. Targeted literature and semantic mathematical-record searches found no equivalent or dominating equivariant computation; negative search alone cannot prove absolute novelty.

## Limitations
The statement concerns rational \(G\)-modules, not integral representation-lattice isomorphisms or equivariant homotopy equivalences. The group action is identified using the classical dodecahedral symmetry group and an exhaustive graph automorphism calculation. The proof relies on finite exact enumeration and elimination, with complete standalone source supplied. An equivalent equivariant calculation in unindexed literature remains possible.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first submitted 2010-07-02, https://arxiv.org/abs/1007.0418.
2. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, first submitted 2020-08-14, https://arxiv.org/abs/2008.06267.
3. S. Goyal, S. Shukla, A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, first submitted 2019-05-16, https://arxiv.org/abs/1905.06926.
4. *The dodecahedral independence complex is a wedge of four 5-spheres*, publicly indexed exact computation, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-dodecahedral-independence-complex-is-a-wedge-of-four-5-spher--ba0161fd495f/RESULT.md.
5. E. W. Weisstein, *Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/DodecahedralGraph.html.
6. DistanceRegular.org, *Dodecahedron* graph data, https://www.math.mun.ca/distanceregular/graphs/dodecahedron.html.
