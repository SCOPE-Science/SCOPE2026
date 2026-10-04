# Exact graph metric of consecutive-layer S-hypersimplices
## Finding
For every integer \(d\ge 2\) and integers \(0\le a<b\le d\), consider the consecutive-layer S-hypersimplex
\[
P_{d;a,b}=\Delta(d,\{a,a+1,\ldots,b\})
=\operatorname{conv}\{\mathbf 1_A:A\subseteq[d],\ a\le |A|\le b\}.
\]
For two vertices \(\mathbf 1_A,\mathbf 1_B\), write
\[
p=|A|,\qquad q=|B|,\qquad r=|A\cap B|.
\]
Then their distance in the one-skeleton is
\[
\operatorname{dist}(A,B)=\min\!\left\{
 p+q-2r,
 p+q-a-\min(a,r),
 2b-p-q+\max(0,p+q-r-b)
\right\}.
\]
In particular,
\[
\operatorname{diam} P_{d;a,b}=\min\{b,d-a\},
\]
where the diameter refers to the ordinary undirected vertex-edge graph.

## Assumptions and scope
The parameters satisfy \(d\ge2\) and \(0\le a<b\le d\). The result concerns the interval choice \(S=\{a,a+1,\ldots,b\}\), not arbitrary S-hypersimplices. The edge description used below is Theorem 1 of Manecke--Sanyal--So: for consecutive layers, an edge either adds or removes one element between adjacent cardinalities, or swaps one element at a fixed cardinality; such same-layer swap edges occur only at the boundary layers \(a\) and \(b\).

It is useful to name the three displayed candidates. Put
\[
H=p+q-2r,
\qquad
L=p+q-a-\min(a,r),
\qquad
U=2b-p-q+\max(0,p+q-r-b).
\]
The terms correspond respectively to a coordinate-flip route, a route using the bottom Johnson layer, and a route using the top Johnson layer.

## Proof
First construct paths of lengths \(H\), \(L\), and \(U\).

For \(H\), pair as many deletions from \(A\setminus B\) as possible with additions from \(B\setminus A\). Each pair can be performed in two adjacent-layer edges while staying in the cardinality interval: if the current layer is below \(b\), add first and delete second; at layer \(b\), delete first and add second. After all paired changes, the remaining changes are all additions or all deletions and move monotonically from cardinality \(p\) to \(q\). Every differing coordinate is changed exactly once, so the length is \(H=|A\triangle B|\).

For \(L\), descend in \(p-a\) deletion edges to an \(a\)-subset \(C\subseteq A\), use same-layer swaps at level \(a\), and then ascend in \(q-a\) addition edges to \(B\). Choose the two level-\(a\) sets so that their intersection has size \(\min(a,r)\). Their Johnson distance is therefore \(a-\min(a,r)\), giving total length
\[
(p-a)+(a-\min(a,r))+(q-a)=L.
\]
Such choices exist: if \(r\ge a\), use a common \(a\)-subset of \(A\cap B\); if \(r<a\), retain all \(r\) common elements and complete independently from \(A\setminus B\) and \(B\setminus A\).

For \(U\), ascend to \(b\)-supersets \(C\supseteq A\) and \(D\supseteq B\), use top-layer swaps, and descend to \(B\). If \(|A\cup B|\le b\), take a common \(b\)-superset and use no swaps. If \(|A\cup B|>b\), choose \(C,D\) so that \(C\cup D=A\cup B\); then their Johnson distance is \(|A\cup B|-b=p+q-r-b\). Thus the top route has length exactly \(U\).

Hence the graph distance is at most \(\min\{H,L,U\}\). For the reverse inequality, fix \(B\) and define
\[
D_B(X)=\min\{H(X,B),L(X,B),U(X,B)\}.
\]
Across an add/delete edge, each of \(H,L,U\) changes by at most one, so their minimum does also. Across a bottom swap, \(|X|=a\), and
\[
H(X,B)-L(X,B)=a-|X\cap B|\ge0.
\]
Thus on the bottom layer \(D_B=\min\{L,U\}\); both \(L\) and \(U\) change by at most one under a swap because only \(|X\cap B|\) can change, by at most one. Across a top swap, \(|X|=b\), and
\[
H(X,B)-U(X,B)=|B|-|X\cap B|\ge0,
\]
so again \(D_B=\min\{L,U\}\) and changes by at most one. Therefore \(D_B\) is one-Lipschitz on every graph edge. Since \(D_B(B)=0\), every path from \(A\) to \(B\) has length at least \(D_B(A)=\min\{H,L,U\}\), proving the distance formula.

For the diameter, first show the upper bound \(\operatorname{dist}(A,B)\le b\). If \(|A\cup B|\le b\), then \(H=|A\cup B|-|A\cap B|\le b\). If \(|A\cup B|>b\), then \(U=b-r\le b\). Complementing all sets identifies the interval \([a,b]\) with \([d-b,d-a]\), so the same argument gives \(\operatorname{dist}(A,B)\le d-a\). Hence the diameter is at most \(\min\{b,d-a\}\).

If \(a+b\le d\), choose disjoint sets with \(|A|=a\) and \(|B|=b\). The distance formula gives \(\operatorname{dist}(A,B)=b\). If \(a+b\ge d\), choose \(|A|=a\), \(|B|=b\), and \(A\cup B=[d]\); then \(|A\cap B|=a+b-d\) and the distance formula gives \(\operatorname{dist}(A,B)=d-a\). These witnesses prove sharpness in both regimes.

## Verification
The standalone checker `artifacts/verify_interval_metric.py` constructs the one-skeleton directly from the published edge criterion, computes all-pairs shortest paths, and compares them with the closed formula for every interval \([a,b]\) in dimensions \(2\) through \(8\). It also checks the diameter formula. A replay returned:

`VERIFY_OK consecutive-layer S-hypersimplex metric intervals=119 ordered_pairs=1382942 max_d=8`

This finite exhaustive computation is a stress test only; the proof above establishes the theorem for all allowed dimensions and parameters.

## Relationship to prior work
Manecke, Sanyal, and So define S-hypersimplices and give the exact edge criterion from which the graph used here is derived. Their paper studies faces, dissections, pulling triangulations, and monotone path polytopes; its further-questions section discusses volumes, Gröbner bases, and extension complexity. No all-pairs graph-distance formula or graph-diameter theorem is stated there.

The same objects occur earlier as polytopes of cardinality-homogeneous set systems in work of Grötschel. The accessible description of that work emphasizes linear descriptions, greedy optimization, dual solutions, and separation rather than one-skeleton metrics. Cardinality-constrained matroid-polytope work of Maurras and Stephan concerns inequalities, facets, and separation for a broader optimization setting. These are plausible terminology aliases and were checked specifically because a distance theorem could otherwise be hidden under that language.

## Limitations
The theorem is restricted to consecutive cardinality sets \(S\). It does not determine distances for arbitrary gapped S-hypersimplices, directed monotone-path distances, diameters of monotone-path polytopes, or higher-dimensional face adjacency. The computational replay covers only \(d\le8\) and is not used as an infinite proof. A residual bibliographic risk remains that an older result on cardinality-homogeneous set-system polytopes states an equivalent graph metric under different terminology; the sources and searches inspected did not reveal such a statement.

## References
1. S. Manecke, R. Sanyal, J. So, *S-hypersimplices, pulling triangulations, and monotone paths*, Electronic Journal of Combinatorics 27(3) (2020), P3.16. DOI: 10.37236/8457. Preprint: arXiv:1812.07491, first version 2018-12-18.
2. M. Grötschel, *Cardinality Homogeneous Set Systems, Cycles in Matroids, and Associated Polytopes*, ZIB Report 02-19 (2002); later in *The Sharpest Cut*, Chapter 8. DOI: 10.1137/1.9780898718805.ch8.
3. J. F. Maurras, R. Stephan, *On the cardinality constrained matroid polytope*, Networks 57 (2011), 240--246. Preprint: arXiv:0902.1932.
