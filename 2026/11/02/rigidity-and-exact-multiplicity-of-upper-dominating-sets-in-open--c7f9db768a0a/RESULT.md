# Rigidity and exact multiplicity of upper-dominating sets in open ladders

## Finding

Let \(L_n=P_2\square P_n\), for every integer \(n\ge2\), with two labelled rows and columns \(1,\ldots,n\). An *upper-dominating set* means an inclusion-minimal dominating vertex set of maximum possible cardinality. Write a vertex subset as a word \(a_1\cdots a_n\) over \(\{0,1,2,3\}\), where a column symbol is the binary row-membership mask: \(0\) means neither vertex, \(1\) means the top vertex, \(2\) means the bottom vertex, and \(3\) means both vertices.

**Theorem.** The upper domination number is \(\Gamma(L_n)=n\). Every upper-dominating set is one of the four words
\[
1^n,\qquad 2^n,\qquad 1212\cdots,\qquad 2121\cdots,
\]
with each alternating word truncated to length \(n\), or, **only when \(n\) is even**, one of two additional words
\[
30033003\cdots,\qquad 03300330\cdots,
\]
again truncated to length \(n\). These are six distinct labelled words when \(n\) is even, and four distinct labelled words when \(n\) is odd. In particular, the number of maximum-cardinality minimal dominating sets equals
\[
\#\{D\subseteq V(L_n):D\text{ minimal dominating},\ |D|=n\}=
\begin{cases}4,&n\text{ odd},\\6,&n\text{ even}.
\end{cases}
\]
Exactly two of the extremal sets are independent (the two checkerboards). The other two, or four when \(n\) is even, induce edges. Each vertex occurs in exactly half the extremal sets.

## Assumptions and scope

All graphs are finite, simple, undirected. Domination uses closed neighborhoods; a dominating set is **minimal** if deleting any one selected vertex destroys domination. Here \(P_n\) is an open path, not a cycle. Rows and columns are labelled; the count is of actual vertex subsets, not symmetry orbits. Theorem applies for every integer \(n\ge2\). It also agrees with the two sets when \(n=1\), but that degenerate case is not needed in the statement. A vertex \(u\) is a *private neighbor* of a selected vertex \(v\) if its closed neighborhood meets the selected set in exactly \(\{v\}\).

## Proof

**1. An injection bound.** Let \(D\) be any inclusion-minimal dominating set. Every \(v\in D\) has a private neighbor, for otherwise deleting \(v\) would leave all vertices dominated. Use the vertical rung edges as a perfect matching of \(V(L_n)\). If \(v\) is isolated in the induced graph \(L_n[D]\), assign to \(v\) its vertically matched vertex \(v'\), which lies outside \(D\). Otherwise choose a private neighbor \(p(v)\) of \(v\): because \(v\) has a selected neighbor, \(p(v)\) is outside \(D\). These outside assignments are distinct. Private neighbors belonging to different nonisolated selected vertices are distinct by definition; vertical mates of isolated vertices are distinct by the perfect matching; and a vertical mate of an isolated \(v\) cannot be private to a different selected vertex because it is adjacent to \(v\). Thus \(D\) injects into its complement, and \(|D|\le n\). The all-top-row set is minimal dominating and has size \(n\), proving \(\Gamma(L_n)=n\).

**2. Exact balance of empty and full columns.** Fix a minimal dominating \(D\) of size \(n\). Let \(k\) be the number of columns with mask \(3\), let \(e\) be the number with mask \(0\), and let \(s\) be the number of single-vertex columns. From \(2k+s=n=k+e+s\), one has \(e=k\).

Every vertex of a full column is nonisolated in \(D\), so must have an *external* private neighbor. Such a neighbor lies in an adjacent column, in the same row. It cannot lie in a singleton column: if that neighbor is unselected, its vertical mate is selected and it has two selected neighbors (the mate and the original full-column vertex). Nor can it lie in a full column. Thus every vertex selected in a full column has a private neighbor in an empty column. These \(2k\) private neighbors are distinct, and the empty columns contain exactly \(2e=2k\) outside vertices; hence **every vertex of every empty column** is the private neighbor of exactly one selected full-column vertex. Therefore every empty column has exactly one full-column neighbor: zero would leave its vertices without the required full-column private origin, and two would give both its vertices two selected neighbors. An empty column cannot be adjacent to a singleton column, because its vertex in the singleton's selected row would then have an extra selected neighbor and would not be private to a full-column vertex.

A full column cannot be adjacent to a singleton column either. Indeed, the selected vertex \(v\) in that singleton column would be nonisolated, so it needs an external private neighbor. Its vertical mate has at least two selected neighbors, namely \(v\) and the nearby full-column vertex. In the other neighboring column, if there is one, the same-row vertex is either selected (if that column selects the same row), has its selected vertical mate (if that column selects the other row), or lies in an empty column (whose vertices, as just shown, are private only to full-column vertices). No choice is a private neighbor of \(v\). This contradicts minimality.

Since the ladder's column path is connected, no singleton column can coexist with an empty or a full column: otherwise two different column types must be adjacent, contradicting the previous paragraph. Thus exactly one of the following two cases holds.

**3. Every column is a singleton.** Write \(r_i\in\{1,2\}\) for the selected row in column \(i\). Every such word dominates because each unselected vertex has its vertical selected mate. For an interior column, if \(r_{i-1}=r_i=r_{i+1}\), the selected vertex has its vertical mate as a private neighbor. If \(r_{i-1}\ne r_i\ne r_{i+1}\), the selected vertex is isolated in \(D\), so is its prior neighbor. However, if precisely one adjacent row equals \(r_i\), the vertex is nonisolated, its vertical mate has another selected neighbor, and its only other unselected closed neighbors (in the opposite-row-selected adjacent column) are adjacent to their own selected vertical mates. It has no private neighbor. The end-column selected vertices always have private neighbors: either themselves or their vertical mates. Hence minimality is exactly the set of interior equalities \(r_{i-1}=r_{i+1}\), equivalently \(r_{i+2}=r_i\). There are four length-\(n\) choices for \(n\ge2\), precisely the two constant-row and two alternating-row words.

**4. Every column is empty or full.** Each empty column has exactly one neighboring full column by Step 2. Every full column must have at least one neighboring empty column, because each of its two selected vertices needs an external private neighbor and all columns are now empty/full. In the path of columns, consider edges joining unlike masks. There are exactly \(k\) such edges, one incident to each empty column, and each of the \(k\) full columns meets at least one. Thus every full column also meets exactly one unlike edge. The unlike-mask edges form a perfect matching on the path \(P_n\); the path has a perfect matching only for even \(n\), and it is uniquely \(\{\{1,2\},\{3,4\},\ldots,\{n-1,n\}\}\). Consequently masks change across each matched edge and agree across the intervening edges. This forces precisely \(30033003\cdots\) and \(03300330\cdots\). Conversely, in each of these two words every empty vertex has a unique full-column neighbor, and every selected vertex has an empty-column private neighbor; therefore they are minimal dominating and have \(n\) selected vertices.

**5. Multiplicity and independence.** The four singletons words are pairwise distinct for \(n\ge2\), and the even-length full/empty words are distinct from them and from each other. Both alternating-singleton words are independent and maximal; all other listed words have an edge in their induced subgraphs. Complementing every column mask exchanges the two constants, exchanges the checkerboards, and, when present, exchanges the two full/empty words. Therefore the extremal family is partitioned into complementary pairs, proving that every vertex belongs to half its members. This completes the proof.

## Verification

The standalone `verify.py` checks the theorem against the definition of minimal domination, without invoking the structural classification in the test predicate. It enumerates every subset of cardinality \(n\) for \(2\le n\le10\), and identifies exactly the predicted sets. Independently it enumerates all vertex subsets for lengths \(1\le n\le9\), reproducing the known total numbers of minimal dominating sets from OEIS A290379, and directly checks the constructive words for lengths \(11\le n\le100\). Running `python verify.py` with Python 3 (standard library only) should print an exact `VERIFY_OK` line. These finite checks are cross-checks, not the basis of the infinite proof.

## Relationship to prior work

Sahbi (arXiv:2610.03785, originally public 2026-09-30), Theorem 3.1, determines the upper domination **number** of every rectangular grid, which gives \(\Gamma(L_n)=n\); its theorem does not enumerate or classify all maximum-cardinality minimal dominating sets. Goddard and Henning's general matching inequality also supplies the upper bound, but not the equality-case classification here. OEIS A290379 (Howroyd and Weisstein) gives the total number of minimal dominating sets in each open ladder, summed over **all** sizes, not the distribution at the maximum permitted size and not the four-/six-word classification. The present proof is self-contained, including the cardinality bound.

## Limitations

This theorem concerns the ordinary domination notion, open two-row rectangular ladders, and the maximum-cardinality layer among *inclusion-minimal* dominating sets. It does not provide the entire minimal-domination size polynomial, nor does it extend to circular ladders or grids of width at least three. Known general upper-domination or ladder-enumeration results may still furnish an implicit route to the count; historical priority has not been independently certified.

## References

1. R. Sahbi, *Upper Domination in Rectangular Grid Graphs and Its Relation to Sub-Quorum Colorings*, arXiv:2610.03785 (first posted 2026-09-30). https://arxiv.org/abs/2610.03785
2. W. Goddard and M. A. Henning, *Domination Parameters and Added Matchings*, Aequationes Mathematicae 99 (2025), 2009–2024. https://doi.org/10.1007/s00010-025-01196-z
3. OEIS Foundation, A290379, *Number of minimal dominating sets in the n-ladder graph*, with recurrence attributed to A. Howroyd (2017). https://oeis.org/A290379
4. E. J. Cockayne, O. Favaron, C. Payan and A. G. Thomason, *Contributions to the theory of domination, independence and irredundance in graphs*, Discrete Mathematics 33 (1981), 249–258. https://doi.org/10.1016/0012-365X(81)90268-5
