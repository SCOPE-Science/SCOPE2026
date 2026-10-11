# Universal Santaló and volume-product laws for homothetic frusta
## Finding
For every dimension \(d\ge2\), let \(K\subset\mathbb R^{d-1}\) be a convex body translated so that its Santaló point is the origin. For \(0\le a\le1\), form the \(d\)-dimensional homothetic frustum
\[
F_a(K)=\operatorname{conv}(K\times\{0\},\,aK\times\{1\}).
\tag{1}
\]
The height-one normalization is without loss of affine generality. Write
\[
b=1-a,\qquad S_d(a)=\sum_{j=0}^{d-1}a^j,
\qquad
 t_d(a)=\frac{2}{2+db+\sqrt{4-4b+d^2b^2}}.
\tag{2}
\]
For each \(0<t<1\), the polar volume about \((0,t)\) is exactly
\[
\boxed{\operatorname{vol}_d\big((F_a(K)-(0,t))^\circ\big)
=\frac{\operatorname{vol}_{d-1}(K^\circ)}{d\,t(1-t)(1-bt)^{d-1}}.}
\tag{3}
\]
The **unique Santaló point** is \((0,t_d(a))\), independent of the base shape. The **axial centroid** has coordinate
\[
g_d(a)=\frac{\sum_{j=0}^{d-1}(j+1)a^j}{(d+1)S_d(a)}.
\tag{4}
\]
It satisfies the sharp order law
\[
\boxed{t_d(a)<g_d(a)\quad\text{for }0<a<1,}
\tag{5}
\]
with equality at the pyramid and prism endpoints \(a=0\) and \(a=1\).

Writing the Santaló volume product of a \(k\)-dimensional body as
\[
\Pi_k(L)=\operatorname{vol}_k(L)\operatorname{vol}_k((L-S(L))^\circ),
\]
one has the exact **base-independent factorization**
\[
\boxed{\Pi_d(F_a(K))=\Pi_{d-1}(K)\,\Phi_d(a),\qquad
\Phi_d(a)=\frac{S_d(a)}{d^2t_d(a)(1-t_d(a))(1-bt_d(a))^{d-1}}.}
\tag{6}
\]
For each \(d\ge2\) the function \(\Phi_d\) is **strictly increasing** on \([0,1]\), with
\[
\Phi_d(0)=\frac{(d+1)^{d+1}}{d^{d+2}},
\qquad
\Phi_d(1)=\frac4d.
\tag{7}
\]
The pyramid-endpoint formula in (7) and its center location are already known from Meyer--Reisner, Lemma 11. The new theorem gives (3)--(6) and the strict comparison for every nondegenerate homothetic frustum.

## Assumptions and scope
A convex body means a compact convex subset with nonempty interior in its own affine span. The \((d-1)\)-dimensional base \(K\) can be asymmetric, nonsmooth, and nonpolyhedral. It is translated so that its unique Santaló point is zero; equivalently, the centroid of its polar \(K^\circ\) is zero.

The case \(a=0\) is a pyramid, \(a=1\) a prism, and \(0<a<1\) a genuine homothetic frustum. Neither smoothness nor any symmetry of \(K\) is assumed. Polarity is Euclidean polarity about the indicated point and is used only through its affine-invariant volume product.

## Proof
**1. Exact polar sections.** Fix \(d\ge2\), \(a\in(0,1]\), and \(t\in(0,1)\). Write \(p=(0,t)\). A covector \((y,s)\in\mathbb R^{d-1}\times\mathbb R\) belongs to \((F_a(K)-p)^\circ\) precisely when the inequalities at the two generating faces hold:
\[
h_K(y)-ts\le1,
\qquad a h_K(y)+(1-t)s\le1.
\tag{8}
\]
Here \(h_K\) is the support function of \(K\). Since \(0\in\operatorname{int}K\), the horizontal section at axial dual coordinate \(s\) is a dilation of \(K^\circ\) by
\[
R(s)=\min\left\{1+ts,\,\frac{1-(1-t)s}{a}\right\}
\]
for \(-1/t\le s\le1/(1-t)\). The two affine scales meet at
\[
s_*=\frac{b}{1-bt},\qquad
1+ts_*=\frac1{1-bt},\qquad
1-(1-t)s_*=\frac a{1-bt}.
\tag{9}
\]
Consequently the polar volume is \(\operatorname{vol}_{d-1}(K^\circ)\) times
\[
\begin{aligned}
&\int_{-1/t}^{s_*}(1+ts)^{d-1}\,ds
+\int_{s_*}^{1/(1-t)}\left(\frac{1-(1-t)s}{a}\right)^{d-1}\,ds\\
&=\frac1{d\,t(1-bt)^d}+\frac a{d(1-t)(1-bt)^d}\\
&=\frac1{d\,t(1-t)(1-bt)^{d-1}},
\end{aligned}
\]
which proves (3). For \(a=0\), the second integral vanishes in the limit and the same expression holds directly. In particular all horizontal polar sections are homothetic to \(K^\circ\), a feature not requiring symmetry of \(K\).

**2. The exact Santaló location.** For every axial point \(p=(0,t)\), each horizontal section of its polar has zero horizontal first moment because the centroid of \(K^\circ\) is zero. Hence the horizontal components of the polar centroid vanish. Its axial centroid vanishes exactly when the derivative in \(t\) of its volume vanishes, by differentiation of the polar-volume functional. From (3),
\[
\frac{\partial}{\partial t}\log\operatorname{vol}_d((F_a(K)-(0,t))^\circ)
=-\frac1t+\frac1{1-t}+\frac{(d-1)b}{1-bt}.
\tag{10}
\]
Setting (10) to zero yields
\[
(d+1)b t^2-(2+db)t+1=0.
\tag{11}
\]
The second derivative of the logarithm in (10) is strictly positive:
\[
\frac1{t^2}+\frac1{(1-t)^2}+\frac{(d-1)b^2}{(1-bt)^2}>0.
\]
The unique axial solution in \((0,1)\) is \(t_d(a)\) from (2). The full polar centroid at that point is therefore zero. The characterization of the Santaló point by zero centroid of its polar, together with uniqueness, proves it is \((0,t_d(a))\). It is not necessary to assume a priori that the Santaló point lies on an axis of symmetry.

**3. Centroid separation.** By slicing (1), the axial coordinate of the ordinary centroid is the mean of a random variable \(Z\in[0,1]\) with probability density proportional to
\[
\rho(z)^{d-1},\qquad \rho(z)=1-bz.
\tag{12}
\]
Direct integration yields (4). Put
\[
 g=\mathbb E Z,\qquad \mu_2=\mathbb E Z^2,
\qquad Q(x)=-1+(2+db)x-(d+1)b x^2.
\]
Integrating the derivative of \(z(1-z)(1-bz)^d\) gives the exact identity
\[
1-(2+(d+1)b)g+(d+2)b\mu_2=0,
\]
and therefore
\[
Q(g)=b\bigl[(d+2)\operatorname{Var}(Z)-g(1-g)\bigr].
\tag{13}
\]
To determine the sign, expand the positive weight in (12):
\[
(1-bz)^{d-1}
=(a+b(1-z))^{d-1}
=\sum_{k=0}^{d-1}\binom{d-1}{k}a^{d-1-k}b^k(1-z)^k.
\tag{14}
\]
After normalization, the distribution of \(Z\) is a mixture of \(\mathrm{Beta}(1,k+1)\) laws. The component mean and variance are
\[
m_k=\frac1{k+2},\qquad
v_k=\frac{k+1}{(k+2)^2(k+3)}.
\]
Writing \(\mathbb E_*\) and \(\operatorname{Var}_*\) for expectation and variance over the mixture label, the law of total variance gives
\[
\begin{aligned}
&(d+2)\operatorname{Var}(Z)-g(1-g)\\
&\qquad=\mathbb E_*\left[(d+2)v_k-m_k(1-m_k)\right]
 +(d+1)\operatorname{Var}_*(m_k)\\
&\qquad=\mathbb E_*\left[\frac{(k+1)(d-k-1)}{(k+2)^2(k+3)}\right]
 +(d+1)\operatorname{Var}_*(m_k).
\end{aligned}
\tag{15}
\]
Both terms are nonnegative. When \(0<a<1\), every mixture component has positive weight, including a component with \(k<d-1\); hence the first term is strictly positive. Since \(b>0\), (13) gives \(Q(g)>0\). On the other hand (11) says \(Q(t_d(a))=0\), and \(Q(0)<0\) while \(Q(1)=a>0\). Its unique zero in \((0,1)\) must therefore satisfy \(t_d(a)<g\). At \(a=0\), only the \(k=d-1\) beta component survives, and both coordinates equal \(1/(d+1)\); at \(a=1\), the height density is uniform and both equal \(1/2\). This proves (5).

**4. Exact volume product and strict monotonicity.** Direct slicing gives
\[
\operatorname{vol}_d(F_a(K))
=\operatorname{vol}_{d-1}(K)\int_0^1(1-bz)^{d-1}\,dz
=\frac{S_d(a)}d\operatorname{vol}_{d-1}(K).
\tag{16}
\]
Multiplying (16) by the polar volume (3) at \(t=t_d(a)\) proves (6).

To prove strict monotonicity of \(\Phi_d\), let \(I(a)=\int_0^1(1-(1-a)z)^{d-1}\,dz\). The minimizing-height first-order condition (10) and the envelope differentiation of \(\log\Phi_d\) give, for \(0<a<1\),
\[
\frac d{da}\log\Phi_d(a)
=(d-1)\left[
\mathbb E\frac{Z}{1-bZ}-\frac{t_d(a)}{1-bt_d(a)}
\right].
\tag{17}
\]
The function \(f(z)=z/(1-bz)\) is increasing and strictly convex on \([0,1]\) when \(0<b<1\). Since \(Z\) is nonconstant, Jensen's inequality and (5) show
\[
\mathbb E f(Z)>f(g)>f(t_d(a)),
\]
so the derivative in (17) is strictly positive. Continuity at the endpoints implies strict monotonicity on all of \([0,1]\). Substituting \(a=0\) and \(a=1\) in (6) gives (7). The \(a=0\) equality agrees with Meyer--Reisner's earlier pyramid lemma; this endpoint is not a new claim.

## Verification
The accompanying `verify.py` reproduces symbolic implications of the centroid-order identity for dimensions \(2\) through \(12\), numerically checks the strict order and product increase along a dense parameter grid, and independently constructs the full polar polytopes of nonsymmetric triangular-base and centrally symmetric square-base frusta in dimension \(3\). The latter direct convex-hull calculations compare measured polar volume with (3). The verifier outputs `VERIFY_OK` and the largest absolute discrepancy observed. These finite computations are regression tests; the theorem for all \(d\) and all bases is established by the exact integrals and beta-mixture argument above.

## Relationship to prior work
Meyer and Reisner establish the classical Santaló point and volume-product factor for pyramids in Lemma 11 of *Shadow systems and volumes of polar convex bodies*. Their exact constant is the first endpoint in (7); it is not an originality claim here. Their surrounding theorems treat shadow systems, reverse inequalities, and polytopes with few vertices; they do not state the polar-section formula or a monotonic frustum law with nonzero upper base. The paper's first public version is arXiv:math/0606305v1 (13 June 2006).

Pavlov and Telen study rational polar-volume functions and Santaló points for general polytopes, showing broad algorithmic and algebraic frameworks. Their materially inspected preprint does not provide a shape-independent homothetic-frustum reduction; a general algorithm that can compute a center is not an explicit formula or strict monotonicity theorem. Izmestiev treats Santaló centers through projective transformations and centers of cone sections; these are related general constructions but differ from the two-parallel-face frustum invariant computed here.

The new theorem determines the entire nondegenerate homothetic-frustum family for **every convex base**, including nonsymmetric bases, and proves the strict centroid displacement and monotonicity of the Mahler factor. Search comparisons used truncated pyramid/cone, pyramidal frustum, trapezoid, homothetic prismatoid, polar-volume, Mahler-product, and Santaló-center terminology. None of the compared primary statements implies (3)--(6) without new calculations; lack of a search hit alone is not treated as proof of historical novelty.

## Limitations
The top base must be a positive homothetic copy of the bottom base with a common homothety center; general skew prismatoids with unrelated cross-sections are not included. The base must be put at its own Santaló point before the universal axial formula is applied, although any original base can be translated to meet this convention. The result does not determine the Santaló point of arbitrary trapezoids with bases in nonhomothetic positions unless an affine shear and translation place them in this class.

The pyramid value (7) and the Santaló--polar-centroid characterization are established prior literature. Originality of elementary formulas in older unindexed projective or convex-geometry texts cannot be guaranteed by searchable sources; this is the principal residual historical risk.

## References
1. M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, arXiv:math/0606305v1 (13 June 2006); corrected v2 (14 July 2008), *Mathematika* 53 (2006), 129--148. In particular, Lemma 11 for the pyramid endpoint.
2. D. Pavlov and S. Telen, *Santaló Geometry of Convex Polytopes*, arXiv:2402.18955v1 (29 February 2024), particularly the introduction and the rational-volume framework.
3. I. Izmestiev, *Matching centroids by a projective transformation*, arXiv:1409.6176v1 (2014), *Geometriae Dedicata* 217, article 53 (2023), DOI:10.1007/s10711-023-00789-9, especially §4 on cone sections and the polar-centroid characterization.
