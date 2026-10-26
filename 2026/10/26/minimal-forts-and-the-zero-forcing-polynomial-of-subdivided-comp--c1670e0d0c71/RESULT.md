# Minimal forts and the zero-forcing polynomial of subdivided complete graphs

## Finding

For every integer \(n\ge3\), let \(H_n\) be the graph obtained by subdividing every edge of the labeled complete graph \(K_n\) exactly once. Its vertices have two distinguishable types: original vertices \(v\in[n]\) and edge-vertices \(w_e\) for \(e\in E(K_n)\), with \(w_{\{u,v\}}\) adjacent precisely to original vertices \(u,v\). Put \(m=\binom n2\).

**Theorem.** The inclusion-minimal forts of \(H_n\) are exactly these three disjoint families:

1. The sets \(\{w_e:e\in E(C)\}\), where \(C\) is a simple undirected cycle of \(K_n\), with its edges distinguished but orientations and starting points not distinguished.
2. The \(n\) sets \(\bigl([n]\setminus\{v\}\bigr)\cup\{w_e:v\in e\}\), one for each original vertex \(v\).
3. The set \([n]\) of all original vertices.

Consequently their size polynomial is
\[
\mathcal M_n(z)=z^n+n z^{2n-2}+\sum_{k=3}^n\frac{n!}{2k(n-k)!}z^k.
\]
Let \(\mathcal F_n(u)=\sum_{T\subseteq E(K_n),\,([n],T)\text{ a forest}}u^{|T|}\) be the ordinary edge-count enumerator of labeled (not necessarily connected) spanning forests. **Every** zero-forcing starting set of \(H_n\) consists of a nonempty set \(X\subseteq[n]\) of original vertices together with edge-vertices \(\{w_e:e\in B\}\), where \(E(K_n)\setminus B\) is a forest; the sole excluded configurations have \(X=\{v\}\) and \(E(K_n)\setminus B\) the complete star centered at \(v\). Therefore the polynomial that counts all zero-forcing starting sets by cardinality is
\[
\boxed{\mathcal Z_n(z)=\bigl((1+z)^n-1\bigr)z^m\mathcal F_n(z^{-1})-nz^{m-n+2}.}
\]
Its least degree and the multiplicity of that degree are, respectively,
\[
\boxed{Z(H_n)=m-n+2,\qquad [z^{m-n+2}]\mathcal Z_n(z)=n\bigl(n^{n-2}-1\bigr).}
\]
The minimum numerical value \(Z(H_n)\) was already known from general subdivision results; the asserted structural fort classification, complete zero-forcing-set enumerator, and multiplicities are the new graph-specific assertions assessed here.

## Assumptions and scope

All graphs are finite, undirected, loopless, simple, and labeled as stated. A *fort* is a nonempty vertex set \(U\) for which every vertex outside \(U\) has either zero or at least two neighbors in \(U\). A fort is *inclusion-minimal* if it contains no proper nonempty fort. A *zero-forcing set* is an initial set of blue vertices from which repeated moves coloring the unique white neighbor of a blue vertex blue can eventually color the whole graph. The polynomials count actual labeled vertex subsets, not isomorphism classes. The theorem's quantified domain is every \(n\ge3\); the case \(n=2\) is excluded.

## Proof

**Incidence description.** Identify an arbitrary vertex subset \(U\subseteq V(H_n)\) with a pair \((A,B)\) in which \(A=U\cap[n]\) and \(B=\{e:w_e\in U\}\). Write \(\delta(A)=\{\{a,b\}\in E(K_n):a\in A,b\notin A\}\) and \(\deg_B(v)=|\{e\in B:v\in e\}|\). By examining first edge-vertices and then original vertices outside \(U\), the fort definition is **equivalent** to
\[
(A,B)\ne(\varnothing,\varnothing),\qquad \delta(A)\subseteq B,\qquad \deg_B(v)\ne1\quad(v\notin A).\tag{1}
\]
Indeed, any unselected edge-vertex sees precisely its two original endpoints, while an unselected original vertex sees precisely the selected incident edge-vertices. No other adjacency types exist.

**No selected originals.** For \(A=\varnothing\), (1) says the subgraph \(([n],B)\) has no degree-one vertex and has at least one edge. Each nonempty graph with no vertex of degree one contains a simple cycle: select any nontrivial component, whose minimum degree is at least two. The edges of such a cycle alone satisfy (1), and removing any cycle edge leaves a nonempty path with a degree-one vertex. Therefore the inclusion-minimal forts with \(A=\varnothing\) are exactly the edge-vertex sets of simple cycles.

**Selected originals.** Suppose \(A\ne\varnothing\) and \(U\) is inclusion-minimal. If \(([n],B)\) contains a cycle, that cycle's edge-vertices form a proper fort contained in \(U\), which is impossible. Hence \(B\) must be acyclic. If \(2\le |A|\le n-2\), then \(B\supseteq\delta(A)\) includes a four-cycle of the complete bipartite cut graph \(K_{|A|,n-|A|}\), a contradiction. If \(|A|=1\), say \(A=\{v\}\), all \(n-1\) star edges at \(v\) belong to \(B\). Each other original vertex already has one selected incident edge, so (1) forces some additional edge joining two vertices other than \(v\). Those two star edges and this additional edge form a triangle in \(B\), again a contradiction. Therefore \(|A|=n-1\) or \(|A|=n\).

If \(A=[n]\), there is no boundary cut, and \(([n],\varnothing)\) is itself a fort. Thus minimality requires \(B=\varnothing\). This all-original set is minimal: a proper nonempty original subset with no selected edge-vertices violates the cut condition in (1).

If \(A=[n]\setminus\{v\}\), the cut \(\delta(A)\) is exactly the full star at \(v\), and (1) holds for \(B=\delta(A)\) since \(\deg_B(v)=n-1\ge2\). Every additional edge in \(B\) joins two vertices in \(A\), and together with their two star edges would form a triangle, so minimality requires \(B=\delta(A)\). Conversely, this star family is minimal: a putative smaller fort with no selected originals would require a cycle inside the star; a putative one with selected original set \(A'\) satisfying \(\varnothing\ne A'\subsetneq A\) would require, by (1), the edge between any \(a\in A'\) and any \(b\in A\setminus A'\) to lie in \(B\), whereas that edge is absent from the star. Keeping all of \(A\) forces all of the star \(B\). This proves the exact three-family classification.

There are \(\binom nk(k-1)!/2=n!/(2k(n-k)!)\) undirected labeled simple cycles of length \(k\). Their selected sets have size \(k\); the all-original set has size \(n\), and the \(n\) star-family sets have size \(2n-2\). This proves \(\mathcal M_n(z)\), including overlaps in *cardinality* but not in selected vertex sets.

**Fort hitting and zero forcing.** A vertex set \(S\) zero-forces a finite graph if and only if it intersects every fort. In one direction, if \(S\) misses a fort, no first forcing move can enter that fort, so forcing can never finish. Conversely, if forcing from \(S\) stops before coloring everything, the final nonempty white set has no outside blue vertex with exactly one white neighbor and is a fort disjoint from \(S\). Every fort contains an inclusion-minimal fort because the graph is finite. Thus it suffices to meet precisely the three families above.

Write \(S=X\cup\{w_e:e\in B\}\) with \(X\subseteq[n]\). Meeting the all-original fort requires \(X\ne\varnothing\). Meeting every cycle fort requires \(B\) to intersect every cycle edge set of \(K_n\), equivalently \(T=E(K_n)\setminus B\) to be an acyclic edge set. For the special fort indexed by \(v\), disjointness occurs exactly when \(X\subseteq\{v\}\) and \(B\cap\delta(\{v\})=\varnothing\). If \(|X|\ge2\), no special fort is missed. If \(X=\{v\}\), disjointness requires the entire star at \(v\) to belong to the forest \(T\). That forest cannot contain any other edge, because every edge joining two leaves closes a triangle. Hence \(T\) is exactly that star. This establishes the stated complete characterization of zero-forcing sets.

Each forest \(T\) corresponds to a unique \(B=E(K_n)\setminus T\), contributing \(z^{m-|T|}\). All nonempty \(X\) contribute \((1+z)^n-1\). There is precisely one excluded pair for each \(v\), namely \(X=\{v\}\) and \(T\) the centered star (\(n-1\) edges); its size is \(1+m-(n-1)=m-n+2\). Subtracting these \(n\) distinct pairs proves \(\mathcal Z_n(z)\).

Every forest has at most \(n-1\) edges and \(X\) is nonempty, so every zero-forcing set has at least \(m-n+2\) vertices. This bound is attained by taking one original vertex \(v\) and the complement of any spanning tree other than the star centered at \(v\). Cayley's formula supplies \(n^{n-2}\) spanning trees, exactly one of which is that forbidden star for fixed \(v\). Distinct choices of \(v\) and spanning tree give distinct labeled sets. The minimum and its multiplicity follow.

For completely explicit coefficient extraction, the classical exponential formula for labeled trees yields
\[
\sum_{n\ge0}\frac{t^n}{n!}\mathcal F_n(u)=
\exp\!\left(\sum_{r\ge1}\frac{r^{r-2}}{r!}u^{r-1}t^r\right),
\]
where the \(r=1\) summand is interpreted as \(t\) (one isolated vertex). Therefore the theorem determines every coefficient of \(\mathcal Z_n(z)\) by finite exact arithmetic.

## Verification

The standalone script `verify.py` forms the original subdivision graph, independently evaluates the degree-one-neighbor fort condition, checks inclusion-minimality against *all proper subsets* by subset dynamic programming, and directly simulates zero-forcing moves. It separately constructs the proposed minimal-fort families via graph cycles and compares exact families, then compares every starting vertex set against the forest characterization. It also matches polynomial coefficients and the minimum-size multiplicities.

The exhaustive checks covered \(n=3,4,5\), respectively \(63\), \(1023\), and \(32767\) nonempty vertex subsets. The minimal-fort totals were \(5,12,43\), the total zero-forcing-set counts were \(46,566,9016\), and minimum zero-forcing-set counts were \(6,60,620\). All exact-family and coefficient comparisons passed. Run `python3 verify.py` to reproduce `verification_output.txt`. This finite check is corroborative; the proof above handles every integer \(n\ge3\).

## Relationship to prior work

Becker–Cameron–Hanely–Ong–Previte (arXiv:2404.05963, first public 9 April 2024) developed systematic minimal-fort enumeration, including path, cycle, spider and graph-product constructions. Its inspected full PDF contains no complete subdivision or incidence-graph classification. The new theorem instead gives the complete minimal-fort obstruction hypergraph for the once-subdivided clique and converts it into a full zero-forcing-set enumerator.

Barrett–Butler–Catral–Fallat–Hall–Hogben–Young (2014, *Electronic Journal of Linear Algebra*, vol. 27, pp. 444–457) already derived the numerical zero-forcing parameter for complete subdivisions generally (Theorem 1.3) and proved in Remark 3.4 that a minimum zero-forcing set for a 2-edge-connected base has exactly one original vertex. Accordingly, the numerical value and that one-original restriction are not asserted to be new. Their inspected theorem and remark do not classify all forts or all starting sets, nor state the forest-indexed full polynomial or the \(n(n^{n-2}-1)\) labeled optimum count. The latter is compatible with, but not a restatement of, their result.

The exact cycle/forest equivalences, not the absence of a search hit, provide the claimed distinction. Equivalent unindexed statements, or an unexamined treatment of the full zero-forcing polynomial for incidence graphs, remain a priority risk.

## Limitations

The theorem concerns the once-subdivided *complete* graph with distinguishable original and edge-vertices, not general complete subdivisions, repeated subdivisions, or arbitrary incidence graphs. It does not classify forcing move orders or settle maximum-nullity questions beyond previously published work. The sources and literature comparisons do not constitute proof of global bibliographic uniqueness. No independent mathematical validation has been performed.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, 9 April 2024. https://arxiv.org/pdf/2404.05963
2. W. Barrett, S. Butler, M. Catral, S. M. Fallat, H. T. Hall, L. Hogben and M. Young, *The maximum nullity of a complete subdivision graph is equal to its zero forcing number*, Electronic Journal of Linear Algebra 27 (2014), 444–457. https://journals.uwyo.edu/index.php/ela/article/download/1381/1381/
3. A. Cayley, *A theorem on trees*, Quarterly Journal of Mathematics 23 (1889), 376–378, for the classical labeled-tree count used in the coefficient corollary.
