# Transposition-fixed homotopy of Johnson-graph clique complexes

## Finding

For integers \(n\geq6\) and \(3\leq k\leq n-3\), let \(J(n,k)\) be the graph on the \(k\)-element subsets of \([n]\), with edges joining subsets whose intersection has size \(k-1\). Write \(K(n,k)=\operatorname{Cl}(J(n,k))\) for its clique complex (equivalently, its inclusive graph-metric Vietoris–Rips complex at scale one). Let \(t=(1\;2)\) act through permutation of the ground-set elements. Set \(m=n-2\), and, for \(1\leq j\leq m-1\), define

\[
 b(m,j)=\binom mj-1-\frac{j(m-j)}2\binom mj
       +\binom m{j-1}\binom{m-j}{2}
       +\binom m{j+1}\binom j2.
\]

Then the *geometric fixed-point space*, rather than the fixed-vertex subcomplex, has the homotopy type

\[
 \boxed{|K(n,k)|^{\langle t\rangle}\simeq
   \bigvee^{\binom{n-2}{k-1}-1}S^1
   \;\vee\;
   \bigvee^{b(n-2,k)+b(n-2,k-2)}S^2.}
\]

Zero summands are omitted. In particular, the fundamental group is free of rank \(\binom{n-2}{k-1}-1\). The only possibly nonzero reduced integral homology groups are free abelian in degrees one and two, with ranks given by the corresponding exponents in the displayed formula. For instance, \((n,k)=(6,3)\) gives five circles and no two-spheres; \((8,4)\) gives nineteen circles and twenty two-spheres.

## Assumptions and scope

The action is simplicial on the finite clique complex; fixed points mean literal points fixed in its geometric realization. The convention for Vietoris–Rips complexes includes edges at graph distance exactly one. The integers satisfy \(n\geq6\) and \(3\leq k\leq n-3\). Each binomial coefficient is evaluated at the displayed nonnegative integer arguments. All homotopy types and integral homology statements are nonequivariant statements about the fixed-point space; no claim is made about the equivariant homotopy type of the entire action.

## Proof

**1. Orbit simplices model geometric fixed points.** Put \(B=[n]\setminus\{1,2\}\), so \(|B|=m\). An orbit of \(t\) on the vertices of \(K(n,k)\) is of one of three forms:

* \(A_P=\{P\}\), with \(P\subseteq B\) and \(|P|=k\);
* \(D_Q=\{Q\cup\{1,2\}\}\), with \(Q\subseteq B\) and \(|Q|=k-2\);
* \(C_S=\{S\cup\{1\},S\cup\{2\}\}\), with \(S\subseteq B\) and \(|S|=k-1\).

Each \(C_S\) is a graph edge; hence every such orbit spans a simplex. For a finite simplicial complex with a simplicial involution, fixed barycentric coordinates on any invariant face are constant on the vertex orbits. Consequently its realization's fixed set is homeomorphic to the orbit complex whose vertices are the admissible orbits and whose faces are those collections of orbits whose *union of original vertices* is a face. This statement follows directly by sending each orbit vertex to the barycenter of the corresponding original-vertex orbit and gluing the affine identifications over invariant faces.

**2. The orbit complex is a graph of two Johnson complexes.** Pairwise Johnson adjacency yields the complete compatibility rules. The \(A\)-vertices form \(K(m,k)\); the \(D\)-vertices form \(K(m,k-2)\). No \(A\)-vertex is compatible with a \(D\)-vertex, since their original subsets differ in at least two exchanges. Distinct \(C_S\) are incompatible, since \(S\cup\{1\}\) and \(T\cup\{2\}\) differ in at least two exchanges when \(S\ne T\). For a fixed \(S\), \(C_S\) is compatible with precisely the \(A_P\) with \(S\subset P\), and precisely the \(D_Q\) with \(Q\subset S\). The first such vertices span a simplex \(\Delta^A_S\), since each is \(S\) plus one element of \(B\setminus S\). The second span a simplex \(\Delta^D_S\), since each \(Q\) is obtained by deleting one element from \(S\). Both are nonempty in the stated range. Compatibility is pairwise sufficient here because the original complex is flag.

Thus the orbit complex is the disjoint union of the two Johnson complexes, with, for each \(S\), an additional vertex \(C_S\) coned separately onto the disjoint simplices \(\Delta^A_S\subset K(m,k)\) and \(\Delta^D_S\subset K(m,k-2)\). The stars of different \(C_S\) meet only in the original two Johnson complexes. Since the attachment simplices are contractible, the homotopy-pushout description replaces these two cones by a single interval joining the two complexes. There are exactly \(N=\binom m{k-1}\) such intervals. Each Johnson graph in question is connected, so, after using one interval to join the two components, the other \(N-1\) intervals contribute independent circles. Hence

\[
 |K(n,k)|^{\langle t\rangle}\simeq
 K(m,k)\vee K(m,k-2)\vee\bigvee^{N-1}S^1.
\]

This reduction alone already computes the entire fundamental group once the two smaller Johnson complexes are known to be simply connected.

**3. Self-contained homotopy type of the smaller Johnson complexes.** We verify that, for every \(m\geq4\) and \(1\leq j\leq m-1\),

\[
 K(m,j)\simeq\bigvee^{b(m,j)}S^2.
\]

If \(j=1\) or \(j=m-1\), the graph is complete and its clique complex is a simplex; the stated formula gives \(b(m,j)=0\). Otherwise \(2\leq j\leq m-2\). Fix adjacent \(j\)-sets \(X=R\cup\{a\}\) and \(Y=R\cup\{b\}\), with \(|R|=j-1\). A common neighbor of \(X\) and \(Y\) either contains \(R\) or lies in the \((j+1)\)-set \(R\cup\{a,b\}\). Vertices of the two nontrivial alternatives are not adjacent. It follows that every maximal clique is exactly a *star* of all \(j\)-sets containing one fixed \((j-1)\)-set, or a *top* of all \(j\)-sets inside one fixed \((j+1)\)-set. Distinct maximal cliques intersect in at most an edge. In particular, every face on three or more vertices belongs to a unique maximal clique.

Choose a distinguished vertex in each maximal clique. Within that clique, remove elementary free-face pairs \((F,F\cup\{v\})\), for subsets \(F\) not containing \(v\) with at least three vertices, in decreasing order of \(|F|\). No other maximal clique contains \(F\), so these are valid collapses independently for each clique. All vertices and edges remain, and the surviving triangles of this clique are precisely those containing \(v\). Therefore \(K(m,j)\) collapses to a connected two-dimensional complex.

For completeness, the original clique complex is simply connected. Choose a root \(j\)-set \(R_0\) and use Johnson-graph distance \(d(X,R_0)=|X\setminus R_0|\). Whenever adjacent vertices \(X,Y\) are both at distance \(d>0\), they have a common neighbor at distance \(d-1\): if their exchange replaces an element outside \(R_0\) by another outside element, replace the first by a missing root element; if it exchanges two root elements, instead replace any common non-root element by the second root element. Both cases give triangles that push horizontal edges down one level. For each \(X\) at distance \(d>0\), its neighbors at distance \(d-1\) are obtained by replacing one of the \(d\) non-root elements of \(X\) by one of the \(d\) missing root elements; their induced graph is the connected \(d\)-by-\(d\) rook graph. Consequently, after pushing horizontal edges down, every passage through a vertex at maximal distance can be replaced by a path among its lower neighbors, using only triangles with apex \(X\). Repeating reduces every edge loop to the root. Thus the original complex, and its two-dimensional collapse, are simply connected.

There are \(\binom mj\) vertices and \(\tfrac12\binom mjj(m-j)\) edges. The collapsed two-dimensional core has

\[
 T=\binom m{j-1}\binom{m-j}{2}
  +\binom m{j+1}\binom j2
\]

triangles: each star has \(m-j+1\) vertices and retains \(\binom{m-j}{2}\) triangles, and each top has \(j+1\) vertices and retains \(\binom j2\). Unique maximal-clique ownership prevents double counting. Its integral second homology is free of rank \(V-E+T-1=b(m,j)\); all other positive integral homology vanishes. Hurewicz and the homological Whitehead theorem identify this simply connected two-complex with a wedge of that many two-spheres. The conclusion also holds in the complete-graph boundary cases.

**4. Assemble.** Apply step 3 with \(j=k\) and \(j=k-2\) to the reduction in step 2. Both indices lie between \(1\) and \(m-1\) by the hypotheses. This yields the claimed full homotopy type and integral fundamental-group and homology statements.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter and no third-party packages. The program independently constructs the transposition orbits of \(k\)-subset vertices, includes an orbit exactly when its original vertices form a clique, constructs each orbit-complex face by pairwise cross-orbit adjacency, and computes all mod-two simplicial boundary ranks using bit-vector elimination. It compares all reduced Betti numbers, including vanishing in other dimensions, with the displayed formula for the finite parameter cases encoded in the verifier. Examples \((6,3)\), \((8,4)\), \((10,5)\) and \((11,5)\) are included. This finite mod-two check tests the orbit model and predicted ranks; it is not used as a proof of the all-parameter homotopy equivalence or of integral torsion-freeness, which follow from steps 1–4.

## Relationship to prior work

Shuldiner and Oldford (2022, arXiv:2208.12710) characterize the star/top clique families of Johnson graphs. Their results classify graph cliques, not the geometry of an involution's fixed-point space. Goyal, Shukla and Singh (2020, arXiv:2009.12130) study clique-complex homotopy types for line graphs, including the rank-two Johnson boundary family \(J(m,2)\), without a fixed-point classification. A publicly available 2026 analysis of the ambient scale-one Johnson clique complexes establishes their ordinary sphere-wedge homotopy types in the interior parameter range; it does not classify the geometric fixed points of a ground-set transposition. Knowing the ordinary homotopy type or the representation on ambient homology determines at most ordinary Betti numbers and fixed-point Lefschetz traces; neither determines the fixed space's fundamental group or its full homotopy type. The new statement addresses those missing invariants for every specified parameter pair.

## Limitations

The theorem treats one ground-set transposition and the scale-one clique complex only. It does not classify fixed spaces for general permutations or the full equivariant homotopy type. Searches cannot exclude every differently phrased prior theorem; the closest retrieved works concern ordinary homotopy, line-graph cases, clique enumeration or homology representations. The finite verifier uses mod-two arithmetic and does not itself establish the integral or infinite-family conclusions.

## References

1. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first public version 2020-09-25, https://arxiv.org/html/2009.12130v2 .
2. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710, first public version 2022-08-26, https://arxiv.org/html/2208.12710v1 .
3. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, publicly available scientific result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518 .
