# Integral homotopy and symmetry of the two-independence complexes of diameter-four trees

## Finding
For every finite tree \(T\) of diameter at most four, the integral homotopy type of its **two-independence complex** \(\operatorname{Ind}_2(T)\) is given by a complete, branch-size-dependent formula. In the noncontractible diameter-four case, its top integral homology also has an explicit natural automorphism module.

Let \(c\) be a central vertex, with neighbors \(a_1,\ldots,a_k\). Let \(B_i\) denote the pendant-neighbor set of \(a_i\) other than \(c\), and write \(b_i=|B_i|\), \(p=|\{i:b_i>0\}|\). The complete formula is
\[
\operatorname{Ind}_2(T)\simeq
\begin{cases}
\mathrm{pt},&k=0,\\
\bigvee^{b_1}S^1,&k=1,\\
\bigvee^{k-1}S^1,&k\ge2,\ p=0,\\
S^1,&k\ge2,\ p=1,\\
\mathrm{pt},&k\ge2,\ p\ge2,\ p<k,\\
\bigvee^{\prod_i(b_i-1)}S^{2k-1},&k\ge2,\ p=k.
\end{cases}
\]
The empty wedge means a point. In particular, for a tree of diameter exactly four, all \(k\) branches have positive sizes; the complex is noncontractible exactly when every branch has at least two leaves. The number of spheres is then \(\prod_i(b_i-1)\), with their common dimension \(2k-1\). All reduced integral homology is free and is concentrated in the displayed sphere dimension.

For diameter-four trees with \(b_i\ge2\) throughout, the center \(c\) is unique. Write \(I(B_i)=\ker(\mathbb Z[B_i]\xrightarrow{\sum}\mathbb Z)\). The full graph automorphism group, acting on the unique center, on branches, and on their leaves, acts on the top reduced integral homology by the canonical module isomorphism
\[
\widetilde H_{2k-1}(\operatorname{Ind}_2(T);\mathbb Z)\cong\bigotimes_{i=1}^k I(B_i).
\]
The permutation of factors carries no additional graded sign. If \(g\) acts on the branch indices with cycles \(C\), let \(f_C\) count leaves fixed by the composite bijection going once around \(C\). The complete rational trace is
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{2k-1}(\operatorname{Ind}_2(T);\mathbb Q)\bigr)=\prod_C(f_C-1).
\]

## Assumptions and scope
A two-independent face is a subset \(S\subseteq V(T)\) whose induced subgraph has no component on three or more vertices. For a tree this is equivalent to containing no complete three-vertex path, whether or not other vertices are selected. All graphs are finite, simple, and undirected. A tree of diameter at most four admits the described depth-two rooting at a center; for trees of diameter exactly four this center is unique. The module and trace formulas concern the noncontractible diameter-four case; they make no assertion of equivariant homotopy equivalence. The boundary cases \(k=0\), \(k=1\), and short arms are included in the nonequivariant statement.

## Proof
Set \(X=\operatorname{Ind}_2(T)\). Deletion of \(c\) splits the graph into disjoint stars \(K_{1,b_i}\), so
\[
D=X-c=\bigast_{i=1}^k\operatorname{Ind}_2(K_{1,b_i}).
\]
For \(b\ge1\), writing \(B\) for the leaves and \(a\) for the star center, the star complex is exactly the union of the full leaf simplex \(\Delta(B)\) and the cone on the discrete complex of singleton leaves with apex \(a\). Both pieces are contractible and intersect in precisely the \(b\) isolated leaf vertices. Therefore the star complex is homotopy equivalent to \(\bigvee^{b-1}S^1\), and its first reduced integral homology is naturally the augmentation kernel \(I(B)\). For \(b=0\) it is a simplex point. Thus \(D\) is contractible if any \(b_i=0\); otherwise it is the join of \(k\) circle bouquets, with dimension \(2k-1\), multiplicity \(\prod_i(b_i-1)\), and top integral homology \(\bigotimes_i I(B_i)\). This statement includes the case \(b_i=1\), when the corresponding factor is contractible.

The link \(L=\operatorname{lk}_{X}(c)\) has at most one neighbor \(a_i\), because selecting \(c\) and two children makes an induced component of size three. If it chooses \(a_i\), it must omit every leaf in \(B_i\), but may select any leaf outside \(B_i\). Hence, with \(B=\bigsqcup_i B_i\),
\[
L=\Delta(B)\ \cup\ \bigcup_{i=1}^k\bigl(a_i*\Delta(B\setminus B_i)\bigr).
\]
Here the expression \(a_i*\Delta(\varnothing)\) means the isolated vertex \(a_i\); it should not be confused with a geometric cone on a point. If \(p\ge2\), each set \(B\setminus B_i\) is nonempty, and every new simplex with apex \(a_i\) is a cone attached along a nonempty face simplex contained in \(\Delta(B)\). Successively collapsing these cone pieces shows that \(L\) is contractible. If \(p=1\), the unique child with leaves is isolated in \(L\) and all other children attach by simplices to \(\Delta(B)\), so \(L\) has exactly two contractible components and is homotopy equivalent to \(S^0\). If \(p=0\), the link consists of \(k\) isolated vertices.

Finally, \(X=D\cup_L(c*L)\) is the homotopy cofiber of the simplicial inclusion \(L\hookrightarrow D\). When \(L\) is contractible and nonempty, this inclusion is a homotopy equivalence on its homotopy-cofiber contribution, giving \(X\simeq D\). When \(p\le1\) and \(k\ge2\), at least one \(b_i=0\), so \(D\) is contractible and \(X\simeq\Sigma L\). The suspension of \(k\) discrete points is a wedge of \(k-1\) circles; the suspension of \(S^0\) is a circle. If \(k=1\), the entire original tree is the star \(K_{1,b_1+1}\), yielding \(\bigvee^{b_1}S^1\). If \(k=0\), the complex is a point. These exhaust all cases.

When \(b_i\ge2\) for every branch, \(L\) is contractible and \(D\hookrightarrow X\) induces a natural, integral, automorphism-equivariant isomorphism on reduced homology. The join Künneth isomorphism for the star summands identifies top homology with \(\bigotimes_i I(B_i)\). Swapping two degree-one factors in a join has Koszul sign \((-1)^{(1+1)(1+1)}=+1\), so a branch permutation merely reorders the augmentation factors. The trace of a cycle of tensor-factor permutations with intertwining leaf bijections equals the trace of their composite on one augmentation lattice; the latter trace equals the number of fixed leaves minus one. Multiplication over cycles yields the character formula.

## Verification
The standalone program `verify_height2.py` independently enumerates every vertex subset and checks the induced-component-size condition. It computes the complete mod-two homology of each finite test complex by exact boundary-matrix elimination and compares it with the theorem. It checks all branch vectors with \(1\le k\le4\), \(0\le b_i\le2\), and at most twelve vertices, plus seven additional cases. It also independently evaluates eleven signed fixed-simplex Lefschetz traces against the stated automorphism-character formula. The recorded output is `verification_output.txt`. These checks independently corroborate finite instances; the general integral statement follows from the proof above, not from finite enumeration.

## Relationship to prior work
Deshpande and Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448, initially public January 15, 2020), determine the homotopy types for **perfect regular** \(m\)-ary trees; their height-two specialization is already covered and is **not** asserted as new here. Their concluding Question 2 asks for the number of spheres for general trees. Their Theorem 6.1 records a general sphere-wedge result for chordal graphs, without a branch-dependent count. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* (arXiv:2605.25150, May 24, 2026), establishes vertex decomposability for all trees and all parameters; this proves qualitative wedge behavior but does not supply the present full diameter-four numerical classification or its natural integral automorphism module. Abdelmalek and collaborators (arXiv:2106.10863) independently study the chordal setting. The claimed contribution is the arbitrary unequal-branch classification, the zero-branch boundary cases, and the integral symmetry identification for all noncontractible diameter-four trees.

## Limitations
This class is restricted to trees of diameter at most four and the two-independence parameter. No general formula for arbitrary trees, other independence parameters, all chordal graphs, equivariant homotopy splitting, or publication-priority certification is claimed. Uniform regular subclasses and certain small stars appear in prior published theory. An unindexed equivalent classification could exist. The finite verification is over characteristic two and does not by itself establish torsion-freeness; the integral proof does.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public May 24, 2026, https://arxiv.org/html/2605.25150v1 .
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first public January 15, 2020, https://arxiv.org/html/2001.05448v2 .
3. S. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public June 21, 2021, https://arxiv.org/abs/2106.10863 .
