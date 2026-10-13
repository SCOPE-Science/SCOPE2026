# Complete higher-support geometry of a ternary \([25,5,14]_3\) LCD code

## Finding

Let \(C\) be the ternary \([25,5,14]_3\) Euclidean linear complementary-dual (LCD) code \(\mathcal C_{3,4}\) specified by the generator matrix below, appearing in Proposition 4.1 of An–Hong–Kim–Lim. For \(1\le r\le5\), write \(N_r(s)\) for the number of \(r\)-dimensional subcodes of \(C\) whose union of coordinate supports contains exactly \(s\) coordinates. The **entire higher-support census** is:

| \(r\) | Nonzero values \(s:N_r(s)\) |
|---|---|
| \(1\) | \(14:11,\ 15:28,\ 16:31,\ 17:16,\ 18:10,\ 19:12,\ 20:6,\ 21:2,\ 22:2,\ 23:3\) |
| \(2\) | \(19:6,\ 20:87,\ 21:291,\ 22:326,\ 23:216,\ 24:205,\ 25:79\) |
| \(3\) | \(22:15,\ 23:255,\ 24:445,\ 25:495\) |
| \(4\) | \(24:25,\ 25:96\) |
| \(5\) | \(25:1\) |

In particular the generalized Hamming-weight hierarchy is \((d_1,d_2,d_3,d_4,d_5)=(14,19,22,24,25)\). Exactly **six** two-dimensional subcodes attain \(d_2=19\), meeting the general elementary ternary lower bound. With positions numbered \(1\) through \(25\), their **six-coordinate common-zero sets** are precisely

\[
\begin{gathered}
\{2,4,12,16,22,24\},\quad\{2,5,18,20,21,25\},\\
\{2,6,12,15,22,23\},\quad\{2,11,12,20,21,22\},\\
\{2,17,19,20,21,23\},\quad\{3,8,14,20,23,24\}.
\end{gathered}
\]

These are the six maximum six-point intersections of the \(25\) projective generator columns with projective planes in \(\operatorname{PG}(4,3)\). Five of the six planes contain the generator point at coordinate \(2\), while no other coordinate belongs to five of them. Among the fifteen plane-pair intersections with the selected column set, seven contain one selected point, two contain two, and six contain three.

## Assumptions and scope

All calculations are over \(\mathbb F_3=\{0,1,2\}\), with ordinary arithmetic reduced modulo \(3\). The code is **exactly** the row span of the following \(5\)-by-\(25\) generator, transcribed from the cited original preprint. Each line is one row; the first twenty and last five entries are separated by a space only for readability:

```text
10000220001102111221 21020
01000002221001121111 12121
00100212202022200211 20200
00010202111222011010 02100
00001111021120010111 21222
```

The first row is, for example, the \(25\)-tuple \((1,0,0,0,0,2,2,0,0,0,1,1,0,2,1,1,1,2,2,1,2,1,0,2,0)\). There are no hypotheses about other generators or about all LCD codes of these parameters. Supports count coordinates on which **at least one** word in the subcode is nonzero; coordinate multiplicities and projective-plane comparisons use this fixed order.

## Proof

The displayed matrix has rank \(5\), and its Gram matrix \(GG^\top\) has rank \(5\) over \(\mathbb F_3\). Thus its row span is LCD. Direct enumeration of all \(3^5=243\) words gives its ordinary weight distribution
\[
W_C(z)=1+22z^{14}+56z^{15}+62z^{16}+32z^{17}+20z^{18}+24z^{19}+12z^{20}+4z^{21}+4z^{22}+6z^{23}.
\]
In particular, its minimum nonzero distance is \(14\), as stated by An–Hong–Kim–Lim. Since each one-dimensional subcode has exactly two nonzero words of equal weight, halving the nonconstant coefficients proves the first row of the support table.

Each \(r\)-space in \(\mathbb F_3^5\) has a **unique** reduced-row-echelon basis. List all increasing pivot sequences and assign all \(0,1,2\) entries strictly to the right of their pivots in nonpivot columns. These enumerate each space exactly once. For such a basis matrix \(A\), let \(P_j\) be the \(j\)-th column of \(G\). Coordinate \(j\) lies outside the subcode support if and only if \(A P_j=0\). Therefore
\[
 |\operatorname{Supp}(\operatorname{rowspan}(AG))|
 =25-\#\{j\in\{1,\ldots,25\}:A P_j=0\}.
\]
The exact, finite \(\mathbb F_3\) enumeration checks respectively \(121,1210,1210,121,1\) spaces in dimensions \(1,2,3,4,5\), giving the five table rows. These totals are the Gaussian coefficients \(\left[{5\atop r}\right]_3\), independently matching the enumeration counts; `verify.py` contains the complete enumeration, expected counts, and assertions. Since all \(25\) projective columns are nonzero and pairwise distinct, the \(25\) four-space supports missing precisely one column also follow geometrically.

For a two-dimensional ternary subcode \(U\), its four distinct projective nonzero codewords have the property that every occupied coordinate is nonzero in exactly three of these four words. Hence
\[
3\,|\operatorname{Supp}(U)|=\sum_{[u]\in\operatorname{PG}(U)}\operatorname{wt}(u)\ge4\cdot14=56,
\]
so every such \(U\) has support size at least \(19\). The census gives six attaining \(19\); in each, the four projective nonzero-word weights, sorted, equal \((14,14,14,15)\). This proves tightness without mistaking sampling for an infinite bound.

Duality of finite-dimensional vector spaces sends any two-dimensional coefficient space \(U\le\mathbb F_3^5\) to a three-dimensional annihilator \(U^\perp\). Its projectivization is a plane in \(\operatorname{PG}(4,3)\), and the coordinates missing from the subcode support are precisely the generator columns lying on this plane. Enumerating every three-dimensional coefficient subspace separately gives, by number \(t\) of its incident selected points, the incidence histogram
\[
(t\mapsto \#\text{planes})=(0:79,1:205,2:216,3:326,4:291,5:87,6:6).
\]
This independently reproduces the dimension-two support census, with \(s=25-t\). The same incidence computation identifies the six planes' exact intersections and their coordinate multiplicities as asserted above. All checks use integer and finite-field arithmetic, not floating-point tolerances.

## Verification

Run `python3 verify.py` with an ordinary Python 3 installation; only its standard library is used. It rebuilds the transcribed generator, checks the rank and LCD Gram criterion, exhaustively enumerates all \(243\) codewords and all \(2663\) nonzero-dimensional coefficient subspaces, recomputes every support census entry, independently enumerates the \(1210\) projective planes, checks their six maximal intersections and pairwise intersection counts, and prints `VERIFY_OK` only when all assertions hold.

## Relationship to prior work

An, Hong, Kim, and Lim (2026), Proposition 4.1, explicitly construct this \([25,5,14]_3\) LCD code using shortest LCD embeddings; their work supplies the generator and minimum-distance context but does not state its higher-dimensional subcode support counts or the six-maximum-plane incidence configuration. Anderssen and Johnsen (2026) explain general matroid methods for determining generalized weight polynomials, with a projective Reed–Muller example; a general method to compute these invariants does not itself imply the explicit values or the six geometric witnesses for this different code. The first higher weight is a standard invariant beyond ordinary minimum distance; here the natural complete census identifies all minimal two-dimensional support configurations, not merely their minimum numerical value.

## Limitations

The statement concerns only the fixed, displayed \(25\)-coordinate code, not all ternary \([25,5,14]\) LCD codes or equivalent families with different generators. Exhaustiveness comes from the finite RREF parametrization and a separately checked dual-plane census; it is not a claim of new general coding-theory inequalities. Literature searches cannot rule out every unpublished, differently indexed, or inaccessible account of the same exact spectrum. No independent audit has been performed.

## References

1. J. An, J.-H. Hong, J.-L. Kim, H. Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600v1 (first public 2026-01-28), Proposition 4.1. https://arxiv.org/html/2601.20600v1
2. J. Anderssen, T. Johnsen, *Generalized Weight Polynomials of Codes through Flats and Orlik-Solomon Algebras of Matroids*, arXiv:2609.29796v1 (first public 2026-09-24). https://arxiv.org/abs/2609.29796
