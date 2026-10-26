# Inclusion-minimal total domination of direct products of complete graphs

## Finding

Let \(2\le p\le q\) be integers and let \(G_{p,q}=K_p\times K_q\) denote the **categorical (direct/tensor) product**. Its vertices are the cells \((i,j)\in[p]\times[q]\); two cells are adjacent if and only if both coordinates differ. A total dominating set \(S\subseteq V(G_{p,q})\) gives every vertex, including each vertex in \(S\), at least one neighbor in \(S\). It is inclusion-minimal if no proper subset remains total dominating. Write

\[
M_{p,q}(z)=\sum_{S\text{ inclusion-minimal total dominating}}z^{|S|}.
\]

**Theorem.** For all integers \(2\le p\le q\),

\[
M_{p,q}(z)=
\begin{cases}
\left(\binom{q}{2}\right)^2 z^4,&p=2,\\[2mm]
6\binom{p}{3}\binom{q}{3}z^3+
\left(\binom{p}{2}\left(\binom{q}{2}\right)^2+\binom{q}{2}\left(\binom{p}{2}\right)^2-\binom{p}{2}\binom{q}{2}\right)z^4,&p\ge3.
\end{cases}
\]

For \(p\ge3\), the inclusion-minimal sets are **exactly** three kinds:

1. Three cells in three distinct rows and three distinct columns (a size-three matching in the incidence bipartite graph).
2. Four cells supported in exactly two rows, with exactly two selected cells in each of those rows.
3. Four cells supported in exactly two columns, with exactly two selected cells in each of those columns.

Kinds 2 and 3 overlap exactly on full two-by-two subrectangles. For \(p=2\), only kind 2 exists. In particular, the minimum and upper total domination numbers are

\[
(\gamma_t(G_{p,q}),\Gamma_t(G_{p,q}))=
\begin{cases}(4,4),&p=2,\\
(3,4),&p\ge3.\end{cases}
\]

Hence \(K_p\times K_q\) is well-totally-dominated if and only if \(\min(p,q)=2\), and the upper total domination number equals \(4\) for **all** \(p,q\ge2\). The last statement resolves the \(k=1\) specialization of Kazemi's general upper \(k\)-tuple total domination question (Question 1 in arXiv:1603.02428); it does not resolve \(k>1\).

## Assumptions and scope

All graphs are finite, simple and undirected. The product is categorical, **not** Cartesian or strong. Both factors contain at least two vertices; the product with \(p=q=2\) is two disjoint copies of \(K_2\), and is included. All vertex subsets and combinatorial counts are labeled, without quotienting by row permutations or graph automorphisms. A total dominating set is evaluated with **open** neighborhoods (selected vertices must themselves have selected neighbors). The polynomial counts *inclusion-minimal* total dominating sets only, not all total dominating sets or minimal ordinary (closed-neighborhood) dominating sets. The coefficient of \(z^j\) counts sets of exactly \(j\) vertices.

## Proof

**Step 1: translate to a bipartite edge set.** Identify the cell \((i,j)\) with the edge joining row vertex \(r_i\) and column vertex \(c_j\) of the complete bipartite incidence graph \(K_{p,q}\). Let \(F\) be the set of edges corresponding to \(S\). The open neighborhood of cell \((i,j)\) consists exactly of cells whose row is not \(i\) and whose column is not \(j\). Consequently \(S\) is total dominating if and only if, for every \((i,j)\), at least one edge of \(F\) avoids both \(r_i\) and \(c_j\). Equivalently,

\[
F\not\subseteq\operatorname{star}(r_i)\cup\operatorname{star}(c_j)
\quad\text{for every }i\in[p],j\in[q].\tag{1}
\]

Thus the failure obstruction is *a mixed row--column vertex cover* of \(F\). This characterization includes the need to dominate selected cells themselves.

**Step 2: selected cells with a three-edge matching.** If \(F\) contains three pairwise disjoint incidence edges, then the three selected cells have distinct rows and columns. Any board cell disagrees in both coordinates with at least one of these three cells: at most one selected cell can share its row and at most one can share its column, so a third avoids both. Therefore that three-cell set is total dominating. Any of its two-cell subsets fails: if two selected cells lie in rows \(a,b\) and columns \(c,d\), the mixed pair \((a,d)\) yields a mixed cover, as in (1). Hence every three-cell matching is inclusion-minimal. An inclusion-minimal total dominating set containing such a matching must coincide with it.

**Step 3: selected cells without a three-edge matching.** Suppose \(F\) has no matching of size three. By Kőnig's bipartite matching--vertex-cover theorem, the minimum vertex-cover size of \(F\) is at most two. A cover of size one immediately implies a mixed cover, contrary to (1); a two-vertex cover with one row and one column likewise violates (1). Therefore every total dominating \(F\) without a three-edge matching is covered by two **rows** or by two **columns**. These covers may be chosen with exactly two elements even if they are not minimum; one-element covers have already been ruled out.

If \(F\) lies in the union of rows \(a,b\), condition (1) is equivalent to both rows containing at least two edges with distinct column endpoints. Indeed, if row \(b\) contains no edge or only the edge in column \(j\), then all edges are in row \(a\) or column \(j\), contradicting (1), and similarly with \(a,b\) exchanged. Conversely, if both rows contain at least two edges in distinct columns, deleting either row together with any one column still leaves an edge in the other row; a mixed cover involving some third row also cannot cover all four or more edges. Hence the condition is sufficient.

Such an \(F\) is inclusion-minimal if and only if it contains **exactly two** edges in each of the two rows: selecting more than two in either row permits an edge to be removed while the condition remains satisfied, whereas removing any edge from a two-plus-two selection leaves only one in a row and violates (1). The identical argument with rows and columns reversed yields kind 3. Because all selected cells lie in two rows, and both rows have two selected cells, an inclusion-minimal set of kind 2 cannot contain any matching of size three, so no missing cases arise. For \(p=2\) only two-row support is possible and the argument gives all minimal sets.

**Step 4: count without double counting.** For kind 1, choose three rows and three columns and biject them: \(\binom{p}{3}\binom{q}{3}\cdot3!\) sets. For kind 2, choose two rows, then independently choose two columns in each: \(\binom{p}{2}\left(\binom{q}{2}\right)^2\) sets. For kind 3, exchange rows and columns: \(\binom{q}{2}\left(\binom{p}{2}\right)^2\) sets. A set in both kinds 2 and 3 uses two rows and two columns and has four cells, so it is exactly the full \(2\times2\) rectangle, counted once per \(\binom{p}{2}\binom{q}{2}\) choices. Subtract this intersection. When \(p=2\), the four-cell rows-only sets number \(\left(\binom{q}{2}\right)^2\). This proves the polynomial.

For \(p\ge3\) the three-cell matching exists and the four-cell constructions exist. Thus both degrees occur, giving \(\gamma_t=3\) and \(\Gamma_t=4\). When \(p=2\), every minimal set has four cells, giving both parameters equal to four and the stated well-totally-dominated classification. The upper value \(4\) for \(p\ge3\) supplies the \(k=1\) instance of the cited question. \(\square\)

## Verification

The standalone Python 3 program `check_minimal_total.py` uses only the standard library. Run `python3 check_minimal_total.py`. It enumerates **all vertex subsets** and determines total domination directly from adjacency (different row and column), then checks inclusion-minimality by deleting each selected vertex and retesting the original condition. It compares the resulting coefficient dictionary against the theorem for eleven parameter pairs: \((2,2),(2,3),\ldots,(2,7),(3,3),(3,4),(3,5),(3,6),(4,4)\). All eleven exhaustive checks passed. Representative dictionaries were \(\{3:6,4:45\}\) for \((3,3)\), \(\{3:24,4:144\}\) for \((3,4)\), and \(\{3:96,4:396\}\) for \((4,4)\). These checks support the characterization for finite instances but are not an infinite proof; Steps 1--4 provide that proof.

## Relationship to prior work

Henning--Kazemi (2012) already determine the **minimum** \(k\)-tuple total domination number for products of two complete graphs, including the known \(\gamma_t=3\) case for both factors of size at least three. The minimum value alone does not determine the **inclusion-minimal census** or the upper parameter. Kazemi (arXiv:1603.02428; first posted 2016) defines upper \(k\)-tuple total domination, establishes the \(K_n\times K_2\) case, and explicitly asks whether the corresponding bound holds for general products of complete graphs. The theorem here proves its \(k=1\) case without claiming any solution for larger \(k\).

Bahadır--Ekim--Gözüpek (arXiv:2010.02341; first posted 2020-10-05) study well-totally-dominated graphs, and Burcroff--O'Brien (arXiv:2110.00709; first posted 2021-10-02), Section 5.1, study **ordinary domination** polynomials of direct products of complete graphs. An ordinary domination polynomial counts all *closed-neighborhood* dominating sets and does not imply this polynomial for **inclusion-minimal open-neighborhood** total dominating sets. Their respective definitions and product-specific results provide the 2020--2021 literature context for the present refined census. Burcroff (arXiv:2008.03887) studies paired domination and ordinary upper domination in direct products; these are also distinct invariants.

## Limitations

The characterization is specific to **two** complete-graph factors and does not extend without additional work to products of three or more factors, noncomplete factors, or \(k\)-tuple total domination for \(k>1\). No exact enumeration of *all nonminimal* total dominating sets is asserted. Although accessible source texts and indexed mathematical records were compared, unindexed papers and alternative formulations could contain prior equivalent results; mathematical originality is therefore subject to residual literature-priority risk. Verification is exhaustive only for the eleven finite test graphs stated above. No independent validation or external audit is claimed.

## References

1. S. Bahadır, T. Ekim and D. Gözüpek, *Well-Totally-Dominated Graphs*, arXiv:2010.02341 (2020), https://arxiv.org/abs/2010.02341.
2. A. Burcroff and G. O'Brien, *Unimodality and monotonic portions of certain domination polynomials*, arXiv:2110.00709 (2021), Section 5.1, https://arxiv.org/html/2110.00709v1.
3. M. A. Henning and A. P. Kazemi, *k-tuple total domination in cross products of graphs*, Journal of Combinatorial Optimization 24 (2012), 339--346, https://doi.org/10.1007/s10878-011-9389-z.
4. A. P. Kazemi, *Upper k-tuple total domination in graphs*, arXiv:1603.02428, Section 5, Proposition 7 and Question 1, https://arxiv.org/pdf/1603.02428.
5. A. Burcroff, *Tightness of paired and upper domination inequalities for direct product graphs*, arXiv:2008.03887 (2020), https://arxiv.org/abs/2008.03887.
