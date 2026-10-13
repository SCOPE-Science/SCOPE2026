# Odd chromatic number of rook graphs
## Finding
Let
\[
R_{m,n}=K_m\square K_n
\]
be the rook graph on an \(m\)-by-\(n\) board, with
\[
2\le m\le n.
\]

If
\[
m<n,
\]
then
\[
\chi_o(R_{m,n})=n.
\]
More strongly, every proper \(n\)-coloring of \(R_{m,n}\) is automatically an odd coloring.

If
\[
n\ge3,
\]
then the square rook graph satisfies
\[
\chi_o(R_{n,n})=n+2.
\]

The square boundary is therefore a genuine two-color jump: ordinary chromatic number remains \(n\), but neighborhood-parity odd coloring needs \(n+2\) colors.

## Assumptions and scope
An odd coloring of a graph is a proper vertex coloring such that for every non-isolated vertex \(v\), some color occurs an odd number of times in the open neighborhood \(N(v)\). The least number of colors is denoted by
\[
\chi_o(G).
\]

Vertices of \(R_{m,n}\) are cells \((i,j)\). Two cells are adjacent exactly when they share a row or a column. Thus every row is a clique of order \(n\) and every column is a clique of order \(m\).

For a proper coloring \(\varphi\), write
\[
\mathcal R_i=\{\varphi(i,j):1\le j\le n\}
\]
for the color set of row \(i\), and
\[
\mathcal C_j=\{\varphi(i,j):1\le i\le m\}
\]
for the color set of column \(j\).

The already known boundary \(R_{2,2}=C_4\), for which \(\chi_o(C_4)=4\), is not part of the new square-family assertion.

## Proof
We first establish the local criterion used throughout the proof.

Fix a cell \((i,j)\) with color \(x=\varphi(i,j)\). Properness implies that a color occurs at most once in row \(i\) and at most once in column \(j\). The color \(x\) itself occurs zero times in the open neighborhood of \((i,j)\), because its only row and column occurrence is the cell \((i,j)\).

For any other color \(c\), its multiplicity in \(N(i,j)\) is
\[
\mathbf 1_{\{c\in\mathcal R_i\}}+\mathbf 1_{\{c\in\mathcal C_j\}}.
\]
This multiplicity is odd exactly when \(c\) belongs to precisely one of the two sets. Hence \((i,j)\) has an odd neighborhood color exactly when
\[
\mathcal R_i\ne\mathcal C_j.
\tag{1}
\]

### Rectangular case
Assume
\[
2\le m<n.
\]
Since every row is a clique of order \(n\),
\[
\chi_o(R_{m,n})\ge\chi(R_{m,n})=n.
\]

Take any proper \(n\)-coloring. Every row uses all \(n\) colors, so
\[
|\mathcal R_i|=n.
\]
Every column contains \(m\) pairwise adjacent vertices, so it uses exactly \(m\) distinct colors:
\[
|\mathcal C_j|=m<n.
\]
Thus
\[
\mathcal R_i\ne\mathcal C_j
\]
for every cell. By (1), every proper \(n\)-coloring is odd. Therefore
\[
\chi_o(R_{m,n})=n.
\]

### Square lower bound
Now let
\[
m=n\ge3.
\]
A proper \(n\)-coloring uses all \(n\) colors in every row and every column. Hence
\[
\mathcal R_i=\mathcal C_j
\]
at every cell, and (1) shows that no proper \(n\)-coloring is odd.

Suppose next that a proper odd coloring uses exactly \(n+1\) colors. Each row contains \(n\) distinct colors, and therefore omits exactly one color. Let \(r_i\) be the color omitted by row \(i\). Similarly, let \(c_j\) be the color omitted by column \(j\).

For each color \(a\), let
\[
\alpha_a=|\{i:r_i=a\}|,
\qquad
\beta_a=|\{j:c_j=a\}|.
\]
Counting the total occurrences of color \(a\) by rows gives
\[
n-\alpha_a,
\]
while counting the same occurrences by columns gives
\[
n-\beta_a.
\]
Therefore
\[
\alpha_a=\beta_a
\tag{2}
\]
for every color \(a\).

Some color is omitted by a row, because every row omits one color. For such a color \(a\),
\[
\alpha_a>0.
\]
Equation (2) gives
\[
\beta_a>0.
\]
Hence there are a row \(i\) and a column \(j\) that both omit \(a\). At their intersection,
\[
\mathcal R_i=\mathcal C_j,
\]
contradicting (1). Thus no odd coloring can use \(n+1\) colors, and
\[
\chi_o(R_{n,n})\ge n+2.
\tag{3}
\]

### Square construction
Set
\[
q=n+2
\]
and work in the cyclic group \(\mathbb Z_q\). Index the \(n\) rows by
\[
A=\mathbb Z_q\setminus\{0,1\}
\]
and the \(n\) columns by
\[
B=\mathbb Z_q\setminus\{0,2\}.
\]
Color cell \((a,b)\) by
\[
\varphi(a,b)=a+b\pmod q.
\]

For fixed \(a\), different values of \(b\) give different colors, and for fixed \(b\), different values of \(a\) give different colors. Thus the coloring is proper.

Row \(a\) omits exactly the two colors
\[
a,\ a+2,
\]
whereas column \(b\) omits exactly
\[
b,\ b+1.
\]
For \(q\ge5\), a translate of the two-point set \(\{0,2\}\) cannot equal a translate of \(\{0,1\}\): equality would force the same cyclic difference to be both \(1\) and \(2\) up to sign. Hence no row color set equals any column color set. By (1), the coloring is odd.

It uses at most \(q=n+2\) colors, so together with (3),
\[
\chi_o(R_{n,n})=n+2.
\]

## Verification
The included checker implements the odd-coloring definition directly and separately implements the row-set versus column-set criterion.

For the rectangular boards
\[
(2,3),\ (2,4),\ (3,4),
\]
it enumerates every proper \(n\)-coloring after fixing the first row to remove color-name symmetry. Every one is odd.

For square boards
\[
n=2,3,4,
\]
it exhaustively enumerates normalized proper colorings with \(n\) and \(n+1\) colors. None is odd. The checker then verifies the cyclic \(n+2\)-color construction directly.

Across these cases it checks \(5{,}029\) normalized proper colorings. It also validates the construction for every
\[
2\le n\le50.
\]

## Relationship to prior work
Petruševski and Škrekovski introduced neighborhood-parity odd coloring and the parameter \(\chi_o\), focusing on planar graphs and general bounds. Their paper records, for example, the already known value
\[
\chi_o(C_4)=4.
\]

Dujmović, Morin, and Odak study odd colorings for graphs with product structure. Their main theorems concern subgraphs of strong products with bounded-treewidth factors and give general boundedness results; they do not give an exact theorem for Cartesian products of two complete graphs.

A later paper devoted specifically to Cartesian products determines exact odd chromatic numbers for products of paths and cycles and for \(K_m\square P_n\) and \(K_m\square C_n\). Its stated family list does not include \(K_m\square K_n\).

Targeted searches under “rook graph,” “Hamming graph,” “line graph of \(K_{m,n}\),” and “Cartesian product of complete graphs” did not locate an exact neighborhood-parity odd-coloring theorem for the present family. A known exact result for complete multipartite graphs does not subsume rook graphs: except for small degenerate boundaries, \(K_m\square K_n\) is not complete multipartite.

## Limitations
The theorem treats two-dimensional rook graphs only. It does not determine odd chromatic numbers of higher-dimensional Hamming graphs.

The square-family novelty statement begins at \(n=3\), because \(R_{2,2}=C_4\) was already evaluated in the initiating paper.

The explicit cyclic construction proves existence with \(n+2\) colors but does not classify or count all optimal square colorings.

The literature comparison cannot exclude a differently phrased or non-indexed exact treatment of the same family.

## References
1. M. Petruševski and R. Škrekovski, “Colorings with neighborhood parity condition,” arXiv:2112.13710v1, first public version 27 December 2021; Discrete Applied Mathematics 321 (2022), 385–391, DOI 10.1016/j.dam.2022.07.018.
2. V. Dujmović, P. Morin, and S. Odak, “Odd Colourings of Graph Products,” arXiv:2202.12882v1, first public version 25 February 2022.
3. B. Liu, Q. Dou, and F. Yang, “The odd coloring of some Cartesian product graphs,” AIMS Mathematics 11(1) (2026), 1311–1331, DOI 10.3934/math.2026056.
