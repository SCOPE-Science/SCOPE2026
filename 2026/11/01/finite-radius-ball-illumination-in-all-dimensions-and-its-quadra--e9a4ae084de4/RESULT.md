# Finite-radius ball-illumination in all dimensions and its quadratic terminal law

## Finding
For every integer \(n\ge3\), every \(0<r<R\), and every volume increment \(0<\delta<\delta_*\), where
\[\delta_*:=\kappa_n(R^n-r^n),\qquad \kappa_j:=\frac{\pi^{j/2}}{\Gamma(j/2+1)},\]
the radius-\(R\) illumination body of the Euclidean ball \(K=rB_2^n\) is itself a centered ball. The radius is given *at finite increments*, not only asymptotically, by the one-dimensional integral formula below. In addition, its approach to the maximal radius is precisely quadratic in the remaining volume deficit, with an explicit dimension-dependent constant.

Put \(c=R-r\) and, for \(0\le\alpha\le\pi\), define
\[s_\alpha=c\cos\alpha+\sqrt{R^2-c^2\sin^2\alpha},\qquad q_\alpha=-r\cos\alpha.\]
Set
\[\begin{aligned}
V_n(\alpha):=\kappa_{n-1}\bigg[&\int_{-r}^{q_\alpha}(r^2-z^2)^{(n-1)/2}\,dz\\
&+\int_{q_\alpha}^{s_\alpha}\left(\sqrt{R^2-(z-c\cos\alpha)^2}-c\sin\alpha\right)^{n-1}\,dz\bigg].
\end{aligned}\]
Then \(V_n\) is continuous and strictly decreasing on \([0,\pi]\), with \(V_n(0)=\kappa_n R^n\) and \(V_n(\pi)=\kappa_n r^n\). For the unique \(\alpha(\delta)\in(0,\pi)\) satisfying \(V_n(\alpha(\delta))-\kappa_nr^n=\delta\),
\[I_R^\delta(K)=s_{\alpha(\delta)}B_2^n.\]
Let \(B(a,b)=\Gamma(a)\Gamma(b)/\Gamma(a+b)\), and set
\[T_n:=(R-r)(n-1)\kappa_{n-1}R^{n-1}B(1/2,n/2).\]
The sharp terminal laws are
\[\lim_{\delta\uparrow\delta_*}\frac{(2R-r)-s_{\alpha(\delta)}}{(\delta_*-\delta)^2}=\frac{(R-r)(2R-r)}{2RT_n^2}\]
and
\[\lim_{\delta\uparrow\delta_*}\frac{\kappa_n(2R-r)^n-|I_R^\delta(K)|}{(\delta_*-\delta)^2}=\frac{n\kappa_n(R-r)(2R-r)^n}{2RT_n^2}.\]
All constants are positive, so exponent two is exact. For \(n=3\), \(T_3=\pi^2(R-r)R^2\).

## Assumptions and scope
The radius-\(R\) ball-convex hull of \(A\subset\mathbb R^n\) is the intersection of all *closed* radius-\(R\) balls that contain \(A\). Write \([K,x]_R\) for the hull of \(K\cup\{x\}\), and
\[I_R^\delta(K)=\{x:\lvert[K,x]_R\setminus K\rvert\le\delta\}.\]
We restrict to \(n\ge3\), \(0<r<R\), and \(r\le |x|\le2R-r\), where the family of covering balls is nonempty. At \(\delta=0\) the illumination body is \(K\); at \(\delta=\delta_*\) the radius reaches \(2R-r\). The two-dimensional calculation was already available independently and is **not** claimed here as new.

## Proof
**1. Meridian reduction.** Put \(x=se_1\). A closed radius-\(R\) ball \(B(m,R)\) contains \(rB_2^n\) if and only if \(|m|\le c\); it also contains \(x\) if and only if \(|m-se_1|\le R\). Thus admissible centers comprise the lens
\[C_s=B(0,c)\cap B(se_1,R).\]
For a candidate point \(y=ze_1+wu\), \(u\perp e_1\), \(w\ge0\), consider an arbitrary center \(m=ae_1+bu+v\), with \(v\perp\operatorname{span}\{e_1,u\}\). The center \(m'=ae_1-\sqrt{b^2+|v|^2}\,u\) has the same length and first coordinate as \(m\), hence belongs to \(C_s\) whenever \(m\) does. Moreover \(|y-m'|\ge|y-m|\). Therefore the furthest admissible center from \(y\) may be chosen in the meridian plane, on the opposite transverse side; the \(n\)-dimensional hull's meridian sections are exactly the planar radius-\(R\) ball hull of the disk of radius \(r\) together with the point \((s,0)\).

**2. Two-arc boundary and slices.** For \(r<s<2R-r\), the two circles in center space, \(|m|=c\) and \(|m-se_1|=R\), intersect in the centers \((c\cos\alpha,\pm c\sin\alpha)\), where \(s=s_\alpha\). The circle through the added point with lower center \((c\cos\alpha,-c\sin\alpha)\) is tangent to \(rB_2^2\) at \((q_\alpha,r\sin\alpha)\). Elementary circle support inequalities show that the upper meridian boundary follows the original radius-\(r\) circle from its leftmost point to this tangency, then follows the radius-\(R\) circle to \((s,0)\). Explicitly its nonnegative transverse radius is
\[\rho_\alpha(z)=\begin{cases}
\sqrt{r^2-z^2},&-r\le z\le q_\alpha,\\
\sqrt{R^2-(z-c\cos\alpha)^2}-c\sin\alpha,&q_\alpha\le z\le s_\alpha.
\end{cases}\]
For completeness, every boundary point on the second arc is exactly distance \(R\) from the stated admissible center; every other admissible center lies closer by the circle-center lens constraint. For the first arc the antipodal radius-\(c\) center is admissible and the original ball lies in all the covering balls. Conversely, any point strictly outside either arc violates the covering-ball inequality for the corresponding center. Rotation about \(e_1\), followed by Cavalieri integration, gives the displayed \(V_n(\alpha)\).

**3. Strict invertibility and the illumination ball.** The function \(s_\alpha\) is strictly decreasing from \(2R-r\) to \(r\). If \(r\le s_1<s_2\le2R-r\), then \(s_1e_1\in\operatorname{conv}(rB_2^n\cup\{s_2e_1\})\subseteq[rB_2^n,s_2e_1]_R\); consequently the hull for \(s_1\) is contained in the hull for \(s_2\). Inclusion is strict with a positive-volume difference because the second hull extends strictly further along the axis. Therefore \(V_n\) is strictly decreasing. The endpoint hulls are respectively \(rB_2^n\) and the single radius-\(R\) ball centered at \(ce_1\). Rotation invariance implies that the illuminated set is the claimed centered ball.

**4. Quadratic terminal law.** As \(\alpha\downarrow0\), direct expansion gives
\[2R-r-s_\alpha=\frac{c(2R-r)}{2R}\alpha^2+O(\alpha^4).\]
Differentiation of the volume integrals at \(\alpha=0^+\) is legitimate by domination; moving endpoint terms vanish because the corresponding section radii agree at tangency and vanish at the right endpoint. Only the downward displacement \(-c\sin\alpha\) of the second arc contributes at first order:
\[V_n(0)-V_n(\alpha)=c(n-1)\kappa_{n-1}\alpha\int_{-R}^R(R^2-t^2)^{(n-2)/2}\,dt+o(\alpha)=T_n\alpha+o(\alpha).\]
Eliminate \(\alpha\) using \(\delta_*-\delta=V_n(0)-V_n(\alpha)\); this proves the first limit. The second follows by differentiating \(\kappa_n s^n\) at \(s=2R-r\). No finite sampling is used to prove these limits.

## Verification
The accompanying `verify.py` numerically integrates the stated slice formula for \(n=2,3,4,6\), two rational radius pairs and multiple angles, tests strict increase with the attachment radius, independently compares the \(n=2\) integral with the elementary circular-arc area, and checks both endpoint scalings. It reports 140 finite checks passed. Run `python verify.py` with `mpmath` installed according to `requirements.txt`. These are corroborations, not exhaustive proofs.

## Relationship to prior work
Oliva, Werner and Yalikun (2026) introduced radius-\(R\) illumination bodies, established convexity and small-increment curvature-based asymptotics, and studied relative surface area. The present result fixes a spherical input and determines the entire finite-increment law in all dimensions \(n\ge3\), including a terminal regime not given by its small-increment theorem. Bezdek (2019) studies congruent-ball intersections and spindle extremal geometry but not this complete ball-plus-point illumination-volume inversion. A previously obtained exact planar circular-arc calculation covers \(n=2\); all planar consequences are excluded from the novelty claim.

## Limitations
The formulas rely on concentric Euclidean-ball input and equal covering radius. They do not classify nonball inputs or weighted illumination bodies. The integral representation is exact but need not reduce to elementary functions in all dimensions. Historical priority of the meridian representation in older ball-convexity literature cannot be ruled out; independent validation is not performed.

## References
1. B. E. Oliva, E. M. Werner, D. Yalikun, *Illumination bodies for ball-convex bodies*, arXiv:2607.13714v1 (2026-07-15), https://arxiv.org/html/2607.13714v1.
2. K. Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118v1 (2019-12-11), https://arxiv.org/abs/1912.05118.
