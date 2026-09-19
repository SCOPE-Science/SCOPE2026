# Exact amplitude energy obstructs the claimed Hopf–Langford torus bifurcation

## Statement

Consider the system studied in arXiv:2609.18010v1,
\[
\dot x=x(\mu-\alpha)-\beta y+xz,\qquad
\dot y=\beta x+y(\mu-\alpha)+yz,
\]
\[
\dot z=\mu z-\gamma(x^2+y^2+z^2),
\tag{1}
\]
with \(\gamma>0\) and \(\beta\ne0\). Put \(r=(x^2+y^2)^{1/2}\), \(a=\alpha-\mu\), and
\[
b^2=\frac{a(\mu-\gamma a)}{\gamma},\qquad
T=(2\gamma+1)\mu-2\gamma\alpha.
\tag{2}
\]
Whenever \(b^2>0\), (1) has the exact periodic orbit
\[
r=b,\qquad z=a,\qquad \theta=\beta t+\theta_0.
\tag{3}
\]
For this four-parameter vector field the orbit cannot undergo a generic Neimark–Sacker bifurcation. If \(T\ne0\), no invariant circle of the angular return map can surround (3). If \(T=0\), the reduced amplitude dynamics is conservative and (3) belongs to a continuum of nearby invariant two-tori. Thus the exact unit-modulus surface is
\[
\boxed{(2\gamma+1)\mu-2\gamma\alpha=0,}
\tag{4}
\]
and the crossing is a center degeneracy rather than a generic Neimark–Sacker point.

This contradicts Theorem 2(b) of arXiv:2609.18010v1, which states a unique invariant torus on one side of a computed Neimark–Sacker curve with a strictly positive first Lyapunov coefficient.

## Exact reduction and Floquet multipliers

Writing \(x=r\cos\theta\), \(y=r\sin\theta\) gives exactly
\[
\dot r=r(z-a),\qquad \dot\theta=\beta,
\qquad \dot z=\mu z-\gamma(r^2+z^2).
\tag{5}
\]
Hence the angular Poincaré map is the time-\(2\pi/|\beta|\) map of the autonomous planar \((r,z)\) system. The equilibrium \((b,a)\) corresponds to (3), and its Jacobian is
\[
J_*=
\begin{pmatrix}0&b\\-2\gamma b&T\end{pmatrix}.
\tag{6}
\]
Therefore
\[
\lambda_\pm=\frac{T\pm\sqrt{T^2-8\gamma b^2}}2,
\qquad
M_\pm=\exp\!\left(\frac{2\pi}{|\beta|}\lambda_\pm\right).
\tag{7}
\]
For a complex pair, \(|M_\pm|=1\) if and only if \(T=0\), proving (4).

## Exact energy obstruction

Let \(u=\log r\), so \(\dot u=z-a\), and set \(w=r^\gamma>0\). Direct substitution in (5) gives
\[
\boxed{\ddot w-T\dot w=\gamma^2b^2w-\gamma^2w^{1+2/\gamma}.}
\tag{8}
\]
Define
\[
V(w)=-\frac{\gamma^2b^2}{2}w^2+
\frac{\gamma^3}{2(\gamma+1)}w^{2+2/\gamma},
\qquad
E=\frac12\dot w^2+V(w).
\tag{9}
\]
Then
\[
\boxed{\dot E=T\dot w^2.}
\tag{10}
\]
Let \(P\) denote the time-\(2\pi/|\beta|\) amplitude map. For every non-equilibrium point \(q\),
\[
E(Pq)-E(q)=T\int_0^{2\pi/|\beta|}\dot w(t)^2\,dt.
\tag{11}
\]
If \(T>0\), an invariant circle surrounding the fixed point would contain a maximum of \(E\), but (11) maps that maximum to a point on the same circle with strictly larger energy. For \(T<0\), use a minimum. Hence no surrounding invariant circle exists when \(T\ne0\).

At \(T=0\), (8) is conservative. Its positive equilibrium is \(w_*=b^\gamma\), and
\[
V''(w_*)=2\gamma b^2>0.
\tag{12}
\]
Thus \(w_*\) is a nonlinear center surrounded by closed amplitude levels. Suspending these closed curves by \(\dot\theta=\beta\) yields a continuum of nearby invariant two-tori. Consequently the first radial Neimark–Sacker Lyapunov coefficient at this crossing must vanish.

## Explicit conflict with the displayed source curve

Take the source-admissible family
\[
\alpha=\varepsilon,\qquad \beta=1,\qquad
\gamma=1,\qquad \mu=\nu\varepsilon.
\tag{13}
\]
At \(\nu=2/3\), the two nontrivial source inequalities become
\[
(\nu-1)(1-2\nu)=\frac19>0,
\qquad
12-36\nu+25\nu^2=-\frac89<0.
\tag{14}
\]
Moreover
\[
b^2=(1-\nu)(2\nu-1)\varepsilon^2>0
\quad (1/2<\nu<1),
\tag{15}
\]
and
\[
T=(3\nu-2)\varepsilon.
\tag{16}
\]
Therefore the exact Floquet crossing is
\[
\boxed{\nu_{\rm crit}(\varepsilon)=2/3}
\tag{17}
\]
for every nonzero \(\varepsilon\).

For the same coefficients, equation (7) of arXiv:2609.18010v1 gives
\[
\widehat\mu_0=\frac23,
\qquad
\widehat\mu_1=\frac{8\pi^2-2}{27}\approx2.85025315587833.
\tag{18}
\]
Hence its asserted curve is
\[
\nu_{\rm source}(\varepsilon)=\frac23+
\frac{8\pi^2-2}{27}\varepsilon+O(\varepsilon^2),
\tag{19}
\]
whereas the exact crossing has no \(O(\varepsilon)\) correction. On the asserted curve,
\[
T=\frac{8\pi^2-2}{9}\varepsilon^2+O(\varepsilon^3)\ne0,
\tag{20}
\]
so (11) rules out the claimed surrounding invariant circle there.

More generally, for
\[
\alpha=\alpha_1\varepsilon+\alpha_2\varepsilon^2+O(\varepsilon^3),\quad
\gamma=\gamma_0+\gamma_1\varepsilon+O(\varepsilon^2),
\]
\[
\mu=(\nu_0+\nu_1\varepsilon+O(\varepsilon^2))\varepsilon
+\mu_2\varepsilon^2+O(\varepsilon^3),
\]
the exact condition \(T=0\) forces
\[
\nu_0=\frac{2\gamma_0\alpha_1}{2\gamma_0+1},
\qquad
\nu_1=\frac{2\gamma_0\alpha_2}{2\gamma_0+1}
+\frac{2\gamma_1\alpha_1}{(2\gamma_0+1)^2}-\mu_2.
\tag{21}
\]
In particular, the exact modulus-crossing coefficient contains no angular-frequency dependence.

## Prior work and originality scope

The polar/amplitude reduction is prior. Vassilev and Nikolov (2025) reduce a more general Hopf–Langford family to a planar amplitude system plus \(\dot\theta=\beta\); under the present parameter identification, one of their integrability conditions is exactly \(T=0\). Earlier Hopf–Langford literature also contains exact periodic solutions and center/annulus or integrable cases. None of those general facts is claimed as new.

The source-specific contribution is the exact obstruction (10)–(11) applied to arXiv:2609.18010v1, the resulting contradiction with its generic Neimark–Sacker conclusion, the exact Floquet surface (4), and the admissible family (13)–(20) showing that the displayed source curve already disagrees with the exact dynamics at its first correction. Searches found no public correction of this theorem or overlapping SCOPE record.

## Verification and limitations

`artifacts/verify_exact_reduction.py` checks the reduction, periodic-orbit condition, Jacobian, energy identity, center curvature, perturbative crossing coefficients, and the concrete discrepancy (18). The computation is an algebraic reproducibility check, not independent validation.

The result concerns \(\gamma>0\), \(\beta\ne0\), and \(b^2>0\). It does not classify the symmetry axis, \(\gamma\le0\), \(\beta=0\), or generalized Hopf–Langford systems with additional terms. The full texts of Yang–Yang (2018) and Nikolov–Vassilev (2021) were not inspected; they remain residual originality risks for equivalent broader no-cycle or center statements. The originality claim is therefore limited to the explicit source-specific correction above.

## References

1. G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (2026). https://arxiv.org/abs/2609.18010
2. V. M. Vassilev, S. G. Nikolov, *First and Second Integrals of Hopf–Langford-Type Systems*, Axioms 14 (2025), 8. https://doi.org/10.3390/axioms14010008
3. S. G. Nikolov, V. M. Vassilev, *Completely integrable dynamical systems of Hopf–Langford type*, Commun. Nonlinear Sci. Numer. Simul. 92 (2021), 105464. https://doi.org/10.1016/j.cnsns.2020.105464
4. Q. Yang, T. Yang, *Complex dynamics in a generalized Langford system*, Nonlinear Dynamics 91 (2018), 2241–2270. https://doi.org/10.1007/s11071-017-4012-1
5. W. F. Langford, *Periodic and steady-state mode interactions lead to tori*, SIAM J. Appl. Math. 37 (1979), 22–48. https://doi.org/10.1137/0137003
