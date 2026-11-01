# Sharp nonparametric area maximum in the paired-arc reduced-body construction

## Finding
A natural class of thickness-one reduced planar convex bodies, made of two paired curved boundary pieces and two joining segments, admits a **unique global area maximizer within its entire measurable curvature-profile class**. Its curvature-radius split is zero on a central angular interval and saturates at one half on two exterior intervals; the extremal body is not in the previously optimized two-parameter cosine-profile subfamily.

For \(m\in(0,\pi/2]\), define \(u_t=(\cos t,\sin t)\), \(v_t=(-\sin t,\cos t)\), and \(k=\tfrac12\cot^2m\). An admissible profile is a measurable function \(r:[0,2m]\to[-\tfrac12,\tfrac12]\) satisfying the two real moment constraints
\[
 \int_0^{2m}(r(t)-k)v_t\,dt=0.
\]
Its associated paired-arc body \(K(m,r)\) is defined in the next section. An admissible profile exists exactly when \(\pi/4\le m\le\pi/2\).

For each feasible \(m\), put
\[
 \alpha(m)=\arcsin\!\left(2\sin m-\frac1{\sin m}\right)\in[0,m].
\]
Then, **up to changes on measure-zero sets**, the unique area-maximizing curvature profile is
\[
 \boxed{r_m(t)=\frac12\,\mathbf{1}_{\{|t-m|>\alpha(m)\}}},\qquad 0\le t\le2m.
\]
Its exact area is
\[
 \boxed{F(m)=m-\frac{\alpha(m)}2+\cos m\sin\alpha(m)
             -\frac14\sin(2\alpha(m)).}
\]
Over **all** feasible angles and profiles, there is a unique maximum at
\[
 \boxed{m_*=\arcsin\sqrt{\frac{1+\sqrt{17}}8}},\qquad
 \alpha_*=\arcsin\!\left(2\sin m_*-\frac1{\sin m_*}\right),
\]
with the sharp global value
\[
 \boxed{A_*=m_*-\frac{\alpha_*}2+\cos m_*\sin\alpha_*
       -\frac14\sin(2\alpha_*)=0.794578508627854\ldots.}
\]
The value is strictly greater than \(\pi/4\), and every body in the admissible family is reduced with minimum width one. Uniqueness here is for the normalized curvature-profile parameters; Euclidean translations and rotations do not alter the maximizing shape.

## Assumptions and scope
Define the absolutely continuous vector curve
\[
 c(t)=\int_0^t r(s)v_s\,ds,
 \qquad a(t)=c(t)+\tfrac12u_t,
 \qquad b(t)=c(t)-\tfrac12u_t,\quad 0\le t\le2m.
\]
The closed boundary traverses the curve \(a(t)\) in increasing \(t\), the segment from \(a(2m)\) to \(b(0)\), the curve \(b(t)\) in increasing \(t\), and the segment from \(b(2m)\) to \(a(0)\). These are the paired-arc and two-gap edges of the reduced-body construction motivated by Kominers. The closure condition fixes
\[
 c(2m)=k(u_{2m}-u_0).
\]
At the endpoints, \(m=\pi/4\) gives the quarter disk and \(m=\pi/2\) gives a body of constant width one; both are included. Profiles are allowed to be nonsmooth, discontinuous and of either sign within the stated interval. In particular the maximizing profile has jumps in the curvature-radius density, which are permitted for convex boundaries.

For almost every active normal, the two curved boundary pieces have nonnegative curvature radii \(\tfrac12+r(t)\) and \(\tfrac12-r(t)\). The joining edges have length \(\cot m\); the width is exactly one for active normal angles, and is strictly greater than one at the interior angles of the two gaps when \(m<\pi/2\). The gap-width formula, with angular gap parameter \(z\in[0,\pi-2m]\), is
\[
 W(z)=\cos z+\cot m\sin z\ge1,
\]
with strict inequality in the open gap when its length is positive. Consequently the minimum width is one. Any convex subset with minimum width at least one must contain all active exposed support points on both curves; their convex hull contains the joining edges, and hence equals the original body. Thus every admissible \(K(m,r)\) is reduced. Where a curvature radius vanishes on a full interval, its normal angles correspond to one exposed point, not a positive-dimensional support face, so the argument still applies.

The theorem concerns this **complete paired-arc curvature-profile class**, not the global maximum over all reduced planar convex bodies.

## Proof
**1. Feasible angles and the exact area functional.** Put \(x=t-m\). The vector moment constraints are equivalent to
\[
 \int_{-m}^{m}r(m+x)\cos x\,dx=\frac{\cos^2m}{\sin m},
 \qquad \int_{-m}^{m}r(m+x)\sin x\,dx=0.
\]
Since \(\cos x\ge0\) and \(r\le1/2\), the first equation requires \(\cos^2m/\sin m\le\sin m\), hence \(m\ge\pi/4\). Conversely the proposed profile is feasible for every \(m\in[\pi/4,\pi/2]\), because the identity
\[
 \sin\alpha(m)=2\sin m-\csc m
\]
gives \(\int r_m(m+x)\cos x\,dx=\sin m-\sin\alpha=\cos^2m/\sin m\), while symmetry makes the sine moment zero.

A direct Green-theorem calculation along the two curves, followed by the fixed joining segments, gives
\[
 \operatorname{area}K(m,r)
 =\frac m2+\frac{\sin(2m)}4+Q_m(r),
 \qquad
 Q_m(r)=\int_0^{2m}r(t)\int_0^t r(s)\sin(t-s)\,ds\,dt.
\]
Equivalently,
\[
 Q_m(r)=\frac12\int_0^{2m}\int_0^{2m}
  r(t)r(s)\sin|t-s|\,ds\,dt.
\]
All integrals are well defined for bounded measurable profiles. The endpoint closure makes the joining-segment area contribution independent of the profile.

**2. Strict concavity on the two-moment affine space.** Let \(f\) be the difference of two admissible profiles and define
\[
 p(t)=\int_0^t f(s)\sin(t-s)\,ds.
\]
Then \(p''+p=f\) almost everywhere and \(p(0)=p'(0)=0\). The moment constraints imply \(p(2m)=p'(2m)=0\). Integration by parts yields
\[
 Q_m(f)=\int_0^{2m}f(t)p(t)\,dt
 =\int_0^{2m}\bigl(p(t)^2-p'(t)^2\bigr)\,dt.
\]
Since \(2m\le\pi\) and \(p\) vanishes at both ends, the Dirichlet Poincaré inequality gives \(Q_m(f)\le0\). Equality for \(2m<\pi\) forces \(p=0\). When \(2m=\pi\), the only possible nonzero equality function would be a multiple of \(\sin t\), contradicting \(p'(0)=0\). Thus **\(Q_m(f)<0\) whenever \(f\ne0\) almost everywhere** and both moment constraints vanish. This establishes strict concavity of area on each feasible affine space.

**3. A pointwise dual certificate for the entire infinite-dimensional optimization.** Fix a feasible \(m\), abbreviate \(\alpha=\alpha(m)\), and write \(r_*(m+x)=\tfrac12\mathbf1_{\{\alpha<|x|<m\}}\). Define the first-variation potential
\[
 H(x)=\int_{-m}^{m}r_*(m+y)\sin|x-y|\,dy,
 \qquad \lambda=\cos\alpha-\cos m.
\]
Direct integration over the two exterior intervals gives the exact *complementarity relation*
\[
 \boxed{H(x)-\lambda\cos x=
 \begin{cases}0,&|x|\le\alpha,\\
 1-\cos(|x|-\alpha),&\alpha<|x|\le m.
 \end{cases}}
\]
For any other admissible \(r\), put \(f=r-r_*\). The cosine moment of \(f\) is zero. On the exterior intervals, \(r_*\) attains its allowed upper bound, so \(f\le0\), while \(H-\lambda\cos x>0\); on the central interval the dual factor vanishes. Therefore
\[
 \int_{-m}^{m}H(x)f(m+x)\,dx\le0.
\]
The exact quadratic expansion of the area difference is
\[
 \operatorname{area}K(m,r)-\operatorname{area}K(m,r_*)
 =\int_{-m}^{m}H(x)f(m+x)\,dx+Q_m(f)\le0.
\]
Strict negativity of \(Q_m(f)\) for every nonzero feasible \(f\) proves **uniqueness**. This proof covers all admissible measurable profiles, not only a finite Fourier or cosine ansatz.

**4. Exact optimized profile area and global angle.** The profile consists of two equal length intervals, each of length \(m-\alpha\), on which \(r=1/2\). Put \(\ell=m-\alpha\). Each of the two constant-radius intervals contributes \(\tfrac14(\ell-\sin\ell)\) to \(Q_m\). Their cross contribution is
\[
 \frac14\{2\sin(m+\alpha)-\sin(2\alpha)-\sin(2m)\}.
\]
Adding the fixed boundary term \(m/2+\sin(2m)/4\) and using \(\sin(m+\alpha)-\sin(m-\alpha)=2\cos m\sin\alpha\) simplifies the area to
\[
 F(m)=m-\frac\alpha2+\cos m\sin\alpha-\frac14\sin2\alpha.
\]
For \(\pi/4<m<\pi/2\), put \(s=\sin m\) and \(u=s^{-2}\in(1,2)\). Differentiation yields
\[
 F'(m)=(1-s^2)\bigl[(4+u)-(2+u)\sqrt{4-u}\bigr].
\]
The two terms in the brackets are positive; their squared difference factors as
\[
 (4+u)^2-(2+u)^2(4-u)=u(u^2+u-4).
\]
Thus the derivative has the sign of \(u^2+u-4\), which changes once because \(u=\csc^2m\) decreases strictly from \(2\) to \(1\). The unique maximum satisfies \(u_*=(\sqrt{17}-1)/2\), giving \(\sin^2m_*=(1+\sqrt{17})/8\). Both endpoints yield \(F=\pi/4\); strict derivative signs show that the displayed interior critical point is the unique global optimum. Exact rational enclosures in the supplied verifier establish
\[
 0.79457850<A_*<0.79457852.
\]
In particular, \(A_*>\pi/4\), and the more precise decimal in the statement is a numerical evaluation of the explicit elementary expression.

## Verification
The standalone `verify.py` uses only Python's standard library. It proves a rational enclosure of the sharp area using exact rational square-root brackets and a rational Taylor-series enclosure for inverse sine. Independently of the area integral, it constructs the two boundary curves for seven selected angles, checks polygonal Green-theorem area against the exact formula, checks the closure equations, and numerically compares the dual potential with its piecewise closed formula. Running `python verify.py` produces `VERIFY_OK`.

The rational interval check certifies the displayed coarse numerical enclosure; polygonal and potential comparisons are finite checks, not substitutes for the infinite-dimensional concavity and complementarity proof. The explicit formula for the optimum and the uniqueness theorem follow analytically.

## Relationship to prior work
S. D. Kominers (arXiv:2606.28612v1, first public June 26, 2026) constructed a thickness-one reduced body using two paired arcs and two joining edges, with a smooth cosine-type curvature-radius split. Its displayed example has area \(0.7862156027\ldots\) and disproves the previously conjectured \(\pi/4\) upper bound. The paper points out that its parameter choices need not optimize area.

The later published *Exact area optimizer on the fixed-angle blunted quarter-disk slice* optimizes one positive cosine-amplitude parameter at fixed \(m=15/16\), obtaining \(0.7871835267\ldots\). The published *Unique optimal blunting angle in a two-parameter family of reduced planar bodies* optimizes both cosine-profile parameters on a specified quadrant, obtaining \(0.7888437886\ldots\). Both results optimize proper finite-dimensional subsets of the admissible profile space. Their proofs and stated domains do not provide the dual-certificate classification of **all bounded measurable curvature-radius splits**, the new piecewise-constant optimizing curvature, or the algebraic global angle. The new maximum is strictly larger than their values; its profile is not a cosine-profile member. The moment-space concavity argument is the structural new ingredient.

The theory of reduced convex bodies and support functions predates this construction and supplies its geometric context. No claim of global optimality among arbitrary reduced bodies, nor of priority over all unindexed formulations of this particular infinite-dimensional extremum, is made.

## Limitations
The admissible class requires a pair of antipodal active arcs with unit total support width, two prescribed straight gaps, and bounded curvature-radius splits satisfying the exact closure moments. Other reduced bodies may have larger area. The theorem is about maximum area, not perimeter or shape stability. The extremizer's profile is discontinuous (its boundary remains convex and piecewise continuously curved). The rational verifier certifies area bounds rather than the exact global functional inequality; the latter is proved using the displayed integral identities and the Dirichlet Poincaré inequality. Historical priority for the full nonparametric theorem remains provisional.

## References
1. S. D. Kominers, *A reduced planar body with area greater than \(\pi\Delta^2/4\)*, arXiv:2606.28612v1 (first public June 26, 2026), https://arxiv.org/html/2606.28612v1.
2. *Exact area optimizer on the fixed-angle blunted quarter-disk slice* (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-area-optimizer-on-the-fixed-angle-blunted-quarter-disk-sli--369c8e768fcb.
3. *Unique optimal blunting angle in a two-parameter family of reduced planar bodies* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-unique-optimal-blunting-angle-in-a-two-parameter-family-of-reduc--d114e83fb3e1.
4. M. Lassak and H. Martini, *Reduced convex bodies in Euclidean space—a survey*, Expositiones Mathematicae 29 (2011), 204–219.
