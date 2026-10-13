# Power-domination support criterion and minimal-set spectrum of rectangular rook graphs

## Finding

For all integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n\), with cells indexed by \([m]\times[n]\), two distinct cells adjacent exactly when they share a row or column. For a vertex set \(S\), write \(r(S)\) and \(c(S)\) for the numbers of rows and columns that contain a member of \(S\). Then
\[
S\text{ is power dominating}\quad\Longleftrightarrow\quad
r(S)\ge m-1\ \text{or}\ c(S)\ge n-1.
\tag{1}
\]
Every successful power-domination process finishes immediately after initial neighborhood observation or after one further, simultaneous forcing round; no unsuccessful configuration has a first force.

The **complete cardinality polynomial** of power dominating sets is
\[
\mathcal P_{m,n}(z)=(1+z)^{mn}-
\sum_{a=0}^{m-2}\sum_{b=0}^{n-2}\binom ma\binom nb H_{a,b}(z),
\tag{2}
\]
where
\[
H_{a,b}(z)=\sum_{i=0}^{a}\sum_{j=0}^{b}
(-1)^{i+j}\binom ai\binom bj(1+z)^{(a-i)(b-j)}.
\tag{3}
\]
Here \(H_{a,b}\) counts selected subsets of an \(a\)-by-\(b\) rectangle which meet every row and every column; in particular \(H_{0,0}=1\), while \(H_{a,0}=H_{0,b}=0\) for positive \(a\) or \(b\).

A power dominating set is **inclusion-minimal** if deleting any selected vertex destroys power domination. Every inclusion-minimal set has exactly one of the following forms:

1. **Row type:** it occupies exactly \(m-1\) rows, with exactly one selected cell in each, and occupies at most \(n-2\) columns.
2. **Column type:** it occupies exactly \(n-1\) columns, with exactly one selected cell in each, and occupies at most \(m-2\) rows.
3. **Joint type:** only possible when \(m=n\); it contains \(m-1\) pairwise nonattacking rooks, leaving precisely one row and one column empty.

These three types are disjoint. For \(2\le m<n\), the polynomial enumerating inclusion-minimal sets by their cardinality is
\[
\boxed{\displaystyle
\mathcal M_{m,n}(z)=m n^{m-1}z^{m-1}
+n\left(\sum_{a=1}^{m-2}\binom ma a!\left\{\begin{matrix}n-1\\a\end{matrix}\right\}\right)z^{n-1}.}
\tag{4}
\]
The second summation is empty when \(m=2\), and the braced symbol is a Stirling number of the second kind. For \(m>n\), interchange the two parameters. For \(m=n\ge2\),
\[
\boxed{\displaystyle
\mathcal M_{m,m}(z)=\bigl(2m^m-m^2(m-1)!\bigr)z^{m-1}.}
\tag{5}
\]
Consequently the known minimum power-domination number and the maximum cardinality of an inclusion-minimal power dominating set, respectively, satisfy
\[
\gamma_P(R_{m,n})=\min\{m,n\}-1,
\qquad
\Gamma_P(R_{m,n})=
\begin{cases}
1,&\min\{m,n\}=2,\\
\max\{m,n\}-1,&\min\{m,n\}\ge3.
\end{cases}
\tag{6}
\]
The notation \(\Gamma_P\) is defined here by maximization **only over inclusion-minimal power dominating sets**, not over all power dominating sets. In particular, for every \(n\ge4\), \(R_{3,n}\) has minimum size \(2\) but also inclusion-minimal sets of size \(n-1\), an unbounded ratio.

## Assumptions and scope

Graphs are finite, simple, undirected, and the two complete factors have orders at least \(2\). The power-domination procedure starts with the closed neighborhood of the chosen set \(S\). Thereafter any observed vertex with exactly one unobserved neighbor may observe that neighbor; repetitions continue until no further force is possible. Distinct labeled cell subsets are counted separately. All enumerators and the minimum/maximum expressions hold for every pair of integers \(m,n\ge2\), including the smallest square \(R_{2,2}\).

## Proof

**Unobserved rectangle and forcing barrier.** Let \(A\subseteq[m]\) be the rows met by \(S\) and \(B\subseteq[n]\) its columns; put \(p=m-|A|\) and \(q=n-|B|\). A cell is initially observed if and only if its row belongs to \(A\) or its column belongs to \(B\). Therefore the unseen cells immediately after the neighborhood step are exactly
\[
U=([m]\setminus A)\times([n]\setminus B).
\]
For an observed cell, the number of neighbors in \(U\) is either \(0\), \(p\), or \(q\): it is \(p\) when its row is occupied and its column is unoccupied, and \(q\) in the transposed case. If \(p,q\ge2\), no observed vertex has exactly one unseen neighbor. Thus no force can begin and \(S\) is not power dominating.

Conversely, if \(p=0\) or \(q=0\), the neighborhood step already observes everything. If \(p=1\) and \(q>0\), there is at least one occupied row because \(m\ge2\); for each unoccupied column, a cell in that occupied row has exactly one unseen neighbor, lying in the unique unoccupied row. These forces cover all of \(U\) in one round. The case \(q=1\) is symmetric. This proves (1) and the forcing-round dichotomy, including \(S=\varnothing\).

**All-set polynomial.** Fix exact row support \(A\) of size \(a\) and column support \(B\) of size \(b\). Inclusion–exclusion over rows and columns omitted from the selected subset gives (3): if \(i\) rows and \(j\) columns are forbidden, the remaining \((a-i)(b-j)\) cells contribute \((1+z)^{(a-i)(b-j)}\). There are \(\binom ma\binom nb\) choices of the supports. By (1), the non-power-dominating sets are precisely those with \(a\le m-2\) and \(b\le n-2\). Subtracting their generating polynomial from that of all \(2^{mn}\) subsets proves (2). The empty set is correctly removed by \(H_{0,0}=1\).

**Inclusion-minimal structure.** Write \(A_0\) for the condition \(r(S)\ge m-1\) and \(B_0\) for \(c(S)\ge n-1\). If a minimal set satisfies \(A_0\) but not \(B_0\), every selected cell must be indispensable to \(A_0\). Thus it has exactly \(m-1\) occupied rows and exactly one selected cell per such row; it occupies at most \(n-2\) columns, giving row type. The converse follows because deleting any cell leaves only \(m-2\) occupied rows and still fewer than \(n-1\) occupied columns. The column-type argument is symmetric.

If both \(A_0\) and \(B_0\) hold, deleting *each* selected cell must destroy *both* conditions. Every occupied row and every occupied column must consequently contain exactly one selected cell, with \(r(S)=m-1\) and \(c(S)=n-1\). The selected-cell count then equals both \(m-1\) and \(n-1\), so \(m=n\) and the cells form a nonattacking partial permutation of order \(m-1\). Again, deleting any selected cell violates both thresholds. This proves the disjoint, exhaustive classification.

**Enumeration and extremal sizes.** Suppose \(m<n\). A row-type set chooses its one empty row in \(m\) ways and then independently selects one of \(n\) columns in each remaining row, giving \(m n^{m-1}\) sets, all of size \(m-1\). A column-type set chooses its one empty column in \(n\) ways, then chooses \(a\) occupied rows with \(1\le a\le m-2\), and assigns the \(n-1\) occupied columns surjectively to them. There are \(\binom ma a!\left\{\begin{smallmatrix}n-1\\a\end{smallmatrix}\right\}\) assignments. All column-type sets have size \(n-1\), proving (4). When \(m=n\), the union of the row-singleton and column-singleton families has \(2m\cdot m^{m-1}=2m^m\) members before duplicates. Their intersection consists of the nonattacking partial permutations: select the omitted row, omitted column, and bijection among the remaining \(m-1\) positions, giving \(m^2(m-1)!\) duplicates. This proves (5). The minimum and maximum exponents in (4)–(5), with the empty-column-type boundary \(m=2\), prove (6). The previously known value of \(\gamma_P\) is recorded for completeness, not claimed as new.

## Verification

The companion standalone program `verify.py` reconstructs adjacency and power-domination forcing directly, without applying criterion (1) to its verdict. It exhausts all \(107{,}654\) nonempty selected subsets on the ten labeled boards: all nine cases with \(2\le m,n\le4\), plus \((m,n)=(3,5)\), compares each power-domination verdict against (1), tests inclusion-minimality against the stated structural types, and independently compares the full coefficient vector of (2) with the direct enumeration. It checks the minimal-set counts from (4)–(5). Run `python3 verify.py`. Its final status is:

`VERIFY_OK subset_checks 107654 power_sets 107194 minimal_sets 694 boards 2..4 plus 3x5 coefficient_cases 10`

Finite exhaustive checks corroborate the general proof and are not asserted as an infinite proof.

## Relationship to prior work

The graph-theoretic power-domination formulation traces to Haynes–Hedetniemi–Hedetniemi–Henning. Dorbec–Mollard–Klavžar–Špacapan (2008) analyze power-domination numbers for other graph products, especially products of paths and lexicographic products. Soh–Koh (2014, Theorem 3.3) already establish \(\gamma_P(K_m\square K_n)=\min\{m,n\}-1\), which is therefore **not** a novelty claim. Benson and collaborators' graph-product work (first arXiv version 2015) supplies general power-domination/zero-forcing comparisons but no cardinality enumerator for the complete-by-complete Cartesian product. Brimkov–Patel–Suriyanarayana–Teich (2018) define and develop the general power-domination polynomial framework and evaluate several graph families; the present formulas evaluate a different family and additionally classify its inclusion-minimal sets. Ordinary domination polynomials of rook graphs count a stricter set condition and do not count the forcing-enabled sets in (1).

## Limitations

The exact statements are restricted to Cartesian products of **two** complete graphs of orders at least two; they do not assert formulas for longer products, weighted sensors, fault tolerance, or different propagation rules. The available indexed content of the 2014 rook-graph minimum-number paper confirms its minimum theorem, but a fully accessible version was not obtained; an uninspected fuller statement could affect the originality comparison. Earlier or differently indexed formulas also remain possible. Neither search nonhits nor finite tests certify novelty or independent validation.

## References

1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM Journal on Discrete Mathematics 15 (2002), 519–529. DOI: 10.1137/S0895480100375831.
2. P. Dorbec, M. Mollard, S. Klavžar, and S. Špacapan, *Power Domination in Product Graphs*, SIAM Journal on Discrete Mathematics 22 (2008), 554–567. DOI: 10.1137/060661879; first verified online date: 2008-03-21.
3. K. W. Soh and K. M. Koh, *A Note on Power Domination Problem in Diameter Two Graphs*, AKCE International Journal of Graphs and Combinatorics 11 (2014), 51–55. DOI: 10.1080/09728600.2014.12088762.
4. K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska, and B. Wissman, *Power domination and zero forcing*, arXiv:1510.02421v1 (2015-10-08); subsequently published as *Zero forcing and power domination for graph products*, Australasian Journal of Combinatorics 70 (2018), 221–235.
5. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (2018-05-28).
6. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (2024), Journal of Integer Sequences 27 (2024), Article 24.3.7; ordinary, not power, domination.
