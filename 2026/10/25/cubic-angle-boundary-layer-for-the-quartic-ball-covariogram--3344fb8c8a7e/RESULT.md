# Cubic-angle boundary layer for the quartic-ball covariogram

## Finding
Let \(K=\{(x,y)\in\mathbb R^2:x^4+y^4\le1\}\) and let \(g(v)=|K\cap(K+v)|\). For real \(\lambda\), \(t>0\), and \(e_{\lambda,t}=(\cos(\lambda t^3),\sin(\lambda t^3))\), define the exact directional width
\[
w_{\lambda,t}=2\left(|\cos(\lambda t^3)|^{4/3}+|\sin(\lambda t^3)|^{4/3}\right)^{3/4}.
\]
There is a continuous even strictly increasing function \(F\) on nonnegative arguments such that, locally uniformly in real \(\lambda\),
\[
 w_{\lambda,t}t-\bigl(|K|-g(te_{\lambda,t})\bigr)=t^5F(\lambda)+o(t^5).
\]
For each \(0\le r\le1\), let \(m=m(\lambda,r)\) denote the unique real root of
\[
 m^3+\tfrac14r^2m+\lambda=0.
\]
Then the crossover coefficient has the explicit one-dimensional integral
\[
 F(\lambda)=2\int_0^1\left(\tfrac34|\lambda|^{4/3}-\tfrac34m^4+\tfrac18r^2m^2+\tfrac1{64}r^4\right)\,dr.
\]
It satisfies
\[
 F(0)=\frac1{160},\qquad
 F(\lambda)=\frac{|\lambda|^{2/3}}4-\frac7{480}+O(|\lambda|^{-2/3})
 \quad(|\lambda|\longrightarrow\infty).
\]
Thus the angular crossover has scale \(\theta\asymp t^3\): the flat-axis correction is fifth order, while a fixed nonaxial direction has a third-order curvature correction.

## Assumptions and scope
The body is the unit \(\ell_4\) disk in the Euclidean plane, the translation parameter \(t\downarrow0\) is Euclidean distance, and \(\lambda\) is fixed (uniformity asserted on every bounded real interval). Area is planar Lebesgue area. The width used in the normalization is the *true width perpendicular to translation*, not the constant coordinate width. The theorem is not claimed for arbitrary \(\ell_p\) disks or dimensions.

## Proof
**1. Exact chord identity.** For a centrally symmetric convex planar body with a direction \(e\) and perpendicular unit normal \(n\), let \(h\) denote its support in direction \(n\) and \(L(z)\) the length of its section on the line \(\langle x,n\rangle=z\), parallel to \(e\). Concavity of \(L\) and central symmetry imply \(\{z:L(z)\ge s\}=[-z_s,z_s]\), for sufficiently small \(s\). Translating each chord by \(se\) gives
\[
 D_e(t):=|K|-|K\cap(K+te)|=\int_{-h}^h\min\{t,L(z)\}\,dz,
 \qquad 2ht-D_e(t)=2\int_0^t(h-z_s)\,ds. \tag{1}
\]
For the quartic disk, \(2h=2\|n\|_{4/3}\), giving the claimed width exactly. Central symmetry is essential for the factor two.

**2. Uniform quartic local model.** Put \(\theta=\lambda t^3\), \(e=(\cos\theta,\sin\theta)\), and \(n=(-\sin\theta,\cos\theta)\). Write the upper boundary near \((0,1)\) as \(y(x)=(1-x^4)^{1/4}\). At \(x=tu\), uniformly on bounded \(u\)-ranges and bounded \(\lambda\)-ranges,
\[
 \langle(tu,y(tu)),n\rangle
 =1-t^4 f_\lambda(u)+O(t^6),\qquad
 f_\lambda(u)=\frac{u^4}{4}+\lambda u. \tag{2}
\]
The projected upper support is
\[
 h=1+\frac34|\lambda|^{4/3}t^4+O(t^6). \tag{3}
\]
Indeed the minimizer of \(f_\lambda\) is \(u_0=-\operatorname{sgn}(\lambda)|\lambda|^{1/3}\), where \(\min f_\lambda=-3|\lambda|^{4/3}/4\); equation (3) also follows directly from the dual-norm support function.

**3. Limit of chord endpoints.** For a chord of Euclidean length \(s=tr\), \(0<r\le1\), the two endpoints have the same projected coordinate and differ by \(tre\). Strict convexity makes its midpoint unique. If its rescaled horizontal midpoint is \(m_t\), then the endpoint abscissas divided by \(t\) are \(m_t\pm r\cos\theta/2\). The transverse-coordinate equation (2) forces their limits to have equal \(f_\lambda\)-values. For each \(r>0\) this is equivalent to
\[
 m^3+\frac{r^2}{4}m+\lambda=0, \tag{4}
\]
whose derivative in \(m\) is nonnegative and whose cubic is strictly increasing, hence there is exactly one real root. No solutions escape to infinity: the support and all these short chords lie in a fixed rescaled neighborhood of the unique upper support point; otherwise strict convexity and the quartic Taylor model contradict their common height. This localization is uniform for \(r\in[0,1]\) and \(\lambda\) in compact intervals; at \(r=0\) the two endpoints coalesce and (4) continuously chooses \(u_0\). Uniform convergence then follows by compactness and uniqueness. Consequently
\[
 t^{-4}(h-z_{tr})\longrightarrow
 \Phi_\lambda(r)=\frac34|\lambda|^{4/3}+f_\lambda(m+r/2)
\]
uniformly on \(0\le r\le1\) and on bounded \(\lambda\)-ranges. Eliminating \(\lambda\) with (4) yields
\[
 \Phi_\lambda(r)=\frac34|\lambda|^{4/3}-\frac34m^4+\frac18m^2r^2+\frac1{64}r^4. \tag{5}
\]
Because \(\Phi_\lambda(r)\) is a difference from the minimum of \(f_\lambda\), it is nonnegative. Substitute \(s=tr\) into (1), divide by \(t^5\), and integrate (5) to obtain the stated limit and its local uniformity.

**4. Monotonicity.** Reflection in the horizontal axis makes \(F\) even. For \(\lambda>0\), set \(L=\lambda^{1/3}\); the root of (4) satisfies \(-L<m<0\) when \(r>0\). Differentiating the expression \(\Phi_\lambda(r)=3\lambda^{4/3}/4+f_\lambda(m+r/2)\) along its equal-endpoint solution, using \(\partial_\lambda m=-1/(3m^2+r^2/4)\), gives
\[
 \partial_\lambda\Phi_\lambda(r)
 =m+L-\frac{mr^2}{2(3m^2+r^2/4)}>0 \qquad(r>0). \tag{6}
\]
Indeed both \(m+L\) and the second displayed contribution are positive. Integration proves strict increase of \(F\) on \([0,\infty)\) (continuity gives the endpoint).

**5. Endpoints.** At \(\lambda=0\), equation (4) has \(m=0\), so \(\Phi_0(r)=r^4/64\) and \(F(0)=1/160\). As \(\lambda\to+\infty\), write \(L=\lambda^{1/3}\) and solve (4) uniformly for \(0\le r\le1\):
\[
 m=-L+\frac{r^2}{12L}+O(L^{-5}).
\]
Substituting into (5) gives
\[
 \Phi_\lambda(r)=\frac38L^2r^2-\frac7{192}r^4+O(L^{-2}),
\]
uniformly; integration gives \(F(\lambda)=L^2/4-7/480+O(L^{-2})\).

**6. The two outer regimes.** For a translation precisely along the horizontal axis, direct slicing gives
\[
 D_{(1,0)}(t)=2\int_0^t(1-s^4/16)^{1/4}\,ds
 =2t-\frac{t^5}{160}+O(t^9).
\]
For every fixed direction \(e=(\cos\theta,\sin\theta)\) with \(0<\theta<\pi/2\), the support point with normal \((-\sin\theta,\cos\theta)\) has positive curvature \(\kappa(\theta)\). The quadratic boundary graph gives \(h-z_s=\kappa(\theta)s^2/8+o(s^2)\), hence by (1)
\[
 D_e(t)=w(\theta)t-\frac{\kappa(\theta)}{12}t^3+o(t^3).
\]
Here \(\kappa(\theta)\sim3\theta^{2/3}\) as \(\theta\downarrow0\), matching the large-parameter asymptotic \(F(\lambda)\sim\lambda^{2/3}/4\) after \(\theta=\lambda t^3\). This matching is an asymptotic comparison, not an assertion of uniform interchange of the two limits.

## Verification
A standalone numerical checker solves the exact pair of quartic endpoint equations for each short chord and integrates the exact chord deficit. It independently computes \(F\) by the real cubic root and numerical quadrature. For \(\lambda\in\{0,0.2,1,5,20\}\), the normalized overlap remainders converge to the integral values as \(t\downarrow0\). Algebraic verification of (4)--(6) and the large-\(\lambda\) expansion is independent of those finite numerical experiments. Run `python verification.py` with Python, NumPy, and SciPy.

## Relationship to prior work
Ramesh and Weiss [1, Examples 4.2 and 4.4] compute high-precision overlap areas for two planar quartic-norm balls at prescribed translations and describe deformation-related differential operators, but do not give the joint small-translation/vanishing-angle scaling profile. Haddad, Jiménez and Resende Guedes [2] analyze a smooth radial replacement of the classical covariogram and its level-set scaling limits; this is a different operation and does not yield the coefficient above. General smooth-curvature chord expansions explain the fixed nonaxial cubic term but are nonuniform as the quartic disk's curvature vanishes at its coordinate support points. The crossover is determined by the separate singular quartic rescaling carried out here.

## Limitations
Only the planar quartic disk and the stated \(\theta=\lambda t^3\) boundary layer are classified. The regime in which \(\lambda\to\infty\) simultaneously with \(t\downarrow0\) without a prescribed relation is not proved. The symbolic argument proves the continuum result; numerical tests are supporting checks, not a substitute for proof. Literature coverage cannot rule out an unindexed equivalent specialization; the historical inverse-covariogram literature was inspected primarily through accessible abstracts and previews.

## References
[1] L. Ramesh and N. Weiss, *Exact Volumes of Semi-Algebraic Convex Bodies*, arXiv:2602.04707 (first submitted 2026-02-04), especially Examples 4.2 and 4.4. https://arxiv.org/abs/2602.04707

[2] J. Haddad, C. H. Jiménez, and M. Resende Guedes, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700 (first submitted 2026-10-08). https://arxiv.org/abs/2610.11700

[3] G. Bianchi, F. Segala and A. Volčič, *The solution of the covariogram problem for plane C2+ convex bodies* (2002), cited for inverse-covariogram context, not as a theorem on quartic flat-boundary scaling.
