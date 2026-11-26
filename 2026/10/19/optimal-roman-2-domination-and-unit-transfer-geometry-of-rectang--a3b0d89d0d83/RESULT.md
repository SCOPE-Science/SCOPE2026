# Unit-transfer geometry of optimal Roman \(\{2\}\)-dominating functions on rectangular rook graphs

## Finding

For integers \(2\le m\le n\), let \(R_{m,n}=K_m\square K_n\) be the graph of an \(m\)-row, \(n\)-column rectangular board: two cells are adjacent precisely when they share a row or a column. A Roman \(\{2\}\)-dominating (Italian dominating) function is a map \(f:V(R_{m,n})\to\{0,1,2\}\) with \(\sum_{u\sim v}f(u)\ge2\) whenever \(f(v)=0\). Its weight is \(w(f)=\sum_vf(v)\).

**Known optimum families.** The exact minimum, optimizer classification and counts were given in *Minimum Italian domination on rook graphs: exact optimizers and a sharp transition* [6]. We recall them to specify the vertex sets of the reconfiguration graphs; these facts are not claimed as contributions here. The minimum weight is
\[
\gamma_{\{R2\}}(R_{m,n})=\min\{n,2m\}.
\]
Define family \(\mathcal A\) to consist of zero-one arrays having exactly one \(1\) in every column and at least one \(1\) in every row. Define family \(\mathcal B\) to consist of arrays with total label-weight exactly \(2\) in every row (one label \(2\), or two labels \(1\)). The entire collection of minimum functions is
\[
\mathcal M_{m,n}=
\begin{cases}
\mathcal A,&n<2m,\\
\mathcal A\cup\mathcal B,&n=2m,\\
\mathcal B,&n>2m.
\end{cases}
\]
In particular, with \(S(n,m)\) denoting a Stirling number of the second kind,
\[
A_{m,n}=|\mathcal A|=m!S(n,m)
 =\sum_{j=0}^m(-1)^j\binom mj(m-j)^n,\qquad
B_{m,n}=|\mathcal B|=\binom{n+1}{2}^{m}.
\]
Consequently \(|\mathcal M_{m,n}|=A_{m,n}\) if \(n<2m\), \(B_{m,n}\) if \(n>2m\), and
\[
|\mathcal M_{m,2m}|=A_{m,2m}+B_{m,2m}
-\frac{(2m)!}{2^m}.
\]

**Unit-transfer theorem.** Regard the vertex labels as fixed. The *unit-transfer graph* \(\mathcal U_{m,n}\) has vertex set \(\mathcal M_{m,n}\). Two arrays are adjacent if a single unit is removed from one cell carrying a positive label and deposited at one *different* cell carrying less than two units, with the new array again Roman \(\{2\}\)-dominating and of minimum weight. The transfer need not follow an edge of the underlying rook graph.

The graph \(\mathcal U_{m,m}\) consists of precisely \(m!\) isolated vertices. For every \(n>m\), the graph \(\mathcal U_{m,n}\) is connected. In the regime \(n>2m\), it is the \(m\)-fold Cartesian power of the multiset-pair graph \(T_n\): its vertices are size-two multisets drawn from \([n]\), and adjacency moves one occurrence of a symbol to another symbol. This supplies
\[
\operatorname{rad}(\mathcal U_{m,n})
=\operatorname{diam}(\mathcal U_{m,n})=2m,\qquad n>2m,
\]
and the exact degree distribution
\[
\#\{f\in\mathcal M_{m,n}:\deg_{\mathcal U_{m,n}}(f)
=(n-1)(m+k)\}
=\binom mk\, n^{m-k}\binom n2^{k},
\quad 0\le k\le m.
\]
Here the index \(k\) is the number of rows containing two distinct label-\(1\) cells, rather than one label-\(2\) cell.

## Assumptions and scope

All indices and labels are distinguished; no quotient by row/column permutations or by any other graph automorphism is taken. The integer parameters satisfy \(2\le m\le n\). The domination condition constrains only the zero-labeled vertices. A unit transfer is a single simultaneous change of the form \(-1\) at one cell and \(+1\) at a different cell, subject to label bounds and feasibility. It is not token sliding along edges.

The graph \(T_n\) has vertices \(\{a,b\}\) where repetition is permitted, and an edge means replacement of one occurrence of \(a\) or \(b\) by a different value, respecting multiplicity two.

## Proof

Write \(r_i=\sum_{j=1}^n f(i,j)\) for the weight in row \(i\), and \(c_j=\sum_{i=1}^m f(i,j)\) for the weight in column \(j\). At a zero cell \((i,j)\), the neighborhood-weight condition simplifies exactly to
\[
r_i+c_j\ge2,
\]
because the row and column neighborhoods are disjoint and \(f(i,j)=0\).

**Recap of the optimum classification [6].** If some column \(j\) has \(c_j=0\), then every cell of that column is zero, whence \(r_i\ge2\) for each row \(i\). Thus \(w(f)\ge2m\). Otherwise every column has positive weight, giving \(w(f)\ge n\). Therefore \(w(f)\ge\min\{n,2m\}\).

Each family supplies feasible functions. In \(\mathcal A\), every row has positive weight and every column has weight \(1\), so at each zero cell \(r_i+c_j\ge2\); its total weight is \(n\). In \(\mathcal B\), every row has weight \(2\), and at each zero cell \(r_i+c_j\ge2\); its total weight is \(2m\). The claimed minimum follows.

When \(n<2m\), a minimum function has weight \(n\) and cannot have an empty column; consequently each column has weight exactly \(1\), and nonempty rows are necessary by the zero-cell condition. Thus the minima are exactly \(\mathcal A\). When \(n>2m\), every weight-\(2m\) minimum must have an empty column; otherwise its weight would be at least \(n>2m\). The bound from the empty column forces every row to have weight \(2\), precisely \(\mathcal B\). When \(n=2m\), the alternatives partition minima into \(\mathcal A\) and \(\mathcal B\) in the same way.

The family \(\mathcal A\) is exactly the set of onto maps from the set of labeled columns to the set of labeled rows. Inclusion-exclusion gives \(A_{m,n}\). Every row of \(\mathcal B\) independently chooses a multiset of two columns, hence \(B_{m,n}\). At equality \(n=2m\), the intersection \(\mathcal A\cap\mathcal B\) consists of column-to-row maps with precisely two columns mapped to each row, counted by \((2m)!/(2!)^m\). Inclusion-exclusion for the union yields the stated count.

**Reconfiguration when \(n=m\).** Every minimum has one \(1\) in each row and column. It is a permutation matrix. Any unit transfer changes this configuration and would require some row or column to be left empty (or a column to have weight \(2\)); by the just-proved structural classification no different minimum can result. There are \(m!\) isolated matrices.

**Connectivity of \(\mathcal A\) for \(n>m\).** In a column with a single unit, moving that unit to another row is a valid one-unit move precisely when the donor row will remain nonempty. Thus the induced graph on \(\mathcal A\) is the graph of onto maps under recoloring one column without vacating its former row.

Take two onto maps. First move columns from rows exceeding their desired target cardinalities to rows with cardinalities below target; each donor has at least two columns because every desired cardinality is at least one. Now row cardinalities agree with the target. It remains to permute the labeled columns between row classes. Such permutations are products of transpositions between two different rows.

If at least one of the two rows has two or more columns, the swap can be executed in two valid single-column recolorings: temporarily move one column to the other row and then move the other column back. If both rows are singleton, the condition \(n>m\) guarantees a third row with at least two columns. Move a reserve column from that row into the first singleton row, swap the desired singleton columns using two further recolorings, and return the reserve to its original row (four moves total). Every intermediate row is nonempty. Thus all onto maps are connected.

**Connectivity of \(\mathcal B\), and of the critical union.** Two rows of a state in \(\mathcal B\) each have weight \(2\). Reallocate weight within one row by transferring one unit from a positive cell to another cell. Such moves keep every row at weight \(2\), and the elementary multiset-pair graph \(T_n\) is connected. Therefore the induced graph on \(\mathcal B\) is connected.

When \(n=2m\), \(\mathcal A\cap\mathcal B\neq\varnothing\), since the labeled columns can be paired into \(m\) distinct rows. The two connected induced subgraphs thus share vertices, and their union \(\mathcal U_{m,2m}\) is connected. For \(m<n<2m\), \(\mathcal U_{m,n}\) is exactly the connected onto-map graph, and for \(n>2m\) it is exactly the connected graph on \(\mathcal B\). This proves the asserted connectivity dichotomy.

**Cartesian decomposition and exact metric for \(n>2m\).** In this regime every minimum has exactly two units in every row and at least one empty column (since the total weight is \(2m<n\)). Any one-unit transfer between different rows leaves one row with weight \(1\), which is impossible for a minimum because the empty-column lower-bound argument forces every row weight to be at least \(2\). Conversely every one-unit transfer inside a row retains feasibility. Hence
\[
\mathcal U_{m,n}\cong T_n\square\cdots\square T_n
\]
with \(m\) factors.

In \(T_n\), distance equals half of the \(\ell_1\) distance between the length-\(n\) multiplicity vectors of two size-two multisets; this number is at most \(2\). For \(n>2m\ge4\), hence \(n\ge5\), every multiset has a disjoint-support target, so its eccentricity is \(2\). Distances add under Cartesian products, making every vertex eccentricity \(2m\).

A repeated-symbol multiset \(\{a,a\}\) has exactly \(n-1\) neighbors; a distinct-symbol multiset \(\{a,b\}\) has \(2(n-1)\). If exactly \(k\) of the \(m\) rows use distinct columns, the graph degree is \((n-1)(m+k)\), with \(\binom mk n^{m-k}\binom n2^k\) such arrays. This finishes all claims.

## Verification

Two independent finite programs are included as source files: `italian_rook_check1.py` and `italian_rook_check2.py`. Both require only the Python standard library.

`italian_rook_check1.py` enumerates all \(\{0,1,2\}\)-arrays of weight below and at the asserted minimum, checks the Italian condition by direct row/column-neighbor summation, and constructs actual one-unit-transfer neighbors. It exhaustively verifies the classification and connected-component dichotomy for \(2\le m\le4\) over the documented test cases through \(n=7\).

`italian_rook_check2.py` independently constructs every rowwise multiset configuration in selected \(n>2m\) cases, verifies the neighborhood inequalities and full degree distributions, and independently counts the two families and their intersection at the critical boundary for \(m=2,3,4\).

Outputs of actual execution are provided in `italian_rook_check1.out` and `italian_rook_check2.out`. These finite checks corroborate, but do not replace, the all-parameter argument above.

## Relationship to prior work

Chellali, Haynes, Hedetniemi and McRae introduced Roman \(\{2\}\)-domination and studied bounds, complexity and its relation to rainbow domination. Klostermeyer and MacGillivray subsequently developed relationships between Roman, Italian and ordinary two-domination. Reference [6] gives the complete minimum-weight classification and exact counts for rectangular rook graphs, including the critical intersection at \(n=2m\). It determines the state sets used here, but does not analyze one-unit-transfer connectivity or distances.

Varghese and Lakshmanan studied **perfect** Italian domination, which requires neighborhood weight *exactly* \(2\) at a zero, rather than *at least* \(2\). For example the ordinary minimum on \(K_3\square K_4\) is \(4\), while their perfect variant has minimum \(6\) (Theorem 2.4). Davila and Krop distinguish Roman \(\{k\}\)-domination, which constrains only zeros, from \(\{k\}\)-domination, which requires the closed-neighborhood bound at every vertex; their general Cartesian product bounds do not address unit transfers.

The contribution is the exact connectivity threshold under unrestricted transfers, the product description for \(n>2m\), and the resulting metric and degree formulas. The connectivity argument supplies explicit legal paths within the onto-map family and at the critical union; these are not furnished by merely listing the optimum labelings.

## Limitations

This theorem applies only to \(2\le m\le n\) complete-graph Cartesian products and to the **unrestricted-cell** unit transfer defined above; it does not describe edge-adjacent token slides, general Cartesian products, or shortest paths in the critical regime.

The proof and the finite test files have been checked within a single mathematical review. No independent external validation or publication-priority determination has been conducted. The complete text of the original 2016 foundational paper and of the 2019 comparative paper could not be inspected; equivalent information in unavailable full texts or computational tables remains a residual originality risk. The 2016-05-11 date identifies a verifiable dated public bibliographic record for the original Roman \(\{2\}\)-domination article, not a claim that no earlier online-first version existed.

## References

1. M. Chellali, T. W. Haynes, S. T. Hedetniemi and A. A. McRae, *Roman \(\{2\}\)-domination*, Discrete Applied Mathematics 204 (2016), 22–28, DOI: 10.1016/j.dam.2015.11.013.
2. W. F. Klostermeyer and G. MacGillivray, *Roman, Italian, and 2-Domination*, Journal of Combinatorial Mathematics and Combinatorial Computing 108 (2019), 125–146.
3. J. Varghese and A. Lakshmanan S., *Perfect Italian Domination Number of Graphs*, Palestine Journal of Mathematics 12(1) (2023), 158–168; earlier public preprint arXiv:1910.12260.
4. R. Davila and E. Krop, *On a Vizing-type integer domination conjecture*, arXiv:1708.01656 (2017).
5. A. Almulhim, A. D. Akwu and B. AlSubaiei, *Survey on Roman \(\{2\}\)-Domination*, Mathematics 12 (2024), 2771.
6. *Minimum Italian domination on rook graphs: exact optimizers and a sharp transition*, [published record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-minimum-italian-domination-on-rook-graphs-exact-optimizers-and-a--73393dbef1b4), Finding and proof of the optimizer classification.
