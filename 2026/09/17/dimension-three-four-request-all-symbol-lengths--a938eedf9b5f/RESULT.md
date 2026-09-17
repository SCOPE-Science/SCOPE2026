# Exact dimension-three four-request all-symbol code lengths

## Statement

Let \(q\) be a prime power.  With the notation of Boruchovsky--Gruica--Niemann--Yaakobi for minimum lengths of four-request all-symbol PIR and batch codes,
\[
\boxed{
ASP(3,4,q)=ASB(3,4,q)=
\begin{cases}
7,&\operatorname{char}(\mathbb F_q)=2,\\
8,&\operatorname{char}(\mathbb F_q)\ne2.
\end{cases}}
\]

The characteristic-two case is Proposition 24 of *Serving Every Symbol: All-Symbol PIR and Batch Codes*.  The new part is the odd-characteristic lower bound \(ASP(3,4,q)\ge8\), which closes the one-column gap left by their Theorem 23 at \(k=3\).  Their Lemma 22 already gives the matching odd-characteristic upper bound \(ASB(3,4,q)\le8\).

Thus dimension three exhibits a sharp characteristic dependence: seven servers are optimal in characteristic two, while every odd-characteristic field requires eight.

## Definitions

For a full-rank generator matrix \(G=(g_1,\ldots,g_n)\in\mathbb F_q^{k\times n}\), a set \(R\subseteq[n]\) is a recovery set for \(v\in\mathbb F_q^k\) if \(v\) lies in the span of \(\{g_j:j\in R\}\).  A four-all-symbol PIR matrix requires four pairwise disjoint recovery sets for four copies of every column \(g_i\).  A four-all-symbol batch matrix requires disjoint recovery sets for every multiset of four columns.  The corresponding minimum lengths are denoted \(ASP(k,4,q)\) and \(ASB(k,4,q)\).

## Proof of the odd-characteristic lower bound

Assume that \(q\) is odd and, for contradiction, that there is a rank-three four-all-symbol PIR matrix
\[
G=(g_1,\ldots,g_7)\in\mathbb F_q^{3\times7}.
\]
The known dimension-two value is \(ASP(2,4,q)=6\).  Hence the assumed equality \(ASP(3,4,q)=7=ASP(2,4,q)+1\), together with Lemma 16 of Boruchovsky et al., implies that an optimal \(3\times7\) realizing matrix has pairwise distinct columns.

We need a slightly stronger consequence.

### 1. The seven columns are projectively distinct

No column is zero.  Otherwise deleting a zero column preserves rank and preserves every recovery relation for the remaining columns after removing that zero coordinate from recovery sets, producing a length-six four-all-symbol PIR matrix, contrary to the lower bound \(ASP(3,4,q)\ge7\).

Also no two nonzero columns are proportional.  Indeed, independently multiplying columns by nonzero scalars preserves every subset span and therefore preserves the all-symbol PIR property.  If two columns were proportional, rescale one of them to make the two columns equal.  This would give another length-seven realization with repeated columns, contradicting Lemma 16.

Consequently the columns determine a seven-point set \(S\subset PG(2,q)\).

### 2. Every point induces a perfect matching on the other six points

Fix \(p\in S\).  There are four pairwise disjoint recovery sets for four copies of \(p\).  We may take one recovery set to be the singleton \(\{p\}\): if one of the original recovery sets contains the coordinate of \(p\), replace it by that singleton; if none does, add the singleton and retain any three of the original four recovery sets.

The other three recovery sets avoid \(p\).  Since the seven columns are projectively distinct, none of these sets can be a singleton.  Only six coordinates remain, so the three disjoint sets must each have size exactly two and together partition \(S\setminus\{p\}\).  If \(\{a,b\}\) is one of the three pairs, then
\[
p\in\langle a,b\rangle,
\]
so \(p,a,b\) are collinear in \(PG(2,q)\).

Thus, for every \(p\in S\), the other six points split into three pairs, each pair lying with \(p\) on a projective line.

### 3. Every secant contains an odd number of selected points

Let \(L\) be a line through \(p\in S\).  In the matching associated with \(p\), every point \(a\in (L\cap S)\setminus\{p\}\) must be paired with another selected point on \(L\), because the unique line through \(p\) and \(a\) is \(L\).  Therefore
\[
|(L\cap S)\setminus\{p\}|\quad\text{is even}.
\]
Hence every line determined by two points of \(S\) contains an odd number of points of \(S\).  Since \(S\) has rank three, such a line cannot contain all seven points, so its intersection size is either three or five.

A five-point line is impossible.  Suppose \(L\) contains five points of \(S\), leaving two points \(x,y\notin L\).  For any \(a\in L\cap S\), the line \(xa\) contains at least two selected points and hence, by the odd-intersection property, must contain a third selected point.  It meets \(L\) only at \(a\), so that third point must be \(y\).  Thus \(x,y,a\) would be collinear for all five choices of \(a\), whereas the line \(xy\) meets \(L\) in only one point.  Contradiction.

Therefore every pair of points of \(S\) lies on a line containing exactly three points of \(S\).  The resulting triples form the unique Steiner triple system on seven points, namely the Fano-plane incidence structure.

### 4. The Fano incidence cannot occur in odd characteristic

For completeness, this obstruction can be checked directly.  Choose three noncollinear points and use projective coordinates
\[
p_1=(1,0,0),\qquad p_2=(0,1,0),\qquad p_3=(0,0,1).
\]
Write the Fano triples so that
\[
\{p_1,p_2,p_4\},\quad
\{p_1,p_3,p_5\},\quad
\{p_2,p_3,p_6\},\quad
\{p_4,p_5,p_6\}
\]
are lines.  Rescaling coordinates lets us take
\[
p_4=(1,1,0),\qquad p_5=(1,0,1),\qquad p_6=(0,1,\lambda).
\]
Collinearity of \(p_4,p_5,p_6\) gives \(\lambda=-1\).

The remaining Fano triples include
\[
\{p_1,p_6,p_7\},\qquad
\{p_2,p_5,p_7\},\qquad
\{p_3,p_4,p_7\}.
\]
The first two force
\[
p_7\sim(1,-1,1).
\]
But every point of the line through \(p_3=(0,0,1)\) and \(p_4=(1,1,0)\) has equal first and second coordinates.  Thus the third triple forces \(1=-1\), which is possible only in characteristic two.

This contradicts the assumption that \(q\) is odd.  Hence
\[
ASP(3,4,q)\ge8\qquad(q\text{ odd}).
\]

Boruchovsky et al. construct, for every odd \(q\), the length-eight four-all-symbol batch matrix
\[
\begin{pmatrix}
1&0&0&-1&-1&0&1&1\\
0&1&0&-1&0&-1&1&1\\
0&0&1&0&-1&-1&1&1
\end{pmatrix},
\]
so \(ASB(3,4,q)\le8\).  Since \(ASP\le ASB\), both quantities equal eight for odd \(q\).  Combining this with their characteristic-two Proposition 24 proves the displayed classification.

## Verification

The accompanying script `artifacts/verify_small_fields.py` performs two finite sanity checks:

- it exhaustively verifies the displayed length-eight matrix against every four-request multiset over \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\);
- it enumerates all spanning seven-point subsets of \(PG(2,3)\) and confirms that none has the per-point perfect-matching property forced by a hypothetical length-seven realization.

These computations support the proof but are not used as substitutes for the general argument.

## Relation to prior work and originality boundary

Boruchovsky, Gruica, Niemann and Yaakobi introduced the all-symbol batch notion and systematically studied all-symbol PIR codes.  Their Theorem 23 leaves, for odd \(q\) and \(k=3\), exactly the interval
\[
7\le ASP(3,4,q)\le ASB(3,4,q)\le8,
\]
while Proposition 24 proves the exact value seven in characteristic two.  Their concluding section explicitly lists exact \(t=4\) values and alphabet dependence as open directions.

The obstruction used here is classical: the Fano matroid is representable over a field if and only if the field has characteristic two.  No originality is claimed for that matroid fact.  The contribution is the reduction from a hypothetical optimal length-seven four-all-symbol PIR code to the Fano incidence structure, yielding the exact odd-characteristic value and hence the complete dimension-three classification.

Searches were made under the exact `ASP/ASB` notation, the phrases “all-symbol PIR”, “all-symbol batch”, “disjoint repair group”, and equivalent Fano/projective-geometry terminology.  No earlier source establishing this exact parameter value was located.  Older disjoint-repair-group and majority-logic-decoding literature is a residual originality risk because the all-symbol PIR property overlaps those frameworks, although the 2026 source paper itself treats the odd-characteristic \(t=4\) value as unresolved.

## References

1. A. Boruchovsky, A. Gruica, J. Niemann and E. Yaakobi, *Serving Every Symbol: All-Symbol PIR and Batch Codes*, arXiv:2601.04041v2 (2026); ISIT 2026, DOI: 10.1109/ISIT62367.2026.11653879. https://arxiv.org/abs/2601.04041
2. R. Li and M. Wootters, *Lifted Multiplicity Codes and the Disjoint Repair Group Property*, APPROX/RANDOM 2019, LIPIcs 145, Article 38. DOI: 10.4230/LIPIcs.APPROX-RANDOM.2019.38. https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.38
3. M. A. Mendez, A. Rincón and J. A. de la Peña, *Completion and decomposition of a clutter into representable matroids*, Linear Algebra and its Applications 478 (2015), 120--143. The paper records the standard fact that the Fano matroid is representable exactly in characteristic two. https://doi.org/10.1016/j.laa.2015.01.023
