# Integral sphere-wedge topology and affine symmetry of a Paley higher-independence complex

## Finding
Let \(P_{17}\) be the 17-vertex quadratic-residue Paley graph and let \(X=\operatorname{Ind}_2(P_{17})\) be its two-independence complex. Then
\[
\boxed{X\simeq\bigvee^{18} S^3.}
\]
The natural group \(A=\mathbb F_{17}\rtimes\langle2\rangle\) of order 136 acts on \(X\). Its complete rational action on the only nonzero reduced homology group \(\widetilde H_3(X;\mathbb Q)\) is determined by the following character:
\[
\chi(1,0)=18,\qquad \chi(1,b)=1\ (b\ne0),\qquad
(\chi(2^j,b))_{j=1}^7=(0,-2,0,2,0,-2,0),
\]
for every \(b\in\mathbb F_{17}\). Here \((a,b)\) denotes \(x\mapsto ax+b\), and \(2\) has order eight modulo 17.

In particular, the translation-invariant subspace has dimension two and is the rational \(C_8\)-module \(\mathbb Q(i)\) with generator acting as multiplication by \(i\), and
\[
\boxed{\widetilde H_k(|X|/A;\mathbb Q)=0\quad(k\in\mathbb Z).}
\]
This is rational acyclicity, not a claim that the quotient is contractible.

## Assumptions and scope
Vertices of \(P_{17}\) are \(0,\ldots,16\), identified with \(\mathbb F_{17}\), and the nonzero squares are
\[
Q=\{1,2,4,8,9,13,15,16\}.
\]
Two distinct vertices \(u,v\) are adjacent precisely when \(v-u\pmod{17}\in Q\). The graph is strongly regular with parameters \((17,8,3,4)\). A face of \(X\) is precisely a subset \(\sigma\) whose induced subgraph \(P_{17}[\sigma]\) has no vertex of degree at least two. Equivalently, no connected triple of vertices is completely contained in \(\sigma\). Include the empty face in the abstract simplicial complex and use increasing vertex order for integer simplex orientations. The result concerns only this graph, this cutoff, and this indicated affine subgroup; no assertion about all Paley graphs or all automorphisms is needed.

## Proof
**1. Exhaustive face identification.** Enumerate integers \(0\le m<2^{17}\), with bit \(v\) of \(m\) indicating whether \(v\in\sigma\). Admit \(m\) if each occupied vertex has at most one occupied neighbor. The verifier checks all \(131071\) nonempty subsets and obtains exactly \(867\) nonempty faces, with dimension-wise face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(17,136,340,306,68).
\]
The graph's adjacency parameter checks \((17,8,3,4)\) and downward closure are independently recomputed, rather than accepted from a table.

**2. Complete acyclic discrete-Morse matching.** On all nonempty faces, take the ordered vertices
\[
(16,10,2,12,6,13,15,4,7,5,8,3,0,14,9,11,1).
\]
At each vertex \(v\), visit the still-unmatched faces in increasing bit-mask order and pair every face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both remain available, removing both. This gives exactly \(423\) matched codimension-one pairs. The unmatched faces consist of one vertex, one triangle of mask \(16396\), and nineteen tetrahedra. Form the directed Hasse graph by directing each unmatched face incidence downward, and each matched incidence upward. A topological sort removes all \(867\) nodes, proving that the matching is acyclic; the result therefore has a Morse CW model with one 0-cell, one 2-cell and nineteen 3-cells.

**3. Exact integral attaching degrees.** Give an oriented face \((v_0<\cdots<v_k)\) the standard incidence sign \((-1)^j\) on the facet omitting \(v_j\). The coefficient of the unique critical 2-cell in a triangle \(t\) is computed recursively. It is one on the critical triangle, zero if \(t\) is matched down to an edge, and if \(t\) is matched upward to a tetrahedron \(b\) then it is
\[
R(t)=-[b:t]^{-1}\!\sum_{u\subset b,\;\dim u=2,\;u\ne t}[b:u]R(u).
\]
Acyclicity ensures termination. Evaluating \(\sum_{t\subset c}[c:t]R(t)\) for the nineteen critical tetrahedra \(c\), in increasing mask order, gives the exact integer Morse boundary row
\[
(0,0,0,0,0,-1,1,-1,1,1,-1,1,0,0,0,0,0,0,1).
\]
Its entries have greatest common divisor one. An independent integer column-elimination computation gives the same coefficient multiset, and a separate complete binary boundary calculation gives ranks \((16,120,220,68)\) in degrees one through four. Because the critical 2-cell is a sphere and at least one 3-cell attaches by degree \(\pm1\), that 2-cell together with a single 3-cell forms a contractible CW subcomplex. The other eighteen 3-cell attaching maps into this contractible subcomplex are nullhomotopic, proving the stated integral sphere wedge. Merely computing field Betti numbers would not establish this homotopy type.

**4. Affine character and quotient.** Since \(a\in Q\) preserves the quadratic-residue difference relation, every map \(g_{a,b}:x\mapsto ax+b\) is a simplicial automorphism; the 136 pairs \((a,b)\) are distinct. For each map, compute the signed fixed-face alternating trace
\[
T(g)=\sum_{\emptyset\ne\sigma\in X,\;g\sigma=\sigma}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
The integral homotopy classification gives reduced rational homology only in degree three, hence the simplicial Lefschetz formula yields \(\chi_{\widetilde H_3}(g)=1-T(g)\). Exhaustively evaluating the 136 signed traces gives the character above. Averaging over the 17 translations yields a two-dimensional space of invariants whose \(C_8=\langle2\rangle\) character is \((2,0,-2,0,2,0,-2,0)\). This is the rational 2-dimensional quarter-turn representation. Its invariant subspace is zero; equivalently, summing the 136 homology-character values gives zero. After barycentric subdivision, rational cellular chains on the finite orbit space identify with the finite-group coinvariant chains; rational coinvariants are exact and equal to invariants. Therefore all reduced rational homology of \(|X|/A\) vanishes.

## Verification
Execute `python3 verify_paley17_ind2.py` with Python 3 and no third-party dependencies. It reconstructs all 131071 nonempty subsets from the adjacency definition; checks the 867 admissible faces, all integral boundary compositions, independent mod-two ranks, 423 Morse pairs and Hasse acyclicity, signed gradient recurrence, and 136 affine signed Lefschetz traces. It terminates with `PALEY17_IND2_INTEGRAL_MORSE_AND_AFFINE_CHARACTER_OK`; the complete actual output is `verification_output.txt`. The separate `verify_morse_elimination.py` performs integer column elimination without using the gradient recurrence; its recorded output is `morse_elimination_output.txt`. Both checkers are part of this package. The finite exhaustive computations are the proof for this specified finite complex, not an inductive theorem for other graph orders.

## Relationship to prior work
Deshpande and Singh [1] introduced a systematic homotopy study of higher-independence complexes, determining types for complete multipartite, fully whiskered, path, cycle and perfect rooted tree families. Abdelmalek and collaborators [2] studied structural properties for trees, caterpillars and chordal graphs. These statements do not cover the nonchordal Paley graph: \(0,1,3,4\) induce a chordless four-cycle. A separately published exact two-independence calculation for the Petersen graph [3] concerns a different ten-vertex graph and does not imply the present number of spheres or affine action. The published result for the Lovász **open-neighborhood complex** of \(P_{17}\) [4] analyzes a different simplicial functor on the same graph: its faces are subsets of a single vertex's open neighborhood, not vertex sets with induced maximum degree at most one. A previously recorded ordinary \(\operatorname{Ind}_1(P_{17})\) result likewise concerns a different complex and does not determine this cutoff-two homotopy type. Searches for aliases, graph identification, higher-independence formulas, stronger classifications and matching exact tables found no theorem implying the claim. The possibility of an equivalent unindexed calculation remains.

## Limitations
Only \(\operatorname{Ind}_2(P_{17})\) is classified, not higher cutoffs or other Paley orders. The representation concerns the specified affine subgroup; the complete abstract automorphism group is not required. The quotient is rationally acyclic, not proved contractible. The proof is exact and exhaustive for 17 vertices but does not give a parameterized infinite-family theorem. Literature searches do not certify publication priority, and no independent external audit has been performed.

## References
[1] P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public version 2020-01-15, especially sections 2–5 and the main graph-class classification; MSC 55P15.

[2] F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public version 2021-06-21, especially definitions and sections 2–4.

[3] *The 2-independence complex of the Petersen graph is a 3-sphere*, publicly available mathematical result and complete proof: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a .

[4] *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, publicly available mathematical result and complete proof: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8 .
