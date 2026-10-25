# Klein-four symmetry of the matching complex of a four-by-six categorical path product

## Finding

Let \(P_n\) denote the path on \(n\) vertices, let \(G=P_4\times P_6\) be the *categorical* graph product (simultaneous adjacency in both factors), and let \(X=\mathsf M(G)\) be the simplicial complex of sets of pairwise vertex-disjoint edges of \(G\). Write \(r(i,j)=(3-i,j)\) and \(s(i,j)=(i,5-j)\) for the commuting row and column reversals, indexing both paths from zero. Set \(V_4=\langle r,s\rangle\), and let \(\alpha\) and \(\beta\) be the rational one-dimensional characters specified by \(\alpha(r)=-1,\alpha(s)=1\) and \(\beta(r)=1,\beta(s)=-1\).

The complete reduced rational \(V_4\)-homology representation is

\[
\widetilde H_k(X;\mathbb Q)\cong
\begin{cases}
\alpha\beta,&k=5,\\
2\alpha\oplus2\beta,&k=6,\\
3\mathbf1\oplus\alpha\beta,&k=7,\\
0,&\text{otherwise}.
\end{cases}
\]

Equivalently, the characters at \((1,r,s,rs)\) are respectively \((1,-1,-1,1)\), \((4,0,0,-4)\), and \((4,2,2,4)\) in degrees \(5,6,7\). As a nonequivariant consequence,
\[
X\simeq S^5\vee\bigvee^4 S^6\vee\bigvee^4 S^7.
\]
The quotient \(X/V_4\) has precisely three independent reduced *rational* homology classes, all in degree seven; its other reduced rational homology vanishes.

## Assumptions and scope

The graph product is the categorical/direct graph product, **not** the Cartesian grid. The graph \(G\) has \(24\) vertices and \(30\) edges. Matching complexes are ordinary abstract simplicial complexes containing the empty face, with their standard geometric realizations. The group action is the specified subgroup \(V_4\), not an assertion about the full automorphism group. All representation and quotient-homology statements use characteristic zero; the displayed nonequivariant homotopy equivalence is integral. The statement concerns exactly \(P_4\times P_6\), not all path dimensions.

## Proof

**1. Split the graph and its matching complex.** Every edge of the categorical product joins \((i,j)\) to \((i\pm1,j\pm1)\), so the parity of \(i+j\) is constant along edges. Each parity class induces a connected component, with twelve vertices and fifteen edges; row reversal interchanges the two isomorphic components \(A\) and \(B\), while the simultaneous reversal \(t=rs\) preserves each component. Because matchings on disjoint graph components are independent,
\[
X=\mathsf M(A)*\mathsf M(B).
\]

**2. Determine the two component homotopy types.** Enumerate the edges of \(A\) lexicographically by their endpoint pairs and encode matchings as fifteen-bit masks. Enumeration of all pairwise disjoint edge families gives \(383\) augmented faces, with face counts in dimensions \(-1,0,1,2,3,4,5\) equal to \((1,15,75,150,115,26,1)\). For each edge index in increasing order, pair every currently unmatched face not containing that edge with its one-edge enlargement, provided both faces remain unmatched. The resulting matching has \(190\) pairs and three unpaired faces, of dimensions \(2,3,3\). Reverse its matched Hasse incidences, orient all others from larger to smaller simplices, and topologically sort the complete \(383\)-vertex directed Hasse graph; all vertices are removed, so the matching is acyclic. Its integral algebraic Morse boundary from the two critical three-cells to the critical two-cell is the zero matrix \((0\ \ 0)\): this is obtained by signed facet elimination, with each matched incidence having coefficient \(\pm1\). For an ordinary nonaugmented Forman matching, omit just the empty-face-to-vertex pair: this makes that vertex the unique critical zero-cell and cannot create a directed cycle. Thus the ordinary Morse CW model has a basepoint, one two-cell and two three-cells. Because attaching maps of three-cells to the two-sphere are classified by their cellular degree \(\pi_2(S^2)\cong\mathbb Z\), zero boundary yields
\[
\mathsf M(A)\simeq\mathsf M(B)\simeq S^2\vee S^3\vee S^3.
\]
The join identity \(S^p*S^q\simeq S^{p+q+1}\) yields the displayed nonequivariant type; all its integral homology is free.

**3. Identify the action of the component-preserving half-turn.** On the fifteen lexicographically indexed edges of \(A\), \(t=rs\) induces the involution that reverses the ordering. In oriented simplicial chains, an invariant simplex contributes the sign of the induced permutation of its vertices. Splitting chains into the \(+1\) and \(-1\) eigenspaces, the exhaustive rational boundary-rank calculation gives
\[
\begin{array}{c|cc}
 &\dim H_2(\mathsf M(A);\mathbb Q)&\dim H_3(\mathsf M(A);\mathbb Q)\\\hline
 t=+1&0&2\\
 t=-1&1&0
\end{array}
\]
(here the row label indicates the eigenvalue). Thus \(t\) acts by \(-1\) on the rank-one second homology and by \(+1\) on the rank-two third homology. The same holds for \(B\), using the interchange isomorphism induced by \(r\), which commutes with \(t\).

**4. Recover the complete group character.** On reduced join homology, the Künneth identification is a degree-shifted tensor product. Any automorphism interchanging the two isomorphic graph components acts on a summand of bidegree \((p,q)\) by the graded interchange \((-1)^{(p+1)(q+1)}\), followed by the component isomorphisms. Hence each of \(r,s\) has trace \(-1\) on degree five (the \(2,2\) tensor), trace zero on degree six (the cross terms interchange), and trace \(+2\) on degree seven (the trace of the flip on a two-dimensional tensor square). The product \(t=rs\) preserves components, and its component eigenvalues from Step 3 give traces \(+1,-4,+4\) in degrees five, six, seven. Along with the dimensions \(1,4,4\), these are the three stated complete characters. Fourier inversion for \(V_4\) gives exactly \(\alpha\beta\), \(2\alpha\oplus2\beta\), and \(3\mathbf1\oplus\alpha\beta\).

**5. Pass to the symmetry quotient.** Over \(\mathbb Q\), finite-group averaging identifies the rational homology of a simplicial finite-group quotient with the invariant subspace of the original homology (after equivariant subdivision if needed). The representation from Step 4 therefore leaves exactly three invariant classes, all in degree seven.

## Verification

Run `python3 verify_path_product.py` with Python 3 and SymPy. The standalone checker constructs both parity components and all simplices from the edge definition, topologically sorts every incidence of the greedy Morse matching, calculates its signed integral Morse boundary, computes the eigenspace boundary ranks over exact rational arithmetic, and directly evaluates signed reduced simplicial Lefschetz numbers on all \(146689\) augmented faces of \(X\). Its expected final line is `CATEGORICAL_PATH_PRODUCT_CHARACTER_VERIFIED`. The independent full-face Lefschetz totals on \((1,r,s,rs)\) are \((-1,-1,-1,-9)\), agreeing with the alternating sum of the three graded characters. These finite checks are exhaustive for this finite graph, not an assertion about a general path-product family.

## Relationship to prior work

Gupta, Sarkar, Sawant and Shukla, *On the matching complexes of categorical product of path graphs*, first publicly available as arXiv:2403.15298v1 on 2024-03-22, prove in Theorem 1.3 that all \(\mathsf M(P_n\times P_m)\) with \(3\le m\le5\) are wedges of spheres. Their Section 4 develops recurrence-based nonequivariant reductions for \(m=4\). Thus the existence of a sphere-wedge decomposition, and the computability of its multiplicities from prior recurrences, are **not** claimed as new. The claim assessed here is the *complete graded rational action of the two path-reflection symmetries*, including the three invariant quotient classes. Their statements and reductions do not specify reflection-induced chain maps or character values; the present computation supplies that additional invariant. Caputi, Collari and Ramos, arXiv:2401.01248v1, study matching complexes of certain bipartite half-graphs/ladders in a quiver setting, not this four-by-six categorical product with the stated reflection action. Related indexed claims about a six-rung Cartesian ladder and about \(P_6\times P_6\) concern different underlying edge sets or parameters, so do not imply these character values.

## Limitations

No infinite-width character formula, integral \(V_4\)-lattice decomposition, independent replication or publication-priority certification is asserted. The source comparison examines the primary theorem statements and relevant Section 4 reductions of arXiv:2403.15298v2, plus a targeted abstract-level inspection of arXiv:2401.01248. Unindexed equivalent equivariant computations remain a residual originality risk; an abstract-only source is not treated as a full-text negative check. The exact finite verification and separate argument for group actions establish only the stated case.

## References

1. R. K. Gupta, S. Sarkar, S. S. Sawant and S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298v1 (first released 2024-03-22); reviewed also v2, 2026-04-23. https://arxiv.org/abs/2403.15298 .
2. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (2024-01-02). https://arxiv.org/abs/2401.01248 .
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. (Standard acyclic matching framework; the matching and matrices used here are independently specified and checked.)
