# Minimum Italian domination on rook graphs: exact optimizers and a sharp transition

## Finding

Let \(1\le m\le n\) be integers and let \(R_{m,n}=K_m\square K_n\) be the rook graph with vertex set \([m]\times[n]\); two distinct cells are adjacent if they share a row or a column. An *Italian dominating function* is a map \(f:[m]\times[n]\to\{0,1,2\}\) such that every zero-labelled cell has open-neighbourhood label sum at least \(2\). Its weight is \(w(f)=\sum_{i,j}f(i,j)\). Write \(\gamma_I\) for the minimum weight and \(N_{m,n}\) for the number of minimum-weight functions on the **labelled** board.

**Theorem.** For every \(1\le m\le n\),
\[
\gamma_I(R_{m,n})=\min\{n,2m\}.
\]
Let \(S(n,m)\) denote a Stirling number of the second kind (the number of partitions of an \(n\)-element set into \(m\) nonempty unlabeled blocks). Then
\[
N_{m,n}=\begin{cases}
m!S(n,m),&n<2m,\\[2pt]
\left(\frac{n(n+1)}{2}\right)^m+m!S(n,m)-\frac{n!}{2^m},&n=2m,\\[2pt]
\left(\frac{n(n+1)}{2}\right)^m,&n>2m.
\end{cases}
\]
All minimum-weight functions are exactly the following configurations, with no exceptions:

- **Column-saturating family:** each column has precisely one label \(1\) and all other entries \(0\), and each row contains at least one label \(1\). This family has weight \(n\) and cardinality \(m!S(n,m)\).
- **Row-heavy family:** each row has total weight exactly \(2\); independently in each row this is either one label \(2\) or two labels \(1\), with every other entry \(0\). This family has weight \(2m\) and cardinality \(\bigl(n+\binom n2\bigr)^m\).

The first family is the complete optimal family for \(n<2m\); the second is the complete optimal family for \(n>2m\). At the boundary \(n=2m\), the complete optimal family is their union, and their intersection consists of the column-saturating functions having exactly two labels \(1\) in each row, of cardinality \(n!/(2!)^m\). This includes the degenerate one-cell graph \(R_{1,1}\), where the only optimum labels the vertex \(1\).

## Assumptions and scope

Graphs are finite, simple, undirected, and their cells are distinguished by row and column indices. The labels are integers \(0,1,2\), and the Italian condition is imposed **only at zero-labelled vertices**. This is ordinary Italian domination (also called Roman \(\{2\}\)-domination), not the stricter *perfect Italian* version, which requires equality at each zero. The theorem concerns the minimum weight, its complete equality cases and their number, not the full Italian domination polynomial or unlabelled graph orbits. By symmetry one can use \(m=\min\{a,b\}\) and \(n=\max\{a,b\}\) for any Cartesian product \(K_a\square K_b\).

## Proof

For a function \(f\), define its nonnegative row sums \(r_i=\sum_{j=1}^n f(i,j)\), column sums \(c_j=\sum_{i=1}^m f(i,j)\), and total \(W=\sum_i r_i=\sum_j c_j\). If \(f(i,j)=0\), its open-neighbourhood sum equals \(r_i+c_j\), because the own entry contributes zero and each other cell of its row or column is counted exactly once. Thus the Italian condition at a zero cell is exactly \(r_i+c_j\ge2\).

**Lower bound.** If some row has \(r_i=0\), every cell in that row is zero, so every column sum satisfies \(c_j\ge2\). It follows that \(W\ge2n\), and in particular \(W\ge\min\{n,2m\}\). Otherwise every row sum is positive. If any row has \(r_i=1\), then precisely one of its entries, say at column \(j_0\), is labelled \(1\). Its own column satisfies \(c_{j_0}\ge1\). Every other entry in that row is zero, so \(1+c_j\ge2\) for each \(j\ne j_0\). Hence **every** column has positive sum, and \(W\ge n\). If no row has sum \(1\), then every row has sum at least \(2\), and \(W\ge2m\). These possibilities exhaust all functions, so every valid function has \(W\ge\min\{n,2m\}\).

**Attainment.** Choose one different row for each of the first \(m\) columns, then place the label \(1\) in exactly one cell of every remaining column, in arbitrary rows. All columns have sum \(1\), and every row has positive sum. Every zero cell sees at least \(1+1=2\) in its row and column, so this is a valid function of weight \(n\). Alternatively, choose in each row either one label \(2\) or two labels \(1\). Every row then sums to \(2\), so every zero in that row already receives at least \(2\) from its row-neighbours. This is a valid function of weight \(2m\). Hence \(\gamma_I(R_{m,n})=\min\{n,2m\}\).

**Equality classification.** Because \(W=\gamma_I\le n<2n\), a minimum function cannot have a zero-sum row: such a row would force \(W\ge2n\). If \(n<2m\), a minimum function has weight \(n<2m\), so not all rows can have sum at least \(2\). Some row has sum \(1\), which forces every column to have positive sum. As their total is exactly \(n\), each column has sum exactly \(1\), and therefore consists of exactly one \(1\). Every row is nonempty, giving precisely the column-saturating family. If \(n>2m\), a minimum function has weight \(2m<n\), so no row can have sum \(1\); all \(m\) positive row sums are therefore exactly \(2\), giving precisely the row-heavy family. If \(n=2m\), any minimum function either has a row of sum \(1\), forcing all columns to sum exactly \(1\), or has no such row, forcing all rows to sum exactly \(2\). Thus it belongs to the union of the two stated families.

**Counting.** A column-saturating function assigns each of the \(n\) distinguished columns to exactly one of the \(m\) distinguished rows, using every row; it is a surjection and can be counted in \(m!S(n,m)\) ways. Independently, each row-heavy row can place one \(2\) in \(n\) ways or two \(1\)'s in \(\binom n2\) ways, giving \(\left(n+\binom n2\right)^m\) choices. At \(n=2m\), a function belongs to both families precisely when each column has a single \(1\) and each row has two such \(1\)'s; the \(n\) distinguished columns can be partitioned into \(m\) prescribed pairs in \(n!/(2!)^m\) ways. Inclusion–exclusion gives the claimed formula. All arguments also cover \(m=1\), including \(n=1\). \(\square\)

## Verification

The standalone file `verify_italian_rook.py` computes the predicted optimum and count using integer Stirling-surjection inclusion–exclusion, and **independently** checks each label assignment against literal rook-graph open neighbourhoods. Run with `python3 verify_italian_rook.py` (standard library only). It exhaustively visited \(1{,}152{,}264\) assignments over fourteen graph sizes: \(m=1\), \(1\le n\le7\); \(m=2\), \(2\le n\le6\); and \(m=3\), \(3\le n\le4\). It additionally inspected all \(696{,}634\) assignments whose weight is at most the claimed optimum for sizes \((m,n)=(3,5),(3,6),(4,5),(4,6)\). Every predicted minimum and multiplicity matched; the latter enumeration is exhaustive **only up to that weight**, not over all assignments. The infinite theorem is established by the proof, not by these finite experiments.

Examples \((m,n,\gamma_I,N_{m,n})\) include \((2,3,3,6)\), \((2,4,4,108)\), \((3,5,5,150)\), and \((3,6,6,9711)\).

## Relationship to prior work

Shao and Zhao (arXiv:2610.00108, 2026) formulate Italian domination weight-enumeration and give methods for paths, trees and cycles, but do not treat rook graphs. Varghese and Lakshmanan (arXiv:1910.12260, Theorem 2.4) obtain the **perfect** Italian domination minimum on \(K_m\square K_n\), which equals \(n\) for \(m=n\) and \(2m\) for \(m<n\). This is a stricter invariant: perfect Italian functions require neighbourhood sum **equal to** \(2\) at zeros, whereas ordinary Italian functions require **at least** \(2\). Comparing with that credited theorem, the two minima differ by \(2m-n\) in the interval \(m<n<2m\) and coincide for \(n=m\) and for \(n\ge2m\). The perfect result does not determine the ordinary minimizers or their multiplicities; in particular, \(K_2\square K_3\) has ordinary Italian minimum \(3\) versus perfect minimum \(4\).

Kazemi, Pahlavsay and Stones (arXiv:1509.08208, Proposition 1) study rook graphs under *\(2\)-tuple total domination*: every vertex, including selected vertices, needs two selected neighbours, and labels are binary. This is mathematically different from imposing a weighted-neighbour requirement only on zero-labelled vertices. Its minimum and example matrices do not imply the present three-state optimizer enumeration. This finding isolates a new low-weight coefficient and complete equality cases, not a claim to the general full domination polynomial.

## Limitations

The theorem does not enumerate Italian functions of nonminimum weight or address arbitrary Cartesian products. Exact bibliographic priority has not been independently certified; equivalent unpublished or difficult-to-index results could exist. The comparison to perfect Italian domination uses the specifically credited prior theorem and does not re-prove its separate invariant.

## References

1. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles* (2026), arXiv:2610.00108, https://arxiv.org/abs/2610.00108 .
2. J. Varghese and A. Lakshmanan S., *Perfect Italian Domination Number of Graphs* (2019/2021), arXiv:1910.12260, especially Section 2 and Theorem 2.4, https://arxiv.org/html/1910.12260v2 .
3. A. P. Kazemi, B. Pahlavsay and R. J. Stones, *Cartesian product graphs and \(k\)-tuple total domination* (2018), arXiv:1509.08208, especially Section 3 and Proposition 1, https://arxiv.org/pdf/1509.08208 .
