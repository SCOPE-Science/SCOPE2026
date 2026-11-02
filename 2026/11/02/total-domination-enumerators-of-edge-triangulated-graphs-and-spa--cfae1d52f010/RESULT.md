# Total-domination enumerators of edge-triangulated graphs and sparse minimal spectra

## Finding

For a finite simple graph \(G=(V,E)\), form its **edge-triangulation** \(R(G)\) by retaining every original edge \(uv\) and adding one new vertex \(w_{uv}\), adjacent exactly to \(u\) and \(v\), for every \(uv\in E\). Thus each original edge belongs to a new triangle. If \(G\) has no isolated vertices, the complete two-variable total-domination polynomial of \(R(G)\) is the vertex-cover product stated below. The first variable counts chosen original vertices; the second counts chosen new vertices.

For \(a,b\ge2\), all inclusion-minimal total dominating sets of \(R(K_{a,b})\) fall into four explicit types, giving the bivariate polynomial

\[
\boxed{\mathcal M_{a,b}(x,y)=b x^{a+1}+a x^{b+1}+b^a x^a y^a+a^b x^b y^b.}
\]

A total dominating set is a set \(D\) of vertices such that **every** vertex, including those in \(D\), has a neighbor in \(D\). Inclusion-minimal means that no proper subset retains this property; it does **not** mean minimum cardinality.

Consequently the cardinality polynomial is

\[
\boxed{\mathcal M_{a,b}(z,z)=b z^{a+1}+a z^{b+1}+b^a z^{2a}+a^b z^{2b},}
\]

with coefficients added when powers coincide. In particular,

\[
\gamma_t(R(K_{a,b}))=\min(a,b)+1,\qquad
\Gamma_t(R(K_{a,b}))=2\max(a,b),
\]

where \(\Gamma_t\) is the largest cardinality of an inclusion-minimal total dominating set. The total number of such minimal sets is \(a+b+b^a+a^b\).

For every \(b\ge5\), the attainable cardinalities in the connected, \(2\)-degenerate graph \(R(K_{2,b})\) are exactly

\[
\boxed{\{3,4,b+1,2b\}.}
\]

The \(b-2\) successive sizes \(b+2,b+3,\ldots,2b-1\) are therefore impossible. Moreover, the proportion of inclusion-minimal total dominating sets having the **largest** possible cardinality is precisely

\[
\frac{2^b}{2^b+b^2+b+2}\longrightarrow1.
\]

Thus almost every minimal total dominating set in this family is largest, even though the minimum cardinality remains three.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. The arbitrary-base identity assumes \(|V|\ge2\) and no isolated vertices (disconnected graphs are allowed). The complete-bipartite minimal-set classification requires integers \(a,b\ge2\). Every new vertex \(w_e\) is distinguished by its underlying edge \(e\); objects related by an automorphism are **not** identified when counting.

Write \(m=|E|\). For \(S\subseteq V\), define

\[
I(S)=\{v\in S:N_G(v)\cap S=\varnothing\},
\]

and let \(d_G(v)\) be the degree of \(v\) in \(G\). A vertex cover is a subset \(S\subseteq V\) that meets every edge. Define

\[
\mathcal T_{R(G)}(x,y)=
\sum_{\substack{D\subseteq V(R(G))\\ D\text{ total dominating}}}
 x^{|D\cap V|}y^{|D\cap\{w_e:e\in E\}|}.
\]

The general identity is

\[
\boxed{\mathcal T_{R(G)}(x,y)=
\sum_{\substack{S\subseteq V\\S\text{ vertex cover}}}
 x^{|S|}(1+y)^{m-\sum_{v\in I(S)}d_G(v)}
 \prod_{v\in I(S)}\bigl((1+y)^{d_G(v)}-1\bigr).}
\]

For completeness, specializing this identity to \(K_{a,b}\) gives the full (not necessarily minimal) bivariate total-domination polynomial

\[
\begin{aligned}
\mathcal T_{a,b}(x,y)={}&
 x^a\Bigl(\bigl((1+y)^b-1\bigr)^a+\bigl((1+x)^b-1\bigr)(1+y)^{ab}\Bigr)\\
&+x^b\Bigl(\bigl((1+y)^a-1\bigr)^b+\bigl((1+x)^a-1\bigr)(1+y)^{ab}\Bigr)\\
&-x^{a+b}(1+y)^{ab}.
\end{aligned}
\]

## Proof

**1. Necessary and sufficient condition for total domination.** Every new vertex \(w_{uv}\) has exactly the original vertices \(u,v\) as neighbors. Hence any total dominating set \(D\) of \(R(G)\) must select \(S=D\cap V\) meeting every original edge. Conversely, if \(S\) is a vertex cover, every new vertex is already dominated. Since \(G\) has no isolated vertices, each original vertex outside \(S\) has a neighbor in \(S\): every incident edge has its opposite endpoint selected. An original vertex in \(S\) is dominated by another original vertex exactly when it is not in \(I(S)\); otherwise, it must have at least one incident new vertex in \(D\). These are all the conditions.

**2. Independence of the requirements.** Distinct vertices of \(I(S)\) are nonadjacent in \(G\), since each is isolated in \(G[S]\). Thus no edge of \(G\) is incident to two vertices of \(I(S)\), and the incident-edge sets for distinct \(v\in I(S)\) are disjoint. For each such \(v\), the selected new vertices on its \(d_G(v)\) incident edges must be a nonempty subset, contributing \((1+y)^{d_G(v)}-1\). All other \(m-\sum_{v\in I(S)}d_G(v)\) new vertices are unrestricted, giving \((1+y)\) apiece. Multiply the factors and sum over vertex covers \(S\). This proves the general identity, including every coefficient and all quantifiers.

**3. Specialization to complete bipartite graphs.** In \(K_{a,b}\), every vertex cover contains the entirety of one shore, called \(A\) or \(B\). If \(S=A\) alone, all its \(a\) vertices are isolated in \(G[S]\); at least one of the \(b\) incident new vertices must be chosen for each, contributing \(x^a((1+y)^b-1)^a\). If \(S=A\cup T\) with nonempty \(T\subseteq B\), then \(I(S)=\varnothing\), so every new vertex is optional; summing over \(T\) contributes \(x^a((1+x)^b-1)(1+y)^{ab}\). Transpose the shores. The case \(S=A\cup B\) was counted twice, so subtract \(x^{a+b}(1+y)^{ab}\). This proves the displayed closed formula for \(\mathcal T_{a,b}\).

**4. Minimality of the new-vertex choices.** In a minimal total dominating set, no chosen new vertex can be redundant. Once \(S\) is fixed, only a new vertex incident to some \(v\in I(S)\) can be essential, and there must be **exactly one** chosen new vertex incident to each member of \(I(S)\). If two are chosen, removing either preserves total domination; if a chosen new vertex is incident to no member of \(I(S)\), removing it also preserves total domination. The incident-edge groups are disjoint by Step 2.

**5. Four minimal classes.** If \(S=A\cup T\) with \(\varnothing\ne T\subseteq B\), Step 4 forces no selected new vertices. If \(|T|\ge2\), deleting one selected member of \(T\) leaves a total dominating set, so the original choice is not minimal. If \(|T|=1\), deleting its only member would leave all selected original vertices in \(A\) without a neighbor, whereas deleting any member of \(A\) would leave an original edge uncovered because \(b\ge2\). Hence precisely the \(b\) choices \(A\cup\{v\}\) are minimal. The opposite shore supplies \(a\) choices \(B\cup\{u\}\).

If \(S=A\), Step 4 forces exactly one new incident vertex for each member of \(A\). There are \(b^a\) choices. Each selected new vertex is essential for the isolated original vertex it supports. Each selected original vertex is also essential: removing it leaves new vertices of its incident edges without any selected original endpoint. Thus these are all minimal, and their size is \(2a\). Interchanging shores gives \(a^b\) additional minimal sets of size \(2b\). The four classes are pairwise disjoint for \(a,b\ge2\) even when their sizes coincide, proving \(\mathcal M_{a,b}\).

**6. Exact gaps, degeneracy, and concentration.** Put \(a=2\). The four exponents become \(3,4,b+1,2b\), distinct when \(b\ge5\) and all with positive coefficients. Thus the gap and extremal cardinalities follow. The graph is connected because its base \(K_{2,b}\) is connected. Eliminate the degree-two new vertices first; the remaining base graph \(K_{2,b}\) has a degree-at-most-two elimination ordering, so \(R(K_{2,b})\) is \(2\)-degenerate. Substituting \(a=2\) gives exactly \(2^b\) largest minimal sets out of \(2^b+b^2+b+2\), and elementary division yields the limit.

## Verification

Run `python3 verify_total_domination.py` with Python 3 and no third-party packages. The script builds each edge-triangulated graph directly, enumerates vertex subsets, tests open-neighborhood total domination, and checks every chosen vertex for indispensability. It independently compares the bivariate counts against the formulas and checks the general vertex-cover product on small graphs without isolated vertices. A successful run reports:

`VERIFY_OK general_graphs=46 biclique_graphs=9 direct_vertex_subsets=1259880 arithmetic_pairs=121`

These are finite tests, not a proof for all orders. The proof above establishes the unrestricted statements; the enumeration is a reproducibility check.

## Relationship to prior work

Sigarreta (2021) studies total domination under the operators \(S(G)\), \(R(G)\), and \(Q(G)\). Theorem 2 there identifies the **minimum** total-domination number of \(R(G)\) with a total co-independent domination parameter of \(G\); the paper does not enumerate all total dominating sets by their original/new-vertex counts or classify all inclusion-minimal sets on \(R(K_{a,b})\). The scalar minimum \(\min(a,b)+1\) is therefore not separately asserted as new. Bermudo (2022) specializes total-domination-number bounds to tree operators, rather than the complete-bipartite minimal-set spectrum. Bahadır, Ekim, and Gözüpek (2020) examine well-totally-dominated graphs and minimal-total-domination cardinalities in general, but the inspected material provides no equivalent edge-triangulation enumerator. The new claim is the coefficientwise identity, the four-class minimal-set census, and the sharp sparse-spectrum/concentration conclusions.

## Limitations

The general product formula assumes no isolated original vertices; a graph with an isolated original vertex has no total dominating set in this construction and must be treated separately. The four-class minimal census assumes both shores of the complete bipartite base have at least two vertices. The result does not supply an efficient evaluation algorithm for arbitrary base graphs: the universal sum ranges over vertex covers. It does not assert independent external validation or absolute publication priority; synonymous, unindexed descriptions of this graph construction remain a possible literature risk. Finite verification cannot rule out a proof error outside the tested range.

## References

1. José M. Sigarreta, *Total Domination on Some Graph Operators*, Mathematics 9(3), 241 (first published 26 January 2021), DOI: 10.3390/math9030241. Specifically Section 2.2 and Theorem 2. Open-access full text at https://pdfs.semanticscholar.org/7f62/c4797adbc654d8a90af4c863f581f1a5a46f.pdf.
2. Sergio Bermudo, *Total Domination on Tree Operators*, Mediterranean Journal of Mathematics 20, article 42 (first published 20 December 2022), DOI: 10.1007/s00009-022-02236-7. Specifically Section 3.
3. Selim Bahadır, Tınaz Ekim, Didem Gözüpek, *Well-Totally-Dominated Graphs*, first preprint 5 October 2020, arXiv:2010.02341. General background on inclusion-minimal total dominating sets and their cardinalities.
