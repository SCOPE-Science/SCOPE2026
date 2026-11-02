# Independent domination of subdivided bicliques: exact polynomials and multiplication-table gaps

## Finding

Let \(S(G)\) be the graph obtained by replacing **every** edge of a finite simple graph \(G\) with a path of length two. Let \(D_i(H;z)=\sum_{I}z^{|I|}\), where the sum is over all inclusion-maximal independent vertex sets of \(H\), equivalently all independent dominating vertex sets.

**Theorem 1 (full-subdivision transform).** For any finite simple graph \(G=(V,E)\), writing \(v=|V|\), one has
\[
D_i(S(G);z)=\sum_{\substack{U\subseteq V:\ U=\varnothing\ \mathrm{or}\ \delta(G[U])\ge1}} z^{v-|U|+|E(G[U])|}.
\]
The induced minimum-degree restriction applies only to nonempty \(U\); no minimum degree is assigned to the empty induced graph.

**Theorem 2 (complete bipartite graphs).** For all integers \(a,b\ge1\),
\[
D_i(S(K_{a,b});z)=z^{a+b}+\sum_{p=1}^{a}\sum_{q=1}^{b}\binom ap\binom bqz^{a+b-p-q+pq}.
\]
For \(a,b\ge2\) its degree support is exactly
\[
\operatorname{supp}D_i(S(K_{a,b});z)=\{a+b-1\}\cup\{a+b-1+ij:1\le i\le a-1,\ 1\le j\le b-1\}.
\]
Consequently the lower and upper independent domination numbers are \(a+b-1\) and \(ab\); there are \(1+(2^a-1)(2^b-1)\) maximal independent sets in total. In the star boundary \(a=1\), the formula reduces to \((2^b-1)z^b+z^{b+1}\), and symmetrically when \(b=1\). The coefficient at the minimum degree \(a+b-1\) is \(a(2^b-1)+b(2^a-1)-ab\); this minimum-degree count is independently available from earlier ordinary-domination analysis and is *not* the claimed novelty.

**Corollary 3 (multiplication-table rigidity).** If \(n\ge2\), put \(M(N)=|\{ij:1\le i,j\le N\}|\). Then \(S(K_{n,n})\) has exactly \(1+M(n-1)\) distinct maximal-independent-set cardinalities. For \(n\ge3\) the largest is \(n^2\), and the second largest is \(n^2-n+1\), so all \(n-2\) intermediate cardinalities \(n^2-n+2,\ldots,n^2-1\) fail to occur. Ford's Corollary 3 [3] states \(M(N)\asymp N^2/((\log N)^\delta(\log\log N)^{3/2})\), where \(\delta=1-(1+\log\log2)/\log2>0\). Hence the fraction of integer cardinalities between the minimum \(2n-1\) and maximum \(n^2\) that occur has order \(1/((\log n)^\delta(\log\log n)^{3/2})\) and tends to zero. This asymptotic invokes Ford's established theorem; it is not a new analytic-number-theory proof.

## Assumptions and scope

All graphs are undirected, finite, and simple. Disconnected graphs and isolated original vertices are allowed in Theorem 1; if an original isolated vertex exists it necessarily belongs to each independent dominating set of the subdivision. Theorem 2 assumes \(a,b\) are positive integers and counts labeled vertex subsets, not isomorphism orbits. The integer-degree spectrum and Ford asymptotic are asserted only in the displayed parameter ranges. The subdivision operation replaces every original edge once, not an arbitrary selection of edges; the original bipartite graph \(K_{a,b}\) is not itself the subdivided graph. At \(n=2\), the claimed top gap is empty.

## Proof

**Step 1: A bijection valid for every graph.** Denote the original vertices of \(S(G)\) by \(V\), and the new vertex on edge \(e=uv\) by \(s_e\). Original vertices are pairwise nonadjacent in \(S(G)\), as are subdivision vertices. For an independent dominating set \(I\), define \(U=V\setminus(I\cap V)\). A subdivision vertex \(s_{uv}\) belongs to \(I\) if and only if both of its endpoints \(u,v\) belong to \(U\). Indeed, if either endpoint is selected, independence forbids selection of its subdivision vertex. Conversely, if neither endpoint is selected, the subdivision vertex has no selected neighbor unless it is itself selected, and domination therefore forces it into \(I\). Thus \(I\) is uniquely determined by \(U\):
\[
I(U)=(V\setminus U)\cup\{s_{uv}:uv\in E(G[U])\}.
\]
Every unselected original vertex \(u\in U\) has as neighbors precisely subdivision vertices of incident original edges. It is dominated by \(I(U)\) exactly when it is incident to an edge inside \(G[U]\). Hence domination of all omitted original vertices is equivalent to \(U=\varnothing\) or \(\delta(G[U])\ge1\). All remaining unselected subdivision vertices have a selected original endpoint by construction, hence are dominated. The selected vertices are independent since the only edges in \(S(G)\) join an original endpoint to its subdivision vertex, never between simultaneously selected vertices. This proves necessity, sufficiency, uniqueness, and the weight \(|I(U)|=v-|U|+|E(G[U])|\) in Theorem 1.

**Step 2: Biclique specialization.** Let \(G=K_{a,b}\) with shores \(A,B\) of sizes \(a,b\). For \(U\ne\varnothing\), the graph \(G[U]\) has no isolated vertex if and only if \(p=|U\cap A|\ge1\) and \(q=|U\cap B|\ge1\). Such an induced graph contains exactly \(pq\) edges, and there are \(\binom ap\binom bq\) ways to choose its original vertex set. The empty \(U\) contributes the sole term \(z^{a+b}\). Substitution into Step 1 proves the exact polynomial without overcounting.

**Step 3: Cardinality spectrum and boundary.** The exponent for any nonempty \(U\) is
\[
a+b-p-q+pq=a+b-1+(p-1)(q-1).
\]
When \(a,b\ge2\), all factors \(p-1\in\{0,\ldots,a-1\}\) and \(q-1\in\{0,\ldots,b-1\}\) are realizable; zero is attained by \(p=1\) or \(q=1\) and each positive attainable product arises from \(p,q\ge2\). The empty-\(U\) degree \(a+b\) is already among the products, because choosing \(p=q=2\) gives \((p-1)(q-1)=1\). Therefore the displayed support is exact. Its minimum is \(a+b-1\), and its maximum is \(a+b-1+(a-1)(b-1)=ab\). Distinct choices of \(U\) are distinct independent dominating sets by Step 1, even when exponents coincide. Evaluating at \(z=1\) gives \(1+(2^a-1)(2^b-1)\). For the minimum coefficient, count pairs \(p=1\) or \(q=1\) by inclusion-exclusion to get \(a(2^b-1)+b(2^a-1)-ab\). When a shore has size one, the positive-shore case has exponent \(a+b-1\) throughout, while the empty-\(U\) term has exponent \(a+b\); this proves the boundary formula.

**Step 4: Balanced spectra and missing intervals.** For \(a=b=n\), the nonzero products in Step 3 are exactly the distinct entries of the \((n-1)\times(n-1)\) integer multiplication table, shifted by \(2n-1\). The additional unshifted zero accounts for the extra cardinality. The largest product is \((n-1)^2\). Among all pairs other than \((n-1,n-1)\), at least one factor is at most \(n-2\), and hence their product is at most \((n-1)(n-2)\), achieved by \((n-1,n-2)\). Shifting yields largest degree \(n^2\) and next largest degree \(n^2-n+1\), proving the forbidden interval and its length exactly. Finally the number of integers from minimum degree through maximum inclusive is \(n^2-2n+2\). Substituting Ford's established estimate for \(M(n-1)\) into the exact support count proves the stated sparse-support order. No claim of an asymptotic leading constant is made.

## Verification

The standalone script `verify_inddom_subdivision.py` reconstructs incidence-subdivision adjacencies and checks maximal independent sets **directly from the adjacency lists**, using separate independence and domination tests. It enumerates all \(715{,}550\) nonempty vertex subsets across ten complete-bipartite subdivision instances, including one-vertex shores and the \(3\times4\) biclique. It also checks \(1{,}783\) subsets for 31 general graphs, including all labeled simple graphs with at most three vertices and 20 labeled four-vertex examples, and compares the exact degree supports and extremal coefficients for 136 parameter pairs. Expected result: `VERIFY_OK complete_bipartite_instances= 10 direct_bipartite_subsets= 715550 general_graph_instances= 31 direct_general_subsets= 1783 support_parameter_pairs= 136`. It runs with ordinary Python 3 standard library alone. The finite tests corroborate but do not establish the all-parameter claims, which follow from Steps 1–4.

For example, \(D_i(S(K_{2,2});z)=8z^3+2z^4\), \(D_i(S(K_{2,3});z)=17z^4+4z^5+z^6\), and \(D_i(S(K_{3,3});z)=33z^5+10z^6+6z^7+z^9\).

## Relationship to prior work

Jahari and Alikhani [1] define and study the independent domination polynomial, including joins and lexicographic graph products (their Sections 1–4 and Theorem 2.3). The present edge-subdivision graph is neither a join nor the lexicographic product to which those composition formulas apply. Babikir, Dettlaff, Henning, and Lemańska [2] study the **independent-domination subdivision number**: how many edges must be subdivided to increase the minimum independent domination number, with results including bicliques. Their invariant does not count maximal independent sets by cardinality in the graph obtained by subdividing *every* edge. Prior ordinary-domination enumerations of fully subdivided graphs can account for the minimum cardinality and its multiplicity, but do not supply an independent-set-filtered complete polynomial or its multiplicative support. Ford [3] already proved the multiplication-table asymptotic; the contribution here is its exact manifestation in the spectra of a natural family of graphs, not the number-theoretic estimate itself. Searches did not identify equivalent complete formulas; this absence is not a proof of publication priority.

## Limitations

Originality is assessed against the cited accessible primary literature and targeted research records; an equivalent statement could occur in unindexed literature. The asymptotic depends explicitly on Ford's prior theorem, and no leading constant is asserted. The proof does not address random maximal-independent-set sampling distributions, graph-specific hardness, or partial subdivisions. The subset checker is finite and not a substitute for the structural proof. The minimum-degree multiplicity alone is known from a separate ordinary-domination analysis and is not a new finding.

## References

[1] S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369 (first posted 21 August 2018), https://arxiv.org/abs/1808.07369. Definition of the polynomial and graph-product identities.

[2] A. Babikir, M. Dettlaff, M. A. Henning, and M. Lemańska, *Independent Domination Subdivision in Graphs*, *Graphs and Combinatorics* 37 (2021), 691–709, first published 13 March 2021, https://doi.org/10.1007/s00373-020-02269-3. Open full text, including the complete-bipartite discussion.

[3] K. Ford, *The distribution of integers with a divisor in a given interval*, *Annals of Mathematics* 168 (2008), 367–433, Corollary 3, https://arxiv.org/abs/math/0401223 and https://doi.org/10.4007/annals.2008.168.367. The classical multiplication-table growth bound.
