# Power domination of triangular graphs: star-forest rigidity and full enumerators

## Finding

Let \(n\ge 3\) be an integer, and let \(\operatorname{Tri}(n)=L(K_n)=J(n,2)\) denote the graph whose vertices are the unordered pairs from \([n]\), adjacent when the pairs intersect. Interpret a set \(S\subseteq V(\operatorname{Tri}(n))\) as an ordinary edge set of \(K_n\). Let \(i(S)\) count the vertices of \(K_n\) not incident with any edge of \(S\).

**Complete placement criterion.** The set \(S\) is power dominating in \(\operatorname{Tri}(n)\) if and only if \(i(S)\le2\). Every successful power-domination process is complete after the initial domination step and at most one forcing step; if \(i(S)\ge3\), the process cannot perform its first force.

**Full polynomial.** Define
\[
F_s(z)=\sum_{j=0}^{s}(-1)^j\binom{s}{j}(1+z)^{\binom{s-j}{2}}
\quad(s\ge0).
\]
Here \(F_s\) is the edge-set polynomial for labeled simple graphs with \(s\) vertices and no isolated vertices; in particular, \(F_0(z)=1\) and \(F_1(z)=0\). The complete power-domination polynomial is
\[
\boxed{\mathcal P(\operatorname{Tri}(n);z)
=\sum_{u=0}^{2}\binom n u F_{n-u}(z).}
\]
It counts every power-dominating \(S\) by \(|S|\), with no exclusions or asymptotic restrictions.

**Inclusion-minimal sets.** Such an \(S\) is inclusion-minimal power dominating precisely in one of these disjoint situations:

1. \(i(S)=1\) and \(S\) is a matching on the other \(n-1\) vertices (necessarily \(n\) odd);
2. \(i(S)=2\) and every nontrivial component of the graph \(([n],S)\) is a star, including the two-vertex star \(K_{1,1}\).

Consequently, writing \(\gamma_P\) for the minimum size and \(\overline\gamma_P\) for the maximum size of an inclusion-minimal power-dominating set,
\[
\boxed{\gamma_P(\operatorname{Tri}(n))
=\left\lceil\frac{n-2}{2}\right\rceil,\qquad
\overline\gamma_P(\operatorname{Tri}(n))=\max\{1,n-3\}.}
\]
In particular, all inclusion-minimal power-dominating sets have equal size exactly for \(n\in\{3,4,5\}\); for \(n\ge6\) their possible sizes range without gaps from \(\lceil(n-2)/2\rceil\) through \(n-3\).

For the number \(M_n\) of minimum-cardinality sets,
\[
\boxed{M_3=3,}
\]
and, for even \(n=2m\ge4\),
\[
\boxed{M_n=\binom n2
\frac{(n-2)!}{2^{m-1}(m-1)!}.}
\]
For odd \(n=2m+1\ge5\),
\[
\boxed{M_n=
n\frac{(n-1)!}{2^{m}m!}
+\binom n2\binom{n-2}{3}
\,3\,\frac{(n-5)!}{2^{m-2}(m-2)!}.}
\]

The *complete inclusion-minimal size polynomial* also has a concise exponential-formula description. Set \(c_2=1\) and \(c_s=s\) for integers \(s\ge3\), and write
\[
\Psi(t,z)=\exp\!\left(
\sum_{s\ge2}c_s z^{s-1}\frac{t^s}{s!}
\right).
\]
If \(\mathcal M_n(z)\) counts inclusion-minimal power-dominating sets by size, then
\[
\boxed{\mathcal M_n(z)=
\binom n2(n-2)![t^{n-2}]\Psi(t,z)
+\mathbf1_{\{n\ {\rm odd}\}}\,
\frac{n(n-1)!}{2^{(n-1)/2}((n-1)/2)!}
z^{(n-1)/2}.}
\]
The coefficient notation extracts the coefficient of the indicated power of \(t\) from a formal power series.

**Maximal failures.** For \(n\ge5\), every inclusion-maximal non-power-dominating set consists of all the edges internal to a chosen \((n-3)\)-subset of \([n]\); there are exactly \(\binom n3\) such failures. For \(n=3,4\), the empty set is the unique inclusion-maximal failure.

## Assumptions and scope

All graphs are finite, undirected, simple and labeled. The graph \(K_n\) has vertex set \([n]\). A vertex of \(\operatorname{Tri}(n)\) is therefore an edge of \(K_n\), not a vertex of a triangular lattice. Two such vertices are adjacent exactly when their corresponding original edges share an endpoint.

For a candidate power-dominating set \(S\), initially observe \(S\) and all its neighbors in \(\operatorname{Tri}(n)\). Subsequently, an observed vertex with exactly one unobserved neighbor forces that neighbor to become observed; repeat until no force is available. The empty set is not power dominating. The symbol \([t^r]\) means formal coefficient extraction, and \(\mathbf1\) denotes an indicator. Falling factorials and other nonstandard conventions are not needed.

The term *inclusion-minimal* never means *minimum-cardinality*: a power-dominating set is inclusion-minimal if deleting any selected vertex destroys the property. The upper parameter is the maximum cardinality among such minimal sets.

## Proof

**1. Unobserved pairs and the one-step dichotomy.** Regard \(S\) as an edge set of \(K_n\); let \(U\subseteq[n]\) be the set of its isolated vertices and put \(u=|U|\). By the definition of the line graph, an edge \(ab\) of \(K_n\) belongs to the closed neighborhood of \(S\) in \(\operatorname{Tri}(n)\) if and only if it shares an endpoint with some edge of \(S\). Thus the *entire unobserved set immediately after domination* is exactly the edge set of the clique \(K_U\).

If \(u\le1\), no vertex remains unobserved. If \(u=2\), exactly one vertex, corresponding to the edge between the two elements of \(U\), remains unobserved. Since \(S\ne\emptyset\), there is a vertex of \(K_n\) incident with a selected edge outside \(U\); a cross edge from that vertex to \(U\) is observed and adjacent to the unique unobserved vertex. Hence one force completes the process.

If \(u\ge3\), inspect any observed edge \(ab\) of \(K_n\). Since an edge internal to \(U\) is unobserved, \(ab\) has either zero or one endpoint in \(U\). In the first case it is adjacent to no unobserved vertex. In the second it is adjacent to exactly \(u-1\ge2\) unobserved vertices, corresponding to edges from its endpoint in \(U\) to the other elements of \(U\). Thus no observed vertex has a unique unobserved neighbor; no force can start. This proves the criterion and the sharp propagation dichotomy.

**2. The polynomial.** For each \(u\in\{0,1,2\}\), choose the exact \(u\) isolated original vertices in \(\binom n u\) ways. On the remaining \(n-u\) vertices choose any edge set with no isolated vertices. Requiring every vertex to be incident with some selected edge and applying ordinary inclusion-exclusion over the vertices that would otherwise be isolated gives
\[
F_s(z)=\sum_{j=0}^s(-1)^j\binom sj (1+z)^{\binom{s-j}{2}}.
\]
These cases are disjoint. Summing them proves the complete power-domination polynomial.

**3. Essential edges and star forests.** Let \(d_S(v)\) be the degree of a vertex \(v\) in the selected-edge graph \(([n],S)\). When a selected edge \(ab\) is deleted, the number of newly isolated original vertices is
\[
\mathbf1_{\{d_S(a)=1\}}+\mathbf1_{\{d_S(b)=1\}}\le2.
\]
An edge is essential to a power-dominating \(S\) if and only if this deletion leaves at least three isolated original vertices. If \(i(S)=0\), no deletion can achieve this, so \(S\) is not inclusion-minimal. If \(i(S)=1\), every selected edge must have both endpoints of selected degree one; equivalently, \(S\) is a matching. If \(i(S)=2\), each selected edge must have at least one degree-one endpoint. A connected component of a graph with at least one edge satisfies this edge condition if and only if it is a star: two adjacent vertices of degree at least two are prohibited, forcing every nonleaf to be the unique center of its component. Conversely, all the listed cases have every edge essential. This proves the precise minimal-set classification.

**4. Extremal cardinalities and minimum-set counts.** A set of \(k\) edges can meet at most \(2k\) original vertices. Since it must meet at least \(n-2\), we obtain \(k\ge\lceil(n-2)/2\rceil\). Matchings attain the bound when \(n\) is even by covering exactly \(n-2\) vertices, and when \(n\) is odd by covering \(n-1\) vertices. Therefore the lower bound is sharp.

For even \(n=2m\), a minimum set has \(m-1\) edges and must cover \(2m-2\) distinct original vertices, so it is a matching leaving two vertices unmatched. The standard number of matchings on \(2m-2\) labeled vertices proves the even formula.

For odd \(n=2m+1\), a minimum set has \(m\) edges and covers at least \(2m-1\) vertices. If it covers \(2m\), it is a matching, leaving one unmatched vertex; these number \(n(n-1)!/(2^m m!)\). If it covers exactly \(2m-1\), exactly one endpoint overlap occurs; the edge set consists of a two-edge path on three vertices and \(m-2\) disjoint isolated edges, with two unmatched vertices. Choose those two unmatched vertices, choose the three path vertices, choose its center in three ways, and perfectly match the remaining \(n-5\) vertices. The second odd summand follows. The case \(n=3\) consists of three singleton selections.

For a minimal set with two isolated vertices, the selected-edge graph has \(n-2\) nonisolated vertices and \(c\ge1\) star components. Since each star on \(s\) vertices contains \(s-1\) edges, \(|S|=n-2-c\le n-3\). This bound is attained for \(n\ge4\) by a single star on \(n-2\) vertices. A matching with one isolated vertex has only \((n-1)/2\) edges and does not exceed \(n-3\) for odd \(n\ge5\). At \(n=3\), every minimal set is a singleton. Hence \(\overline\gamma_P=\max\{1,n-3\}\).

For all integers \(k\) between \(\lceil(n-2)/2\rceil\) and \(n-3\) (when this interval is nonempty), a star forest on \(n-2\) vertices with \(c=n-2-k\) components exists: choose \(c-1\) two-vertex stars and one star on the remaining \(n-2c\) vertices. This proves that no intermediate minimal-set size is absent. The equality of upper and lower cardinalities holds exactly for \(n=3,4,5\).

**5. Inclusion-minimal generating function.** A labeled star on \(s\) vertices has one realization when \(s=2\), and \(s\) realizations for \(s\ge3\) (its choice of center). A star contributes \(s-1\) selected edges. The labeled exponential formula for sets of disjoint stars gives \(\Psi(t,z)\). Choose the two isolated original vertices and extract the coefficient for the remaining \(n-2\), yielding the first term of \(\mathcal M_n\). For odd \(n\), matchings with exactly one isolated vertex contribute the second term. The two families do not overlap, proving the expression.

**6. Inclusion-maximal failures.** For \(n\ge5\), a failed set leaves at least three isolated original vertices. If it leaves four or more, adding an edge from a previously used original vertex to an isolated one keeps at least three isolated (when there is a previously used vertex); if there is none, adding one edge still leaves at least three. Thus a maximal failure leaves exactly three isolated vertices. It must contain all edges internal to its \((n-3)\) used vertices, since adding any such missing edge does not change the isolated set. Conversely a complete induced edge set on \(n-3\ge2\) vertices leaves exactly three isolated, and adding any missing edge meets at least one isolated vertex, making the set power dominating. The three isolated vertices uniquely determine the failure, giving \(\binom n3\) maximal failures. For \(n=3,4\) every nonempty selected edge set succeeds, so the empty set is the sole maximal failure.

## Verification

The accompanying self-contained `verify.py` independently applies the original graph-neighborhood monitoring rules to every subset of the \(\binom n2\) vertices of \(\operatorname{Tri}(n)\), for every \(3\le n\le7\). It compares the resulting power-domination status, coefficient profile, inclusion-minimal members, and maximal failures with the structural claims and inclusion-exclusion formula. This comprises \(2^3+2^6+2^{10}+2^{15}+2^{21}=2{,}131{,}016\) subsets; the exact per-order counts and outputs appear in `verification_output.txt`.

The same script checks the claimed minimum coefficients by independent integer arithmetic for \(3\le n\le14\), including parity boundaries and empty-graph conventions. Its deterministic output must end in `VERIFY_OK`. These finite checks support the calculation and software implementation; the unrestricted \(n\ge3\) theorem is established by the preceding proof, not by exhaustive finite testing.

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich, *Power domination polynomials of graphs* (first public arXiv version 28 May 2018), introduce and investigate the complete power-domination polynomial. Their explicit families and threshold-graph method do not supply the triangular-graph formula or the star-forest minimal-set classification. Their computational study of graphs with fewer than ten vertices necessarily includes the tiny \(n=3,4\) cases of the present family; those small instances are not claimed as separately new.

Lu, Mao and Wang, *Power domination in regular claw-free graphs* (arXiv first public 8 August 2018), give upper bounds for four-regular claw-free graphs. The graph \(\operatorname{Tri}(n)\) has degree \(2(n-2)\), so the four-regular theorem applies only at \(n=4\) and does not determine the general family or its set distribution.

Anitha and Rajasingh, *Power Domination Parameters in Honeycomb-Like Networks* (2019), also use the words *triangle graph*, but define a hexagon-based triangular network of a different order and adjacency structure; it is **not** \(J(n,2)\). The distinction was checked against their definition and depicted network.

The later study *Power Domination Reconfiguration* develops minimum-set reconfiguration and upper-minimal terminology for general graphs, but the relevant sections do not give the specific formulas here. General graph bounds and generic polynomial identities do not by themselves enumerate the edge-cover supports of \(K_n\) or identify the extremal star forests.

## Limitations

The theorem is confined to the ordinary power-domination process on the two-subset Johnson graph \(J(n,2)\), not higher-rank Johnson graphs, arbitrary line graphs, or triangular lattice graphs. The infinite claims depend on the mathematical argument, not on experiments. Small cases of the polynomial may already appear in general graph tables; priority for the full family cannot be guaranteed against obscure or unindexed literature. Independent mathematical validation has not been performed.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1, first posted 2018-05-28, https://arxiv.org/html/1805.10984v1 .
2. C. Lu, R. Mao and B. Wang, *Power domination in regular claw-free graphs*, arXiv:1808.02613v1, first posted 2018-08-08, https://arxiv.org/abs/1808.02613 ; DOI:10.1016/j.dam.2020.03.055.
3. J. Anitha and I. Rajasingh, *Power Domination Parameters in Honeycomb-Like Networks*, in *Applied Mathematics and Scientific Computing*, 2019, DOI:10.1007/978-3-030-01123-9_61, https://ir.vistas.ac.in/id/eprint/8090/1/Prof.AnithaPaper.pdf .
4. *Power Domination Reconfiguration*, *La Matematica*, DOI:10.1007/s44007-025-00187-5, https://link.springer.com/article/10.1007/s44007-025-00187-5 .
