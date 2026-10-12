# Zero-forcing polynomials of rook graphs via bipartite forests

## Finding

For integers \(m,n\ge 1\), let \(R_{m,n}=K_m\square K_n\) be the rook graph with vertices indexed by the cells of an \(m\)-by-\(n\) board. For an initially blue set \(B\), form the bipartite graph \(H_B\) on the full set of \(m\) row labels and \(n\) column labels: an edge is present precisely when its corresponding cell is initially white. In a graph \(H\), let \(\iota_R(H),\iota_C(H)\) be the numbers of isolated row and column vertices, and let \(\lambda_R(H),\lambda_C(H)\) be the numbers of degree-one row and column vertices.

**Theorem.** The set \(B\) is an ordinary zero-forcing set of \(R_{m,n}\) if and only if \(E(H_B)=\varnothing\), or \(H_B\) is a forest satisfying
\[
\bigl(\iota_R(H_B)>0\ \text{and}\ \lambda_C(H_B)>0\bigr)
\quad\text{or}\quad
\bigl(\iota_C(H_B)>0\ \text{and}\ \lambda_R(H_B)>0\bigr).
\]
This description determines all coefficients of the ordinary zero-forcing polynomial \(\mathcal Z(R_{m,n};x)=\sum_{B\text{ zero forcing}}x^{|B|}\) by the explicit bivariate component formula below.

For positive integers \(p,q\), set
\[
T_{p,q}=p^{q-1}q^{p-1},\qquad
U_{p,q}=q^{p-1}p!\,\left\{\!\begin{matrix}q-1\\p\end{matrix}\!\right\},\qquad
V_{p,q}=p^{q-1}q!\,\left\{\!\begin{matrix}p-1\\q\end{matrix}\!\right\},
\]
where the braces denote Stirling numbers of the second kind, with value zero if the lower index is greater than the upper index. Define the formal power series
\[
\mathscr F(u,v,t;\alpha,\beta,\rho,\sigma)
=\exp\!\left[\alpha u+\beta v+
\sum_{p,q\ge1}\frac{u^pv^qt^{p+q-1}}{p!q!}
\left((T_{p,q}-U_{p,q}-V_{p,q})\rho\sigma
+V_{p,q}\rho+U_{p,q}\sigma\right)\right].
\]
For any selector \(z\) among \(\alpha,\beta,\rho,\sigma\), write \(\Delta_z\mathscr F=\mathscr F|_{z=1}-\mathscr F|_{z=0}\), with all selectors not mentioned in a difference evaluated at \(1\). Put
\[
\mathscr G=(\Delta_\alpha\Delta_\sigma+\Delta_\beta\Delta_\rho
-\Delta_\alpha\Delta_\beta\Delta_\rho\Delta_\sigma)\mathscr F.
\]
Then, for every \(m,n\ge1\), the **complete** zero-forcing polynomial is
\[
\boxed{\mathcal Z(R_{m,n};x)=x^{mn}\left(1+m!n![u^mv^n]\mathscr G(u,v,x^{-1})\right).}
\]
All coefficient extractions are finite for fixed \(m,n\); the term \(1\) accounts for the all-blue initial set.

For \(m,n\ge2\), the smallest forcing-set cardinality is the previously known value \(mn-m-n+2\). The **number of minimum forcing sets** is exactly
\[
\boxed{\begin{aligned}
N_{m,n}={}&m(m-1)^{n-1}\left(n^{m-2}-n!\left\{\!\begin{matrix}m-2\\n\end{matrix}\!\right\}\right)\\
&+n(n-1)^{m-1}\left(m^{n-2}-m!\left\{\!\begin{matrix}n-2\\m\end{matrix}\!\right\}\right).
\end{aligned}}
\]
When \(\min(m,n)=1\), the rook graph is complete, with \(\mathcal Z(R_{m,n};x)=x^{mn}+mn\,x^{mn-1}\) if \(mn\ge2\), and \(\mathcal Z(R_{1,1};x)=x\).

## Assumptions and scope

All graphs are finite, undirected and simple. Ordinary zero forcing means that a blue vertex having **exactly one** white neighbor may recolor that neighbor blue; a set is zero forcing if a sequence of such steps recolors every vertex. Isolated row and column vertices are retained in \(H_B\), even when they have no white incident cells. The zero-forcing polynomial counts labeled vertex subsets, not orbits under board symmetries. Formal power series and Stirling numbers are interpreted over the rational numbers, and no convergence assumption is needed. The variable \(t\) counts initially white cells; \(x\) counts initially blue cells.

## Proof

**1. Local forcing move.** Regard a board cell \((a,c)\) as an edge joining row label \(a\) to column label \(c\). A currently blue cell corresponds to an edge absent from the currently white bipartite graph \(H\). Its number of white rook-neighbors is exactly \(d_H(a)+d_H(c)\): white cells in the given row and column are disjoint. It can force if and only if one of these degrees is \(0\) and the other is \(1\). Consequently, if \(H\) has any white edge, the existence of a first force is equivalent to a row isolate together with a column leaf, or a column isolate together with a row leaf. Recoloring removes the unique white edge incident to the leaf.

**2. Cycle obstruction.** Suppose \(H\) contains a cycle, and consider a hypothetical first time when a white edge of that cycle is recolored. Immediately before that time, every cycle edge remains white. Each endpoint of the target edge has at least two incident white cycle edges. Any blue cell adjacent to the target edge shares one endpoint with it and therefore has at least two white rook-neighbors. Thus no such first recoloring can occur; a white cycle is an invariant obstruction. Every successful nonempty white configuration is therefore a forest with the first-force condition of step 1.

**3. Sufficiency.** Suppose \(H\) is a nonempty forest with, for example, an isolated row \(a\) and a column leaf \(c\) incident to a white edge \(bc\). The cell \((a,c)\), currently blue, forces \((b,c)\). After this step, row \(a\) remains isolated and column \(c\) becomes isolated; hence there is an isolate on **each** side. While a white edge remains, the remaining forest has a leaf on one side. Pair that leaf with an isolate on the opposite side to force its unique incident white edge. This removes an edge and preserves both existing isolates. Induction on the number of white edges completes the forcing process. The case of no initial white edges is immediate. This proves the characterization for all \(m,n\ge1\).

**4. Tree components and the polynomial.** A nontrivial connected component of a bipartite forest contains \(p\ge1\) row labels, \(q\ge1\) column labels and exactly \(p+q-1\) edges. The classical two-word bipartite Prüfer encoding gives \(T_{p,q}=p^{q-1}q^{p-1}\) labeled bipartite spanning trees. Its row-degrees are one plus the occurrence counts of row labels in a word of length \(q-1\); similarly the column-degrees use a word of length \(p-1\). Thus there are precisely \(U_{p,q}\) trees **without any row leaf**, and precisely \(V_{p,q}\) trees **without any column leaf**, as the relevant words must be surjective. A tree has at least two leaves, so these two exceptional classes are disjoint. Hence \(T-U-V\) components have leaves on both sides, \(V\) have row leaves only, and \(U\) have column leaves only. Isolated vertices make the singleton components \(\alpha u\) and \(\beta v\). The labeled two-sort exponential formula now gives \(\mathscr F\) as written, where selectors record *existence* of isolates and leaves by evaluation at \(0\) or \(1\). Inclusion–exclusion for the union of the row-isolate/column-leaf and column-isolate/row-leaf conditions gives \(\mathscr G\). Multiplying the coefficient for \(e\) white edges by \(x^{mn-e}\) and adding the zero-white configuration yields the displayed zero-forcing polynomial.

**5. Minimum-set multiplicity.** Suppose \(m,n\ge2\). Every nonempty successful white forest has at least one isolated vertex, so it has at most \(m+n-2\) edges. This bound is attained, for example, by isolating one row and taking a spanning tree on the remaining \(m-1\) rows and all \(n\) columns with at least one column leaf. Thus the smallest blue set has size \(mn-m-n+2\), in agreement with the known cardinality result. A successful white forest with \(m+n-2\) edges has exactly two components: a single isolated vertex and one spanning tree on the other \(m+n-1\) vertices. When the isolated vertex is a row, that tree must have a column leaf. There are \(m\) choices of the isolated row and
\[
(m-1)^{n-1}\left(n^{m-2}-n!\left\{\!\begin{matrix}m-2\\n\end{matrix}\!\right\}\right)
\]
allowed labeled trees, by subtracting the trees without column leaves from the bipartite Prüfer count. Interchanging rows and columns gives the second term in \(N_{m,n}\). The cases are disjoint. If a side has only one label, the graph is a clique and its polynomial is the stated elementary formula. This completes the proof.

## Verification

The standalone, standard-library Python program `verify.py` checks a direct rook-graph forcing simulation against an independently implemented bipartite cycle/leaf criterion for every initial coloring of the boards \(1\times1\), \(1\times2\), \(1\times4\), \(2\times2\), \(2\times3\), \(2\times4\), \(3\times3\), \(3\times4\), and \(4\times4\), totaling **70,502** initial colorings. A separate anchored-component recursion implementing the labeled-forest formula matches every coefficient on the same boards. Direct enumeration of **5,140** bipartite spanning-tree instances verifies the bipartite Prüfer and leaf-exclusion counts for all part sizes at most four. The minimum-set expression is additionally checked against component enumeration at **25** parameter pairs with \(2\le m,n\le6\). Run `python3 verify.py`; `verification_output.txt` records the resulting output. These finite tests corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips and Reinhart introduced the ordinary zero-forcing polynomial in 2018, and determined several extremal coefficients and special graph-family formulas. Montazeri and Soltankhah determined the \(k\)-forcing number of rectangular rook graphs in their 2021 paper: specializing their Theorem 2.1 to \(k=1\) gives the already-known minimum cardinality \(mn-m-n+2\) for \(m,n\ge2\). Neither finding is claimed here. The refinement established here is the **if-and-only-if description of every initially forcing subset**, together with the entire cardinality generating polynomial and the multiplicity of smallest subsets. Related papers by the latter authors discuss zero forcing and path covers, and further Cartesian products; their possible implications beyond the inspected sources remain a literature-comparison limitation.

## Limitations

The result applies only to ordinary zero forcing of rook graphs, not automatically to skew forcing, positive-semidefinite forcing, or arbitrary Cartesian products. The bivariate exponential identity is an exact formal finite-coefficient specification, not a claim of an asymptotically optimal algorithm. An unexamined equivalent enumeration in another literature terminology, or a relevant inaccessible article, could affect originality; no exhaustive global priority claim is asserted. The proof, not the finite verifier, establishes the all-size theorem.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, publicly posted 2018-01-26. https://arxiv.org/abs/1801.08910.
2. Z. Montazeri and N. Soltankhah, *k-Forcing number for Cartesian product of some graphs*, **Contributions to Discrete Mathematics** 16 (2021), 89–97, Theorem 2.1; DOI:10.55016/ojs/cdm.v16i1.68557. https://cdm.ucalgary.ca/article/download/68557/54771/215214.
3. Z. Montazeri and N. Soltankhah, *On the relationship between the zero forcing number and path cover number for some graphs*, **Bulletin of the Iranian Mathematical Society** 46 (2020), 767–776; DOI:10.1007/s41980-019-00290-8 (bibliographic and abstract inspection only).
4. Z. Montazeri and N. Soltankhah, *Zero forcing number for Cartesian product of some graphs*, **Communications in Combinatorics and Optimization** 9 (2024), 635–646; DOI:10.22049/cco.2023.28177.1471 (bibliographic inspection only; full text not accessed).
