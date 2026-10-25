# Dihedral homology characters of the side-two honeycomb perfect-matching complex

## Finding
Let \(G\) be the honeycomb graph dual to the 24 unit triangles of the regular side-two hexagon in the triangular lattice, and let \(X=\mathcal M_p(G)\) be its perfect-matching simplicial complex. Its geometric dihedral symmetry group \(D_6=\langle r,s\mid r^6=s^2=1,\ srs=r^{-1}\rangle\) acts on \(X\). The reduced integral homology is free of rank two in degree three and vanishes in other degrees. More precisely, the complete rational character \(\chi\) on that two-dimensional homology space is
\[
\chi(r^k)=1+(-1)^k,\qquad \chi(r^ks)=(-1)^k-1,\quad 0\le k\le5.
\]
Thus, as rational \(D_6\)-representations,
\[
\widetilde H_3(X;\mathbb Q)\cong\mathbb Q_{(r=1,s=-1)}\oplus\mathbb Q_{(r=-1,s=1)}.
\]
Consequently, reduced rational homology of the cyclic-rotation quotient has dimension one in degree three, while the full dihedral quotient has zero reduced rational homology. Reflection quotients have reduced degree-three rational rank one for \(r^{2j}s\) and rank zero for \(r^{2j+1}s\); these are the two geometrically distinct reflection-axis classes. These are claims about rational quotient homology, not quotient homotopy types.

## Assumptions and scope
Use integer lattice coordinates \((q,t)\), representing the triangular lattice with two unit basis vectors at angle \(60^\circ\). The regular hexagon is the set of elementary triangles contained in the convex region
\[
\max(|q|,|t|,|q+t|)\le2.
\]
Its 24 elementary triangular cells are the graph vertices; two cells are adjacent precisely when they share a full edge, giving 30 graph edges. The perfect-matching complex has these 30 edges as simplicial vertices, and a set of them is a face if it is contained in a perfect matching of the 24-vertex dual graph. We include the empty face, with reduced augmentation degree minus one. Reflection and rotation on lattice coordinates are respectively \(s(q,t)=(t,q)\) and \(r(q,t)=(-t,q+t)\). Every integer \(k\) in the theorem is interpreted modulo six. Homology groups have integral coefficients unless expressly indicated as rational.

## Proof
**Exhaustive finite simplicial model.** A unit triangular cell has one of two forms: \(\{(q,t),(q+1,t),(q,t+1)\}\) or \(\{(q+1,t+1),(q+1,t),(q,t+1)\}\), provided all its vertices lie in the closed hexagon. Lexicographically sort the resulting 24 three-vertex sets, and lexicographically sort the 30 unordered pairs of triangles sharing two lattice vertices. This fixes all vertex and edge labels without arbitrary choices.

A perfect matching of the dual graph can be enumerated recursively: take the least currently unmatched triangle, pair it with each available neighbor, and recurse. Every perfect matching occurs once, since its partner at that least triangle is uniquely determined. The recursion produces exactly 20 perfect matchings, each of 12 graph edges. The union of their downward-closed face sets has exactly 66,370 faces, including the empty face. The attached standalone script constructs this complete finite collection from the coordinate inequalities alone; no face is inferred from a non-exhaustive search.

**Integral homotopy.** Process the 30 simplicial vertices in their fixed order. At vertex \(j\), pair each as-yet-unpaired face not containing \(j\) with its immediate coface obtained by inserting \(j\), whenever that coface remains unpaired. After all 30 stages there are exactly 33,184 matched covering pairs and exactly two critical faces, both containing four graph edges, hence both of dimension three. This covers every one of the 66,370 faces. The verifier builds the *entire* directed Hasse graph, reversing precisely the matched covering relations, and proves the resulting digraph acyclic by a complete topological sort of all 66,370 nodes. Thus the matching is an integral acyclic discrete-Morse matching, not simply a list of critical-cell counts. Its reduced Morse CW complex contains exactly two three-dimensional cells, with no cells in any other nonnegative dimension. The reduced elementary-collapse/discrete-Morse theorem therefore identifies \(X\simeq S^3\vee S^3\), proving all asserted integral homology groups. This homotopy type agrees with the nonequivariant result of Bayer, Jelić Milutinović and Vega; it is not claimed here as original.

**Equivariant chain trace.** Every symmetry acts on the 30 graph edges, and hence by signed vertex permutation on oriented simplices. Given \(g\in D_6\), let \(\mathcal O_g\) be the disjoint cycles of its permutation of these 30 vertices. A \(g\)-invariant face is a union of whole cycles; write \(o(F)\) for the number of chosen cycles. If \(F\) has \(m\) vertices, the simplicial orientation sign equals \((-1)^{m-o(F)}\). Hence its contribution to the *augmented* alternating chain trace is \((-1)^{m-1}(-1)^{m-o(F)}=-(-1)^{o(F)}\). This identity also holds for the empty face, whose augmentation contributes minus one. It follows that the reduced Lefschetz number is
\[
L(g)=-\sum_{\substack{F\in X\\gF=F}}(-1)^{o(F)}.
\]
Since the only nonzero reduced rational homology is in odd degree three, the Hopf trace formula gives \(L(g)=-\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))\). The required character is therefore exactly the finite orbit sum
\[
\chi(g)=\sum_{\substack{F\in X\\gF=F}}(-1)^{o(F)}.
\]

The complete enumeration yields, in the order \(k=0,\ldots,5\), the trace rows
\[
\big(\chi(r^k)\big)=(2,0,2,0,2,0),\qquad
\big(\chi(r^ks)\big)=(0,-2,0,-2,0,-2).
\]
The corresponding counts of invariant faces, including the empty face, are respectively \((66370,4,58,232,58,4)\) and \((240,962,240,962,240,962)\). The script confirms these by two separate computations: the cycle-orbit sum and a direct enumeration of orientation signs of every fixed simplex, including degree-minus-one augmentation. Because the original full face set is exhaustive, this is an exact finite proof for all twelve group elements, not numerical sampling.

**Representation identification and quotients.** The group relations show that \(D_6\) has one-dimensional rational characters \(\lambda(r)=1,\lambda(s)=-1\) and \(\mu(r)=-1,\mu(s)=1\). Their character sum is exactly the computed twelve-element row. Maschke semisimplicity and uniqueness of rational characters therefore give \(\widetilde H_3(X;\mathbb Q)=\lambda\oplus\mu\). The invariant dimension under \(\langle r\rangle\) is one; under the full \(D_6\) it is zero; and a reflection \(r^ks\) has invariant dimension one for even \(k\) and zero for odd \(k\). Passing to barycentric subdivision eliminates simplex inversions, and transfer over \(\mathbb Q\) identifies homology of any finite-group quotient with the invariant rational homology. This proves the stated quotient Betti numbers.

## Verification
Run `python3 verify.py` from the directory containing this result. The standard-library-only program reconstructs the 24 triangles and 30 adjacency edges from their defining coordinates, enumerates all 20 perfect matchings and all 66,370 faces, checks all 33,184 Morse pairs and the entire oriented Hasse digraph for acyclicity, verifies the twelve dihedral permutations and their relations, and independently computes both augmented signed chain traces and invariant-orbit sums for every symmetry. The asserted values are verified by exact integer arithmetic. The complete printed output identifies invariant-face counts and traces element by element.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega (arXiv:2209.02803v1, first public September 6, 2022) prove the nonequivariant sphere-wedge homotopy type in their section on the exceptional \(2\times2\times2\) honeycomb; their introduction, section four and appendix give the precise object and the underlying tiling bijection. That result implies only the dimension of the homology representation. The new statement determines the action of every sixty-degree rotation and both reflection conjugacy classes. Kuperberg's work (arXiv:math/9410224) enumerates symmetry-constrained plane partitions and lozenge tilings, i.e. *facets* here; fixed-facet counts are not the signed alternating sums over *all faces* needed to determine the homology character. No claim that literature searches alone establish novelty is made.

## Limitations
The group representation is determined over \(\mathbb Q\), not as a \(\mathbb Z[D_6]\)-module; the latter may contain extension data invisible to rational characters. Quotient homotopy types and integral quotient torsion are not determined. The result concerns only the side-two regular honeycomb, not all hexagonal side lengths. The homotopy type was previously known, and there remains some risk of an unindexed equivalent equivariant analysis. The finite calculation is exhaustive for this single precisely specified complex; it implies no larger-family theorem.

## References
1. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first public 2022-09-06), https://arxiv.org/html/2209.02803v1.
2. G. Kuperberg, *Symmetries of Plane Partitions and the Permanent-Determinant Method*, arXiv:math/9410224 (1994), https://arxiv.org/abs/math/9410224.
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145; standard acyclic matching/discrete-Morse collapse theorem.
