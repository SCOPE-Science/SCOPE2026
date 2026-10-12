# Exact census of maximum general-position sets in path–star strong products

## Finding

Let \(P_s\) be a path with vertices \(0,1,\ldots,s-1\), where \(s\ge2\). Let \(K_{1,m}\) be the star with center \(o\) and labeled leaves \(1,\ldots,m\), where \(m\ge3\). Set
\[
G_{s,m}=P_s\boxtimes K_{1,m}.
\]
A vertex set is in **general position** if no three distinct selected vertices occur on a common geodesic. By the known path-factor product theorem,
\[
\operatorname{gp}(G_{s,m})=2m.
\]
The following result classifies and enumerates **all** sets attaining this value.

**Theorem.** Every maximum general-position set \(S\subseteq V(G_{s,m})\) has the following properties:

1. The star center is never selected: \(S\subseteq\{(i,a):0\le i<s,\ 1\le a\le m\}\).
2. For every leaf \(a\in\{1,\ldots,m\}\), exactly two distinct path positions \(i\) satisfy \((i,a)\in S\).
3. Writing \(T=\{i:\exists a\ (i,a)\in S\}\), the occupied path positions satisfy \(2\le|T|\le4\), and their arrangement obeys precisely one of the following cases.

If \(|T|=2\), the two occupied layers each contain all \(m\) leaves. If \(|T|=3\), either the three positions are consecutive (any assignment of each leaf to exactly two of the three positions is feasible), or exactly one of their consecutive gaps is \(1\), in which case the two adjacent occupied layers must have disjoint leaf sets. If \(|T|=4\), the occupied positions are \(i<i+1<j<j+1\), where \(j\ge i+2\), and the leaf sets at \(i,i+1\) must be disjoint, as must those at \(j,j+1\). Conversely, each configuration satisfying these requirements is a maximum general-position set.

Let \(M(s,m)\) be the number of maximum general-position sets, counting vertex subsets in the labeled graph, not quotienting by automorphisms. Then
\[
\boxed{
M(s,m)=\binom{s}{2}+(3^m-3)(s-2)
 +(2^m-2)(s-2)(s-3)
 +(2^m-2)^2\binom{s-2}{2}.
}
\]
The four terms count respectively two-layer sets, three-consecutive-layer sets, three-layer sets with exactly one adjacent gap, and four-layer sets.

In particular, the top coefficient of the general-position polynomial
\[
\psi(G_{s,m};x)=\sum_{S\text{ general-position}}x^{|S|}
\]
is \(M(s,m)\). For each fixed \(m\ge3\), this is a quadratic polynomial in \(s\), with leading coefficient
\[
\frac{(2^m-1)^2}{2}.
\]
At \(m=3\),
\[
M(s,3)=\frac{49s^2-193s+192}{2},
\]
and its first values for \(s=2,3,4,5,6,7,8\) are
\[
1,\ 27,\ 102,\ 226,\ 399,\ 621,\ 892.
\]

## Assumptions and scope

Graphs are finite, simple, undirected, connected. The strong product has vertex set \(V(P_s)\times V(K_{1,m})\), where distinct pairs are adjacent when both coordinates are equal or adjacent in their respective factors. The path and star vertices are labeled, and counted maximum sets are distinct subsets of the resulting labeled product.

The restriction \(m\ge3\) is substantive: for \(m=2\), the star itself has maximum general-position sets containing its center, and the center-exclusion assertion here is no longer valid. The restriction \(s\ge2\) ensures the path factor has general-position number \(2\).

## Proof

**Step 1: Every maximum set contains two copies of each leaf and no center.**

For vertices \(u=(i,a)\), \(v=(j,b)\) of a strong product,
\[
d_{G_{s,m}}(u,v)=\max\{|i-j|,d_{K_{1,m}}(a,b)\}.
\]
We recall and verify the auxiliary bipartite-graph argument of the path-factor theorem, because its equality case is essential here.

For any general-position set \(S\), form the graph \(X(S)\) on \(S\), joining \(u=(i,a)\) and \(v=(j,b)\) precisely when
\[
|i-j|>d_{K_{1,m}}(a,b).
\]
The graph \(X(S)\) is bipartite. Indeed, a triangle in \(X(S)\) would make product distances of all three pairs equal their path-coordinate distances, placing the median path-coordinate vertex on a geodesic, contrary to general position. If a shortest odd cycle has length at least five, it is induced. Write the consecutive path-coordinate increments as \(e_i\). Two consecutive increments cannot share a sign: if they did, the triangle inequality for the star metric and strict inequalities along the two cycle edges would give
\[
|e_i+e_{i+1}|=|e_i|+|e_{i+1}|>
 d_{K_{1,m}}(a_i,a_{i+2}),
\]
creating a chord between vertices two steps apart. Thus signs would have to alternate around an odd cycle, which is impossible. This proves bipartiteness (the same argument is used in the initiating product paper).

In either independent color class of this bipartite graph, all pairwise path-coordinate distances are at most the corresponding star distances. The projections to the star are distinct and in general position: the product distances restricted to the class equal the star distances, so a geodesic triple in the star projections would give one in the product. Each class therefore has at most \(\operatorname{gp}(K_{1,m})=m\) vertices. Consequently \(|S|\le2m\). Equality is attained by taking all leaves in any two distinct path layers.

For \(m\ge3\), the **unique** maximum general-position subset of \(K_{1,m}\) is the set of all \(m\) leaves. Indeed, its leaves are pairwise at distance \(2\), while a set containing the center and two distinct leaves has the center on a geodesic. If \(|S|=2m\), both bipartition classes of \(X(S)\) must have cardinality \(m\); both star projections must therefore consist of all \(m\) leaves. Thus no center is selected and every leaf occurs exactly twice in distinct path positions.

**Step 2: Classify the occupied path layers.**

Restrict attention to the leaf-only vertices. Within a path layer, distinct leaves have distance \(2\). In distinct path layers at gap \(g\ge2\), every pair of leaves has product distance \(g\); at gap \(1\), the distance is \(1\) for equal leaves and \(2\) for unequal leaves.

Any triple using at most two path layers is automatically in general position: within-layer triples are equilateral, and two points in one layer together with a third in another yield either distance pattern \((2,g,g)\) with \(g\ge2\), or \((2,1,2)\) or \((2,2,2)\) for gap one. None satisfies equality in the triangle inequality.

Consider three selected leaf vertices at distinct path positions \(i<j<k\). The endpoint distance equals \(k-i\). The middle vertex lies on an endpoint geodesic exactly when the distances from \(i\) to \(j\) and from \(j\) to \(k\) equal their path gaps. Therefore:

- If both gaps are at least \(2\), the triple is forbidden regardless of leaf labels.
- If only \(j-i=1\), the triple is forbidden precisely when the leaves at positions \(i,j\) have the same label.
- If only \(k-j=1\), the analogous statement holds for the labels at \(j,k\).
- If both gaps equal \(1\), the triple is forbidden precisely when all three vertices carry the same leaf label; this cannot occur in a maximum set, in which every label occurs exactly twice.

Five occupied path positions would give three selected vertices at the first, third, and fifth occupied layers, whose two intervening gaps are at least \(2\). Hence at most four layers may be occupied.

For three occupied layers \(i<j<k\), the displayed triple-layer test proves exactly the claimed classification: both gaps cannot exceed one, and when only one gap is adjacent, the two layers on that adjacent side must have disjoint leaf labels. For four occupied layers \(i<j<k<\ell\), applying the triple-layer test to \((i,j,\ell)\) forces \(j=i+1\) and disjoint labels in those two layers; applying it to \((i,k,\ell)\) forces \(\ell=k+1\) and disjoint labels in those two layers. These two disjointness conditions also prevent every other forbidden triple. The two-layer case has no restrictions beyond the twice-per-leaf condition. This proves the exact classification.

**Step 3: Enumerate without overcounting.**

If the support has two layers, each leaf must occur in both; there is one set for every choice of two layers, giving \(\binom{s}{2}\).

For three consecutive occupied layers, each of the \(m\) leaf labels independently chooses one of the three two-layer subsets in which to appear. There are \(3^m\) assignments. Exactly three assignments omit an entire layer (all leaves choose the same two-layer subset), so the contribution is \((3^m-3)(s-2)\).

For three occupied layers with exactly one adjacent pair, say \(i,i+1,k\), every leaf must occur once in the distant layer \(k\) and once in exactly one of the two adjacent layers. Both adjacent layers must be occupied; there are \(2^m-2\) choices. The number of ordered three-layer supports with exactly one adjacent gap equals \((s-2)(s-3)\), giving the third term.

For four occupied layers, the first two and the last two form two disjoint adjacent pairs. Each leaf occurs once in each of these two pairs, and every one of the four layers must be occupied. The \(m\) leaf labels choose independently between the two layers of each pair, with \(2^m-2\) nonconstant assignments for each pair, giving \((2^m-2)^2\) color assignments. The two adjacent path edges can be selected with no common endpoint in exactly \(\binom{s-2}{2}\) ways. This yields the fourth term.

The cases are mutually exclusive and exhaustive. Summing completes the proof.

## Verification

The standalone script `artifacts/verify.py` constructs strong-product edges and computes all-pairs distances by breadth-first search, independently of the product-distance formula. It exhaustively checks every \(2m\)-vertex subset against the geodesic condition and against the claimed structural classification for \(m=3\), \(2\le s\le8\); for \(m=4\), \(2\le s\le4\); and for \(m=5\), \(2\le s\le3\).

A second route enumerates the two path positions of each leaf directly and compares all four support-type totals for \(m=3\) through \(s=14\), for \(m=4\) through \(s=7\), and for \(m=5\) through \(s=5\).

The reproducible output is stored in `artifacts/verification_output.txt`. All checks passed; the direct subset census tested \(1,641,522\) candidate vertex sets. These finite checks corroborate rather than replace the arbitrary-parameter analytic proof.

## Relationship to prior work

Vesel's 2026 paper establishes the scalar identity \(\operatorname{gp}(P_s\boxtimes H)=2\operatorname{gp}(H)\) for every connected \(H\). Its Section 2 develops the auxiliary bipartite graph used in Step 1. That theorem supplies the known optimal cardinality \(2m\), which is **not claimed as new**. The inspected source does not count all maximum sets for path–star products or classify their two-, three-, and four-layer supports.

Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial and enumerated general-position sets on several graph families and operations, including Cartesian-product grids; their paper does not give this strong-product coefficient. Dokyeesun, Klavžar, Kuziak, and Tian study outer, dual, and total general-position variants of strong products; those are different constraints and do not entail the ordinary maximum-set count here. Klavžar and Yero's earlier strong-resolving-graph work gives general scalar product bounds and examples, not this enumeration.

The present theorem isolates a nontrivial equality case of the path-factor scalar theorem: the entire optimum-set census is a quadratic polynomial in path order, with exact exponential dependence on the star degree and a four-layer support cutoff.

## Limitations

This is the top coefficient of the general-position polynomial, not its full coefficient distribution. The classification applies to star degree \(m\ge3\); it does not claim the same formula for \(m=1,2\), when maximum sets of the star may contain its center. The counts distinguish labeled vertex subsets and do not quotient by automorphisms.

The literature comparison covers the primary path-factor theorem, original polynomial paper, and earlier product literature, but indexing of graph products under alternate names remains a residual originality risk. No independent external audit is asserted.

## References

1. A. Vesel, “General position sets in strong products with paths and cycles,” arXiv:2607.26844v1, first public July 29, 2026. Primary MSC \(05C12\), followed by \(05C69,05C76\).
2. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, “General Position Polynomials,” Results in Mathematics 79 (2024), article 110. DOI 10.1007/s00025-024-02133-3.
3. S. Klavžar and I. G. Yero, “The general position problem and strong resolving graphs,” Open Mathematics 17 (2019), 1126–1135. DOI 10.1515/math-2019-0088.
4. P. Dokyeesun, S. Klavžar, D. Kuziak, and J. Tian, “General position problems in strong and lexicographic products of graphs,” Computational and Applied Mathematics 45 (2026), article 97. DOI 10.1007/s40314-025-03547-7.
