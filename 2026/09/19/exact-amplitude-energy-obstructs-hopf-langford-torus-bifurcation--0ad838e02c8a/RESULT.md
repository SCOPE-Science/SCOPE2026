# Exact amplitude energy obstructs the claimed Hopf–Langford torus bifurcation

## Statement

Consider the Hopf–Langford-type system studied in arXiv:2609.18010v1,
\[
\dot x=x(\mu-\alpha)-\beta y+xz,\qquad
\dot y=\beta x+y(\mu-\alpha)+yz,
\]
\[
\dot z=\mu z-\gamma(x^2+y^2+z^2).
\tag{1}
\]
Assume \(\gamma>0\) and \(\beta\ne0\). On \(r=\sqrt{x^2+y^2}>0\), set
\[
a=\alpha-\mu,
\qquad
b^2=\frac{a(\mu-\gamma a)}{\gamma},
\qquad
T=(2\gamma+1)\mu-2\gamma\alpha.
\tag{2}
\]
Whenever \(b^2>0\), system (1) has the exact periodic orbit
\[
\Gamma_*:\qquad
r(t)=b,\quad z(t)=a,\quad \theta(t)=\beta t+\theta_0,
\tag{3}
\]
of period \(2\pi/|\beta|\).

For this specific four-parameter system, the periodic orbit cannot undergo a generic Neimark–Sacker bifurcation. More precisely:

1. **If \(T\ne0\), no invariant circle of the angular Poincaré map can surround \(\Gamma_*\).** Hence there is no invariant torus of Neimark–Sacker type surrounding this periodic orbit.
2. **If \(T=0\), the amplitude dynamics is conservative near \(\Gamma_*\)** and a full one-parameter family of nearby invariant tori is present. The Poincaré fixed point is therefore a degenerate center, not a generic Neimark–Sacker point; its first radial Lyapunov coefficient vanishes.
3. The exact unit-modulus condition for the nontrivial Floquet multipliers of \(\Gamma_*\) is
\[
\boxed{(2\gamma+1)\mu-2\gamma\alpha=0.}
\tag{4}
\]
It is independent of \(\beta\).

Consequently, Theorem 2(b) of arXiv:2609.18010v1, which asserts a unique invariant torus on one side of a smooth Neimark–Sacker curve with a strictly positive first Lyapunov coefficient, is incompatible with the exact reduction of its own vector field.

## Exact reduction

Writing
\[
x=r\cos\theta,\qquad y=r\sin\theta,
\]
gives, without approximation,
\[
\boxed{
\dot r=r(\mu-\alpha+z)=r(z-a),\qquad
\dot\theta=\beta,
}
\tag{5}
\]
\[
\boxed{
\dot z=\mu z-\gamma(r^2+z^2).
}
\tag{6}
\]
Thus the angular variable is exactly decoupled and the Poincaré map on \(\theta=0\pmod{2\pi}\) is simply the time-\(2\pi/|\beta|\) map of the autonomous planar amplitude system (5)–(6).

The equilibrium \((r,z)=(b,a)\) of the amplitude system is exactly (3). Its Jacobian is
\[
J_*=
\begin{pmatrix}
0&b\\
-2\gamma b&T
\end{pmatrix},
\tag{7}
\]
so
\[
\lambda_\pm=
\frac{T\pm\sqrt{T^2-8\gamma b^2}}{2}.
\tag{8}
\]
The two nontrivial Floquet multipliers of \(\Gamma_*\) are therefore
\[
\boxed{
M_\pm=\exp\!\left(\frac{2\pi}{|\beta|}\lambda_\pm\right).
}
\tag{9}
\]
Near a complex-pair crossing, \(|M_\pm|=1\) holds if and only if \(T=0\), proving (4).

## A strict Lyapunov law for the amplitude dynamics

Let
\[
u=\log r,
\qquad y_1=\dot u=z-a.
\]
Using (2), the exact amplitude equations yield
\[
\dot y_1=-\gamma y_1^2+Ty_1+\gamma(b^2-r^2).
\tag{10}
\]
Now define
\[
w=r^\gamma>0.
\]
A direct calculation cancels the quadratic \(y_1\)-term and gives the scalar equation
\[
\boxed{
\ddot w-T\dot w
=\gamma^2b^2w-\gamma^2w^{1+2/\gamma}.
}
\tag{11}
\]
Set
\[
V(w)=-\frac{\gamma^2b^2}{2}w^2
+\frac{\gamma^3}{2(\gamma+1)}w^{2+2/\gamma}
\tag{12}
\]
and
\[
E(w,\dot w)=\frac12\dot w^2+V(w).
\tag{13}
\]
Then (11) gives the exact identity
\[
\boxed{
\frac{dE}{dt}=T\dot w^2.
}
\tag{14}
\]
This identity is the obstruction to a generic torus bifurcation.

### Case \(T\ne0\)

Let \(P\) be the time-\(2\pi/|\beta|\) amplitude map. If \(q\) is not the equilibrium, then
\[
E(Pq)-E(q)
=T\int_0^{2\pi/|\beta|}\dot w(t)^2\,dt,
\tag{15}
\]
which has the strict sign of \(T\). If a compact invariant circle \(C\) surrounded the fixed point, then for \(T>0\) a point where \(E\) attains its maximum on \(C\) would be mapped to a point of strictly larger \(E\) still lying on \(C\), a contradiction. For \(T<0\), use the minimum instead. Thus no such invariant circle exists.

Because \(\dot\theta=\beta\ne0\), an invariant torus surrounding \(\Gamma_*\) would intersect an angular section in exactly such an invariant circle. Hence it is excluded whenever \(T\ne0\).

### Case \(T=0\)

Equation (11) becomes conservative. The equilibrium in the \(w\)-coordinate is \(w_*=b^\gamma\), and
\[
V''(w_*)=2\gamma b^2>0.
\tag{16}
\]
Therefore \(w_*\) is a nonlinear center: every sufficiently small regular energy level of (13) is a closed amplitude orbit. Suspending these closed curves by the independent angular rotation \(\dot\theta=\beta\) yields a continuum of smooth invariant two-tori near \(\Gamma_*\). Depending on the frequency ratio, trajectories on an individual torus are periodic or quasiperiodic, but the invariant surface exists in either case.

This is a center foliation on the single surface \(T=0\), rather than the birth of a unique invariant circle on one side of a generic Neimark–Sacker crossing. In particular, a nonzero first Neimark–Sacker Lyapunov coefficient is impossible at this exact conservative crossing.

## Explicit contradiction with the claimed bifurcation curve

The mismatch is already visible in a particularly simple parameter family satisfying the hypotheses of the source theorem. Take
\[
\boxed{
\alpha=\varepsilon,\qquad
\beta=1,\qquad
\gamma=1,\qquad
\mu=\nu\varepsilon.
}
\tag{17}
\]
For \(\nu\) near \(2/3\), the source conditions (4) hold. At \(\nu=2/3\), their two nontrivial inequalities evaluate to
\[
(\nu-1)(1-2\nu)=\frac19>0,
\tag{18}
\]
\[
12-36\nu+25\nu^2=-\frac89<0.
\tag{19}
\]
The exact off-axis periodic orbit has
\[
b^2=(1-\nu)(2\nu-1)\varepsilon^2>0
\quad\text{for}\quad \frac12<\nu<1,
\tag{20}
\]
and the exact transverse trace is
\[
T=(3\nu-2)\varepsilon.
\tag{21}
\]
Hence the exact unit-modulus surface is
\[
\boxed{\nu_{\rm crit}(\varepsilon)=\frac23}
\tag{22}
\]
for every \(\varepsilon\ne0\).

By contrast, substituting the same coefficients
\[
\alpha_1=1,\ \alpha_2=0,\ \omega=1,\ \beta_1=0,
\ \gamma_0=1,\ \gamma_1=0,\ \mu_2=0
\]
into equation (7) of arXiv:2609.18010v1 gives
\[
\widehat\mu_0=\frac23,
\qquad
\boxed{
\widehat\mu_1=\frac{8\pi^2-2}{27}\approx2.85025315587833.
}
\tag{23}
\]
Thus the curve asserted in Theorem 2(b) has
\[
\nu_{\rm source}(\varepsilon)
=\frac23+\frac{8\pi^2-2}{27}\varepsilon+O(\varepsilon^2),
\tag{24}
\]
whereas the exact Floquet crossing has no \(O(\varepsilon)\) correction at all. On the asserted curve,
\[
T=\frac{8\pi^2-2}{9}\varepsilon^2+O(\varepsilon^3)\ne0
\tag{25}
\]
for sufficiently small nonzero \(\varepsilon\), so the strict Lyapunov law (14) rules out the claimed surrounding invariant circle there.

More generally, if the source perturbation is written as
\[
\alpha=\alpha_1\varepsilon+\alpha_2\varepsilon^2+O(\varepsilon^3),
\qquad
\gamma=\gamma_0+\gamma_1\varepsilon+O(\varepsilon^2),
\]
\[
\mu=\nu(\varepsilon)\varepsilon+\mu_2\varepsilon^2+O(\varepsilon^3),
\qquad
\nu(\varepsilon)=\nu_0+\nu_1\varepsilon+O(\varepsilon^2),
\]
then the exact surface \(T=0\) forces
\[
\boxed{
\nu_0=\frac{2\gamma_0\alpha_1}{2\gamma_0+1},
}
\tag{26}
\]
\[
\boxed{
\nu_1=
\frac{2\gamma_0\alpha_2}{2\gamma_0+1}
+\frac{2\gamma_1\alpha_1}{(2\gamma_0+1)^2}
-\mu_2.
}
\tag{27}
\]
Unlike the coefficient stated in the source, (27) contains neither \(beta\), \(omega\), nor \(pi\), because the angular speed does not affect the modulus crossing of the exact amplitude flow.

## Relation to prior work

The dimensional reduction itself is not new. Vassilev and Nikolov (2025) explicitly reduce a seven-parameter Hopf–Langford-type family to an autonomous two-dimensional amplitude system plus \(\dot\theta=\beta\). Under the parameter identification
\[
\alpha_{\rm VN}=\mu-\alpha,\qquad
\eta_{\rm VN}=1,\quad
\mu_{\rm VN}=\mu,\quad
\delta_{\rm VN}=\gamma,
\]
their integrability condition
\[
2\alpha_{\rm VN}\delta_{\rm VN}+\mu_{\rm VN}\eta_{\rm VN}=0
\]
is precisely \(T=0\). Earlier Hopf–Langford literature also recognizes exact periodic solutions and center/annulus mechanisms in related generalized systems. These facts are therefore not claimed as new.

The source-specific contribution here is the exact obstruction (14) applied to arXiv:2609.18010v1, the resulting proof that its stated generic Neimark–Sacker conclusion cannot hold for system (1), the exact Floquet surface (4), and the explicit admissible family (17)–(25) showing that the paper's displayed bifurcation curve disagrees with the exact dynamics already at its first correction.

## Verification

`artifacts/verify_exact_reduction.py` symbolically checks the polar reduction, the periodic-orbit equilibrium condition, the amplitude Jacobian, the energy identity, the positive curvature at the center, the exact perturbative crossing coefficients, and the concrete discrepancy (23). The accompanying text file records the output. The computation is an algebraic reproducibility check, not independent validation.

## Limitations

The obstruction is stated for \(\gamma>0\), \(\beta\ne0\), \(b^2>0\), which is the regime relevant to the source theorem near its claimed torus bifurcation. It does not classify all invariant sets of (1) when \(r=0\), \(\gamma\le0\), or \(\beta=0\). It also does not assess torus bifurcations of more general Hopf–Langford systems containing additional terms that destroy the constant-damping scalar reduction (11).

The 2018 Yang–Yang paper and the 2021 Nikolov–Vassilev integrability paper are highly relevant prior literature; only the accessible statements and later descriptions were inspected here, while the 2025 Vassilev–Nikolov article was inspected in full. Those older papers may contain equivalent amplitude-center observations in broader notation. The originality claim is therefore deliberately limited to the explicit correction and exact contradiction for arXiv:2609.18010v1, not to the general polar reduction or existence of integrable Hopf–Langford parameter surfaces.

## References

1. G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (2026). https://arxiv.org/abs/2609.18010
2. V. M. Vassilev, S. G. Nikolov, *First and Second Integrals of Hopf–Langford-Type Systems*, Axioms 14 (2025), 8. https://doi.org/10.3390/axioms14010008
3. S. G. Nikolov, V. M. Vassilev, *Completely integrable dynamical systems of Hopf–Langford type*, Communications in Nonlinear Science and Numerical Simulation 92 (2021), 105464. https://doi.org/10.1016/j.cnsns.2020.105464
4. Q. Yang, T. Yang, *Complex dynamics in a generalized Langford system*, Nonlinear Dynamics 91 (2018), 2241–2270. https://doi.org/10.1007/s11071-017-4012-1
5. W. F. Langford, *Periodic and steady-state mode interactions lead to tori*, SIAM Journal on Applied Mathematics 37 (1979), 22–48. https://doi.org/10.1137/0137003
