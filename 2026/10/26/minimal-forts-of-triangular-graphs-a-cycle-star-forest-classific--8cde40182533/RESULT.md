# Minimal forts of triangular graphs: a cycle–star-forest classification

## Finding

Let \(n\ge 3\), and let \(T_n=J(n,2)=L(K_n)\) be the triangular graph. Identify each vertex of \(T_n\) with an edge of the labeled complete graph \(K_n\). A nonempty set \(F\subseteq V(T_n)\) is a *fort* when every vertex outside \(F\) has either zero or at least two neighbors in \(F\). It is *inclusion-minimal* if no proper nonempty subset is a fort.

**Theorem.** For every integer \(n\ge3\), the inclusion-minimal forts of \(T_n\) are exactly the following two disjoint families of edge sets in \(K_n\):

1. The edges of a single simple cycle of length \(k\), where \(3\le k\le n-1\) (a *nonspanning cycle*).
2. The edges of a spanning star forest **with no isolated vertices**, where a two-vertex component \(K_2\) is permitted as a star.

Define \(f_n(z)=\sum_{F}z^{|F|}\), summed over every inclusion-minimal fort of \(T_n\). Then

\[
\boxed{ f_n(z)=n!\,[u^n]\exp\!\left(u(e^{zu}-1)-\frac{zu^2}{2}\right)
+\frac12\sum_{k=3}^{n-1}\binom nk(k-1)!z^k. }
\]

The first summand counts spanning star forests, and the second counts nonspanning cycles. Thus the entire size distribution is determined for every \(n\). The minimum possible size of a fort is \(2\) when \(n=3,4\), and \(3\) when \(n\ge5\). The greatest possible size of an inclusion-minimal fort is \(n-1\); every integer size between these two endpoints occurs. For \(n\ge4\), the number of inclusion-minimal forts of size \(n-1\) is \(n+\frac{n!}{2(n-1)}\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Every graph \(K_n\) has fixed labeled vertex set \([n]\). The edges of \(K_n\), rather than its vertices, are vertices in \(T_n\); two such vertices are adjacent precisely when their edges have a common endpoint. A fort is required to be nonempty. The term *spanning star forest* throughout this result requires the absence of isolated vertices; its components are copies of \(K_{1,r}\) for \(r\ge1\), with a two-vertex component counted once, not twice by its possible centers. A cycle uses distinct vertices and has length at least three.

The notation \([u^n]\) extracts the coefficient of \(u^n\) from a formal power series in \(u\), whose coefficients are polynomials in \(z\). The generating function is a finite-degree polynomial for each fixed \(n\) after coefficient extraction.

## Proof

**1. Exact edge-incidence test.** Given nonempty \(F\subseteq E(K_n)\), form its spanning subgraph \(H=([n],F)\), and write \(d_H(v)\) for the degree of \(v\) in \(H\). A vertex of \(T_n\) outside \(F\) has the form \(uv\notin F\). Its number of neighbors in \(F\) is exactly

\[
|N_{T_n}(uv)\cap F|=d_H(u)+d_H(v),
\]

because the corresponding edges of \(F\) incident with \(u\) and \(v\) are disjoint collections when \(uv\notin F\). This number is one precisely if the two degrees are \(0\) and \(1\) in either order. A zero-degree vertex and a degree-one vertex cannot be adjacent by an edge of \(F\), so their connecting edge is always outside \(F\). Consequently,

\[
\boxed{F\text{ is a fort of }T_n\quad\Longleftrightarrow\quad
H\text{ has no isolated vertex, or }H\text{ has no vertex of degree }1.}
\tag{1}
\]

**2. Nonspanning minimal forts.** Assume \(H\) has an isolated vertex. By (1), all positive degrees of \(H\) are at least two. Hence a nontrivial component of \(H\) contains a simple cycle \(C\). The edge set of \(C\), regarded as a graph on all \(n\) labels, has degree two on the cycle and zero elsewhere, so by (1) it is a fort. If \(F\) was inclusion-minimal, it follows that \(F=E(C)\). The cycle cannot be spanning because \(H\) was assumed to have an isolated vertex. Conversely, removing any nonempty collection of edges from a nonspanning cycle leaves either the empty edge set or a nonempty union of paths. In the latter case there is at least one degree-one vertex and also a zero-degree vertex off the original cycle; by (1), such a proper edge subset is not a fort. Therefore exactly the nonspanning simple cycles are minimal forts in this case.

**3. Spanning minimal forts.** Suppose \(H\) has no isolated vertices, so \(F\) is an edge cover of \([n]\). An inclusion-minimal fort of this kind must be an inclusion-minimal edge cover: otherwise a proper spanning edge cover would remain a fort by (1). An edge cover is inclusion-minimal exactly when each of its edges has at least one endpoint of degree one: an edge with both endpoints of degree at least two can be removed while preserving coverage, whereas any edge incident to a degree-one vertex is essential. The condition that every edge touches a degree-one vertex is equivalent to every nontrivial connected component being a star. Indeed, a non-star connected component contains either a cycle or a path of length three, each of which has an edge whose two endpoints have degree at least two. Thus every inclusion-minimal spanning edge cover is a spanning star forest without isolates. Conversely, consider such a star forest \(H\). Any nonempty proper edge subset either remains spanning, contrary to edge-cover minimality, or leaves at least one isolated vertex. In the latter case it also has a degree-one vertex, since any nonempty subgraph of a star forest is a forest with at least one edge. Criterion (1) rules out a fort. Hence these star forests are all inclusion-minimal forts. The two cases exhaust every fort and prove the classification.

**4. Enumeration.** On a prescribed \(k\)-element label set, the number of unoriented simple cycles is \((k-1)!/2\), and each contributes \(z^k\). Summing over proper vertex supports yields the cycle term of the displayed polynomial.

A star component on a prescribed set of \(m\ge2\) labels has \(m-1\) edges. For \(m=2\) there is one labeled graph; for \(m\ge3\) there are exactly \(m\) choices of its center. Hence the bivariate exponential generating series for one allowed component is

\[
B(u,z)=\frac{zu^2}{2}+\sum_{m\ge3}\frac{m}{m!}u^m z^{m-1}
=u(e^{zu}-1)-\frac{zu^2}{2}.
\]

By the labeled set construction, an arbitrary collection of these components has exponential generating function \(\exp B(u,z)\). Multiplying its \(u^n\) coefficient by \(n!\) enumerates the spanning star forests on \([n]\) with edge-weight \(z\). This proves the polynomial formula.

**5. Size spectrum.** Every spanning star forest on \(n\) vertices with \(r\) components has \(n-r\) edges, where \(1\le r\le\lfloor n/2\rfloor\). Every such \(r\) is realized by taking \(r-1\) disjoint edges and one star on the remaining vertices. Therefore star-forest sizes fill the integer interval from \(\lceil n/2\rceil\) through \(n-1\). Nonspanning cycles have sizes \(3,4,\ldots,n-1\) when \(n\ge4\). The union gives the stated minimum, maximum, and gap-free size spectrum. For \(n\ge4\), the forts of size \(n-1\) consist of the \(n\) spanning stars and the \(\binom n{n-1}(n-2)!/2=n!/(2(n-1))\) cycles on \(n-1\) labels. For \(n=3\), there are exactly three two-edge spanning stars.

## Verification

A standalone Python script, `verify_minimal_forts.py`, constructs the original adjacency relation in \(T_n\) directly from intersecting pairs. For \(n=3,4,5,6\), it tests every nonempty vertex subset against the defining fort condition, independently extracts all inclusion-minimal forts by set inclusion, and compares the resulting sets and counts with the cycle–star-forest classification. An independent recursion based on the component containing a fixed label computes the star-forest coefficients without using the exponential formula. Exact outcomes are in `VERIFY_OUTPUT.txt`.

The direct checks cover \(8\), \(64\), \(1024\), and \(32768\) subsets respectively. In particular, the minimum-fort polynomials for the last two orders are \(f_5(z)=40z^3+20z^4\) and \(f_6(z)=35z^3+195z^4+78z^5\). Subsequent recurrence-only coefficients are provided for \(7\le n\le14\) as arithmetic examples, not exhaustive graph verifications. The proof above is independent of all finite computations.

## Relationship to prior work

Becker, Cameron, Hanely, Ong, and Previte (2024) study the number of inclusion-minimal forts of graphs, proving general bounds and enumerating path, cycle, spider, wheel, sunlet, and windmill families. Their original preprint does not contain a classification of the minimal forts of triangular graphs or the cycle–star-forest enumerator displayed here. Cameron, Hogben, Kenter, Mojallal, and Schuerger (2023 preprint; subsequent revision 2026) develop the fort hypergraph and relate it to the standard zero-forcing problem; their results do not imply the claimed family-specific generating function.

Afzali, Ghodrati, and Maimani (2024) determine the *failed zero-forcing number* of Johnson graphs, which already implies the minimum size \(3\) of a fort in \(J(n,2)\) for \(n\ge5\). That minimum alone is not claimed as novel here. The contribution assessed here is the classification of **all inclusion-minimal forts of every size**, including large ones, and their complete weight enumeration. A full-text comparison with the Afzali–Ghodrati–Maimani article was not available; this is an explicit bibliographic limitation.

## Limitations

The result is for ordinary forts in the two-subset Johnson graph \(J(n,2)\), not for arbitrary Johnson graphs, general line graphs, or skew zero forcing. The polynomial counts *inclusion-minimal forts*, not all forts, and does not itself compute the complete zero-forcing polynomial. Equality between the minimum fort size and the previously published Johnson-graph failed-forcing bound is not a new assertion. The self-review is not independent validation, and unindexed or inaccessible equivalent statements are possible.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, first public 2024-04-09, https://arxiv.org/abs/2404.05963 .
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1, first public 2023-10-27, https://arxiv.org/abs/2310.17904 .
3. F. Afzali, A. H. Ghodrati, H. R. Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, Journal of Applied Mathematics and Computing 70 (2024), 2665–2675, https://doi.org/10.1007/s12190-024-02064-w .
