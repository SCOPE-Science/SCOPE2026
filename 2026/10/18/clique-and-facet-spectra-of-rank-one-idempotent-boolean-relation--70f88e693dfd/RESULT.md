# Clique and facet spectra of rank-one idempotent Boolean relations

## Finding

For every integer \(n\ge2\), consider the simple graph \(G_n\) on the nonzero Boolean factor-rank-one idempotents in \(M_n(\mathbb B)\). Two *distinct* idempotents are adjacent exactly when their Boolean matrix products commute. Every vertex is uniquely \(E_{U,V}=\mathbf1_U\mathbf1_V^{\mathsf T}\), where \(U,V\) are nonempty subsets of \([n]\) with \(U\cap V\ne\varnothing\).

For each \(1\le k\le n\), the number of unordered \(k\)-cliques is
\[
C_{n,k}=\frac1{k!}\sum_{j=0}^k(-1)^j\binom kj(2^{k+1}+k-1-j)^n,
\]
and the number of inclusion-maximal \(k\)-cliques (facets of the clique complex) is
\[
M_{n,k}=\frac1{k!}\sum_{j=0}^k(-1)^j\binom kj(2^{k+1}+k-2-j)^n.
\]
Each \(k\) in this range is realized by an inclusion-maximal clique; no larger clique exists. The unique size-\(n\) clique consists of all singleton diagonal relations. The clique complex is nonpure for every \(n\ge2\).

There are exactly \(4^n-3^n\) vertices, \(3^n-2^n\) of which are isolated. If a vertex \(E_{U,V}\) has \(s=n-|U\cup V|\) unused coordinates and \(u=|U\triangle V|\), its degree equals
\[
d(E_{U,V})=2^u(4^s-3^s).
\]
The complete degree multiset is encoded by
\[
D_n(z)=\sum_{s=0}^{n-1}\sum_{u=0}^{n-s-1}\binom ns\binom{n-s}u 2^u z^{2^u(4^s-3^s)}.
\]
The edge count is \((9^n-2\cdot8^n+7^n)/2\). All nonisolated vertices lie in one connected component, whose diameter is \(1\) at \(n=2\) and \(3\) for every \(n\ge3\).

## Assumptions and scope

The Boolean semiring \(\mathbb B\) has addition \(a\lor b\) and multiplication \(a\land b\). Matrix multiplication is Boolean. Factor-rank one means an outer product of two nonzero Boolean vectors; zero is excluded. The graph is the induced *elementwise* commuting graph on this precisely defined idempotent subset; it is not the more common graph obtained by deleting the center of the full matrix semiring. Cliques are vertex sets rather than ordered families. This statement applies uniformly to every \(n\ge2\).

## Proof

**Parametrization.** A nonzero Boolean rank-one matrix is the characteristic matrix of a nonempty rectangle \(U\times V\); it uniquely determines \(U,V\). Boolean multiplication gives
\[
E_{U,V}E_{W,Z}=\begin{cases}E_{U,Z},&V\cap W\ne\varnothing,\\0,&V\cap W=\varnothing.\end{cases}
\]
It is idempotent precisely when \(U\cap V\ne\varnothing\). For two *distinct* such matrices, if both products are nonzero, equality of their rectangular supports would force \(U=W\) and \(V=Z\), a contradiction. If exactly one product is nonzero they also fail to commute. Thus distinct vertices commute if and only if both cross-intersections vanish.

**Coordinate patterns.** Label an ordered clique by \(1,\ldots,k\). For each ground coordinate \(t\in[n]\), record \(A_t=\{i:t\in U_i\}\) and \(B_t=\{i:t\in V_i\}\). The cross-intersection criterion says that whenever \(i\in A_t\) and \(j\in B_t\), one must have \(i=j\). Therefore every allowed local pattern is exactly one of: \((A,\varnothing)\) with arbitrary \(A\subseteq[k]\), \((\varnothing,B)\) with nonempty \(B\subseteq[k]\), or \((\{i\},\{i\})\) for some \(i\in[k]\). There are \(2^{k+1}+k-1\) patterns including the all-empty pattern. The \(i\)-th matrix is idempotent exactly when its corresponding double-singleton pattern appears at least once. Inclusion-exclusion over missing double-singleton patterns yields
\[
k!C_{n,k}=\sum_{j=0}^k(-1)^j\binom kj(2^{k+1}+k-1-j)^n.
\]
A valid clique has distinct vertices: pairwise annihilating nonzero idempotents cannot coincide. Thus dividing by \(k!\) is exact.

**Maximality.** A further nonzero idempotent \(E_{A,B}\) commutes with every vertex in the family precisely when \(A\subseteq(\cup_i V_i)^c\), \(B\subseteq(\cup_i U_i)^c\), and \(A\cap B\ne\varnothing\). Such a choice exists precisely when there is \(t\notin\cup_i(U_i\cup V_i)\), since then \(A=B=\{t\}\) works. Hence a clique is inclusion-maximal exactly when no ground coordinate has the all-empty local pattern. Removing that one pattern from the preceding inclusion-exclusion gives
\[
k!M_{n,k}=\sum_{j=0}^k(-1)^j\binom kj(2^{k+1}+k-2-j)^n.
\]
Since each matrix must contain its own distinct double-singleton coordinate, \(k\le n\). Conversely, for every \(1\le k\le n\), partition \([n]\) into \(k\) nonempty parts and take \(U_i=V_i\) equal to these parts: this yields a maximal clique. At \(k=n\), all \(n\) coordinates must be the distinct double-singleton patterns, forcing the unique diagonal singleton clique. Presence of maximal cliques at every size proves nonpurity.

**Degrees.** Fix \(E_{U,V}\), set \(s=|[n]\setminus(U\cup V)|\) and \(u=|U\triangle V|\). A neighboring idempotent has supports \(A\subseteq V^c\), \(B\subseteq U^c\), with \(A\cap B\ne\varnothing\). On each of the \(s\) unused coordinates there are four independent presence patterns and, among all patterns on these positions, exactly \(3^s\) contain no simultaneous inclusion. On each of the \(u\) unilateral coordinates there are two choices; every coordinate in \(U\cap V\) is excluded from both supports. Thus \(d=2^u(4^s-3^s)\). Given \(s,u\) with \(s\ge0\), \(u\ge0\), \(s+u\le n-1\), choosing the unused set, unilateral set, and its two possible orientations gives multiplicity \(\binom ns\binom{n-s}u2^u\). Summing yields \(D_n(z)\). Isolates have \(s=0\), yielding \(3^n-2^n\); the edge count follows also from \(C_{n,2}\).

**Connectivity and diameter.** A nonisolated vertex has an unused coordinate \(t\) and hence is adjacent to the diagonal singleton \(E_{\{t\},\{t\}}\). All \(n\) diagonal singletons commute pairwise; therefore all nonisolated vertices lie in one component, with distance at most three. For \(n=2\) the component consists only of two adjacent diagonal singleton vertices. For \(n\ge3\), the vertices with \(U=V=[n]\setminus\{1\}\) and \(U=V=[n]\setminus\{2\}\) each have exactly one neighbor (the corresponding missing diagonal singleton). They are not adjacent, and their unique neighbors are distinct and adjacent, so their distance is exactly three.

## Verification

The standard-library script `artifacts/verify.py` constructs Boolean matrices and literal Boolean products for all vertices through \(n=4\); it also independently enumerates all cliques, inclusion-maximal cliques, degrees, and connected components through \(n=5\), with additional exact integer formula boundary checks through \(n=13\). Run `python3 artifacts/verify.py` to reproduce `VERIFY_OK_BOOLEAN_RANK_ONE_IDEMPOTENT_CLIQUES`. Counts for \(n=2,3,4,5\) are, in successive clique sizes, respectively \((7,1)\), \((37,24,1)\), \((175,385,66,1)\), \((781,5160,2725,165,1)\). Corresponding maximal-clique counts are \((5,1)\), \((19,21,1)\), \((65,295,62,1)\), and \((211,3465,2405,160,1)\). Exhaustive small cases are corroboration; the preceding coordinate-pattern argument proves all \(n\).

## Relationship to prior work

Classical work on idempotent Boolean relation matrices and Boolean matrix semigroups supplies the ambient structures. Butler–Markowsky's individual-idempotent enumerations, also represented in OEIS A363232, already cover the *vertex count* \(4^n-3^n\); that count is not asserted to be original. Dolžan–Oblak studied full matrix-semiring commuting graphs, notably distances and girths; Dolžan–Kokol Bukovšek–Oblak studied their diameters. Neither inspected paper provides the all-cardinality clique and facet formulas for the noncentral, rank-one-idempotent induced graph used here. The novelty assessment attaches to the complete clique and maximal-clique spectra, degree distribution and selected-subgraph decomposition, rather than to elementary rectangular parametrization or known general semiring graph results. Related work on full binary-relation semigroups and maximal commuting subfamilies under alternate terminology leaves a residual historical-priority risk.

## Limitations

This does not enumerate commuting families of arbitrary Boolean idempotents, arbitrary factor ranks, general rectangular matrix sizes, or the customary full commuting graph with its center removed. The complete classical priority literature is not exhaustively searchable; further hidden equivalences remain possible. No independent mathematical audit was performed.

## References

1. D. Dolžan and P. Oblak, *Commuting graphs of matrices over semirings*, Linear Algebra and Its Applications 435 (2011), 1657–1665; available online 13 May 2010, DOI 10.1016/j.laa.2010.04.014.
2. D. Dolžan, D. Kokol Bukovšek and P. Oblak, *Diameters of commuting graphs of matrices over semirings*, arXiv:1012.5505, first submitted 26 December 2010.
3. D. Rosenblatt, *On the Graphs of Finite Idempotent Boolean Relation Matrices* (1963).
4. K. K.-H. Butler and G. Markowsky, *The Number of Maximal Subgroups of the Semigroup of Binary Relations*, Kyungpook Mathematical Journal 12 (1972), June.
5. OEIS A363232, *Idempotent Boolean relation matrices by rank*, https://oeis.org/A363232.
