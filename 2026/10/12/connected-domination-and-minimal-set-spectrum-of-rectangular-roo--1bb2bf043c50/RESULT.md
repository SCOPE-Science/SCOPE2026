# Connected-domination and minimal-set spectrum of rectangular rook graphs

## Finding

Let \(m,n\ge2\). In the rectangular rook graph \(R_{m,n}=K_m\square K_n\), vertices are squares \((i,j)\) of an \(m\)-by-\(n\) board, adjacent when they share a row or a column. A set is *connected dominating* when it dominates the whole graph and induces a connected nonempty graph. Define \(\mathrm{CD}_{m,n}(z)=\sum_S z^{|S|}\), summed over all such sets. To interpret the bivariate series below, use the same definition for positive dimensions having \(m=1\) or \(n=1\), where \(\mathrm{CD}_{1,n}(z)=(1+z)^n-1\) and likewise in the transpose case. Define \(\mathrm{MCD}_{m,n}(z)\) by restricting the sum to inclusion-minimal connected dominating sets.

For formal commuting indeterminates \(u,v,z\), put
\[
F(u,v;z)=\sum_{a,b\ge0}(1+z)^{ab}\frac{u^a v^b}{a!b!},\qquad C(u,v;z)=\log F(u,v;z)-u-v.
\]
Then the complete connected-domination generating function is
\[
\boxed{\sum_{m,n\ge1}\mathrm{CD}_{m,n}(z)\frac{u^mv^n}{m!n!}=(e^u+e^v-1)C(u,v;z).}\tag{1}
\]
Equivalently, if \(C_{a,b}(z)=a!b![u^av^b]C(u,v;z)\) for \(a,b\ge1\), then for every \(m,n\ge2\)
\[
\boxed{\mathrm{CD}_{m,n}(z)=\sum_{b=1}^n\binom nb C_{m,b}(z)+\sum_{a=1}^m\binom ma C_{a,n}(z)-C_{m,n}(z).}\tag{2}
\]
Here \(C_{a,b}(z)\) counts labeled connected bipartite graphs with fixed part sizes \(a,b\) and no isolated vertices, by their number of edges.

The more restrictive inclusion-minimal connected dominating sets admit a complete structural description: their selected board squares form the edges of a bipartite tree on all \(m\) rows and some \(1\le b<n\) columns, with *no leaf among the occupied column vertices*, or the transpose, consisting of a tree on all \(n\) columns and some \(1\le a<m\) rows with no leaf among the occupied row vertices. These two cases are disjoint. In particular, writing \(\left\{\begin{smallmatrix}p\\q\end{smallmatrix}\right\}\) for a Stirling number of the second kind, the exact minimal-set polynomial is
\[
\boxed{\begin{aligned}
\mathrm{MCD}_{m,n}(z)= {}&\sum_{b=1}^{\min(m-1,n-1)}\binom nb\,m^{b-1}b!\left\{\begin{smallmatrix}m-1\\b\end{smallmatrix}\right\}z^{m+b-1}\\
&+\sum_{a=1}^{\min(m-1,n-1)}\binom ma\,n^{a-1}a!\left\{\begin{smallmatrix}n-1\\a\end{smallmatrix}\right\}z^{n+a-1}.
\end{aligned}}\tag{3}
\]
For \(2\le m\le n\), the cardinalities of all inclusion-minimal connected dominating sets form exactly the union of two integer intervals
\[
\boxed{\{m,m+1,\ldots,2m-2\}\ \cup\ \{n,n+1,\ldots,n+m-2\}.}\tag{4}
\]
In particular, there is an internal gap of absent sizes exactly when \(n\ge2m\), when the missing sizes are \(2m-1,\ldots,n-1\). The maximum inclusion-minimal size is always \(m+n-2\), and the minimum possible size is \(\min(m,n)\) (the known connected-domination number).

## Assumptions and scope

All graphs are finite, simple, and labeled. Fix \(m,n\ge2\). A vertex subset \(S\subseteq V(R_{m,n})\) corresponds to an edge subset \(E_S=\{r_i c_j:(i,j)\in S\}\) of the complete bipartite graph \(K_{m,n}\). Let \(H_S\) be the bipartite graph induced by those edges **on their occupied endpoints**, so \(H_S\) has no isolated vertices. Its two part sizes are \(r(S)\), the number of occupied rows, and \(c(S)\), the number of occupied columns. The empty set is excluded from connected domination. A connected dominating set is *inclusion-minimal* if deleting any one of its vertices destroys connectivity or domination; this is equivalent to the absence of any smaller connected dominating subset because connected domination is not assumed monotone but every connected vertex set admits stepwise connected vertex deletion down to any connected subset by pruning a spanning tree. More directly, in this particular class the classification below also rules out non-single-deletion shortcuts.

The two polynomials are ordinary size generating functions in \(z\). The full connected-domination series includes the naturally extended one-row and one-column cases, while the minimal-set theorem and its two-interval spectrum require \(m,n\ge2\). The displayed bivariate series use exponential normalization in the labeled row and column variables \(u,v\). These are formal power series; no analytic convergence is assumed. Stirling numbers count partitions into nonempty unlabelled blocks, with \(\left\{\begin{smallmatrix}p\\q\end{smallmatrix}\right\}>0\) for \(1\le q\le p\).

## Proof

**1. Support criterion.** A square \((i,j)\) is dominated by \(S\) precisely when some selected square lies in row \(i\) or column \(j\). Thus every square is dominated exactly when there are not simultaneously an unoccupied row and an unoccupied column. Equivalently,
\[
S\text{ dominates }R_{m,n}\quad\Longleftrightarrow\quad r(S)=m\text{ or }c(S)=n.\tag{5}
\]
The rook graph is the line graph of \(K_{m,n}\). Two selected squares are adjacent exactly when their incidence edges share an endpoint; hence the nonempty subgraph induced by \(S\) is connected if and only if \(H_S\) is connected. Combining the two conditions proves the announced support characterization.

**2. Enumeration of every connected dominating set.** A graph on fixed labeled vertex classes of sizes \(a,b\), with potential edges only across the classes, has edge-weight generating function \((1+z)^{ab}\). The labeled exponential formula for its decomposition into connected components says that \(\log F\) enumerates connected components, including isolated single-row and single-column vertices, represented by the terms \(u\) and \(v\). It follows that \(C(u,v;z)=\log F-u-v\) enumerates exactly connected components using at least one vertex of each class. Such components are precisely the incidence supports \(H_S\). The subset \(S\) is dominating if its support occupies all rows (additional unoccupied columns allowed) or all columns (additional unoccupied rows allowed). Multiplying \(C\) by \(e^v\) counts the first case, by \(e^u\) counts the second, and subtracting \(C\) avoids double-counting those occupying both classes completely. This proves (1) and its coefficient form (2). There is no contribution with \(m=0\) or \(n=0\).

**3. Inclusion-minimal supports are one-sided-spanning trees.** If \(H_S\) contains a cycle, deleting a cycle edge preserves connectivity and its occupied rows and columns. Equations (5) and the line-graph correspondence then show that \(S\) is not inclusion-minimal. Thus an inclusion-minimal connected dominating set gives a bipartite tree \(H_S\). If this tree occupies *all* rows and columns, it has at least four vertices and contains a leaf. Deleting its incident edge leaves a connected nonempty tree and leaves every vertex of the *opposite* part occupied (the neighbor of the leaf cannot also have degree one). Thus it remains dominating by (5), contradicting minimality. Therefore precisely one side of the incidence tree is completely occupied.

Suppose all \(m\) rows are occupied while only \(b<n\) columns are occupied. If an occupied column is a leaf, deleting its incident edge leaves a nonempty connected tree still occupying all rows, contrary to inclusion-minimality. Conversely, assume every occupied column has degree at least two. Deleting any selected edge of the tree either disconnects the remaining selected edges (if neither endpoint becomes isolated), or deletes a degree-one row (if a leaf is removed). The second case loses full row occupancy while the already proper column support remains proper, so domination fails. There cannot be a degree-one column by hypothesis. Every one-edge deletion therefore destroys connected domination. Moreover any proper connected subset of the tree's edges can be enlarged to the full tree by adding adjacent edges one at a time; since every first deletion already destroys the property, there is no smaller connected dominating subset. Thus this condition is necessary and sufficient. The argument with rows and columns exchanged gives the other case, and the cases cannot overlap because exactly one side is fully occupied.

**4. Exact counts from a weighted bipartite tree identity.** For a complete bipartite graph on \(m\) labeled row vertices and \(b\) labeled column vertices, put independent variables \(x_i\) on rows and \(y_j\) on columns, and give edge \(r_i c_j\) weight \(x_i y_j\). Let \(X=\sum_i x_i\) and \(Y=\sum_j y_j\). The weighted matrix-tree theorem gives
\[
\sum_T\prod_{r_ic_j\in E(T)}x_i y_j=X^{b-1}Y^{m-1}\prod_i x_i\prod_j y_j.\tag{6}
\]
For completeness, delete the Laplacian row and column for column vertex \(c_b\). The remaining matrix has row block \(Y\operatorname{diag}(x_i)\), column block \(X\operatorname{diag}(y_j)_{j<b}\), and cross block \((-x_i y_j)\). Its Schur complement is \(X[\operatorname{diag}(y_j)_{j<b}-(1/Y)(y_j)_{j<b}(y_j)_{j<b}^{\mathsf T}]\). The determinant lemma evaluates this determinant as \(X^{b-1}\prod_{j<b}y_j\cdot y_b/Y\); multiplying by \(Y^m\prod_i x_i\) proves (6). This computation is initially over rational functions and is therefore a valid polynomial identity.

Divide (6) by \(\prod_i x_i\prod_j y_j\) and set every \(x_i=1\). The resulting degree-excess enumerator is \(m^{b-1}(y_1+\cdots+y_b)^{m-1}\), with exponent of \(y_j\) equal to \(\deg_T(c_j)-1\). Requiring every occupied column to have degree at least two is equivalent to requiring every \(y_j\) to appear to a strictly positive power. The sum of these coefficients is the number of onto functions from an \((m-1)\)-element labeled set onto \(b\) labeled columns, namely \(b!\left\{\begin{smallmatrix}m-1\\b\end{smallmatrix}\right\}\). Hence there are exactly
\[
m^{b-1}b!\left\{\begin{smallmatrix}m-1\\b\end{smallmatrix}\right\}
\]
such trees on a prescribed \(m\)-row and \(b\)-column support. Choose the columns in \(\binom nb\) ways, and note that a tree has \(m+b-1\) edges. This is the first sum in (3), with \(1\le b\le\min(m-1,n-1)\). The transpose gives the second sum, proving (3).

**5. The support spectrum.** Assume \(m\le n\). Each first-sum term for \(b=1,\ldots,m-1\) has strictly positive coefficient (because \(b\le m-1\) and \(b<n\)), so it realizes precisely the sizes from \(m\) through \(2m-2\). Similarly the second-sum terms realize precisely the sizes from \(n\) through \(n+m-2\). There are no other minimal sets by step 3. Thus (4) follows. The intervals leave at least one missing integer exactly when \(2m-2<n-1\), or \(n\ge2m\). Their extreme values yield the claimed minimum and upper inclusion-minimal numbers.

## Verification

A standalone deterministic Python verifier accompanies this result as `verify_rook_connected.py`; run with Python 3 using only the standard library. For each listed board it enumerates every nonempty vertex subset, independently evaluates domination using closed rook neighborhoods, checks induced connectivity by breadth-first search, and tests inclusion-minimality by all one-vertex deletions. It separately computes the predicted full polynomial using a root-component recurrence for labeled bipartite graphs, and the predicted minimal polynomial using Stirling-number recurrence. Equality of all coefficients and the one-sided-tree classification is asserted for eleven boards: \((2,2),(2,3),\ldots,(2,8),(3,3),(3,4),(3,5),(4,4)\). There are **190,277** enumerated nonempty subsets, of which **158,351** are connected dominating and **1,548** are inclusion-minimal connected dominating sets, across these boards. As concrete reproducible coefficient checks,
\[
\begin{split}
\mathrm{CD}_{3,3}(z)&=6z^3+72z^4+117z^5+84z^6+36z^7+9z^8+z^9,\\
\mathrm{MCD}_{3,3}(z)&=6z^3+36z^4.
\end{split}
\]
All assertions pass. The finite enumeration does not establish the universal formulas; the support equivalence, tree characterization, and weighted matrix-tree computation in the proof do so.

## Relationship to prior work

The polynomial for *ordinary* dominating sets of rectangular rook graphs was obtained by Mertens (2024), with the same row/column incidence viewpoint, but does not impose connectivity or classify inclusion-minimal connected dominating sets. Kanté, Limouzy, Mary and Nourine (2014) study general minimal connected domination and its algorithmic relation to enumeration of minimal transversals. Kanté and colleagues' other 2014 paper gives an algorithm to enumerate minimal **edge** dominating sets in all graphs (the line-graph alias), without requiring connectedness or giving this family-specific cardinality distribution. Abu-Khzam and coauthors (2022 preprint) develop algorithms for enumerating minimal connected dominating sets in general graphs but do not give the present rook-graph formulas. The labeled connected-bipartite-graph exponential formula and weighted matrix-tree identity are standard enumeration mechanisms used here, not claimed as new individually. The claimed contribution is the combined complete connected-domination polynomial, exact inclusion-minimal tree criterion and enumerator, and sharp two-interval spectrum and gap for the natural rook-graph family.

## Limitations

The claim concerns labeled rectangular rook graphs with \(m,n\ge2\) only; it does not classify arbitrary line graphs or arbitrary edge-dominating subsets of bipartite graphs. The proof is self-contained apart from standard exponential-formula and matrix-tree principles, whose required specializations are explicitly derived. No assertion of priority beyond the recorded literature comparison is made. Earlier presentations under alternative terminology, particularly connected edge domination of complete bipartite graphs, remain a possible unindexed overlap. The finite verifier is corroborating evidence rather than a general proof, and no independent review has been performed.

## References

1. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine, and T. Uno, *Polynomial Delay Algorithm for Listing Minimal Edge Dominating sets in Graphs*, arXiv:1404.3501 (first publicly posted 2014-04-14). https://arxiv.org/abs/1404.3501
2. M. M. Kanté, V. Limouzy, A. Mary, and L. Nourine, *On the Enumeration of Minimal Dominating Sets and Related Notions*, arXiv:1407.2053 (first publicly posted 2014-07-08). https://arxiv.org/abs/1407.2053
3. F. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff, and K. Mann, *Enumerating Connected Dominating Sets*, arXiv:2205.00086 (first publicly posted 2022-04-29). https://arxiv.org/abs/2205.00086
4. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), Article 24.3.7, arXiv:2401.00716 (first publicly posted 2024-01-01). https://arxiv.org/abs/2401.00716
