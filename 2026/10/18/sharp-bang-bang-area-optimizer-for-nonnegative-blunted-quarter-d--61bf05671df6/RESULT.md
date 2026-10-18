# Sharp bang-bang area optimizer for nonnegative blunted-quarter-disk curvature profiles

## Finding
For each \(\pi/4<m<\pi/2\), consider every measurable, midpoint-symmetric profile \(r:[0,2m]\to[0,1/2]\) satisfying the endpoint-closing condition in the next section. Each profile produces a reduced planar convex body of thickness one, with two opposite active width-one arcs joined by two straight edges. **The unique area-maximizing profile, up to equality almost everywhere, is bang-bang**:
\[
r_m^*(m+x)=\begin{cases}0,&|x|<a_m,\\[2pt]\tfrac12,&a_m<|x|<m,\end{cases}
\qquad a_m=\arcsin\!\left(\frac{-\cos(2m)}{\sin m}\right).
\]
The exact maximal area in this infinite-dimensional family is
\[
\boxed{\mathcal A_m^*=\frac m2+\frac{\sin(2m)}4+\frac12\left[(m-a_m)-\sin(m-a_m)+(\cos a_m-\cos m)(\sin m-\sin a_m)\right].}
\]
There is also a quantitative stability inequality in the curvature-profile topology specified in the proof. At the angle \(m=15/16\), the unique optimizer has
\[
0.79455604<\mathcal A_{15/16}^*<0.79455605,
\]
which supplies an explicit improved lower bound for the unrestricted maximal area of reduced planar bodies of thickness one. Neither the unrestricted optimum nor the best angle \(m\) across this larger bang-bang family is determined here.

## Assumptions and scope
All geometry is Euclidean in \(\mathbb R^2\). Set \(u_\theta=(\cos\theta,\sin\theta)\), \(v_\theta=(-\sin\theta,\cos\theta)\), \(k=\frac12\cot^2m\), and \(T=\cot m\). A profile is admissible when it is Lebesgue measurable, \(0\le r(\theta)\le1/2\) almost everywhere, \(r(m+x)=r(m-x)\) almost everywhere, and
\[
\int_0^{2m}(r(\theta)-k)v_\theta\,d\theta=0.
\]
Equivalently, with \(f(x)=r(m+x)\) for \(-m\le x\le m\), the last condition is
\[
\int_{-m}^{m}f(x)\cos x\,dx=2k\sin m=\frac{\cos^2m}{\sin m}.
\]
The constraint is feasible for the stated range of \(m\), and the claimed bang-bang profile is admissible since \(\sin m-\sin a_m=\cos^2m/\sin m\).

Define \(c(\theta)=\int_0^\theta r(t)v_t\,dt\), \(a(\theta)=c(\theta)+\tfrac12u_\theta\), and \(b(\theta)=c(\theta)-\tfrac12u_\theta\). The body \(R_{m,r}\) has boundary, in order, the image of \(a\) on \([0,2m]\), the segment \([a(2m),b(0)]\), the image of \(b\) traversed in reverse, and the segment \([b(2m),a(0)]\). Zero-speed portions of an arc are permitted: the extremal profile is not required to have positive curvature everywhere. The whole theorem pertains to this precisely defined, midpoint-symmetric, nonnegative-profile family; it asserts no maximization among arbitrary reduced bodies.

## Proof
**1. Closing, convexity, width and reducedness.** Midpoint symmetry makes the sine part of the closing integral vanish. Its cosine part is the displayed moment constraint. Hence \(c(2m)=k(\cos2m-1,\sin2m)\), so \(a(0)=(1/2,0)\), \(a(2m)=(-1/2,T)\), and both straight connecting edges have length \(T>0\), independent of the profile.

The support function has, on the active normal interval \([0,2m]\), the form \(h(\theta)=c(\theta)\cdot u_\theta+1/2\), and on the opposite interval \([\pi,\pi+2m]\) the form \(h(\theta)=1/2-c(\theta-\pi)\cdot u_{\theta-\pi}\). On each complementary interval it is the support function of the corresponding endpoint vertex. The absolutely continuous curvature-radius densities on the active intervals are \(1/2+r\) and \(1/2-r\), both nonnegative; the only atomic contributions to \(h+h''\) are the two positive straight-edge masses \(T\). Thus \(h\) is the support function of the asserted convex body, including for discontinuous profiles.

Opposite active support values sum to one. For a normal in a complementary interval, write its angular separation from the preceding active normal as \(z\in[0,\pi-2m]\); its width is \(\cos z+T\sin z\), which is strictly greater than one in the interior and equals one at the endpoints. Therefore \(R_{m,r}\) has thickness exactly one. On active interiors \(h\) is continuously differentiable, so each relevant supporting face is a singleton. Any convex subset with thickness at least one must have both opposite support values equal to those of \(R_{m,r}\) on all active normals; it therefore contains every point of both active arcs. Closure and convexity force it to contain the two connecting segments and hence the whole body. Therefore every \(R_{m,r}\) is reduced.

**2. Exact area as a quadratic functional.** Since \(a'=(1/2+r)v\) and \(b'=(r-1/2)v\) almost everywhere, Green's area formula yields
\[
\operatorname{area}(R_{m,r})=\frac m2+\frac{\sin2m}{4}
+\int_0^{2m}r(\theta)\int_0^\theta r(t)\sin(\theta-t)\,dt\,d\theta.
\]
After the change \(x=\theta-m\), write
\[
\mathcal J(f)=\frac12\int_{-m}^m\!\int_{-m}^m f(x)f(y)\sin|x-y|\,dy\,dx.
\]
Area equals \(m/2+\sin(2m)/4+\mathcal J(f)\).

**3. A strict concavity identity.** Let \(f,g\) be two admissible profiles, \(\delta=f-g\), and \(z(x)=\int_{-m}^m\delta(y)\sin|x-y|\,dy\). Evenness and the fixed cosine moment imply \(z(-m)=z(m)=0\); distributionally \(z''+z=2\delta\). Consequently
\[
\int_{-m}^m\!\int_{-m}^m\delta(x)\delta(y)\sin|x-y|\,dy\,dx
=\frac12\left(\int z^2-\int(z')^2\right)<0
\]
when \(\delta\ne0\), by the Dirichlet Poincaré inequality on an interval of length \(2m<\pi\). Thus \(\mathcal J\) is strictly concave on the affine set of admissible moment profiles.

**4. Global optimality of the bang-bang profile.** Let \(f_*(x)=\tfrac12\mathbf1_{\{|x|>a_m\}}\), and put \(y_*(x)=\int_{-m}^m f_*(t)\sin|x-t|\,dt\). It is even and satisfies \(y_*''+y_*=2f_*\). For \(0\le x<m\), let \(F(x)=y_*(x)/\cos x\). A direct differentiation gives
\[
F'(x)=\frac{y_*'(x)\cos x+y_*(x)\sin x}{\cos^2x},\qquad
\frac d{dx}\bigl(y_*'\cos x+y_*\sin x\bigr)=2f_*(x)\cos x.
\]
The numerator vanishes at zero. Hence \(F\) is constant on \([0,a_m]\) and strictly increasing on \((a_m,m)\). For another admissible \(f\), the difference \(\delta=f-f_*\) is nonnegative on \(|x|<a_m\) and nonpositive on \(|x|>a_m\); the shared cosine moment therefore gives
\[
\int_{-m}^m \delta(x)y_*(x)\,dx
=\int_{-m}^m\delta(x)\cos x\,[F(|x|)-F(a_m)]\,dx\le0.
\]
Expanding the quadratic area functional at \(f_*\) and applying Step 3 shows \(\mathcal J(f)<\mathcal J(f_*)\) whenever \(f\ne f_*\) almost everywhere, proving both sharpness and uniqueness.

**5. Exact optimum and stability.** The two end intervals where \(f_*=1/2\) each have length \(L=m-a_m\). Integrating \(\sin|x-y|\) separately over each interval and across the two intervals yields
\[
\mathcal J(f_*)=\frac12\left[L-\sin L+(\cos a_m-\cos m)(\sin m-\sin a_m)\right],
\]
which is the displayed maximal-area formula. More precisely, let \(z(x)=\int_{-m}^m(f-f_*)(t)\sin|x-t|\,dt\). The expansion above and Poincaré give the quantitative gap
\[
\mathcal A_m^*-\operatorname{area}(R_{m,r})\ge
\frac14\left(1-\frac{4m^2}{\pi^2}\right)\int_{-m}^m|z'(x)|^2\,dx.
\]
The factor is strictly positive for every allowed \(m\). This estimate is a curvature-profile stability statement, not a Hausdorff stability estimate.

## Verification
The file `verify.py` is a self-contained Python 3 program using exact rational arithmetic. It verifies \(\pi/4<15/16<\pi/2\), constructs a rigorous rational bracket for \(a_{15/16}\) through monotone sine bisection with alternating Taylor remainders, and gives rational bounds \(0.79455604<\mathcal A_{15/16}^*<0.79455605\), strictly greater than \(0.788844\). Execute `python verify.py`; successful execution prints `VERIFY_OK`. The universal maximizing assertion is established by the analytic proof above; numerical or finite tests are not substituted for that proof. The area integral and closed form were also cross-checked independently by splitting the piecewise-constant profile into its two intervals and integrating the resulting trigonometric functions.

## Relationship to prior work
S. D. Kominers (arXiv:2606.28612v1, June 26, 2026) introduced the closed two-arc support construction, proved a reduced thickness-one example of area \(0.7862156\ldots\), and explicitly left optimization open. Subsequent published results *Exact area optimizer on the fixed-angle blunted quarter-disk slice* and *Unique optimal blunting angle in a two-parameter family of reduced planar bodies* optimize the **affine-cosine** curvature family \(r=k+\varepsilon(1-q\cos(\theta-m))\), first at fixed \(m\), then over \(m\) and nonnegative \(\varepsilon\); the latter obtains \(0.78884379\ldots\). The present theorem instead optimizes the full infinite-dimensional class of **all bounded measurable midpoint-symmetric nonnegative** curvature profiles with the same closing constraint at each fixed angle; it is not a corollary of either finite-parameter optimization. Its maximizing profile is discontinuous, with entire subarcs at curvature radii zero or one. Classical bang-bang control principles suggest an analogy, but do not determine this geometry-specific fixed-angle extremizer, the area law, or the stated profile stability without additional calculation.

## Limitations
The restriction \(0\le r\le1/2\) is essential to the present argument; it is more restrictive than the bare convexity condition \(-1/2\le r\le1/2\). Midpoint symmetry and a fixed active angle are also essential. In particular no assertion is made about all reduced planar bodies, the unrestricted area optimum, negative curvature-splitting profiles, or the best choice of \(m\). Priority may be affected by unindexed earlier curvature-control formulations.

## References
1. S. D. Kominers, *A reduced planar body with area greater than \(\pi\Delta^2/4\)*, arXiv:2606.28612v1, https://arxiv.org/abs/2606.28612 (first public June 26, 2026).
2. *Exact area optimizer on the fixed-angle blunted quarter-disk slice* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-area-optimizer-on-the-fixed-angle-blunted-quarter-disk-sli--369c8e768fcb/RESULT.md.
3. *Unique optimal blunting angle in a two-parameter family of reduced planar bodies* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-unique-optimal-blunting-angle-in-a-two-parameter-family-of-reduc--d114e83fb3e1/RESULT.md.
4. M. Lassak and H. Martini, *Reduced convex bodies in Euclidean space—a survey*, Expositiones Mathematicae 29 (2011), 204–219, DOI:10.1016/j.exmath.2011.01.006.
5. M. Lassak, *Reduced convex bodies in the plane*, Israel Journal of Mathematics 70 (1990), 365–379, DOI:10.1007/BF02801470.
