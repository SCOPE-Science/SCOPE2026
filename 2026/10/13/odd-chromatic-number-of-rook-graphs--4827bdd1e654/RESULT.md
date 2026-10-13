# Odd chromatic number of rook graphs

## Finding

For integers \(1\le m\le n\) with \(n\ge2\), let
\[
R_{m,n}=K_m\square K_n=L(K_{m,n})
\]
be the rook graph. Then its ordinary odd chromatic number is
\[
\boxed{
\chi_o(R_{m,n})=
\begin{cases}
n,&m<n,\\
n+2,&m=n.
\end{cases}}
\]

There is a local criterion that makes the parity condition transparent. Write a proper coloring of \(R_{m,n}\) as an \(m\times n\) matrix, and let \(R_i\) be the set of colors used in row \(i\) and \(C_j\) the set used in column \(j\). Then the vertex in cell \((i,j)\) has a color occurring an odd number of times in its open neighborhood if and only if
\[
R_i\ne C_j.
\]

For \(m<n\), an optimal coloring is
\[
c(i,j)=i+j\pmod n.
\]
For \(m=n\), no coloring with \(n+1\) or fewer colors is odd, while an explicit \(n+2\)-coloring is obtained as follows. Put
\[
q=n+2,\qquad F=\mathbb Z_q\setminus\{0,2\},
\]
choose a bijection \(f:[n]\to F\), and set
\[
c(i,j)=i+f(j)\pmod q.
\]

## Assumptions and scope

Graphs are finite and simple. An odd coloring is a proper vertex coloring such that every non-isolated vertex has at least one color occurring an odd number of times in its open neighborhood. The parameter \(\chi_o(G)\) is the minimum number of colors in such a coloring.

The theorem uses the standard Cartesian product. For \(1\le m\le n\), the graph \(K_m\square K_n\) is also the rook graph on an \(m\times n\) board and the line graph \(L(K_{m,n})\).

The case \(n=1\) is excluded because the graph has a single isolated vertex; the theorem concerns the nontrivial rook graphs.

## Proof

Arrange the vertices as cells \((i,j)\) of an \(m\times n\) array. Two cells are adjacent exactly when they share a row or a column. Properness therefore implies that every row and every column has pairwise distinct colors.

Fix a cell \((i,j)\), and let its color be \(a\). For any color \(x\ne a\), the number of occurrences of \(x\) in the open neighborhood of \((i,j)\) is
\[
\mathbf 1_{\{x\in R_i\}}+\mathbf 1_{\{x\in C_j\}},
\]
because a proper row and a proper column contain a color at most once. The color \(a\) itself occurs zero times in the open neighborhood: its two incidences with the row and column are the cell \((i,j)\) itself. Hence every neighborhood color multiplicity is even exactly when
\[
R_i=C_j.
\]
This proves the criterion
\[
(i,j)\text{ satisfies the odd condition}\iff R_i\ne C_j.
\]

Every row is a clique of order \(n\), so
\[
\chi_o(R_{m,n})\ge n.
\]

Assume first that \(m<n\). Index rows by \(0,\ldots,m-1\), columns by \(0,\ldots,n-1\), and colors by \(\mathbb Z_n\). Define
\[
c(i,j)=i+j\pmod n.
\]
Each row uses all \(n\) colors, while each column uses only \(m<n\) colors. Thus
\[
R_i\ne C_j
\]
for every cell, so the coloring is odd. Therefore
\[
\chi_o(R_{m,n})=n
\]
when \(m<n\).

Now suppose \(m=n\). A proper \(n\)-coloring makes every row and every column use the full \(n\)-color palette. Consequently
\[
R_i=C_j
\]
at every cell, so no proper \(n\)-coloring is odd.

It remains to exclude \(n+1\) colors. Suppose a proper odd coloring uses a palette of \(n+1\) colors. Each row and each column has \(n\) distinct colors and therefore misses exactly one palette color. Let \(a_i\) be the color missed by row \(i\), and let \(b_j\) be the color missed by column \(j\).

For a palette color \(x\), let \(r_x\) be the number of rows missing \(x\) and \(c_x\) the number of columns missing \(x\). The number of cells colored \(x\), counted by rows, is
\[
n-r_x,
\]
while the same number counted by columns is
\[
n-c_x.
\]
Thus
\[
r_x=c_x
\]
for every \(x\). Since the \(n\) rows miss one color each,
\[
\sum_x r_x=n,
\]
so some \(x\) has \(r_x>0\). Then \(c_x>0\) as well. Hence there are a row \(i\) and a column \(j\) with
\[
a_i=b_j=x.
\]
Both \(R_i\) and \(C_j\) are the entire \(n+1\)-color palette with \(x\) deleted, so
\[
R_i=C_j,
\]
contradicting the odd condition at \((i,j)\). A coloring using fewer than \(n+1\) colors has already been excluded by the clique lower bound and the \(n\)-color argument. Therefore
\[
\chi_o(R_{n,n})\ge n+2.
\]

For the matching upper bound, put
\[
q=n+2
\]
and work in \(\mathbb Z_q\). Let
\[
F=\mathbb Z_q\setminus\{0,2\},
\]
choose any bijection \(f:[n]\to F\), and define
\[
c(i,j)=i+f(j)\pmod q
\]
for \(i=0,\ldots,n-1\). A row is proper because \(f\) is injective, and a column is proper because the row indices are distinct modulo \(q\).

Row \(i\) uses \(i+F\), so it misses exactly
\[
\{i,i+2\}.
\]
Column \(j\) uses
\[
f(j)+\{0,1,\ldots,n-1\},
\]
so, because \(q=n+2\), it misses exactly the consecutive pair
\[
\{f(j)-2,f(j)-1\}.
\]
For \(q\ge4\), a distance-two pair \(\{i,i+2\}\) cannot equal a consecutive pair. Hence
\[
R_i\ne C_j
\]
for every cell, and the coloring is odd. Thus
\[
\chi_o(R_{n,n})\le n+2.
\]
Combining the bounds completes the proof.

## Verification

The accompanying script `artifacts/verify.py` evaluates the odd-coloring condition directly from neighborhood color multiplicities.

It checks the cyclic \(n\)-color construction for every
\[
1\le m<n\le20
\]
and the balanced \(n+2\)-color construction for every
\[
2\le n\le50.
\]
It also exhaustively enumerates all proper colorings of
\[
K_n\square K_n
\]
for \(2\le n\le4\) using \(n\) or \(n+1\) colors, after the harmless global color-symmetry normalization that fixes the first row. None is odd.

Replay output:

`ALL CHECKS PASSED; unbalanced_constructions=190; balanced_constructions=49; balanced_exhaustive_n=2..4; proper_completions_checked=4994`

The finite computation is corroborative only. The all-orders lower and upper bounds are proved analytically above.

## Relationship to prior work

Liu, Dou, and Yang study odd colorings of Cartesian product graphs in 2026. Their exact product results include products of paths and cycles and, in their final section, \(K_m\square P_n\) and \(K_m\square C_n\). The inspected full text does not state a result for \(K_m\square K_n\). Their paper therefore supplies a direct recent motivation for asking for the missing complete-by-complete Cartesian product.

Dujmović, Morin, and Odak study odd colorings of graph products from a broader structural perspective, obtaining bounded-color results through strong-product representations. Those bounds do not determine the exact odd chromatic number of rook graphs.

The complete-multipartite odd-coloring formula is not a covering result: a rook graph is generally not complete multipartite, and the balanced obstruction here is an edge-coloring incidence phenomenon. The line-graph representation
\[
K_m\square K_n=L(K_{m,n})
\]
is useful because a proper rook coloring is exactly a proper edge coloring of \(K_{m,n}\), but the odd condition depends on comparing the two incident color sets at each edge.

## Limitations

The theorem is restricted to Cartesian products of two complete graphs. It does not classify odd colorings of arbitrary line graphs, Hamming graphs of dimension at least three, or products in which one factor is not complete.

The lower-bound argument for the balanced case uses the exact row-column symmetry of \(K_n\square K_n\); it does not directly transfer to rectangular products of other clique-like factors.

The originality assessment is literature-based rather than an absolute uniqueness proof. Rook graphs may also be indexed as line graphs of complete bipartite graphs or as two-dimensional Hamming graphs; those aliases were included in targeted searches, but poorly indexed or concurrent equivalent work remains a residual risk.

## References

1. B. Liu, Q. Dou, and F. Yang, “The odd coloring of some Cartesian product graphs,” AIMS Mathematics 11 (2026), 1311–1331, DOI 10.3934/math.2026056. Published January 16, 2026. MSC \(05C15\), \(05C10\).
2. V. Dujmović, P. Morin, and S. Odak, “Odd Colourings of Graph Products,” arXiv:2202.12882v1, February 25, 2022.
3. M. Petruševski and R. Škrekovski, “Colorings with neighborhood parity condition,” Discrete Applied Mathematics 321 (2022), 385–391, DOI 10.1016/j.dam.2022.07.018.
