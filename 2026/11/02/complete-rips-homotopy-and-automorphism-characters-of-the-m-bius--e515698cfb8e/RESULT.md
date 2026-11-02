# Complete Rips homotopy and automorphism characters of the Möbius–Kantor graph

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph, with vertex shortest-path distance, and let \(R_r=\operatorname{VR}_{\le r}(V(M))\) be the inclusive flag complex of all vertex sets having diameter at most \(r\). For every real \(r\ge0\), the complete **integral homotopy filtration** is

\[
R_r\simeq\begin{cases}
\bigvee^{15}S^0,&0\le r<1,\\
\bigvee^{9}S^1,&1\le r<2,\\
\bigvee^{9}S^2\vee\bigvee^{2}S^3,&2\le r<3,\\
S^7,&3\le r<4,\\
\mathrm{pt},&r\ge4.
\end{cases}
\]

Thus all reduced integral homology groups are free. The complete reduced barcode, with integral coefficients, consists of fifteen degree-zero bars \([0,1)\), nine degree-one bars \([1,2)\), nine degree-two bars \([2,3)\), two degree-three bars \([2,3)\), and one degree-seven bar \([3,4)\). There are no other bars.

Write \(G=\operatorname{Aut}(M)\), of order \(96\), and \(b:G\to\{\pm1\}\) for its action on the two graph bipartition classes. In degree three at radius two, the complete rational representation is
\[
\widetilde H_3(R_2;\mathbb Q)\cong\mathbf1\oplus\mathbb Q_b.
\]
For every \(g\in G\), let \(L_2(g)\) be the alternating signed count of simplices of \(R_2\) fixed setwise by \(g\):
\[
L_2(g)=\sum_{k=0}^3(-1)^k\sum_{\substack{\sigma\in R_2,\ |\sigma|=k+1\\g\sigma=\sigma}}\operatorname{sgn}(g|_\sigma).
\]
Then the **entire degree-two character**, not merely its dimension, is
\[
\chi_{\widetilde H_2(R_2;\mathbb Q)}(g)=L_2(g)+b(g).
\]
Its values \(-3,-1,1,3,9\) occur respectively on \(8,42,39,6,1\) elements of \(G\). The degree-three character is \(1+b\) (value \(2\) on 48 group elements and \(0\) on 48). At radius three, \(G\) acts trivially on \(\widetilde H_7(R_3;\mathbb Q)\).

Consequently the rational quotient homology at scale two has only \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q\), while at scale three it has only \(H_0\cong\mathbb Q\) and \(H_7\cong\mathbb Q\). The full quotient's positive-degree rational barcode has exactly one bar \([2,3)\) in degree three and one \([3,4)\) in degree seven.

## Assumptions and scope
The graph has vertices \(u_i,v_i\), with \(i\in\mathbb Z/8\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). No continuum of points along graph edges is used: the metric space is precisely the sixteen **vertices** with the unweighted graph distance. The scale convention is \(d(x,y)\le r\), not strict inequality or open-ball Čech. All homotopy claims are ordinary, nonequivariant integral homotopy equivalences; group statements concern ordinary rational homology. Graph automorphisms act by vertex permutation at every scale.

## Proof
1. **The first and last scales.** The graph is connected, triangle-free, with sixteen vertices and twenty-four edges. Hence \(R_1=M\simeq\bigvee^9 S^1\); at radius zero the vertices are discrete. Exhaustive breadth-first graph distances give diameter four. Precisely eight pairs of vertices have distance four and they partition the sixteen vertices into disjoint pairs. Thus the scale-three graph is complete except for a perfect matching, and \(R_3\) is the eightfold join of two-point sets: the boundary of an eight-dimensional cross-polytope \(S^7\). At radius four every subset is a simplex.

2. **Exact scale-two Morse reduction.** Encode a nonempty simplex by its sixteen-bit vertex mask. The full scale-two face vector is \((16,72,112,48)\) in dimensions zero through three. The deterministic vertex order
\[
(3,15,13,4,12,6,9,1,14,2,7,10,11,0,8,5)
\]
constructs an explicit matching: for each vertex in order, pair every currently unpaired face not containing that vertex with its coface obtained by adding the vertex, whenever both remain. The result is exactly 118 matched pairs and critical cells in dimensions \((0,1,2,3)\) numbering \((1,0,9,2)\). Direct all 672 face-poset cover relations upward on matched pairs, downward otherwise; exhaustive topological sorting visits all 248 faces, proving the matching acyclic. Exact signed elementary chain cancellation uses only unit coefficients \(\pm1\) and yields **zero integral Morse differential** on the twelve critical cells. The resulting Morse CW structure has one vertex, nine two-cells and two three-cells. The two-cells are attached trivially, and the degree-zero attaching maps of the three-cells are nullhomotopic since \(\pi_2(\bigvee^9S^2)\cong\mathbb Z^9\). This proves the asserted mixed sphere wedge, not only its Betti numbers or homology after reduction modulo a prime.

3. **Symmetry characters.** Exhaustive adjacency-preserving backtracking produces exactly 96 automorphisms, with no duplicates. Two explicit integral third cycles are encoded as signed sums of sixteen tetrahedra apiece by the accompanying checker. Direct simplicial boundary calculations verify they are cycles; their coordinate projections at tetrahedron masks 1290 and 2565 form the identity matrix. Since the Morse reduction proves \(\operatorname{rank}H_3=2\) and there are no four-simplices, these two classes form an integral basis of degree-three homology. Checking the action of each of the 96 automorphisms on these two cycles shows \(\chi_3=1+b\). Lefschetz's alternating trace identity yields \(\chi_2=L_2-1+\chi_3=L_2+b\). For the scale-three cross-polytope, orientation equals the sign of the permutation of the eight opposite pairs times the product of their individual swap signs; this product is \(+1\) for all 96 graph automorphisms. Averaging the characters over the finite group gives invariant dimensions \(0\) in degree two and \(1\) in degree three at scale two, and \(1\) in degree seven at scale three. In degree one at radius one the invariant dimension is zero. Rational orbit-space homology equals group-invariant rational homology after equivariant subdivision, giving the quotient assertions.

4. **Persistent intervals.** Distinct positive-degree reduced groups arise only in the degrees and integer scale windows stated. No homology degree occurs at two adjacent nontrivial integer scales; consequently no positive-degree inclusion map can preserve a nonzero class across a threshold. At radius one the graph becomes connected, giving the degree-zero intervals. This determines the full barcode, with no inferred persistence maps hidden by the separate Betti computations.

## Verification
Run the standalone \(\texttt{verify.py}\) using Python 3. The program rebuilds every distance and scale-two face, performs the 118-pair acyclicity check and exact integer chain cancellations, verifies the signed integral third cycles, exhaustively enumerates the 96 graph automorphisms, and checks all signed characters and their averages. Its success marker is `MOBIUS_KANTOR_RIPS_EXACT_MORSE_96_CHARACTER_OK`. The code requires only Python's standard library. The vertex order and all cycle coefficients are included directly in that file.

## Relationship to prior work
Adams, Frick and Virk prove general homotopy-group comparisons between Vietoris complexes and their metric thickenings, rather than these graph-specific homotopy types. Shukla and Feng determine homology and homotopy patterns for **hypercube** graph Rips complexes; those theorems do not apply to the three-regular graph \(\operatorname{GP}(8,3)\). Knill describes the Möbius–Kantor graph's geodesics, toroidal realization and automorphism group, including Lefschetz calculations on the graph itself, but does not compute the Rips scale-two or scale-three homology representation. A related exact computation of the intrinsic ball-nerve filtration of this graph is about a distinct Čech-type complex and cannot imply the present Rips result simply by a change of indexing or convention.

## Limitations
The theorem concerns a fixed canonical finite metric space, not all generalized Petersen graphs or all scales of arbitrary graph metrics. The quotient conclusions are **rational**, with no assertion about integral torsion in quotient spaces. The finite checker independently reconstructs this finite instance; no claim of externally independent validation or of an exhaustive search of unpublished work is made. Equivalent unindexed computations remain a possible bibliographic risk. The classical use of graph distance on vertices must not be conflated with geodesic distance on the continuously realized graph.

## References
- H. Adams, F. Frick and Ž. Virk, *Vietoris thickenings and complexes have isomorphic homotopy groups*, first public 2022-06-17, arXiv:2206.08812, Journal of Applied and Computational Topology 7 (2023), 221–241.
- S. Shukla, *On Vietoris–Rips complexes (with scale 3) of hypercube graphs*, first public 2022-02-06, arXiv:2202.02756.
- Z. Feng, *Homotopy types of Vietoris–Rips complexes of hypercube graphs*, first public 2023-05-11, arXiv:2305.07084.
- O. Knill, *Remarks about the Moebius–Kantor graph*, first public 2026-05-29, arXiv:2605.30799.
