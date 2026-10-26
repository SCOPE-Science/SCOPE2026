# Sharp closed-neighborhood VC dimension of Cartesian products of cliques

## Finding

Let \(d\ge 1\) and let \(A_1,\ldots,A_d\) be finite nonempty symbol sets with \(q_i=|A_i|\ge 2\). In the Cartesian product \(X=A_1\times\cdots\times A_d\), write \(\operatorname{dist}_H(x,y)\) for the number of coordinates in which two words disagree. Consider the closed radius-one balls
\[
B_1(c)=\{x\in X:\operatorname{dist}_H(x,c)\le1\},\qquad \mathcal B=\{B_1(c):c\in X\}.
\]
Equivalently these are the closed neighborhoods of the graph \(K_{q_1}\square\cdots\square K_{q_d}\). Then their exact VC dimension is
\[
\operatorname{VCdim}(X,\mathcal B)=
\begin{cases}
0,&d=1,\\
1,&d=2\text{ and }q_1=q_2=2,\\
3,&d=2,\ \min(q_1,q_2)\ge3\text{ and }\max(q_1,q_2)\ge4,\\
2,&d=2\text{ in every other case},\\
3,&d\ge3.
\end{cases}
\]
In particular, all products of at least three nontrivial cliques have closed-neighborhood VC dimension exactly three, including the binary three-cube; neither the dimension nor any alphabet size needs to be fixed in advance.

## Assumptions and scope

There are no restrictions on the symbol sets beyond \(q_i\ge2\). A set \(S\subseteq X\) is *shattered* when every \(T\subseteq S\) occurs as \(T=S\cap B_1(c)\) for some \(c\in X\). Empty traces must be realized by actual centers in \(X\). The term *closed neighborhood* includes the center itself and must not be confused with the open neighborhoods of the Hamming graph. The claim concerns the full product, not an arbitrary induced subgraph.

## Proof

**1. Universal upper bound three.** Suppose \(S\) is shattered and \(|S|=4\). The all-positive trace gives a center \(a\in X\) with \(S\subseteq B_1(a)\). Every point of this ball is either \(a\) itself or lies on exactly one of the coordinate lines through \(a\). Call the latter points *arms*, and group them by the coordinate in which they differ from \(a\).

First, \(S\) cannot lie on a single coordinate line \(L\) through \(a\). Indeed, for any center \(c\), the trace \(B_1(c)\cap L\) is either the entire line, a singleton, or empty. It cannot realize a two-element proper trace on a four-point subset of \(L\).

Otherwise there are arms in at least two coordinate groups. Since \(|S|=4\), at least three elements of \(S\) are arms. Choose three of these arms involving at least two groups. They are either in three distinct groups or consist of two in one group and one in another. In both situations **the only radius-one ball containing all three has center \(a\)**:

* For three arms in three distinct groups, the only common radius-one centers of the first two arms are \(a\) and the word obtained by combining their two changed coordinates. The latter word is at distance three from the third arm.
* For two distinct arms on the same coordinate line \(L\), every common radius-one center lies on \(L\); the third arm, on a different coordinate line through \(a\), has distance at most one from exactly one point of \(L\), namely \(a\).

Thus the trace containing exactly these three arms cannot be realized: its unique possible center \(a\) also contains the remaining fourth member of \(S\). This contradiction proves \(\operatorname{VCdim}\le3\) for all products.

**2. Three or more coordinates.** Choose two distinct symbols called \(0\) and \(1\) in the first three coordinates, and fix an arbitrary symbol \(0\) in every other coordinate. Write \(o\) for the all-zero word, \(e_i\) for the word differing from \(o\) only in coordinate \(i\), and \(e_i+e_j\) (respectively \(e_1+e_2+e_3\)) for the word with symbol \(1\) at the indicated coordinates. The set \(S=\{o,e_1,e_2\}\) is shattered. The eight targets and suitable ball centers are

| Desired trace on \(S\) | Center |
|---|---|
| \(\{o,e_1,e_2\}\) | \(o\) |
| \(\{o,e_1\}\) | \(e_1\) |
| \(\{o,e_2\}\) | \(e_2\) |
| \(\{e_1,e_2\}\) | \(e_1+e_2\) |
| \(\{o\}\) | \(e_3\) |
| \(\{e_1\}\) | \(e_1+e_3\) |
| \(\{e_2\}\) | \(e_2+e_3\) |
| \(\varnothing\) | \(e_1+e_2+e_3\) |

All inclusions and exclusions follow by distances zero, one, or at least two. With Step 1, the dimension equals three for every \(d\ge3\).

**3. Two coordinates: the upper restriction.** Identify \(X=A_1\times A_2\) with a rectangular chessboard. A closed ball is exactly the union of one complete row and one complete column (a *cross*). Suppose three points form a shattered set \(S\). Since an all-positive trace is required, all three lie in some cross. They cannot all lie in one row or column: a cross meets a fixed row or column in the entire line or in at most one point, so the two-point trace would be missing.

Hence, after possibly interchanging row and column coordinates, two points share a row \(r\), and the third lies in another row \(s\). If the third shares a column with either of the first two, the three points form an L: the point at the intersection of the repeated row and repeated column cannot be isolated by any cross, because every cross containing it includes either the other point in its row or the other point in its column. This contradicts shattering.

Otherwise the three points occupy two distinct rows and three distinct columns. For a cross to avoid all three (the empty trace), its row must be unused and its column must be unused. This forces at least three rows and four columns. Swapping the roles gives the necessary condition \(\min(q_1,q_2)\ge3\) and \(\max(q_1,q_2)\ge4\).

**4. Two coordinates: sharp witnesses.** If there are at least three rows and four columns, choose the three points \(A=(0,0)\), \(B=(0,1)\), \(C=(1,2)\). The following crosses (specified by row and column of their centers) give all traces:

| Trace | Center |
|---|---|
| \(\{A,B,C\}\) | \((0,2)\) |
| \(\{A,B\}\) | \((0,3)\) |
| \(\{A,C\}\) | \((1,0)\) |
| \(\{B,C\}\) | \((1,1)\) |
| \(\{A\}\) | \((2,0)\) |
| \(\{B\}\) | \((2,1)\) |
| \(\{C\}\) | \((1,3)\) |
| \(\varnothing\) | \((2,3)\) |

When there are four rows and three columns, transpose this configuration. Thus the necessary condition is also sufficient for dimension three.

If both coordinates have size two, each ball contains three of the four vertices. No ball can avoid a two-point subset, so the dimension is at most one; a singleton is shattered, giving dimension one.

In every other two-coordinate case, at least one coordinate has three symbols. Suppose that is the column coordinate. The two points \((0,0)\) and \((0,1)\) are shattered: centers \((0,0)\), \((1,0)\), \((1,1)\), and \((1,2)\) realize both, only the first, only the second, and neither, respectively. Transpose if the row coordinate has three symbols instead. The dimension is therefore two in the remaining cases.

**5. One coordinate.** Every two words differ in at most one coordinate, hence every radius-one ball is all of \(X\). No nonempty set is shattered and the VC dimension is zero. The cases exhaust all parameters. \(\square\)

## Verification

The dependency-free `verify.py` independently forms all vertices and all closed radius-one balls for nineteen Cartesian products, including nonsquare two-factor products, binary three- through five-cubes, and mixed-alphabet three- and four-factor examples. It checks all potential shattered sets of sizes one through four containing a fixed base vertex. This suffices to test existence/nonexistence of a shattered set in each finite instance, since coordinatewise permutations of symbol alphabets act transitively on the vertex set. It verifies the exact formula on each instance and reproduces eight-trace witnesses for representative three-dimensional and rectangular examples. Run `python3 verify.py`. The finite suite does not establish the universal theorem; Steps 1–5 supply the proof.

## Relationship to prior work

Adler, Benediktsson and Macpherson establish the optimal open-neighborhood VC bound of three for Hamming graphs and classify when the open-neighborhood VC dimension equals three [1, Theorems 4.6–4.7]. They note that closed neighborhoods also have bounded VC dimension, but do not give the present exact closed-neighborhood formula. The invariants genuinely differ: the binary three-cube has open-neighborhood VC dimension two by [1, Theorem 4.7], but closed-neighborhood VC dimension three here. Coudert, Csikós, Ducoffe and Viennot develop generic exact algorithms and inequalities for *closed*-neighborhood VC dimension [2], but not this all-parameter Cartesian-product classification. Housholder, Mangiapanello and Senger study the open-neighborhood parameter of Hamming graphs and induced subgraphs [3]; their statements do not imply the closed-neighborhood formula.

## Limitations

The theorem does not claim an exact VC dimension for arbitrary induced subgraphs, Hamming balls of radius greater than one, or Johnson graphs. The argument is mathematical rather than a large finite exhaustive proof. Literature comparison cannot exclude every unindexed equivalent formulation, especially under alternative terminology for unions of rows and columns.

## References

[1] I. Adler, B. G. Benediktsson, and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (first public 2020-07-31), Discrete Applied Mathematics 312 (2022), 29–44; accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/178584/1/Adler_Benediktsson_Macpherson.pdf.

[2] D. Coudert, M. Csikós, G. Ducoffe, and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1 (2024-05-13).

[3] C. Housholder, L. Mangiapanello, and S. Senger, *VC-dimension of subsets of Hamming graphs*, arXiv:2505.14641v1 (2025-05-20).
