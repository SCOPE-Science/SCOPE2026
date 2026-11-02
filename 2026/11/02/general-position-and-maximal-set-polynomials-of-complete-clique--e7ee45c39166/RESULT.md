# General-position and maximal-set polynomials of complete-clique paths

## Finding

Let \(n,L\ge3\) be integers and let \(G_{n,L}=K_n\square P_L\). The vertices are ordered pairs \((i,t)\), where \(1\le i\le n\) and \(1\le t\le L\). A subset is in general position when no three of its vertices lie on any shortest path. Let \(\Psi_{n,L}(z)\) count all general-position subsets by their cardinalities (including the empty set), and let \(M_{n,L}(z)\) count inclusion-maximal general-position subsets by cardinality.

**Exact classification.** Every general-position subset has one of the following, mutually exclusive forms:

1. At most one vertex in each vertical path column \(\{i\}\times[L]\).
2. Precisely two vertices \((i,a),(i,b)\) in one column, with \(a<b\); any other selected vertices occupy distinct columns and each has a layer index strictly between \(a\) and \(b\).

Consequently,
\[
\boxed{\Psi_{n,L}(z)=(1+Lz)^n+n z^2\sum_{h=0}^{L-2}(L-1-h)(1+hz)^{n-1}.}
\]

Define the nonnegative integers
\[
\begin{aligned}
B_{n,L}&=n\sum_{h=1}^{L-2}(L-1-h)h^{n-1},\\
A_{n,L}&=L^n-2n\sum_{h=1}^{L-2}h^{n-1}
+n(n-1)\sum_{a=2}^{L-2}\sum_{b=a+1}^{L-1}(b-a-1)^{n-2}.
\end{aligned}
\]
Empty sums are zero. Then the inclusion-maximal-set polynomial is
\[
\boxed{M_{n,L}(z)=n(L-1)z^2+A_{n,L}z^n+B_{n,L}z^{n+1}.}
\]
For all \(n,L\ge3\), each of the three displayed coefficients is strictly positive. In particular, the cardinality spectrum of maximal general-position sets is **exactly** \(\{2,n,n+1\}\); the largest size is \(n+1\), whereas the smallest is \(2\). The all-set polynomial has degree \(n+1\), with leading coefficient \(B_{n,L}\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The Cartesian product graph has horizontal edges between different columns in the same layer and vertical edges between consecutive layers in the same column. Both factor orders are at least three; no assertion is made about other graph products or factors. A general-position set is inclusion-maximal if no outside vertex can be adjoined while retaining general position; it need not have maximum possible cardinality. Distinct labeled subsets are counted separately.

## Proof

**Step 1: identify all forbidden triples.** For vertices in different or equal columns, respectively, the exact distance is
\[
d((i,s),(j,t))=|s-t|+\mathbf1_{i\ne j}.
\]
A geodesic triple must use at least two vertices of the same column: with three distinct columns, the sum of the two consecutive distances introduces two column-change units while the endpoint distance introduces only one, so equality is impossible, regardless of the ordering of layer coordinates. Three selected vertices in the same column cannot occur because their layer coordinates lie on one path.

Suppose two selected vertices are \((i,a),(i,b)\), \(a<b\), and a third selected vertex is \((j,c)\), \(j\ne i\). If \(c\le a\), then \((i,a)\) lies on a geodesic from \((j,c)\) to \((i,b)\); if \(c\ge b\), the analogous assertion holds with \((i,b)\) as middle vertex. If \(a<c<b\), none of these vertices lies between the other two on a geodesic: in the only potentially delicate equality, traversing via the third column would cost two extra horizontal steps. Therefore compatibility is exactly \(a<c<b\).

If a second column were doubled at \(c<d\), the previous condition would require both \(c,d\) strictly between \(a,b\) and both \(a,b\) strictly between \(c,d\), an impossibility. Conversely, sets satisfying either form in the finding have no forbidden triple, by the distance formula. This proves the classification.

**Step 2: count all sets.** With at most one vertex per column, each of the \(n\) columns contributes \(1+Lz\), giving \((1+Lz)^n\). For the second form, choose its doubled column in \(n\) ways and heights \(a<b\). Each other column is empty or contains one of the \(b-a-1\) interior vertices. This contributes \(nz^2(1+(b-a-1)z)^{n-1}\) for each \(a<b\). Writing \(h=b-a-1\), there are \(L-1-h\) such pairs. The two forms are disjoint, giving \(\Psi_{n,L}\).

**Step 3: classify inclusion-maximal second-form sets.** When \(b=a+1\), no other vertex can be adjoined, yielding precisely \(n(L-1)\) maximal sets of size two. When \(b-a-1\ge1\), each of the remaining columns can accept an interior vertex without violating the classification. Thus these sets are inclusion-maximal exactly when every remaining column is occupied. Their number is
\[
n\sum_{a<b}(b-a-1)^{n-1}=B_{n,L},
\]
and each has size \(n+1\).

**Step 4: classify inclusion-maximal first-form sets.** Such a set cannot be maximal if any column is empty, because a vertex can always be added in that column. Therefore a maximal first-form set has one vertex in every column, and is specified by a labeled height tuple \((t_1,\ldots,t_n)\in[L]^n\). It can be extended by a second vertex in some column if and only if either (i) one height is the unique minimum \(a\), while all other heights lie strictly above it but below \(L\), or (ii) one height is the unique maximum \(b\), while all other heights lie strictly below it but above \(1\). The first possibility has
\[
n\sum_{h=1}^{L-2}h^{n-1}
\]
height tuples, and so does the second. Both are possible at once precisely when the unique minimum is some \(2\le a\le L-2\), the unique maximum is some \(a+1\le b\le L-1\), and all other \(n-2\) heights lie strictly between them. Their intersection has cardinality
\[
n(n-1)\sum_{a=2}^{L-2}\sum_{b=a+1}^{L-1}(b-a-1)^{n-2}.
\]
Inclusion–exclusion among all \(L^n\) tuples gives exactly \(A_{n,L}\). These maximal sets have cardinality \(n\), completing the maximal polynomial.

**Step 5: positivity, degrees, and extrema.** For \(n,L\ge3\), the size-two term is positive. At least one size-\(n\) maximal set exists, for example the tuple with all heights equal to \(1\): adding any second vertex is incompatible with the remaining columns. Finally \(a=1,b=L\) admits an interior vertex in every remaining column, yielding size \(n+1\) and positive \(B_{n,L}\). No general-position set can have more than \(n+1\) vertices by Step 1, so all extrema and the exact cardinality spectrum follow.

## Verification

The companion file `verify.py` uses only Python 3's standard library. From a directory containing that file, run `python3 verify.py`. It constructs each Cartesian product directly, computes shortest-path distances by breadth-first search, rejects a subset when it contains three vertices satisfying a distance equality, and checks inclusion-maximality by attempting every one-vertex extension. This independent predicate enumeration is compared with both closed formulas.

All \(1,450,496\) labeled subsets were evaluated across eight parameter pairs: \((n,L)=(3,3),(3,4),(4,3),(4,4),(3,5),(5,3),(3,6),(4,5)\). All comparisons passed. For instance, \(\Psi_{3,3}(z)=1+9z+36z^2+33z^3+3z^4\) and \(M_{3,3}(z)=6z^2+21z^3+3z^4\). These finite checks support, but do not replace, the proof for all \(n,L\ge3\).

## Relationship to prior work

Iršič, Klavžar, Rus, and Tuite [1] introduced general-position polynomials, gave general inclusion–exclusion using maximal general-position sets, and determined formulas for Cartesian grids of two paths. Their unrestricted inclusion–exclusion identity does not supply the particular maximal subsets or coefficients derived above. Klavžar, Patkós, Rus, and Yero [2] studied maximum general-position sets in Cartesian products, including path-by-path products and Hamming graphs, without the present all-cardinality enumeration. Klavžar, Neethu, and Chandran [3, Theorem 3.5] already established the second-player win in the general-position achievement game on products with a connected bipartite factor; therefore the availability of certain terminal pairs and that game outcome are not claimed here as new. Tian and Klavžar [4] treat total, dual, and outer general-position variants for arbitrary Cartesian products; these are distinct invariants and do not produce the ordinary general-position-set enumerators here.

The point of the present result is the explicit all-set polynomial together with the complete inclusion-maximal polynomial and structural classification of every admissible configuration for clique-by-path Cartesian products.

## Limitations

These formulas apply only to the stated simple Cartesian products, with both factor orders at least three. They do not establish log-concavity, root-location properties, or computational complexity for general graph families. Complete bibliographic uniqueness is not established: differently indexed prior descriptions of the same clique–path configurations may exist. All mathematical verification outside the general proof is finite; independent external audit has not been performed.

## References

[1] V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General Position Polynomials*, Results in Mathematics 79, article 110 (2024), DOI: 10.1007/s00025-024-02133-3; first publicly available as arXiv:2401.05696 on 2024-01-11.

[2] S. Klavžar, B. Patkós, G. Rus, and I. G. Yero, *On General Position Sets in Cartesian Products*, Results in Mathematics 76, article 123 (2021), DOI: 10.1007/s00025-021-01438-x.

[3] S. Klavžar, P. K. Neethu, and U. S. V. Chandran, *The General Position Achievement Game Played on Graphs*, Discrete Applied Mathematics 317, 109–116 (2022), arXiv:2111.07425.

[4] J. Tian and S. Klavžar, *Variety of General Position Problems in Graphs*, Bulletin of the Malaysian Mathematical Sciences Society 48, article 5 (2025), DOI: 10.1007/s40840-024-01788-z.
