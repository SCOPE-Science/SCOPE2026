# Strict hole monotonicity and exact affine-projection norms on spherical annuli

## Finding
For each integer \(d\ge 2\) and \(0\le r<1\), give the spherical annulus
\[
A_{d,r}=\{x\in\mathbb R^d:r\le\|x\|_2\le1\}
\]
normalized uniform volume, and let \(P_{d,r}\) be its real \(L^2\)-orthogonal projection onto the \((d+1)\)-dimensional space of affine functions. Set
\[
\kappa_{d,r}=\frac{(d+2)(1-r^d)}{1-r^{d+2}},\qquad
q_d=\frac{d+1}{2},\qquad
c_d=\frac{\Gamma(d/2+1)}{\sqrt\pi\,\Gamma(q_d)}.
\]
For \(s\ge0\), define the explicit incomplete-beta quantity
\[
H_d(s)=\begin{cases}
0,&0\le s\le1,\\[2pt]
c_d\left[\dfrac{s}{d+1}(1-s^{-2})^{q_d}-\dfrac12
B_{1-s^{-2}}\left(q_d,\frac12\right)\right],&s>1,
\end{cases}
\]
where \(B_z(p,q)=\int_0^z u^{p-1}(1-u)^{q-1}\,du\). Then the *exact, attained endpoint norm* is
\[
\boxed{L_d(r):=\|P_{d,r}\|_{L^\infty\to L^\infty}
=1+\frac{2\,[H_d(\kappa_{d,r})-r^d H_d(r\kappa_{d,r})]}{1-r^d}.}
\]
Every maximizing spatial kernel row lies on the outer sphere \(\|x\|_2=1\), and every outer-sphere point maximizes; points of smaller radius are never maximizers. More strongly, \(L_d(r)\) is **strictly decreasing** for \(0\le r<1\). Its continuous endpoint at \(r=1\) is the affine-projector norm for uniform surface measure on \(S^{d-1}\). Hence
\[
L_d(0)>L_d(r)>L_d(1)\quad(0<r<1).
\]
Removing a small central ball has a dimension-sharp leading effect:
\[
\boxed{L_d(0)-L_d(r)=
I_{1-(d+2)^{-2}}\!\left(\frac{d+1}{2},\frac12\right)r^d
+O_d(r^{d+2}+r^{2d})\quad(r\downarrow0),}
\]
where \(I_z(p,q)=B_z(p,q)/B(p,q)\) is the regularized incomplete beta function. This leading coefficient is strictly between zero and one. Uniformly even when the hole radius depends on dimension,
\[
\boxed{\lim_{d\to\infty}\ \sup_{0\le r\le1}
\left|\frac{L_d(r)}{\sqrt d}-\sqrt{\frac2\pi}\right|=0.}
\]
Here \(r=1\) means the limiting surface projector, not normalized volume on a zero-volume set.

## Assumptions and scope
All functions, scalars, and inner products are real. For \(r<1\), the measure is \(dx/|A_{d,r}|\). The affine projector acts on \(L^2\), but its finite-rank reproducing-kernel formula defines a bounded map on \(L^\infty\). The target maximum norm is the essential supremum of its continuous affine output. Evaluation at a boundary point is understood through the unique continuous representative. The surface case at \(r=1\) is defined separately by normalized surface area. Integer dimensions below two are not asserted for the volume-annulus theorem.

## Proof
**Kernel and sharp rows.** Let \(X\) be uniform on \(A_{d,r}\). Rotational invariance gives \(\mathbb EX=0\) and \(\mathbb E(XX^{\mathsf T})=\kappa_{d,r}^{-1}I_d\), because
\[
\mathbb E\|X\|_2^2=\frac{d}{d+2}\frac{1-r^{d+2}}{1-r^d}.
\]
The affine reproducing kernel is therefore \(K(x,y)=1+\kappa_{d,r}\,x\cdot y\). Its operator norm is
\(\sup_{x\in A_{d,r}}\mathbb E|K(x,X)|\). For fixed direction \(u\), the row integral at \(x=tu\) is \(\mathbb E|1+\kappa_{d,r}t\,u\cdot X|\). This is nondecreasing and convex in \(t\ge0\) by symmetry. It is strictly increasing once the kernel changes sign on a set of positive measure. Since \(\kappa_{d,r}>1\) and the support reaches the unit sphere, every \(t<1\) has strictly smaller row integral than \(t=1\): if \(t\le1/\kappa_{d,r}\), its value is \(1\), while at \(t=1\) it exceeds \(1\); if \(t>1/\kappa_{d,r}\), the derivative is strictly positive. Hence exactly the outer-sphere rows maximize. Taking \(f(y)=\operatorname{sgn}K(u,y)\) for any \(\|u\|_2=1\) gives equality (almost everywhere \(|f|=1\)), including the essential-supremum interpretation.

**Exact beta formula.** If \(Z\) is uniform on the unit ball \(B_2^d\), its first-coordinate density on \([-1,1]\) is \(c_d(1-t^2)^{(d-1)/2}\). Thus \(H_d(s)=\mathbb E(sZ_1-1)_+\). Integration from \(t=1/s\) to \(1\) gives the stated two-term incomplete-beta expression. The annulus law is the normalized difference between full-ball volume and \(r^d\) times a radius-\(r\) ball. By reflection symmetry \(\mathbb E|1+sY_1|=1+2\mathbb E(sY_1-1)_+\). Subtraction of the two ball integrals yields the boxed formula.

**Strict monotonicity via a radial increasing-convex order.** Decompose \(X=R_r U\), where \(U\) is uniform on \(S^{d-1}\), independent of \(R_r\), with \(R_r\) having density \(d\rho^{d-1}/(1-r^d)\) for \(r<\rho<1\). Put \(S_r=\kappa_{d,r}R_r\). Its density is proportional to \(s^{d-1}\) on the interval \([\ell_r,u_r]=[r\kappa_{d,r},\kappa_{d,r}]\). As \(r\) increases, \(u_r\) decreases because \(\mathbb ER_r^2\) increases. The lower endpoint \(\ell_r\) increases strictly: after differentiating \(r(1-r^d)/(1-r^{d+2})\), its derivative numerator is
\[
g_d(r)=1-(d+1)r^d+(d+1)r^{d+2}-r^{2d+2}>0.
\]
Indeed \(g_d(1)=0\) and
\[
g'_d(r)=(d+1)r^{d-1}[-d+(d+2)r^2-2r^{d+2}]<0\quad(0<r<1),
\]
since the bracket increases strictly from \(-d\) to \(0\). Thus, for \(0\le r<t<1\), the support of \(S_t\) is a proper subinterval of that of \(S_r\), and each density is a positive constant times \(s^{d-1}\) on its own support. Consequently the difference of distribution functions \(F_t-F_r\) crosses zero exactly once, from negative to positive. Moreover
\[
\mathbb ES_r=\frac{d(d+2)}{d+1}\frac{1-r^{d+1}}{1-r^{d+2}}
\]
is strictly decreasing, because the derivative of its last ratio has the sign of \(-(d+1)+(d+2)r-r^{d+2}<0\). For every real \(z<u_r\), the one-crossing property and positive mean difference imply
\[
\mathbb E(S_r-z)_+>\mathbb E(S_t-z)_+;
\]
for \(z\ge u_r\), both expressions vanish. To see this explicitly, the difference equals \(\int_z^\infty(F_t-F_r)(s)\,ds\), which is positive for a threshold beyond the crossing; for an earlier threshold it is the positive mean difference minus an integral with negative integrand.

With \(T=U_1\), define \(\phi_d(s)=\mathbb E(sT-1)_+\). It is zero on \([0,1]\), increasing, and strictly convex on \((1,\infty)\), since
\[
\phi_d''(s)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}
\frac{(1-s^{-2})^{(d-3)/2}}{s^3}>0\quad(s>1).
\]
The strict stop-loss comparison, integrated against this positive second derivative on \((1,u_r)\), gives \(\mathbb E\phi_d(S_r)>\mathbb E\phi_d(S_t)\). Since \(L_d(r)=1+2\mathbb E\phi_d(S_r)\), strict decrease follows. Weak convergence \(R_r\to1\) and \(\kappa_{d,r}\to d\) as \(r\uparrow1\) gives the strict surface endpoint by the same comparison.

**Sharp small-hole coefficient.** For sufficiently small \(r\), \(r\kappa_{d,r}\le1\) and hence the inner-ball excess is zero. Also \(\kappa_{d,r}=(d+2)(1-r^d+O_d(r^{d+2}+r^{2d}))\). For \(s>1\), differentiating under the ball expectation gives
\[
H_d(s)-sH_d'(s)=-\Pr(Z_1>1/s).
\]
Taylor expansion in the exact norm formula therefore yields
\(L_d(0)-L_d(r)=2\Pr(Z_1>1/(d+2))r^d+O_d(r^{d+2}+r^{2d})\). Integrating the ball-coordinate density evaluates twice this probability as the regularized beta quantity in the statement.

**Uniform high-dimensional law.** For every \(r\in[0,1]\), \(d\le\kappa_{d,r}\le d+2\) (with \(\kappa_{d,1}=d\)) and \(\mathbb E(1-R_r)\le 1/(d+1)\), because radial truncation stochastically increases radius relative to the full ball. Hence \(\mathbb E|\kappa_{d,r}R_r-d|\le2+(d+2)/(d+1)<4\). With \(T=U_1\), \(\mathbb E|T|\le d^{-1/2}\), so the difference between \(L_d(r)\) and \(\mathbb E|1+dT|\) is at most \(4/\sqrt d\), uniformly in \(r\). The classical Gaussian limit \(\sqrt d\,T\Rightarrow N(0,1)\), together with its bounded second moment, gives \(\mathbb E|1+dT|/\sqrt d\to\sqrt{2/\pi}\). This proves the uniform limit.

## Verification
The companion `verify_annulus.py` uses 48-digit mpmath quadrature to check the incomplete-beta expression independently against a nested spherical/radial integral, strict ordering at selected radii, the ball/sphere dimension relation, the exact three-dimensional ball value, and the leading small-hole coefficient. It returned `VERIFY_OK: 51 high-precision formula, direct-integration, monotonicity, shell/ball, and small-hole checks`. These finite checks are corroboration; the proof above, not the tests, establishes all-dimensional claims. As transparent benchmarks,
\[
L_3(0)=\frac{253}{125}=2.024,\qquad
L_3(1)=\frac53,
\qquad L_2(1)=\frac13+\frac{2\sqrt3}{\pi}.
\]
For \(d\ge3\), the sphere-coordinate marginal identity also gives \(L_d(1)=L_{d-2}(0)\), with the ball endpoint for \(d=1\) understood by its one-dimensional definition.

## Relationship to prior work
Figueroa (2015, arXiv:1503.04485) studies orthogonal-polynomial projection approximation on the weighted unit disk, emphasizing Sobolev estimates and Zernike methods; its inspected result is on a ball, not a hollow concentric annulus with variable hole radius. Wang and Sloan (2015, arXiv:1509.03792) develop filtered polynomial approximation on spheres, with degree and smoothness parameters rather than the present volume-annulus monotonicity. The classical sphere/ball polynomial connection and single-sphere projection constants are background and are not claimed here as original. The newly isolated statement is the *complete strict hole-radius dependence with exact beta norm and leading hole-loss coefficient* for the canonical affine projector. Equivalence under older radial kernel or stochastic-order terminology remains a publication-priority risk; absence of a search hit alone is not a novelty guarantee.

## Limitations
Only concentric Euclidean annuli, real affine orthogonal projections, normalized uniform volume, and the indicated limiting surface measure are treated. No result for eccentric holes, nonradial weights, higher polynomial degrees, or arbitrary nonorthogonal projections is claimed. The weak probabilistic ordering proved here is sufficient for the specific endpoint norm; no assertion about pointwise ordering of the full signed reproducing kernels is made. Numerical quadrature checks cannot independently certify infinite-dimensional quantifiers or publication priority.

## References
1. L. E. Figueroa, *Orthogonal polynomial projection error measured in Sobolev norms in the unit disk*, arXiv:1503.04485, first public preprint 2015-03-15, https://arxiv.org/abs/1503.04485.
2. H. Wang and I. H. Sloan, *On filtered polynomial approximation on the sphere*, arXiv:1509.03792, first public preprint 2015-09-13, https://arxiv.org/abs/1509.03792.
3. Y. Xu, *Orthogonal Polynomials and Cubature Formulae on Spheres and on Balls*, SIAM J. Math. Anal., DOI 10.1137/S0036141096307357 (classical sphere/ball background; abstract inspected).
4. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, and S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, J. Lond. Math. Soc., 2026, DOI 10.1112/jlms.70429 (surface-only comparison; available abstract inspected).
