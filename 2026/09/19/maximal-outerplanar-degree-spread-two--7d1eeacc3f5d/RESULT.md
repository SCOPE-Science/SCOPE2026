# Exact degree-spread two for maximal outerplanar graphs

## Result

For a graph \(G\), let \(n_d\) be the number of vertices of degree \(d\), and define
\[
\operatorname{sp}(G,2)=\max_{p\ge 0}(n_p+n_{p+1}+n_{p+2}).
\]
For \(n\ge 3\), write
\[
\operatorname{MOP}(n,2)=\min\{\operatorname{sp}(G,2):G\text{ is a maximal outerplanar graph on }n\text{ vertices}\}.
\]

The exact value is determined for every \(n\ge 5\):
\[
\boxed{
\operatorname{MOP}(n,2)=
\left\lceil\frac{4n+10}{9}\right\rceil
+\mathbf 1_{\{5,6,7,8,11,13\}}(n).
}
\]
In particular,
\[
\boxed{
\operatorname{MOP}(n,2)=\left\lceil\frac{4n+10}{9}\right\rceil
\qquad(n\ge 14).
}
\]

The small values are

| \(n\) | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\operatorname{MOP}(n,2)\) | 5 | 5 | 6 | 6 | 6 | 6 | 7 | 7 | 8 | 8 | 8 | 9 | 9 | 10 | 10 |

## Context

Caro, Škrekovski and Zarb prove in arXiv:2609.19762v1 that every maximal outerplanar graph of order \(n\ge 5\) satisfies
\[
\operatorname{sp}(G,2)\ge \left\lceil\frac{4n+10}{9}\right\rceil.
\]
They construct equality examples for \(n\equiv2\pmod{18}\), and prove the general upper bound
\[
\operatorname{MOP}(n,2)\le \left\lceil\frac{4n+10}{9}\right\rceil+43.
\]
The same paper reports computer-checked caps for the other residue classes over a finite range and states that presumably the lower bound is exact for every \(n\ge14\), but it does not prove that universal equality statement. The result above proves it and also determines the remaining orders \(5\le n\le13\).

## Boundary-ear extension lemma

Let \(G\) be a triangulation of a convex \(N\)-gon and let \(uv\) be a boundary edge. Insert a new boundary vertex \(w\) between \(u\) and \(v\), retain \(uv\), and add \(uw,wv\). The resulting graph is a triangulation of a convex \((N+1)\)-gon, hence is maximal outerplanar. On degrees, the operation is
\[
(\deg u,\deg v)\longmapsto(\deg u+1,2,\deg v+1).
\]
We call this a boundary-ear insertion.

## Uniform construction for every residue class

Caro–Škrekovski–Zarb construct, for every \(k\ge1\), a maximal outerplanar graph \(H_k\) of order \(18k+2\) with degree counts
\[
 n_2=8k,\qquad n_3=2,\qquad n_5=8k,\qquad n_6=2,\qquad n_8=2k-2,
\]
and no other degrees. Thus \(\operatorname{sp}(H_k,2)=8k+2\).

Use their cyclic labelling \(0,1,\ldots,18k+1\) and put \(c=9k-9\). During the insertions below, positions refer to the *current* cyclic boundary order. An entry \(q\) means insert an ear on the boundary edge whose left endpoint currently has position \(c+q\). In the row \(r=9\), an entry \(N-q\) instead means the boundary edge whose left endpoint has current position \(N-q\), where \(N\) is the current order before that insertion.

For \(0\le r\le17\), apply the following \(r\)-step word to \(H_k\):

| \(r\) | insertion positions |
|---:|:---|
|0|—|
|1|8|
|2|8, 10|
|3|8, 10, 11|
|4|9, 9, 10, 12|
|5|8, 8, 7, 11, 10|
|6|8, 8, 7, 11, 10, 2|
|7|8, 10, 8, 9, 8, 12, 9|
|8|8, 10, 8, 9, 8, 12, 9, 16|
|9|\(c+9,c+9,N-2,N-3,N-2,N-6,N-4,c+10,c+12\)|
|10|8, 8, 8, 8, 12, 11, 8, 11, 10, 8|
|11|9, 9, 10, 12, 10, 9, 12, 13, 13, 12, 11|
|12|8, 8, 8, 8, 12, 11, 8, 11, 10, 8, 10, 2|
|13|8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9|
|14|8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2|
|15|8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 4|
|16|8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 4, 5|
|17|8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 2, 1, 5|

For rows other than \(r=9\), the displayed integers are understood in the default \(c+q\) convention. Every step is a boundary-ear insertion, so maximal outerplanarity is automatic.

A direct local degree update gives the following four potentially dominant windows, written after subtracting \(8k\):

| \(r\) | \(W_{[2,4]}-8k\) | \(W_{[3,5]}-8k\) | \(W_{[4,6]}-8k\) | \(W_{[5,7]}-8k\) | maximum |
|---:|---:|---:|---:|---:|---:|
|0|2|2|2|2|2|
|1|3|3|3|2|3|
|2|3|3|2|3|3|
|3|4|4|2|2|4|
|4|4|4|3|3|4|
|5|4|4|5|5|5|
|6|5|5|4|5|5|
|7|5|5|5|6|6|
|8|6|6|5|5|6|
|9|6|6|6|6|6|
|10|7|7|7|6|7|
|11|7|6|7|7|7|
|12|8|8|7|7|8|
|13|8|8|8|8|8|
|14|9|9|9|8|9|
|15|9|9|8|9|9|
|16|10|10|8|8|10|
|17|10|10|10|10|10|

No degree above \(8\) is created. The remaining windows are at most \(2k+2\), hence are smaller than the displayed maxima for \(k\ge1\). If
\[
 b_r=\left\lceil\frac{18+4r}{9}\right\rceil,
\]
the last column is exactly \(b_r\). Therefore the graph produced from \(H_k\) has order
\[
 n=18k+2+r
\]
and
\[
\operatorname{sp}(G,2)=8k+b_r
=\left\lceil\frac{4n+10}{9}\right\rceil.
\]
This proves the upper bound for every \(n\ge20\). Together with the known lower bound, equality follows for all such orders.

## Orders 14 through 19

The verification artifact contains explicit noncrossing chord sets for convex \(n\)-gons for each \(14\le n\le19\). Each set contains exactly \(n-3\) chords, hence triangulates the polygon. Their degree sequences are:

| \(n\) | degree sequence | \(\operatorname{sp}(G,2)\) |
|---:|:---|---:|
|14|\(2^6 4^2 5^6\)|8|
|15|\(2^6 3^2 5^6 6\)|8|
|16|\(2^6 3^2 4 5^6 6\)|9|
|17|\(2^7 3 4 5^7 6\)|9|
|18|\(2^7 3 4^2 5^7 6\)|10|
|19|\(2^8 3 4 5^7 6^2\)|10|

These values equal \(\lceil(4n+10)/9\rceil\), completing the proof for \(n\ge14\).

## Orders 5 through 13

For the finite range \(5\le n\le13\), the standalone verifier exhausts all triangulations of a convex \(n\)-gon. The recursion is canonical: the triangle incident with the boundary edge \(0(n-1)\) has a unique third vertex \(j\), and choosing \(j\) splits the triangulation into independent triangulations of the two resulting subpolygons. Hence the recursion enumerates every triangulation. The counts obtained are the Catalan numbers
\[
5,14,42,132,429,1430,4862,16796,58786
\]
for \(n=5,\ldots,13\), respectively.

Computing \(\operatorname{sp}(G,2)\) from each degree sequence gives
\[
5,5,6,6,6,6,7,7,8,
\]
which yields the six exceptional orders in the boxed formula. Explicit triangulations attaining each value are also included and independently checked in the artifact.

## Verification

`artifacts/verify_mop_spread.py` uses only the Python standard library. It:

- exhaustively enumerates all triangulations for \(5\le n\le13\) and reproduces the Catalan counts and exact minima;
- checks explicit noncrossing triangulations for every \(5\le n\le19\);
- reconstructs the published \(H_k\) ladder from its chord description;
- applies all eighteen ear templates and checks the degree-count changes and exact three-degree-window maxima for \(1\le k\le50\).

The saved output is `artifacts/verification.txt`. The finite checks support the explicit constructions; the proof for all \(n\ge14\) is the boundary-ear argument above together with the published lower bound.

## Originality scope and limitations

The claim of originality is limited to the proof of the universal exact formula and the complete small-order determination, to the best of our knowledge. The 2026 source already conjectures/presumes the \(n\ge14\) formula and explicitly reports that seventeen additional residue-class caps were found computationally. Accordingly, no originality is claimed for the general idea of changing an end cap or for the existence of residue-specific caps as such.

The supplementary material mentioned in arXiv:2609.19762v1 was not inspected. It is the most plausible source of overlap because it reportedly contains the authors' seventeen caps and finite verification. The main paper itself describes those computations as covering a finite range, states the all-\(n\) formula only as a presumption, and proves only the \(n\equiv2\pmod{18}\) equality plus an additive-43 upper bound. If the supplementary material contains an unadvertised uniform proof rather than finite verification, that would reduce or eliminate the originality of the \(n\ge14\) part. The exact \(5\le n\le13\) values are not stated in the inspected main paper.

The proof for \(5\le n\le13\) is computer-assisted, by exhaustive enumeration of polygon triangulations. The universal \(n\ge14\) theorem is not based on exhaustive enumeration.

## References

1. Y. Caro, R. Škrekovski, C. Zarb, *Spreads of degrees in graphs*, arXiv:2609.19762v1 (2026), https://arxiv.org/abs/2609.19762.
2. Y. Caro, J. Lauri, C. Zarb, *Notes on spreads of degrees in graphs*, Bulletin of the ICA **85** (2019), 79–91; arXiv:1806.08303, https://arxiv.org/abs/1806.08303.
