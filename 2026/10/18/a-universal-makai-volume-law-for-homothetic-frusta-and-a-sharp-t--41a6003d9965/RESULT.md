# A universal Makai-volume law for homothetic frusta and a sharp three-dimensional bound

## Finding
For an integer \(d\ge2\), let \(B\subset\mathbb R^{d-1}\) be any compact convex body with nonempty interior. For \(0\le t<1\), let
\[
P_t(B)=\{(zx,z):x\in B,\ t\le z\le1\}\subset\mathbb R^d.
\]
This is a convex homothetic frustum, with \(t=0\) its pyramidal endpoint. For any full-dimensional convex body \(K\subset\mathbb R^k\), define its **Makai volume** by
\[
\mathcal M_k(K)=\operatorname{vol}_k(K)\operatorname{vol}_k((K-K)^\circ),
\qquad
C^\circ=\{u:\langle u,c\rangle\le1\text{ for all }c\in C\}.
\]
Then the following exact **base-independent factorization** holds:
\[
\boxed{\mathcal M_d(P_t(B))=\mathcal M_{d-1}(B)\,
\frac{\big(1+t+\cdots+t^{d-1}\big)\big(d+1-(d-1)t\big)}{d^2}.}
\tag{1}
\]
The multiplying factor is strictly increasing for \(0\le t<1\), from \((d+1)/d^2\) at the pyramid endpoint toward \(2/d\) at the affine-normalized prism endpoint. Its **exact quadratic prism-endpoint gap** is
\[
\boxed{\frac2d\mathcal M_{d-1}(B)-\mathcal M_d(P_t(B))=
\frac{(1-t)^2}{d^2}\mathcal M_{d-1}(B)
\sum_{j=0}^{d-2}(j+1)(d-1-j)t^j.}
\tag{2}
\]
In particular, the ratio of this gap to \((1-t)^2\mathcal M_{d-1}(B)\) lies between the sharp constants \((d-1)/d^2\) and \((d^2-1)/(6d)\). The lower constant is attained at \(t=0\); the upper is attained as an endpoint limit \(t\uparrow1\). For \(d=2\), these constants agree and the gap is exactly quadratic throughout.

**Sharp three-dimensional Makai inequality for this class.** If \(d=3\), the known planar Eggleston inequality implies, for every compact convex planar base \(B\) and \(0\le t<1\),
\[
\boxed{\mathcal M_3(P_t(B))\ge \frac{2+t+t^2-t^3}{3}\ge\frac23.}
\tag{3}
\]
Equality in the first inequality holds **if and only if** \(B\) is a triangle; equality in the second holds **if and only if** \(t=0\). Thus equality in the unrestricted-in-\(t\) lower bound \(2/3\) holds precisely for tetrahedra in this homothetic-frustum class. For each fixed truncation ratio, the lower bound in (3) is exact and realized by any triangular base.

## Assumptions and scope
Lebesgue volume is taken in the affine span of the body and its polar, with the usual Euclidean pairing. For \(B\), smoothness, symmetry, centeredness, and polytopality are **not** assumed; translation of \(B\) corresponds to an affine shear of \(P_t(B)\), so the formulas are affine invariant. The set \(P_t(B)\) is the convex hull of \(B\times\{1\}\) and \(tB\times\{t\}\). At \(t=0\), \(tB\times\{t\}\) is one apex. The restriction \(t<1\) is essential: \(P_1(B)\) is dimension-deficient, and the prism endpoint in (2) is a limit after rescaling the vertical axis by \(1/(1-t)\). Every formula above holds for every integer \(d\ge2\) and every indicated \(B,t\).

## Proof
**1. The primal volume.** Since the section at height \(z\) is \(zB\), Cavalieri's principle gives
\[
\operatorname{vol}_d(P_t(B))
=\operatorname{vol}_{d-1}(B)\int_t^1 z^{d-1}\,dz
=\frac{1-t^d}{d}\operatorname{vol}_{d-1}(B).
\tag{4}
\]

**2. The key polar-fiber identity.** Put \(m=d-1\). For a horizontal covector \(u\in\mathbb R^m\), set \(r=h_B(u)\), \(\ell=-h_B(-u)\), and \(w=r-\ell=h_{B-B}(u)\ge0\). For a full covector \((u,s)\), the width of \(P_t(B)\) is
\[
W(u,s)=\max_{z\in[t,1]}z(s+r)-\min_{z\in[t,1]}z(s+\ell).
\tag{5}
\]
Because \((P_t(B)-P_t(B))^\circ=\{(u,s):W(u,s)\le1\}\), its fiber over \(u\) is empty when \(w>1\): the width of the top base alone equals \(w\). For \(w\le1\), the interval \(-r\le s\le-\ell\) has length \(w\) and satisfies \(W(u,s)=w\). Above that interval, both \(s+r,s+\ell\) are nonnegative and
\[
W(u,s)=w+(1-t)(s+\ell),
\]
so the permitted upper tail has length \((1-w)/(1-t)\). Below the middle interval, both are nonpositive and the permitted lower tail has the same length. Consequently
\[
\boxed{\operatorname{length}\{s:W(u,s)\le1\}=
\begin{cases}
\displaystyle\frac{2-(1+t)w(u)}{1-t},&w(u)\le1,\\
0,&w(u)>1.
\end{cases}}
\tag{6}
\]
This calculation does not use any symmetry of \(B\) or a choice of origin inside \(B\).

Let \(C=(B-B)^\circ=\{u:w(u)\le1\}\). It is a centrally symmetric full-dimensional convex body. Since \(w\) is its gauge, \(\{u:w(u)\le a\}=aC\) for \(0\le a\le1\). Thus the layer-cake identity, with no smoothness assumptions, yields
\[
\int_C w(u)\,du
=\int_0^1\big(\operatorname{vol}_m(C)-\operatorname{vol}_m(aC)\big)\,da
=\frac{m}{m+1}\operatorname{vol}_m(C).
\tag{7}
\]
Integrating (6) and substituting \(m=d-1\) proves
\[
\operatorname{vol}_d((P_t(B)-P_t(B))^\circ)
=\frac{d+1-(d-1)t}{d(1-t)}\operatorname{vol}_{d-1}((B-B)^\circ).
\tag{8}
\]
Multiplication of (4) and (8), followed by cancellation of \(1-t\), proves (1).

**3. Strict monotonicity and exact stability.** Write \(S_d(t)=\sum_{j=0}^{d-1}t^j\) and \(F_d(t)=S_d(t)(d+1-(d-1)t)\). Elementary polynomial expansion gives
\[
F_d(t)=d+1+2\sum_{j=1}^{d-1}t^j-(d-1)t^d.
\tag{9}
\]
A coefficient comparison gives both exact identities
\[
F_d'(t)=2(1-t)\sum_{j=0}^{d-2}\binom{j+2}{2}t^j>0
\quad(0\le t<1),
\tag{10}
\]
\[
2d-F_d(t)=(1-t)^2\sum_{j=0}^{d-2}(j+1)(d-1-j)t^j.
\tag{11}
\]
Because \(F_d(0)=d+1\) and \(F_d(1)=2d\), these identities imply strict monotonicity and (2). Each coefficient of the polynomial on the right of (11) is positive. Its endpoint values are \(d-1\) and \(\binom{d+1}{3}\); division by \(d^2\) gives the claimed globally sharp two-sided constants and the exact quadratic terminal asymptotic. For \(d=2\) the polynomial is constant.

**4. Sharp three-dimensional consequence.** Eggleston's established planar theorem states
\[
\mathcal M_2(B)\ge\frac32,
\]
with equality exactly for triangles. Putting \(d=3\) in (1) and simplifying gives
\[
\mathcal M_3(P_t(B))=
\frac{4+2t+2t^2-2t^3}{9}\mathcal M_2(B)
\ge\frac{2+t+t^2-t^3}{3}.
\tag{12}
\]
The first equality condition is precisely the planar equality condition because the positive multiplying factor cannot erase a strict inequality. Since \(t+t^2-t^3=t(1+t-t^2)>0\) when \(0<t<1\), the right side is strictly greater than \(2/3\) except at \(t=0\). When \(B\) is triangular and \(t=0\), the resulting pyramid is a tetrahedron. All equality statements follow.

## Verification
The standalone `verify.py` checks the two all-dimensional polynomial identities by exact symbolic expansion for dimensions \(2\) through \(39\), including rational specializations. Separately, it constructs actual full-dimensional frustum vertex configurations with nonsymmetric triangular, quadrilateral, pentagonal, and tetrahedral bases. For \(t=0,0.2,0.61,0.92\), it computes the primal and polar-difference-body volumes directly using convex-hull and halfspace-intersection algorithms, and compares all \(16\) cases with equations (4) and (8). It prints `VERIFY_OK`. These computations are finite reproducibility checks, whereas (4)--(12) establish the universal statements analytically.

## Relationship to prior work
Martin Winter's October 7, 2026 theorem establishes the upper bound \(\operatorname{vol}(P)\operatorname{vol}((P-P)^\circ)\le\mathcal F(P)/(d!)^2\) for polytopes, with \(\mathcal F(P)\) the number of maximal face flags. It does not give the exact functional profile for a nonpolyhedral frustum, and its inequality does not imply the sharp lower bound in (3).

Eggleston's two-dimensional lower bound, also reproduced in Arkadiy Aliev's November 19, 2025 paper, supplies a **previously known** input to (3). Aliev proves the three-dimensional Makai bound under tetrahedral symmetry, a hypothesis that arbitrary homothetic frusta with nonsymmetric bases do not satisfy. The new result is the universal exact reduction (1)--(2) and the resulting wider three-dimensional class, not Eggleston's theorem or the tetrahedrally symmetric case.

The publicly available result *Universal Santaló and volume-product laws for homothetic frusta* concerns the volume of polars **about the Santaló center** and the classical Mahler volume product. Its complete proof contains no polar of the **difference body** and therefore does not imply the identity (8) or the Makai bounds. The available result *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* treats mixed volumes with reflection on **simplex bases only**; it does not compute the polar volume in (8) for arbitrary bases. These are neighboring, but distinct, geometric functionals.

## Limitations
For \(d>3\), the general sharp Makai lower bound for arbitrary convex bases is **not** proved here; only the exact reduction (1) is proved. The sharp bound (3) uses the established planar theorem and is restricted to homothetic frusta, not all three-dimensional convex bodies. The upper endpoint \(t=1\) is interpreted through an affine-normalized limit, not as the volume product of a dimension-deficient body. No claim about unrelated skew prismatoids is made. While the searched and materially examined results do not cover (1)--(3), older unindexed convex-geometric integral formulas remain a possible priority risk. Search absence is not a certificate of global novelty.

## References
1. M. Winter, *A relation between Mahler volume and flag number for convex polytopes*, arXiv:2610.09990v1, first posted October 7, 2026, especially Theorem 1 and the discussion of equality; https://arxiv.org/html/2610.09990v1.
2. A. Aliev, *Mahler-type volume inequality for convex bodies with tetrahedral symmetry*, arXiv:2511.14991v1, November 19, 2025, Theorems 1.1 and 1.2; https://arxiv.org/html/2511.14991.
3. K. Böröczky, E. Makai, M. Meyer, and S. Reisner, *On the volume product of planar polar convex bodies: Lower estimates with stability*, Studia Sci. Math. Hung. 50 (2013), 159--198, DOI:10.1556/SScMath.50.2013.2.1235; discussion of Eggleston's sharp planar result.
4. *Universal Santaló and volume-product laws for homothetic frusta*, publicly available research result (October 2026), complete `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-santal-and-volume-product-laws-for-homothetic-frusta--3dbfdaf0b359.
5. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, publicly available research result (October 2026), complete `RESULT.md` at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949.
