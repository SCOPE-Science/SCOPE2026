# Exact energy obstruction to the claimed Hopf–Langford torus bifurcation

## Statement

Consider the Hopf–Langford-type system studied in arXiv:2609.18010v1,
\[
\dot x=x(\mu-\alpha)-\beta y+xz,\qquad
\dot y=\beta x+y(\mu-\alpha)+yz,\qquad
\dot z=\mu z-\gamma(x^2+y^2+z^2),
\]
with \(\beta\ne0\) and \(\gamma\ne0\).  In cylindrical coordinates
\(x=r\cos\theta\), \(y=r\sin\theta\), the system reduces exactly to
\[
\dot r=r(\mu-\alpha+z),\qquad \dot\theta=\beta,\qquad
\dot z=\mu z-\gamma(r^2+z^2).
\]
Set
\[
s=\alpha-\mu,\qquad
T=(1+2\gamma)\mu-2\gamma\alpha=\mu-2\gamma s,
\qquad
R^2=s\left(\frac{\mu}{\gamma}-s\right).
\]
Whenever \(R^2>0\), there is an exact periodic circle
\[
(r,z)=(R,s),\qquad \theta(t)=\beta t+\theta_0.
\]

On the region \(r>0\), define \(w=r^\gamma\).  Then the complete transverse-amplitude dynamics satisfies the scalar equation
\[
\boxed{
 w''-T w'=\gamma^2R^2w-\gamma^2w^{1+2/\gamma}.
}
\]
For \(\gamma\ne-1\), let
\[
V(w)=-\frac{\gamma^2R^2}{2}w^2
+\frac{\gamma^3}{2(\gamma+1)}w^{2+2/\gamma},
\qquad
E=\frac12(w')^2+V(w).
\]
For \(\gamma=-1\), use instead
\[
V(w)=-\frac{R^2}{2}w^2+\log w.
\]
In both cases one has the exact identity
\[
\boxed{\dot E=T(w')^2.}
\]

Consequently:

1. **No Neimark–Sacker torus exists off \(T=0\).**  If \(T\ne0\), the amplitude energy is strictly monotone along every nonstationary recurrent amplitude trajectory.  Hence the time-\(2\pi/|\beta|\) return map on a \(\theta\)-section cannot possess an invariant Jordan curve surrounding the fixed point corresponding to the periodic circle.  In particular, no smooth invariant torus of the type asserted in Theorem 2 of arXiv:2609.18010v1 can bifurcate on either side of the critical surface.

2. **The exact unit-modulus surface is**
\[
\boxed{T=0\iff (1+2\gamma)\mu-2\gamma\alpha=0.}
\]
Indeed, in first-order variables \((w,v=w')\) the planar divergence is the constant \(T\). Therefore the determinant of its time-\(P\) map is exactly \(e^{TP}\), with \(P=2\pi/|\beta|\). A Neimark–Sacker crossing of the periodic circle would require determinant one and hence necessarily \(T=0\).

3. **At \(T=0\), the bifurcation is a center degeneracy, not a generic Neimark–Sacker bifurcation.**  If \(\gamma>0\) and \(R^2>0\), then the critical amplitude equilibrium is a nonlinear center.  In the \(w\)-equation,
\[
V''(R^\gamma)=2\gamma R^2>0,
\]
so sufficiently small noncritical energy levels are closed amplitude curves.  Their products with the uniformly rotating \(\theta\)-circle form a one-parameter family of invariant tori *on the critical surface itself*.  Thus there is no unique torus born on one side; instead there is a center foliation at the critical parameter value.

The reduced Jacobian at the periodic circle is
\[
J_\perp=
\begin{pmatrix}
0&R\\
-2\gamma R&T
\end{pmatrix},
\qquad
\operatorname{tr}J_\perp=T,
\qquad
\det J_\perp=2\gamma R^2.
\]
For \(\gamma>0\), the circle changes from attracting to repelling as \(T\) crosses zero, but the strict energy identity rules out a surrounding amplitude limit cycle on either side.

## Relation to the averaging curve

The source paper's leading critical coefficient
\[
\widehat\mu_0=\frac{2\alpha_1\gamma_0}{2\gamma_0+1}
\]
is precisely the leading expansion of the exact surface
\[
\mu=\frac{2\gamma\alpha}{1+2\gamma}.
\]
If
\[
\alpha=\alpha_1\varepsilon+\alpha_2\varepsilon^2+O(\varepsilon^3),\quad
\gamma=\gamma_0+\gamma_1\varepsilon+O(\varepsilon^2),\quad
\mu=\mu_1\varepsilon+\mu_2\varepsilon^2+O(\varepsilon^3),
\]
then the exact critical curve for the bifurcation parameter \(\mu_1\) begins
\[
\boxed{
\mu_{1,c}(\varepsilon)
=\frac{2\alpha_1\gamma_0}{1+2\gamma_0}
+\left[
\frac{2\alpha_2\gamma_0}{1+2\gamma_0}
+\frac{2\alpha_1\gamma_1}{(1+2\gamma_0)^2}
-\mu_2
\right]\varepsilon
+O(\varepsilon^2).
}
\]
The exact critical surface is independent of \(\beta\).  More importantly, its critical dynamics has a first integral and a center, so a nonzero radial first Lyapunov coefficient for a generic Neimark–Sacker branch is incompatible with the exact flow.

## Connection with known integrability

The cylindrical reduction itself is prior art.  In particular, Vassilev and Nikolov (Axioms 2025, Proposition 2) study the larger seven-parameter Hopf–Langford family
\[
\dot x_1=\alpha_Ax_1-\beta x_2+\eta x_1x_3+\epsilon x_1x_3^2,
\qquad
\dot x_3=\mu x_3-\gamma_A(x_1^2+x_2^2)-\delta x_3^2,
\]
and give a first integral when
\[
2\alpha_A\delta+\mu\eta=0
\]
(with the stated generic side conditions).  For the present source system,
\[
\alpha_A=\mu-\alpha,\qquad \eta=1,\qquad \delta=\gamma,
\]
so their integrability condition becomes exactly
\[
2\gamma(\mu-\alpha)+\mu=T=0.
\]
Thus the critical first-integrable surface is already implicit in the prior Hopf–Langford literature.  The new point here is the source-specific contradiction with the 2026 Neimark–Sacker claim and the simple off-critical monotone-energy identity that excludes the asserted one-sided torus branch.

## Numerical Example 2 in arXiv:2609.18010v1

The paper's Example 2 uses
\[
\gamma=-1-\varepsilon+\frac1{25}\varepsilon^2,
\]
so \(\gamma_0=-1\).  This violates the theorem's standing hypothesis \(\gamma_0>0\).  At the displayed value \(\varepsilon=10^{-3}\), the printed parameters give
\[
\alpha=0.00100001,\quad
\beta=0.10443004,\quad
\gamma=-1.00099996,\quad
\mu=0.00399321,
\]
with
\[
R^2\approx2.9812898735\times10^{-6},\qquad
T\approx-1.9991761605\times10^{-3},
\]
and
\[
2\gamma R^2\approx-5.9685420883\times10^{-6}<0.
\]
Hence the corresponding periodic circle is a transverse saddle, not an elliptic/focus-type orbit capable of a Neimark–Sacker crossing.  The exact energy obstruction also rules out a surrounding invariant torus because \(T\ne0\).

There is a second internal inconsistency in the same example.  Substitution of its leading values \(\gamma_0=-1\), \(\omega=0.1\) into the paper's displayed Eq. (9) gives
\[
\ell_{1,2}=\frac{25}{4}(1-7\pi^2)\approx-425.54519255,
\]
whereas Example 2 prints
\[
\ell_{1,2}=\frac{49\pi^2-11}{144}\approx3.28201816>0.
\]
The finite trajectory and Poincaré plots in that example therefore cannot establish the claimed invariant torus for the printed exact system.

## Verification

`artifacts/verify_energy_obstruction.py` symbolically checks the energy identity, constant reduced divergence, exact Jacobian trace/determinant, mapping to the previously published first-integral condition, the leading exact critical expansion, and the arithmetic of Example 2.  Its recorded output is in `artifacts/verification.txt`.

## Limitations

This correction applies to the rotationally symmetric four-parameter system written in arXiv:2609.18010v1.  It does not rule out genuine invariant-torus bifurcations in more general Hopf–Langford systems after symmetry-breaking or additional nonlinear terms.  The transformation \(w=r^\gamma\) is used on \(r>0\), which is the neighborhood relevant to the nonzero periodic circle.  This record identifies an exact structural obstruction but does not locate the specific algebraic step in the source paper's averaging calculation where the nonzero Neimark–Sacker coefficient is introduced.

## References

1. G. Domingues, *Torus Bifurcation in the Hopf-Langford type system through Averaging Theory*, arXiv:2609.18010v1 (2026). https://arxiv.org/abs/2609.18010v1
2. V. M. Vassilev and S. G. Nikolov, *First and Second Integrals of Hopf–Langford-Type Systems*, Axioms 14(1), 8 (2025). https://doi.org/10.3390/axioms14010008
3. S. G. Nikolov and V. M. Vassilev, *Completely integrable dynamical systems of Hopf–Langford type*, Communications in Nonlinear Science and Numerical Simulation 92, 105464 (2021). https://doi.org/10.1016/j.cnsns.2020.105464
4. S. G. Nikolov and V. M. Vassilev, *Assessing the Non-Linear Dynamics of a Hopf–Langford Type System*, Mathematics 9(18), 2340 (2021). https://doi.org/10.3390/math9182340
