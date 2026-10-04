# Complete ternary dimension-three locality-\(2\) length profile
## Finding
Let \(n_3(3,d,2)\) denote the minimum length of a ternary linear code of dimension \(3\), minimum Hamming distance at least \(d\), and all-symbol locality at most \(2\). Then
\[
n_3(3,1,2)=n_3(3,2,2)=5,\qquad n_3(3,3,2)=6,
\]
and for every integer \(d\ge 4\),
\[
n_3(3,d,2)=g_3(3,d)
=d+\left\lceil\frac d3\right\rceil+\left\lceil\frac d9\right\rceil .
\]
Thus \(d=4\) is the sharp threshold from which locality \(2\) costs no length beyond the ternary Griesmer bound in dimension three.

## Assumptions and scope
The definition is the standard one for linear all-symbol locally recoverable codes: every code coordinate is recoverable from at most two other coordinates. Generator columns are represented as a spanning multiset of points of \(\mathrm{PG}(2,3)\). For such a multiset \(M\) of total multiplicity \(n\), the code has distance at least \(d\) exactly when every projective line has multiplicity at most \(n-d\).

The locality criterion used here is the geometric criterion for locality \(2\): a positive-multiplicity point either has multiplicity at least two, or lies on a projective line containing at least two other positive-multiplicity points.

## Proof
The general lower bound is immediate from the ternary Griesmer bound:
\[
n_3(3,d,2)\ge d+\left\lceil\frac d3\right\rceil+\left\lceil\frac d9\right\rceil .
\]

Write \(U\) for the full \(13\)-point set of \(\mathrm{PG}(2,3)\), and fix a line \(L\). Choose distinct points \(a,b\notin L\), a noncollinear triple \(A\), and a \(4\)-arc \(Q\), meaning four points with no three collinear. For \(4\le s\le12\), define the following multisets:
\[
\begin{array}{c|c}
s & B_s\\ \hline
4&U\setminus(L\cup\{a,b\})\\
5&U\setminus(L\cup\{a\})\\
6&U\setminus L\\
7&U\setminus\{a,b\}\\
8&U\setminus\{a\}\\
9&U\\
10&U+A\\
11&U+Q\\
12&2(U\setminus L).
\end{array}
\]
Here addition and scalar multiplication mean addition and scaling of point multiplicities.

Each \(B_s\) spans \(\mathrm{PG}(2,3)\), has cardinality
\[
|B_s|=s+\left\lceil\frac s3\right\rceil+\left\lceil\frac s9\right\rceil,
\]
and has maximum line multiplicity \(|B_s|-s\). For \(s=4,5,6\), every line other than \(L\) contributes at most its three affine points. For \(s=7,8,9\), every projective line has at most four points. In \(U+A\), noncollinearity of \(A\) limits the added line multiplicity to two; in \(U+Q\), the \(4\)-arc property does the same. In \(2(U\setminus L)\), every line other than \(L\) has multiplicity six. Therefore the corresponding codes have distances \(s\).

These base multisets also have locality \(2\). For \(B_4,B_5,B_6\), through any retained affine point there are four affine lines, while deleting one or two affine points can spoil at most one or two of those lines; hence a retained point lies on a line with two other retained points. The same argument applies to \(B_7,B_8\). The multiset \(B_9\) has full projective support, as do \(B_{10}\) and \(B_{11}\); any line through a point then supplies two other supported points. Every point of \(B_{12}\) has multiplicity two.

Now let \(d\ge4\), set
\[
s=4+((d-4)\bmod 9),\qquad t=\frac{d-s}{9},
\]
so that \(4\le s\le12\) and \(t\ge0\). Take
\[
M=tU+B_s.
\]
The full projective plane has \(13\) points and every line has \(4\) points, so adding one copy of \(U\) increases length by \(13\) and distance by \(9\). Since
\[
g_3(3,d+9)=g_3(3,d)+13,
\]
the multiset \(M\) has length \(g_3(3,d)\), distance \(d\), and locality \(2\). This meets the Griesmer lower bound for every \(d\ge4\).

It remains to settle \(d\le3\). Two distinct projective lines meeting at \(P\), with one non-\(P\) point deleted from each line, give a five-point spanning set of distance \(2\) and locality \(2\). Hence the same length also works for distance \(1\). No dimension-three length-four code has locality \(2\): its dual has dimension one, so all nonzero dual words have the same support, while all-symbol locality \(2\) would require every coordinate to be covered by a dual word of weight at most three. Covering all four coordinates would force that unique support to have weight four.

For \(d=3\), the union of two distinct projective lines with their intersection removed is a six-point spanning set; each of the two lines contains three selected points, every other line contains at most two, and locality \(2\) is immediate. A ternary \([5,3,3]\) code cannot exist: a rank-two parity-check matrix would need five nonzero, pairwise nonproportional columns, but \(\mathbb F_3^2\) has only four one-dimensional subspaces. Therefore the three small values are exact.

## Verification
The standalone verifier builds all \(13\) points and all \(13\) lines of \(\mathrm{PG}(2,3)\) directly over \(\mathbb F_3\). It instantiates every base multiset \(B_s\), checks spanning rank, cardinality, line-derived distance, direct codeword distance, and the locality-\(2\) condition. It also checks the distance-\(2\) and distance-\(3\) witnesses, the four projective one-spaces in \(\mathbb F_3^2\), and the lifted construction for every \(4\le d\le1000\).

The finite checks corroborate the explicit constructions. The all-\(d\) conclusion itself is proved by the nine-residue construction and the exact recurrence \(g_3(3,d+9)=g_3(3,d)+13\), not by extrapolating the finite test range.

## Relationship to prior work
Kurz defines \(n_q(k,d,r)\), gives the geometric locality criterion used above, and proves the Griesmer lower bound together with eventual equality for fixed parameters when \(d\) is sufficiently large. The same paper exactly determines all binary locality-\(2\) values for dimensions up to seven, but states only selected ternary numerical results; its ternary dimension-three theorem concerns locality \(1\), not locality \(2\).

Hao, Xia, and Chen classify ternary LRCs meeting the Singleton-like bound. Their classification includes the dimension-three locality-\(2\) cases with distances \(2\) through \(6\), so those initial values are not claimed as previously unknown. Their result is restricted to Singleton-optimal LRCs and does not imply the all-distance length function above. In particular, it does not cover the Griesmer-optimal continuation from \(d=7\) onward.

Targeted searches under the native \(n_3(3,d,2)\) notation, dimension-three ternary locality-\(2\) language, Griesmer-equality language, and the projective-plane formulation did not locate a published complete all-distance formula. This is evidence of non-coverage rather than proof that no unindexed prior observation exists.

## Limitations
The result is for ternary linear codes with all-symbol locality at most \(2\). It does not classify all optimal generator multisets, address nonlinear LRCs, or determine higher dimensions or smaller locality. The originality comparison is limited by indexing and terminology: an unindexed thesis, note, or equivalent projective-geometric formulation could contain the same all-distance construction.

## References
1. S. Kurz, “Bounds on the minimum distance of locally recoverable codes,” arXiv:2401.00418, first public version 2023-12-31; Mathematics Subject Classification 94B27, 94B05.
2. J. Hao, S.-T. Xia, and B. Chen, “On Optimal Ternary Locally Repairable Codes,” arXiv:1702.05730, first public version 2017-02-19.
