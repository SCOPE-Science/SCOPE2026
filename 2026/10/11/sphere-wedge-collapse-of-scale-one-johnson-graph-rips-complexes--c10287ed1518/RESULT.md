# Sphere-wedge collapse of scale-one Johnson-graph Rips complexes

## Finding

For every pair of integers \(n\ge 6\) and \(3\le k\le n-3\), let \(J(n,k)\) be the Johnson graph with vertices the \(k\)-element subsets of \([n]\), adjacent precisely when their intersection has size \(k-1\). Equip its vertex set with the shortest-path metric, and let \(K_{n,k}=\operatorname{VR}_{\le}(J(n,k);1)\) denote the inclusive Vietoris–Rips complex at scale one. Then the following all-parameter homotopy classification holds:

\[
K_{n,k}\simeq \bigvee^{\beta(n,k)} S^2,
\]

where

\[
\beta(n,k)=\binom nk-1-\frac{k(n-k)}2\binom nk
 +\binom n{k-1}\binom{n-k}{2}
 +\binom n{k+1}\binom k2.
\]

More strongly, \(K_{n,k}\) admits an explicit sequence of elementary simplicial collapses to a connected two-dimensional simplicial complex. Its reduced integral homology is free of rank \(\beta(n,k)\) in degree two and zero in every other degree. For example, \(\beta(6,3)=19\), \(\beta(7,3)=55\), and \(\beta(8,4)=181\).

## Assumptions and scope

The vertex set is finite, the graph is simple, graph distances are ordinary shortest-path distances, and scale one includes pairs at distance exactly one. Consequently \(K_{n,k}\) is exactly the flag/clique complex of \(J(n,k)\). The range \(3\le k\le n-3\) excludes the already-studied line-graph cases \(k=2\) and \(k=n-2\), and keeps both kinds of maximal Johnson cliques of size at least four. The theorem concerns scale one only; it makes no assertion about higher Rips scales or the entire persistence barcode.

## Proof

**1. Maximal cliques and their intersections.** Take adjacent vertices \(A=S\cup\{a\}\) and \(B=S\cup\{b\}\), where \(|S|=k-1\) and \(a\ne b\) lie outside \(S\). Every third common neighbor is either \(S\cup\{c\}\) for some \(c\notin S\cup\{a,b\}\), or \((S\setminus\{s\})\cup\{a,b\}\) for some \(s\in S\). A vertex of the first kind and a vertex of the second kind have intersection size \(k-2\), and therefore cannot be adjacent. It follows that every maximal clique is exactly one of the following:

* A **star** \(F_S=\{S\cup\{c\}:c\in[n]\setminus S\}\), indexed by \(|S|=k-1\), having \(n-k+1\) vertices.
* A **top** \(F_U=\{U\setminus\{c\}:c\in U\}\), indexed by \(|U|=k+1\), having \(k+1\) vertices.

Two different stars intersect in at most one graph vertex, as do two different tops. A star and a top intersect in at most two graph vertices. Thus every face with three or more vertices belongs to precisely one maximal clique. There are exactly \(\binom n{k-1}\) stars and \(\binom n{k+1}\) tops. These combinatorial descriptions agree with the maximal-clique classification of Shuldiner and Oldford, but the preceding argument independently supplies the property needed for the collapse.

**2. Uniform elementary collapse.** For each maximal clique \(F\), select any vertex \(a_F\in F\). Process subsets \(\tau\subseteq F\setminus\{a_F\}\) with \(|\tau|\ge3\), in strictly decreasing order of cardinality, and for each such \(\tau\) remove the pair of faces \((\tau,\tau\cup\{a_F\})\). This is a valid elementary simplicial collapse: a face \(\tau\) of at least three vertices appears in no other maximal clique, and by the ordering all of its other cofaces have already been removed. The face \(\tau\cup\{a_F\}\) is consequently its unique remaining coface. The resulting complex \(L_{n,k}\) retains every vertex and edge, and in each maximal clique retains exactly the triangles \(\{a_F,x,y\}\) with distinct \(x,y\in F\setminus\{a_F\}\). It has dimension two, and \(K_{n,k}\searrow L_{n,k}\).

**3. Simple connectivity.** Let \(P_{n,k}=\{x\in[0,1]^n:\sum_i x_i=k\}\) be the hypersimplex. This is a convex polytope of dimension \(n-1\), with vertices the characteristic vectors of \(k\)-subsets. Its edges are exactly the exchanges of one chosen and one unchosen coordinate, so its one-skeleton is \(J(n,k)\). Every two-dimensional face is triangular: after fixing coordinate values in \(\{0,1\}\), exactly three coordinates remain free, with their sum equal to one or two. These triangles therefore define a subcomplex of \(K_{n,k}\) containing its entire one-skeleton. The boundary of \(P_{n,k}\) is homeomorphic to \(S^{n-2}\), and its cellular two-skeleton is simply connected because \(n-2\ge4\) and attaching cells in dimensions above two does not alter the fundamental group. Its cellular two-skeleton thus supplies a simply connected subcomplex of \(K_{n,k}\) with the entire one-skeleton; attaching any additional higher-dimensional simplices cannot introduce fundamental-group generators. Therefore \(K_{n,k}\), and hence \(L_{n,k}\), is simply connected.

**4. Euler characteristic and homotopy type.** The number of vertices is \(V=\binom nk\), and the number of edges is \(E=\tfrac12\binom nk k(n-k)\). By uniqueness of a maximal clique containing each triangle, the two-dimensional core has precisely

\[
T=\binom n{k-1}\binom{n-k}{2}
  +\binom n{k+1}\binom k2
\]

triangles. Hence \(\chi(L_{n,k})=V-E+T\), so its second Betti number is \(\chi-1=\beta(n,k)\), because \(L_{n,k}\) is connected, simply connected, and two-dimensional. Its second integral homology is free because it is a subgroup of the free abelian two-chain group. The Hurewicz isomorphism provides two-sphere maps representing an integral basis for \(H_2\); their wedge induces a homology isomorphism and, since both spaces are simply connected CW complexes, a homotopy equivalence by the homological Whitehead theorem. This proves the result for every stated \(n,k\).

## Verification

Run `python3 verify_johnson.py` using Python 3 and no third-party dependencies. It constructs each Johnson graph for all \(4\le n\le8\), \(2\le k\le n-2\), enumerates maximal cliques from graph adjacency, compares the star/top facet list, tests each proposed elementary collapse against all surviving cofaces, and computes exact mod-two boundary ranks. The completed run covered 15 parameter cases and 2,872 elementary collapse pairs, with output ending in `VERIFY_OK cases=15 exact_collapse_pairs=2872`. The smaller boundary cases are verification tests only and are not added to the new theorem's claimed range. These finite checks are not a proof of the unbounded all-parameter statement; the argument above supplies that proof.

## Relationship to prior work

Shuldiner–Oldford determine the two maximal-clique families of Johnson graphs (arXiv:2208.12710, Theorem 3.4 and Proposition 4.2); the present result uses that structure for a simplicial-collapse and homotopy classification absent from their enumerative treatment. Goyal–Shukla–Singh compute topology of clique complexes of line graphs (arXiv:2009.12130); in particular, \(J(n,2)\) is the line graph of a complete graph, so that special case is not asserted as new here. Every graph in the present range has an induced three-leaf claw: at a fixed \(k\)-set, swap three distinct present coordinates for three distinct absent coordinates, yielding three pairwise nonadjacent neighbors. Such a graph cannot be a line graph, since line graphs are claw-free. Adamaszek–Adams (arXiv:1503.03669) give foundational Vietoris–Rips homotopy results for the circle, not Johnson-graph homotopy types. The proof additionally uses the standard face structure of the hypersimplex, without asserting that structure is new.

## Limitations

An equivalent result expressed through hypersimplex one-skeleta, flag complexes, or simplicial Morse reductions may exist in less-indexed literature. The manuscript's originality comparison is limited to the specifically inspected and queried sources and is not an independent literature certification. No generalization to other distances, graph families, or functorial symmetry action is claimed. The finite verifier confirms small cases, not the quantifiers of the theorem.

## References

1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (first public version 2015-03-12), Pacific Journal of Mathematics **290** (2017), 1–40, doi:10.2140/pjm.2017.290.1; primary MSC 05E45 and 55U10.
2. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710 (2022), especially Section 3 and Proposition 4.2.
3. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (2020), especially Lemma 3.2 and Theorem 3.4.
