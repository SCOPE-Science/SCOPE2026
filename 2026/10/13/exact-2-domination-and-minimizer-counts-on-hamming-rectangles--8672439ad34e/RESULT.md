# Exact 2-domination and minimizer counts on Hamming rectangles
## Finding
Let \(1\le m\le n\), and write \(H_{m,n}=K_m\mathbin{\Box}K_n\). A set \(D\subseteq V(H_{m,n})\) is 2-dominating when every vertex outside \(D\) has at least two neighbors in \(D\). Then
\[
\gamma_2(H_{m,n})=\min\{n,2m\}.
\]
There is also a complete description of the minimum sets. Identify \(V(H_{m,n})\) with the cells of an \(m\)-by-\(n\) array.

If \(n<2m\), the minimum sets are exactly those with one chosen cell in every column and at least one chosen cell in every row. Equivalently, they are graphs of surjections from the \(n\) columns onto the \(m\) rows.

If \(n>2m\), the minimum sets are exactly those with two chosen cells in every row.

If \(n=2m\), the minimum sets are exactly the union of the preceding two families.

Writing \(S(n,m)\) for the Stirling number of the second kind and \(N_2(m,n)\) for the number of minimum 2-dominating sets,
\[
N_2(m,n)=
\begin{cases}
m!\,S(n,m),&n<2m,\\
 m!\,S(2m,m)+\binom{2m}{2}^{m}-\dfrac{(2m)!}{2^{m}},&n=2m,\\
\binom{n}{2}^{m},&n>2m.
\end{cases}
\]

## Assumptions and scope
All graphs are finite and simple. The parameter is ordinary 2-domination: vertices in \(D\) have no domination requirement, while each vertex in \(V(H_{m,n})\setminus D\) must have at least two neighbors in \(D\). The factors may be interchanged, so assuming \(m\le n\) loses no generality. The one-vertex case \(m=n=1\) is included and gives \(\gamma_2(H_{1,1})=1\).

## Proof
For a chosen set \(D\), let \(r_i\) be the number of chosen cells in row \(i\), and let \(c_j\) be the number in column \(j\). If the cell \((i,j)\) is not chosen, then its neighbors in \(D\) are precisely the chosen cells in its row together with the chosen cells in its column. Therefore
\[
D\text{ is 2-dominating}\quad\Longleftrightarrow\quad r_i+c_j\ge2\text{ for every unchosen cell }(i,j).
\]

If every column is nonempty, then \(|D|\ge n\). If some column \(j\) is empty, then every cell \((i,j)\) is unchosen, so the displayed criterion forces \(r_i\ge2\) for every row \(i\); hence \(|D|\ge2m\). Thus every 2-dominating set satisfies
\[
|D|\ge\min\{n,2m\}.
\]

For the reverse inequality, when \(n\le2m\), choose one cell in every column so that every row is represented; this is possible because \(n\ge m\). Every unchosen cell then sees at least one chosen cell in its row and exactly one in its column, so the chosen set is 2-dominating and has size \(n\). When \(n\ge2m\), choose any two cells in every row. Every unchosen cell then has two chosen row-neighbors, giving a 2-dominating set of size \(2m\). This proves the value formula.

For the classification, suppose first that \(n<2m\) and \(|D|=n\). An empty column would force \(|D|\ge2m>n\), so every column is nonempty and therefore contains exactly one chosen cell. No row can be empty, because an unchosen cell in an empty row would then have only its single chosen column-neighbor. Conversely, every such column-transversal meeting all rows is 2-dominating.

Next suppose \(n>2m\) and \(|D|=2m\). Since \(2m<n\), some column is empty, which forces every row to contain at least two chosen cells; equality in the total size then forces exactly two in each row. Conversely, any choice of exactly two cells per row is 2-dominating. At \(n=2m\), equality can arise through either branch of the lower-bound dichotomy, giving exactly the union of the two families.

The counts now follow directly. For \(n<2m\), assigning the unique chosen cell of each column to a row is a surjection, counted by \(m!S(n,m)\). For \(n>2m\), the two cells in each row can be chosen independently in \(\binom{n}{2}\) ways. At \(n=2m\), inclusion-exclusion combines the two families; their intersection has row degree two and column degree one, and hence has cardinality \((2m)!/2^m\).

## Verification
The accompanying `verify.py` independently constructs \(K_m\mathbin{\Box}K_n\), tests the ordinary 2-domination condition by direct neighborhood counting, exhaustively enumerates all subsets for every \(1\le m\le n\le4\), and compares both the minimum size and the number of minimum sets with the formulas above. It additionally checks the two explicit construction regimes and the boundary case for \(1\le m\le n\le40\). These computations are finite stress tests; the theorem for arbitrary \(m,n\) is established by the analytic proof above. Actual replay: `ALL CHECKS PASSED; exhaustive_cases=10; subset_candidates=3681; construction_cases=820; exhaustive_range=1<=m<=n<=4; construction_range=1<=m<=n<=40`

## Relationship to prior work
Gravner, Krnc, Milanič, and Raymond introduced the Young-domination framework on Hamming rectangles. Their triangular zero-set \(T_a\) at latency one is exactly ordinary \(a\)-domination, and their principal exact theorem for triangular zero-sets is stated for equal factor orders \(K_n\mathbin{\Box}K_n\). For \(a=2\), that theorem yields \(\gamma_2(K_n\mathbin{\Box}K_n)=n\). The present result determines the unbalanced rectangular case, including the phase transition at \(n=2m\), and classifies and counts every minimum set.

Burchett, Lane, and Lachniet studied \(k\)-domination on the square rook graph; the recent Young-domination paper describes that predecessor as a square-case source. The accessible abstract likewise states results for the rook graph \(R_n\), not a two-parameter rectangular classification.

Carballosa and Wisby study total \(k\)-domination on \(K_m\mathbin{\Box}K_n\). Total 2-domination imposes the two-neighbor condition on selected vertices as well, so it is a different invariant and its formulas do not imply the ordinary 2-domination result here.

## Limitations
The theorem treats ordinary 2-domination only. It does not give an analogous formula for ordinary \(k\)-domination with \(k>2\), for total 2-domination, or for products whose factors are not complete. The 2009 square-rook predecessor was available only at abstract/metadata level during the literature check; this leaves a residual risk that it contains an unadvertised rectangular observation under different notation. The recent Hamming-rectangle paper and the total-domination paper were inspected at full-text level where relevant, and targeted searches did not locate the theorem above.

## References
1. J. Gravner, M. Krnc, M. Milanič, J.-F. Raymond, “Young domination on Hamming rectangles,” arXiv:2501.03788. First public version: 2025-01-07. Primary MSC: 05C35.
2. P. A. Burchett, J. A. Lane, D. Lachniet, “\(k\)-domination and \(k\)-tuple domination on the rook’s graph and other results,” Congressus Numerantium 199 (2009), 187–204.
3. W. Carballosa, J. Wisby, “Total \(k\)-domination in Cartesian product of complete graphs,” Discrete Applied Mathematics 337 (2023), 25–41; arXiv:2001.07850; doi:10.1016/j.dam.2023.04.008.
