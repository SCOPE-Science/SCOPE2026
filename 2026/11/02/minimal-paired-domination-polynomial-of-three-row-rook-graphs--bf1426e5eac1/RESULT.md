# Minimal paired-domination polynomial of three-row rook graphs

## Finding

For every integer \(n\ge3\), let \(G_n=K_3\square K_n\), the rook graph on a three-row board with \(n\) columns. Write \(M_n(z)\) for the generating polynomial of inclusion-minimal paired-dominating vertex subsets, each counted once and weighted by its size. Then

\[
M_n(z)=\frac{3n(n-1)(n+2)}2z^4+\binom n2\binom{n-2}2\binom{n-4}2z^6+\begin{cases}3(2^{n-1}-1)z^n,&n\text{ even},\\3n2^{n-1}z^{n+1},&n\text{ odd}.\end{cases}
\]

The second coefficient is understood to be zero when \(n<6\), and coincident exponents are combined. Consequently, for \(n=3,4\) the size support is \(\{4\}\), for \(n=5,6\) it is \(\{4,6\}\), and for every \(n\ge7\) it is precisely \(\{4,6,2\lceil n/2\rceil\}\). Thus the largest inclusion-minimal paired-dominating set has size \(2\lceil n/2\rceil\), and the number of unattainable even sizes between six and that maximum is unbounded. For example, \(M_7(z)=567z^4+630z^6+1344z^8\).

## Assumptions and scope

All graphs are finite and simple. Vertices of \(G_n\) are pairs \((r,c)\) with \(r\in\{1,2,3\}\) and \(c\in\{1,\ldots,n\}\); two distinct vertices are adjacent when they share a row or a column. A paired-dominating set \(S\) is a dominating vertex set for which \(G_n[S]\) admits a perfect matching. It is inclusion-minimal if **no proper subset** is paired-dominating, not merely if no one-vertex deletion is paired-dominating. Every paired-dominating set has even cardinality. Its upper paired-domination number is the maximum cardinality among inclusion-minimal paired-dominating sets. This theorem concerns the entire polynomial, not the polynomial of all paired-dominating sets.

## Proof

**Domination dichotomy.** A vertex \((r,c)\) outside \(S\) is dominated exactly when row \(r\) or column \(c\) contains a selected vertex. Therefore \(S\) dominates if and only if either all three rows are represented in \(S\), or all \(n\) columns are represented. The reverse implication is immediate; if a row and a column were both empty, their intersection would be undominated.

**Case I: all three rows are represented.** Let \(S\) be inclusion-minimal and choose any perfect matching \(T\) in \(G_n[S]\). Select at most three matching edges with endpoints meeting all three rows. Such a selection always exists because every row contains a matched vertex. Its endpoints still dominate by the row criterion and have a perfect matching. If \(|S|>6\), this proper subset contradicts minimality. Hence \(|S|=4\) or \(|S|=6\). No two-vertex set dominates when \(n\ge3\), since it can neither occupy all rows nor all columns.

If \(|S|=4\), exactly one row contains two selected cells and the other rows have one each. Either the singleton rows lie in the same column, so they can match vertically while the doubled row matches horizontally, or the singleton rows lie in different columns, in which case each must match vertically to a cell of the doubled row. In the latter case the two singleton columns must be exactly the two columns used by the doubled row. Both patterns give a perfect matching, and all such four-sets are minimal because no two vertices dominate. Choose the doubled row in three ways and its unordered pair of columns in \(\binom n2\) ways. For each fixed pair of doubled-row columns, the singletons have \(n\) choices of a common column (possibly one of the fixed two), or exactly two assignments of the fixed columns to their two labeled rows. This gives \(3\binom n2(n+2)=3n(n-1)(n+2)/2\) sets.

If \(|S|=6\), no perfect matching can have an edge joining two distinct rows. Indeed, such an edge covers two rows; among the remaining matching edges, some edge meets the third row, so these two matching edges provide a proper four-vertex paired-dominating subset. Thus every perfect matching is within rows, so the three positive row sizes must all be even, hence exactly two vertices per row. Also, no column may occur in two rows: such a vertical edge together with the horizontal edge joining the third row's two selected cells would form a proper four-set that dominates. Conversely, any selection of two vertices in each row with all six selected columns distinct has a perfect matching entirely within rows. Every proper paired-dominating subset meeting all three rows would need at least two from each row, since no cross-row edges exist inside \(S\). A proper subset cannot occupy all columns either: if \(n>6\) even \(S\) does not, and if \(n=6\) deleting any selected vertex vacates its column. Thus these are precisely the six-sets of Case I. They number \(\binom n2\binom{n-2}2\binom{n-4}2\), with no possibilities for \(n<6\).

**Case II: at least one row is empty.** By the domination dichotomy, every column is occupied. At most two rows are used. Let \(t\) count columns containing two selected vertices. Then \(|S|=n+t\), so \(t\) has the parity of \(n\). Suppose \(t\ge2\), and select two distinct doubled columns. Because total size is even, the occupancies of the two used rows have the same parity. If both are even, remove two vertices of one row from the two doubled columns; the remaining row counts are even and the remaining vertices can be perfectly matched horizontally within each row. If both are odd, remove one vertex from each row, one in each of two doubled columns; again both remaining counts are even and can be matched horizontally. Every column remains occupied. Thus a proper paired-dominating subset exists, contrary to minimality. Therefore \(t=0\) when \(n\) is even and \(t=1\) when \(n\) is odd.

For even \(n\), the \(t=0\) sets comprise one vertex per column in at most two rows; a perfect matching exists exactly when both row occupancies are even. Such a set is minimal: any proper subset loses a represented column, and it never represents all three rows. For each specified empty row, there are \(2^{n-1}\) even-even binary assignments. Every one-row selection is counted twice among the three choices of empty row; there are exactly three such selections. Hence their distinct count is \(3(2^{n-1}-1)\), each of size \(n\).

For odd \(n\), exactly one column is doubled and the remaining \(n-1\) columns each contain one selected vertex. Both occupied row cardinalities have the same parity. If even, a horizontal matching exists; if odd, match the two vertices in the doubled column vertically and match all remaining vertices horizontally. Thus every such selection is paired-dominating. Every proper subset with even size loses at least two vertices, so cannot continue to occupy all \(n\) columns, and no subset occupies all three rows; hence it is minimal. There are three choices for the empty row, \(n\) for the doubled column and \(2^{n-1}\) assignments for the others, totaling \(3n2^{n-1}\) sets of size \(n+1\). These sets all use two rows, so no overcount occurs.

Cases I and II are disjoint and exhaustive. Adding their coefficients proves the polynomial. For \(n\ge7\), the three displayed cardinalities are distinct and have positive coefficients. The boundary cases follow by combining the terms at common exponents. The maximum is \(2\lceil n/2\rceil\). Since only sizes \(4\), \(6\), and that maximum occur, the number of missing even sizes grows without bound. \(\square\)

## Verification

The standalone standard-library program `artifacts/verify.py` constructs each graph directly from row/column adjacency. It tests domination, existence of induced perfect matchings by backtracking, and inclusion-minimality by a downward-subset dynamic program; it does not implement the above counting classification as the decision rule. It additionally checks the predicted structural shapes and all coefficients for \(n=2,\ldots,7\), examining 2,396,730 nonempty vertex subsets, and performs 98 further arithmetic-support checks through \(n=100\). Run `python3 artifacts/verify.py` from the package root; the expected terminal line is `VERIFY_OK graph_orders=6 direct_vertex_subsets=2396730 arithmetic_orders=98`. The isolated \(n=2\) check tests the boundary outside the theorem; it has three minimal paired-dominating pairs. These computations are finite checks, not the proof of the all-order theorem.

## Relationship to prior work

The rectangular rook-graph paired-domination polynomial in [5] counts **all** paired-dominating vertex subsets, including those containing smaller paired-dominating subsets. It yields the same minimum paired-domination number for three rows and necessarily agrees at that minimum-size layer. Its coefficient extraction for all sets does not distinguish higher-cardinality minimal sets from sets containing smaller witnesses. The contribution here is the inclusion-minimal classification and its size distribution, not the minimum-size result. Alizadeh and Gözüpek [1] study upper paired domination and equality with its general bounds. Dorbec and Henning [4] give general upper bounds for claw-free graphs. Brešar, Henning and Rall [6] study minimum paired domination for Cartesian products. None of the inspected statements of these bounds gives the inclusion-minimal distribution above. Burcroff [3] studies direct-product inequalities and also discusses ordinary upper domination of rook graphs, which omits the perfect-matching condition.

## Limitations

The result treats exactly three rows and every \(n\ge3\); it does not classify arbitrary rook-graph dimensions or general paired-dominating sets. The comparison with inspected literature does not establish publication priority. In particular, the full texts of [2] and [6] were not consulted. The computational verifier covers finite cases only.

## References

1. H. Alizadeh and D. Gözüpek, *Upper paired domination versus upper domination*, Discrete Mathematics & Theoretical Computer Science 23(3), 2021. https://arxiv.org/abs/2104.02446
2. X. Jiang, B. Wu, J. Zhang, and P. Rao, *Upper paired domination in graphs*, AIMS Mathematics 7 (2022). https://doi.org/10.3934/math.2022069
3. A. Burcroff, *Tightness of Paired and Upper Domination Inequalities for Direct Product Graphs*, 2020. https://arxiv.org/abs/2008.03887
4. M. Dorbec and M. A. Henning, *Upper Paired-Domination in Claw-Free Graphs*. https://www.labri.fr/perso/dorbec/abstracts/upclaw.pdf
5. *A parity-component formula for the paired-domination polynomial of rook graphs*. https://github.com/Resultary/2026/blob/main/2026/10/13/SCOPE-a-parity-component-formula-for-the-paired-domination-polynomial--45220dd1e169/RESULT.md
6. B. Brešar, M. A. Henning, and D. F. Rall, *Paired-domination of Cartesian products of graphs*, Utilitas Mathematica 73 (2007), 255–265. https://pure.uj.ac.za/en/publications/paired-domination-of-cartesian-products-of-graphs/
