# Improved dimension bounds for multiplicative Hilbert cubes in positive shifted powers
## Finding
Let \(k,n\) be integers with \(n\ge 1\). Let \(A\) be a finite set of positive integers such that, for every subset \(B\subseteq A\), including \(B=\varnothing\),
\[
\prod_{a\in B}a+n
\]
is a perfect \(k\)-th power. Then
\[
|A|\le 7\quad\text{for }k\in\{4,5\},
\qquad
|A|\le 6\quad\text{for }k\ge 6.
\]
This improves the published uniform bound \(|A|\le9\) for \(k\ge3\) in the higher-exponent range \(k\ge4\).

## Assumptions and scope
The set \(A\) is finite and consists of distinct positive integers. The shift is strictly positive: \(n\ge1\). The empty subset is included, with empty product equal to \(1\). The result gives only upper bounds: it does not assert that sets of sizes \(7\) or \(6\) exist, nor that these two bounds are optimal. No improvement is claimed here for \(k=2\) or \(k=3\), and no claim is made for negative shifts.

Write \(A=\{a_1<a_2<\cdots<a_d\}\). The argument uses two ingredients: a positive-shift four-product gap inequality and the lower spacing forced by the empty subset.

## Proof
First prove the needed gap inequality directly. Let \(x<y\) and \(z<w\) be positive integers, and suppose that each of
\[
xz+n,\quad yz+n,\quad xw+n,\quad yw+n
\]
is a perfect \(k\)-th power. Because products of perfect \(k\)-th powers are perfect \(k\)-th powers, there are positive integers \(U,V\) satisfying
\[
U^k=(xz+n)(yw+n),\qquad V^k=(xw+n)(yz+n).
\]
A direct expansion gives
\[
U^k-V^k=n(y-x)(w-z)>0.
\]
Hence \(U\ge V+1\), and therefore
\[
U^k-V^k\ge kV^{k-1}>k(xyzw)^{(k-1)/k},
\]
since \(V^k=(xw+n)(yz+n)>xyzw\). On the other hand,
\[
n(y-x)(w-z)<nyw.
\]
Combining the two estimates, raising to the \(k\)-th power, and cancelling \(y^{k-1}w^{k-1}\) yields the strict gap bound
\[
yw>\frac{k^k(xz)^{k-1}}{n^k}. \tag{1}
\]
For positive \(n\), this avoids the auxiliary size hypothesis required by the more general signed-shift gap lemma in the cited literature.

Assume now that \(d\ge6\) and set
\[
X=\prod_{j=6}^d a_j,
\]
with \(X=1\) only when the displayed product is empty; in the applications below it is nonempty. Apply (1) with
\[
x=a_1a_5X,\qquad y=a_2a_5X,\qquad z=a_3,\qquad w=a_4.
\]
The four required shifted products correspond to four subset products of \(A\), so the hypotheses hold. Thus
\[
a_2a_4a_5X>\frac{k^k(a_1a_3a_5X)^{k-1}}{n^k},
\]
or equivalently
\[
n^k a_2a_4>k^k a_1^{k-1}a_3^{k-1}a_5^{k-2}X^{k-2}.
\]
For \(k\ge3\), we have \(a_1^{k-1}\ge1\), \(a_3^{k-1}>a_2\), and \(a_5^{k-2}>a_4\). Consequently
\[
X<k^{-k/(k-2)}n^{k/(k-2)}. \tag{2}
\]

The empty subset gives \(n+1=q^k\) for some integer \(q\ge2\). For every \(i\ge2\), distinctness and positivity give \(a_i\ge2\), so \(a_i+n\) is a perfect \(k\)-th power strictly larger than \(q^k\). Hence
\[
a_i+n\ge(q+1)^k,
\]
and therefore
\[
a_i\ge(q+1)^k-q^k+1>kq^{k-1}>kn^{(k-1)/k}. \tag{3}
\]
If \(r=d-5\), multiplying (3) over \(i=6,\ldots,d\) gives
\[
X>k^r n^{r(k-1)/k}. \tag{4}
\]

For \(k\in\{4,5\}\), suppose \(d\ge8\). Then \(r\ge3\), and
\[
\frac{3(k-1)}k\ge\frac{k}{k-2}.
\]
The lower bound (4) is therefore strictly larger than the upper scale in (2), a contradiction. Thus \(d\le7\).

For \(k\ge6\), suppose \(d\ge7\). Then \(r\ge2\), and
\[
\frac{2(k-1)}k\ge\frac{k}{k-2}
\]
is equivalent to
\[
k^2-6k+4\ge0,
\]
which holds for every integer \(k\ge6\). Again (4) contradicts (2), so \(d\le6\).

## Verification
The proof is symbolic and applies to all admissible integers; finite computation is not used to infer an infinite statement. The standalone verifier checks the exact determinant-style identity underlying (1), checks the exponent inequalities at the boundary cases \(k=4,5,6\), and checks the monotonic polynomial inequality for a broad finite range as a transcription safeguard. Its successful output is included separately.

A critical boundary check is that the argument for \(d\le6\) begins exactly at \(k=6\): the exponent comparison for a two-factor tail reduces to \(k^2-6k+4\ge0\), which is true at \(k=6\) and increases thereafter. For \(k=5\), a two-factor tail does not suffice, while a three-factor tail does, yielding the separate bound \(d\le7\).

## Relationship to prior work
Tsang and Yip introduced the multiplicative-Hilbert-cube formulation for shifted powers and proved that under these same subset-product hypotheses one has \(|A|\le132\) for \(k=2\) and \(|A|\le9\) for every \(k\ge3\). They explicitly note before their theorem that the bound was not optimized. Their proof for \(k\ge3\) combines a five-factor tail with a general gap lemma valid for signed shifts.

The present argument keeps the same natural object but exploits the additional assumption \(n>0\) already present in that theorem. The identity
\[
(xz+n)(yw+n)-(xw+n)(yz+n)=n(y-x)(w-z)
\]
gives a stronger positive-shift gap inequality without a preliminary lower bound on \(xz\). This permits a tail beginning after the first five generators for every \(d\ge6\), and the number of tail factors can then be matched to \(k\). The resulting \(7\) and \(6\) ceilings are not stated in the inspected source.

Yip's earlier paper supplies the general gap-principle lineage for shifted perfect powers. Croot and Yip study robust Diophantine tuples and product sets in shifted powers; their inspected full text does not state the all-subset multiplicative-Hilbert-cube bounds proved here.

## Limitations
The result does not settle the optimal maximum dimension for any \(k\ge4\). In particular, there is no construction here meeting the bounds. The proof uses \(n>0\) essentially in both the strict four-product gap and the relation \(n+1=q^k\); it therefore does not extend as written to negative shifts. Literature searches and direct source comparisons reduce but cannot eliminate the residual risk that an equivalent refinement appears in an uninspected source under different terminology.

## References
1. K. M. Tsang and C. H. Yip, “Bipartite Diophantine tuples and their applications,” arXiv:2512.03441v1, first public 2025-12-03; Research in Number Theory 12 (2026), Article 16, DOI:10.1007/s40993-026-00709-2.
2. C. H. Yip, “Multiplicatively reducible subsets of shifted perfect kth powers and bipartite Diophantine tuples,” Acta Arithmetica 218 (2025), DOI:10.4064/aa240520-24-9.
3. E. Croot and C. H. Yip, “Diophantine tuples and product sets in shifted powers,” Journal of the London Mathematical Society 113 (2026), e70499, DOI:10.1112/jlms.70499.
