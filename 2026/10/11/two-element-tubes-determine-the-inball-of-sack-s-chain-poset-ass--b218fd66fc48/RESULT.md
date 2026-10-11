# Two-element tubes determine the inball of Sack's chain-poset associahedron
## Finding
Let
\[
n\ge3,
\qquad
C_n=\{1<2<\cdots<n\},
\]
and let
\[
\mathscr A_{\mathrm S}(C_n)\subset\mathbb R^n_{\Sigma=0}
\]
be the explicit realization of the chain-poset associahedron introduced by Andrew Sack.

Put
\[
D_n=\sqrt6+(n-3)\sqrt2
\tag{1}
\]
and
\[
\boxed{
r_n=
\frac{n^{2n}-(n-1)n^4}{D_n}.
}
\tag{2}
\]
Define
\[
\nu_i=
\begin{cases}
\sqrt{3/2},&i=1\text{ or }i=n-1,\\
\sqrt2,&2\le i\le n-2.
\end{cases}
\tag{3}
\]
There is a unique point
\[
p^*\in\mathbb R^n
\]
satisfying
\[
\sum_{j=1}^n p_j^*=0
\tag{4}
\]
and
\[
p_{i+1}^*-p_i^*
=
n^4+r_n\nu_i
\qquad
(1\le i\le n-1).
\tag{5}
\]

Then \(p^*\) is the unique Euclidean incenter of \(\mathscr A_{\mathrm S}(C_n)\), and
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathscr A_{\mathrm S}(C_n)\bigr)=r_n.
}
\tag{6}
\]

The maximal ball is tangent exactly to the
\[
\boxed{n-1}
\]
facets indexed by the two-element tubes
\[
\{1,2\},\{2,3\},\ldots,\{n-1,n\}.
\tag{7}
\]
Every facet indexed by an interval tube of at least three elements lies strictly farther from \(p^*\).

## Assumptions and scope
The realization is Sack's halfspace realization, not an arbitrary realization of the classical associahedron.

The ambient space is
\[
\mathbb R^n_{\Sigma=0}
=
\left\{
p\in\mathbb R^n:\sum_i p_i=0
\right\},
\]
with the Euclidean metric inherited from the standard orthonormal coordinates.

For a chain, every tube is an interval. The full tube \(C_n\) determines the affine hull of the polytope, while every proper interval tube determines a facet.

The range \(n\ge3\) is used because the associahedron then has positive dimension.

## Proof
Sack's realization assigns to a tube \(\tau\) the linear form
\[
\alpha_\tau(p)
=
\sum_{i\lessdot j,\ i,j\in\tau}(p_j-p_i)
\tag{8}
\]
and the halfspace
\[
\alpha_\tau(p)\ge n^{2|\tau|}.
\tag{9}
\]
For the chain \(C_n\), every tube is an interval
\[
[a,b]=\{a,a+1,\ldots,b\}.
\]
The covering relations telescope, so
\[
\alpha_{[a,b]}(p)=p_b-p_a.
\tag{10}
\]
For the full tube,
\[
p_n-p_1=n^{2n}.
\tag{11}
\]
Thus the affine hull is
\[
A_n
=
\left\{
p:
\sum_i p_i=0,\ 
p_n-p_1=n^{2n}
\right\}.
\tag{12}
\]

Introduce adjacent gaps
\[
g_i=p_{i+1}-p_i
\qquad
(1\le i\le n-1).
\tag{13}
\]
Equation (11) becomes
\[
\sum_{i=1}^{n-1}g_i=n^{2n}.
\tag{14}
\]
A proper interval tube of \(s\) elements, with
\[
s=b-a+1,
\]
has facet inequality
\[
\sum_{i=a}^{b-1}g_i\ge n^{2s}.
\tag{15}
\]

We next compute the intrinsic normal lengths. The tangent space of (12) is
\[
T_n
=
\left\{
x:
\sum_i x_i=0,\ 
x_n-x_1=0
\right\}.
\tag{16}
\]
The ambient normal to the interval hyperplane
\[
p_b-p_a=\text{constant}
\]
is
\[
e_b-e_a.
\]
It is orthogonal to \(\mathbf1\). Its projection to \(T_n\) has norm
\[
\eta_{a,b}
=
\begin{cases}
\sqrt{3/2},&a=1\text{ or }b=n,\\
\sqrt2,&1<a<b<n.
\end{cases}
\tag{17}
\]
Indeed, the only further normal to remove is
\[
e_n-e_1,
\]
whose squared norm is \(2\); for a proper interval the scalar product with \(e_b-e_a\) is \(1\) exactly when the interval touches one endpoint and is \(0\) otherwise.

For a two-element tube \([i,i+1]\), the intrinsic normal length is precisely \(\nu_i\) from (3). If a radius-\(\rho\) ball centered at \(q\in A_n\) lies in the polytope, then every two-element facet gives
\[
g_i(q)-n^4\ge \rho\nu_i.
\tag{18}
\]
Summing (18), using (14), and observing that
\[
\sum_{i=1}^{n-1}\nu_i
=
2\sqrt{3/2}+(n-3)\sqrt2
=
D_n,
\tag{19}
\]
gives
\[
\rho
\le
\frac{n^{2n}-(n-1)n^4}{D_n}
=
r_n.
\tag{20}
\]
Thus (2) is a universal upper bound.

Now define \(p^*\) by (4)--(5). Equation (19) makes the sum of the gaps in (5) equal to \(n^{2n}\), so \(p^*\in A_n\). Each two-element facet has slack
\[
r_n\nu_i,
\]
hence lies at intrinsic distance exactly \(r_n\) from \(p^*\).

It remains to prove that every longer interval facet lies strictly farther away.

Let \([a,b]\) have
\[
r=b-a
\]
adjacent gaps, so
\[
2\le r\le n-2.
\]
Its facet normal length is \(\eta_{a,b}\). A direct check from (3) and (17) gives the location-independent identity
\[
\sum_{i=a}^{b-1}\nu_i-\eta_{a,b}
=
(r-1)\sqrt2.
\tag{21}
\]
Indeed, for an internal interval both sides use only \(\sqrt2\); for an interval meeting an endpoint, the single \(\sqrt{3/2}\) term cancels.

The excess slack of this facet beyond what a radius-\(r_n\) ball needs is therefore
\[
\begin{aligned}
E_{n,r}
&=
\left(
\sum_{i=a}^{b-1}g_i^*-n^{2(r+1)}
\right)
-r_n\eta_{a,b}\\
&=
r n^4-n^{2r+2}
+
(r-1)r_n\sqrt2.
\end{aligned}
\tag{22}
\]
We show this is positive.

Since
\[
D_n=\sqrt2\,(n-3+\sqrt3)
\]
and
\[
n-3+\sqrt3<n-1,
\]
we have
\[
r_n\sqrt2
>
\frac{n^{2n}-(n-1)n^4}{n-1}.
\tag{23}
\]
For \(n\ge3\),
\[
n^{2n}-(n-1)n^4
>
(n-1)n^{2n-2},
\tag{24}
\]
because after dividing by \(n^4\), inequality (24) is
\[
n^{2n-6}(n^2-n+1)>n-1.
\]
Thus
\[
r_n\sqrt2>n^{2n-2}.
\tag{25}
\]
Since
\[
r\le n-2,
\]
equation (25) implies
\[
(r-1)r_n\sqrt2
>
n^{2r+2}.
\tag{26}
\]
Substitution in (22) gives
\[
E_{n,r}>r n^4>0.
\tag{27}
\]
Hence every interval tube with at least three elements is strictly farther than \(r_n\) from \(p^*\). This proves that the ball of radius \(r_n\) centered at \(p^*\) is contained in the polytope and has exactly the contact facets in (7).

Finally, if a ball attains the upper bound (20), equality must hold in every inequality (18). Therefore every adjacent gap of its center is forced to equal
\[
n^4+r_n\nu_i.
\]
Together with the zero-sum condition this determines the center uniquely. Hence \(p^*\) is the unique incenter.

## Verification
The proof is symbolic for every \(n\ge3\).

The source-dependent inputs were checked directly in the primary full text and PDF page image: Sack's definition of \(\alpha_\tau\), the support constants \(n^{2|\tau|}\), the affine hyperplane \(H_P\), the realization theorem, and the statement that a chain recovers the classical associahedron.

The accompanying `verify.py` uses exact symbolic arithmetic for
\[
3\le n\le80.
\]
It reconstructs the candidate gap vector, checks the affine equation, computes every proper interval's projected-normal norm, verifies exact tangency for all two-element tubes, and verifies strict separation for every longer interval. These finite checks are corroborative only.

## Relationship to prior work
Galashin introduced poset associahedra as compactifications of order-preserving configuration spaces. Sack subsequently gave the explicit halfspace realization used here and noted that a chain recovers the classical associahedron.

Sack's paper proves the realization and its complete tube-facet structure, but it does not discuss Euclidean inradii, Chebyshev centers, or facet-distance optimization.

The classical associahedron has many inequivalent realizations. In particular, metric formulas for Loday realizations do not transfer to Sack's exponentially separated halfspace model. The incenter here is not the arithmetic-progression center suggested by the chain alone: the two endpoint tube normals have intrinsic norm \(\sqrt{3/2}\), whereas internal two-element tubes have norm \(\sqrt2\), producing the endpoint correction in (5).

Targeted searches under “poset associahedron”, “chain”, “Sack realization”, “inradius”, “Chebyshev center”, and “Euclidean facet distance” did not locate a theorem implying (2)--(7).

## Limitations
The theorem is realization-specific and does not determine the Euclidean inradius of arbitrary associahedron realizations.

The support constants \(n^{2|\tau|}\) are essential to the strict domination argument; other choices of tube heights may have different active facets.

The result determines the inball and its tangent facets, not the circumradius, John ellipsoid, or complete vertex metric.

A residual originality risk remains for an equivalent observation in unpublished notes on Sack's realization. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Andrew Sack, *A Realization of Poset Associahedra*, arXiv:2301.11449, first public version 2023-01-26; Combinatorial Theory 5 (2025), no. 2, DOI 10.5070/C65265407.
2. Pavel Galashin, *P-Associahedra*, arXiv:2110.07257, first public version 2021-10-14; Selecta Mathematica 30 (2024), article 1.
