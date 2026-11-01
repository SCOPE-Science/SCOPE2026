# Unique order-two torsion in the six-point triangle-free graph complex

## Finding
Let \(X\) be the simplicial complex whose vertices are the fifteen edges of the complete graph on \(\{0,1,2,3,4,5\}\), and whose faces are all edge sets that contain no triangle. The complete two-primary torsion subgroup of its fifth integral homology is
\[
\operatorname{Tor}_{2} H_{5}(X;\mathbb Z)\cong\mathbb Z/2.
\]
Here \(\operatorname{Tor}_{2}\) denotes the subgroup of elements whose order is a power of two. In particular, the triangle-free graph complex is not homotopy equivalent to a wedge of spheres.

## Assumptions and scope
Graphs are simple, finite, undirected, and have the fixed six-vertex set above; isolated vertices are permitted. A face is a subset of the fifteen lexicographically ordered unordered graph edges. Every three-point set forbids the simultaneous presence of its three edges. Simplicial chains have the standard increasing-edge orientation and integral coefficients. The assertion concerns degree-five unreduced homology (equal to reduced homology in that degree), not the homology of the clique complex of any single triangle-free graph.

## Proof
The face enumeration is exhaustive: inspect all \(2^{15}\) subsets of potential edges and reject a subset exactly when it contains one of the twenty forbidden three-edge triangle patterns. The numbers of faces in degrees \(-1,0,1,2,3,4,5,6,7,8\) are, respectively,
\[
(1,15,105,435,1125,1773,1560,660,105,10).
\]
Let \(\partial_j:C_j(X;\mathbb Z)\to C_{j-1}(X;\mathbb Z)\) be the oriented simplicial boundary matrix. The relevant dimensions are \(\partial_6: \mathbb Z^{660}\to\mathbb Z^{1560}\) and \(\partial_7:\mathbb Z^{105}\to\mathbb Z^{660}\). Using the exact finite reduction procedures reproduced in `check_tri6.py`, one obtains
\[
\operatorname{rank}_{\mathbb F_2}(\partial_6)=564,\qquad
\operatorname{rank}_{\mathbb F_3}(\partial_6)=565,\qquad
\operatorname{rank}_{\mathbb F_3}(\partial_7)=95.
\]
The code also verifies \(\partial_6\partial_7=0\) entry by entry. Consequently,
\[
565\le\operatorname{rank}_{\mathbb Q}(\partial_6)
\le660-\operatorname{rank}_{\mathbb Q}(\partial_7)
\le660-95=565.
\]
Thus the exact rational rank of \(\partial_6\) is 565. Its integral Smith form therefore has exactly 565 nonzero diagonal invariant factors. Reduction modulo two has rank 564, so *exactly one* of those factors is even.

To find that factor's precise two-adic valuation, perform invertible row and column reductions over \(\mathbb Z/4\): move any odd entry of the current residual matrix to the pivot, invert it modulo four, eliminate its column and row, and repeat. This produces exactly 564 unit pivots, after which every residual entry is even and 630 residual entries are congruent to two modulo four. Since the integral matrix has only one further nonzero invariant factor, that factor is twice an odd integer (it is divisible by two but not by four). Hence the two-primary torsion of \(\operatorname{coker}(\partial_6)\) consists of exactly one copy of \(\mathbb Z/2\).

Finally, because \(\partial_5\partial_6=0\), there is an exact sequence
\[
0\longrightarrow H_5(X;\mathbb Z)\longrightarrow
\operatorname{coker}(\partial_6)\longrightarrow
\operatorname{im}(\partial_5)\longrightarrow0.
\]
The last group is a subgroup of the free abelian group \(C_4\), hence free. The exact sequence splits as an exact sequence of abelian groups, and its torsion is entirely in the first term. This proves the displayed claim. Notice that it does not require calculation of the remaining integral homology groups.

## Verification
Run `python3 check_tri6.py` in a Python environment with NumPy. The standalone program independently reconstructs all faces, explicitly forms both signed boundary matrices, checks their composition, uses a binary bit-vector rank algorithm over \(\mathbb F_2\), a distinct coefficient-aware column elimination over \(\mathbb F_3\), and invertible pivot elimination modulo four. The numerical results and explicit assertions are reproduced in `verification_output.txt`; the programs perform the calculations rather than relying on those recorded lines. The prime-field ranks are exact, as is the modulo-four reduction. The rational-rank conclusion follows from the chain-complex inequality in the proof.

## Relationship to prior work
Linusson and Shareshian study the simplicial complexes of \(t\)-colorable graphs; in particular, their bipartite-graph complex is a strict subcomplex of this triangle-free complex. Their wedge-of-spheres result for bipartite graphs does not determine the topology of the larger triangle-free complex: the five-cycle and an isolated vertex give a six-point triangle-free graph that is not bipartite. Jonsson studies bounded-covering-number graph complexes, which are different families; their homology does not determine the homology of this subcomplex. General descriptions of monotone graph complexes do not, without a suitable relative calculation, imply a Smith invariant in degree six. The closest accessible scientific descriptions examined did not identify this exact two-primary torsion group. Priority remains subject to inspection of additional specialist full texts.

## Limitations
Only the two-primary torsion in fifth integral homology is determined. This calculation makes no claim about odd-primary torsion, complete integral Betti numbers, homotopy type, representation under relabeling, or whether six points is the smallest possible vertex count for such torsion. The code checks finite integer matrices; it does not independently certify bibliographic novelty. Some relevant general books and papers were accessible only through their tables of contents, abstracts, or previews.

## References
- Svante Linusson and John Shareshian, *Topology of Colors (Extended Abstract)*, in *Formal Power Series and Algebraic Combinatorics* (2000), DOI: https://doi.org/10.1007/978-3-662-04166-6_24.
- Svante Linusson and John Shareshian, *Complexes of t-Colorable Graphs*, *SIAM Journal on Discrete Mathematics* 16 (2003), 371–389, DOI: https://doi.org/10.1137/S0895480100366968.
- Jakob Jonsson, *Simplicial Complexes of Graphs and Hypergraphs with a Bounded Covering Number*, *SIAM Journal on Discrete Mathematics* 19 (2005), 633–650, DOI: https://doi.org/10.1137/S0895480104443680.
- Jakob Jonsson, *Simplicial Complexes of Graphs*, Lecture Notes in Mathematics 1928 (2008), DOI: https://doi.org/10.1007/978-3-540-75859-4.
