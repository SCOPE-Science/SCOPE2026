# Exact offcenter centroid core of every convex body

## Finding
Let \(K\subset\mathbb R^n\) be a compact convex body with nonempty interior, \(n\ge2\), and centroid \(c\). Define its **offcenter centroid core** by
\[
\mathcal O(K)=\bigcap_{\substack{B\supseteq K\text{ compact convex body}\\(n+1)\operatorname{cen}(B)-n c\in B}}\big(B-\operatorname{cen}(B)+c\big).
\]
The exact identity is
\[
\boxed{\mathcal O(K)=c+\frac1{n+1}\operatorname{conv}\!\left(n(K-c)\cup(K-K)\right).}
\]
Thus the universal dilate from the offcenter-containment theorem is the *entire* offcenter core if and only if
\[
-(K-c)\subseteq(n-1)(K-c).
\]
In the plane this criterion is equivalent to central symmetry. Every nondegenerate triangle has an offcenter core with nine vertices and area exactly \(7/9\) of its area.

## Assumptions and scope
Every body under consideration is compact, convex, and full dimensional in a finite-dimensional Euclidean space. The centroid is the Lebesgue-volume centroid. The intersection is over **all** offcenter supersets, not just bounded-size families, nested supersets, or polyhedral supersets. The ambient dimension is any integer \(n\ge2\). The affine-invariant formula is valid for arbitrary translations and nonsingular affine changes of variables.

## Proof
Translate so that \(c=0\). For a unit direction \(u\), let
\[
a=h_K(u)>0,\qquad b=h_K(-u)>0.
\]
Write \(S=\frac1{n+1}\operatorname{conv}(nK\cup(K-K))\). Its support function is
\[
h_S(u)=\frac1{n+1}\max\{na,a+b\}.
\]
**Lower inclusion.** For each admissible \(B\) put \(z=\operatorname{cen}(B)\). The offcenter promise means \(q=(n+1)z\in B\). Convexity and \(K\subseteq B\) give \(\frac n{n+1}x+\frac1{n+1}q\in B\) for every \(x\in K\), hence \(\frac n{n+1}K\subseteq B-z\). Independently, the Minkowski–Radon centroid inequality yields, in every direction \(u\),
\[
h_{B-z}(u)\ge\frac{h_B(u)+h_B(-u)}{n+1}\ge\frac{h_K(u)+h_K(-u)}{n+1}.
\]
Equivalently, \(\frac1{n+1}(K-K)\subseteq B-z\). Thus \(S\subseteq\mathcal O(K)\).

**Sharpness separately in every direction.** Fix \(u\) and choose orthogonal coordinates \((z,y)\in\mathbb R\times\mathbb R^{n-1}\) with \(z=x\cdot u\). For \(\lambda,t>0\) form the round frustum
\[
B_{t,\lambda}=\operatorname{conv}\!\left(\{(a,y):\|y\|_2\le t\}\cup\{(-b,y):\|y\|_2\le\lambda t\}\right).
\]
Its cross-section at relative height \(v=(z+b)/(a+b)\in[0,1]\) is an \((n-1)\)-ball of radius \(t[\lambda+(1-\lambda)v]\). For each fixed \(\lambda>0\), sufficiently large \(t\) makes \(B_{t,\lambda}\supseteq K\): the radii at *all* heights are at least \(t\min\{1,\lambda\}\), which eventually dominates the bounded orthogonal projection of \(K\).

Rotational symmetry and Fubini's theorem give \(\operatorname{cen}(B_{t,\lambda})=m(\lambda)u\), with
\[
m(\lambda)=-b+(a+b)\frac{\int_0^1v[\lambda+(1-\lambda)v]^{n-1}\,dv}{\int_0^1[\lambda+(1-\lambda)v]^{n-1}\,dv}.
\]
This continuous function obeys
\[
\lim_{\lambda\downarrow0}m(\lambda)=\frac{na-b}{n+1},\qquad
\lim_{\lambda\to\infty}m(\lambda)=\frac{a-nb}{n+1}.
\]
For every \(\lambda>0\), the ratio of the frustum weight to the cone-endpoint weight, \([\lambda+(1-\lambda)v]^{n-1}/v^{n-1}\), strictly decreases in \(v\in(0,1]\). Thus its weighted mean height is strictly less than the cone-endpoint mean \(n/(n+1)\); in particular \(m(\lambda)<(na-b)/(n+1)\), including at equality-transition parameters.

Set
\[
m_*:=\min\left\{\frac{a}{n+1},\frac{na-b}{n+1}\right\}.
\]
Since \(b>0\), the lower endpoint \((a-nb)/(n+1)\) is strictly below \(a/(n+1)\). Since \(a>0\), the upper endpoint \((na-b)/(n+1)\) is strictly above \(-b/(n+1)\). Consequently there is a sequence \(\lambda_j>0\) with
\[
m(\lambda_j)<m_*,\quad m(\lambda_j)\to m_*,\quad -b<(n+1)m(\lambda_j)<a.
\]
For each such \(\lambda_j\), choose \(t_j\) large enough that the frustum contains \(K\). Its entire axis interval \([-b,a]\times\{0\}\) lies inside it, so the last displayed inequalities guarantee
\[
(n+1)\operatorname{cen}(B_{t_j,\lambda_j})=(n+1)m(\lambda_j)u\in B_{t_j,\lambda_j}.
\]
Thus the frusta are admissible. Their top support is \(h_{B_{t_j,\lambda_j}}(u)=a\); after recentering, the support is \(a-m(\lambda_j)\), tending to
\[
a-m_*=\frac1{n+1}\max\{na,a+b\}=h_S(u).
\]
Because \(\mathcal O(K)\) is contained in *every* recentered admissible superset, this proves \(h_{\mathcal O(K)}(u)\le h_S(u)\). Together with the lower inclusion and arbitrariness of \(u\), equality of convex bodies follows. Translating back gives the stated identity.

**Equality classification and triangle.** The convex hull equals the promised dilate precisely when
\[
K-K\subseteq nK\quad\Longleftrightarrow\quad -K\subseteq(n-1)K.
\]
At \(n=2\) this says \(-K\subseteq K\); equal volume then forces \(-K=K\), or central symmetry about the centroid. For a triangle, affine invariance lets its centered vertices be \((2,0),(-1,\sqrt3),(-1,-\sqrt3)\). The difference body divided by three is a hexagon of area \(2\sqrt3\). The enlarged convex hull also contains the three vertices of \(\frac23K\); each adds an exterior triangle of area \(\sqrt3/9\), producing a nine-vertex polygon of area \(7\sqrt3/3\). Since the original triangle has area \(3\sqrt3\), the exact area fraction is \(7/9\).

## Verification
The preceding support-function argument proves the infinite intersection equality for **every** body and direction; it is not a computational extrapolation. The supplemental `verify.py` checks the frustum centroids by direct polynomial integration in dimensions \(2,3,4,5\), symbolically checks both endpoint limits, and checks the exact planar triangle hull and area ratio with rational shoelace operations in an affine-normalized model. Run `python3 verify.py` using only the Python standard library and SymPy; a successful run prints `OFFCENTER_CORE_CHECKS_OK`. The checker is supplementary and neither samples all convex bodies nor certifies infinite-dimensional statements.

## Relationship to prior work
Feldman, *Arranging convex bodies for maximum intersection volume* (arXiv:2608.04516v1), proves the unrestricted centroid core \(\frac1{n+1}(K-K)\) (Theorem 4) and the promised inner dilate \(\frac n{n+1}K\) (Theorem 15). His Remark 17 explicitly leaves the identity of the full offcenter core open. These two known inclusions together provide only the **lower inclusion** in our result. The new step is the directionwise sharp family of offcenter frusta, which establishes the converse inclusion for the intersection and yields an exact convex-hull formula. The triangle's nine-vertex core and area \(7/9\) are consequences of that exact identity, not claims that the broad centroid-overlap constant is improved.

## Limitations
No optimizer is claimed for a *single finite* offcenter superset or for a fixed finite family. In some directions the sharp support value is obtained only as a limit of admissible frusta. This is an exact description of the offcenter containment core, not a new bound on the optimal number of translates, and not a solution of Feldman's two-body higher-dimensional efficiency question. The known centroid inequalities used for the lower inclusion are classical; only the frustum upper matching and its classification are asserted as new here.

## References
1. David Victor Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1 (first public 2026-08-05), especially Lemma 6, Theorems 4 and 15, and Remark 17.
2. H. Minkowski and J. Radon, classical centroid-support inequality; a complete proof with equality cases appears in Feldman, Section 2.
