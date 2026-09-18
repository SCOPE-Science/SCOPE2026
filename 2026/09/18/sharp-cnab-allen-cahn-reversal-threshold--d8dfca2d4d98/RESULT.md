# Sharp pointwise-reversal threshold for stabilized CN/AB Allen–Cahn stepping

## Statement

Consider the Allen–Cahn equation
\[
u_t=\Delta u-\varepsilon^{-2}f(u),\qquad f(u)=u^3-u,
\]
with periodic or homogeneous Neumann boundary conditions, and the stabilized Crank–Nicolson/Adams–Bashforth time discretization
\[
\frac{u^{n+1}-u^n}{\tau}
=\Delta\frac{u^{n+1}+u^n}{2}
-\frac{S\tau}{\varepsilon^2}(u^{n+1}-u^n)
-\frac1{\varepsilon^2}\left(\frac32f(u^n)-\frac12f(u^{n-1})\right),
\qquad S\ge0.
\]
For a spatially homogeneous initial value \(u^0\equiv a\in(0,1)\), initialize with the exact increasing Allen–Cahn value
\[
u^1=b(h):=\frac1{\sqrt{1+(a^{-2}-1)e^{-2h}}},\qquad h:=\frac{\tau}{\varepsilon^2}.
\]
Let \(g(x)=x(1-x^2)=-f(x)\) on \((0,1)\). There is a unique
\[
b_*(a)\in(1/\sqrt3,1)
\]
satisfying
\[
\boxed{\;3b_*(1-b_*^2)=a(1-a^2).\;}
\]
Define
\[
\boxed{
h_*(a)
=\log\frac{b_*\sqrt{1-a^2}}{a\sqrt{1-b_*^2}}
=\frac12\log\frac{3b_*^3}{a^3}.}
\]
Then, for every \(S\ge0\),
\[
\boxed{
\begin{aligned}
u^2-u^1&>0 &&(0<h<h_*),\\
u^2-u^1&=0 &&(h=h_*),\\
u^2-u^1&<0 &&(h>h_*).
\end{aligned}}
\]
Thus the first wrong-signed increment after an exact increasing start has an exact, sharp threshold
\[
\boxed{\tau_*^{\rm sharp}(a,\varepsilon)=\varepsilon^2h_*(a),}
\]
and the threshold is independent of the stabilization strength \(S\). Stabilization changes the size of the increment but cannot change its sign in this homogeneous test.

The threshold state also has the closed form
\[
\boxed{
b_*(a)=\frac{2}{\sqrt3}
\cos\!\left[\frac13\arccos\!\left(-\frac{\sqrt3}{2}a(1-a^2)\right)\right].}
\]

## Relation to the existing large-step certificate

Li and Wang, Theorem 4.11 of arXiv:2609.19023, derive the homogeneous recurrence
\[
u^{n+1}-u^n
=-\frac{\tau}{\varepsilon^2+S\tau^2}
\left(\frac32f(u^n)-\frac12f(u^{n-1})\right)
\]
and prove the sufficient large-step condition
\[
\tau>\tau_{*,\mathrm{stab}}^{\rm src}
:=\frac{\varepsilon^2}{2}\log\frac{3}{a^3}
\]
for \(u^2<u^1\). Their proof uses an upper bound on the exact ratio \((-f(u^1))/(-f(u^0))\), so this published condition is sufficient rather than an if-and-only-if onset.

The exact threshold above is strictly smaller:
\[
\frac{\tau_{*,\mathrm{stab}}^{\rm src}-\tau_*^{\rm sharp}}{\varepsilon^2}
=-\frac32\log b_*(a)>0.
\]
The gap is largest at \(a=1/\sqrt3\), because \(a(1-a^2)\) is maximal there and the relevant root \(b_*\) lies on the strictly decreasing branch of \(g\). Numerically,
\[
b_*(1/\sqrt3)=0.9283289357843458\ldots,
\]
so
\[
\max_{0<a<1}\frac{\tau_{*,\mathrm{stab}}^{\rm src}-\tau_*^{\rm sharp}}{\varepsilon^2}
=0.111553728505040\ldots.
\]
For example, at \(a=1/2\),
\[
h_*=1.480820616722060\ldots,
\qquad
h_{\rm src}=1.589026915173973\ldots.
\]

## Proof of the sharp threshold

For homogeneous states the Laplacian vanishes, and at the first CN/AB update
\[
u^2-u^1
=-\frac{\tau}{\varepsilon^2+S\tau^2}
\left(\frac32f(b)-\frac12f(a)\right).
\]
The scalar prefactor is positive for every finite \(\tau>0\) and \(S\ge0\). Since \(f=-g\) on \((0,1)\),
\[
\frac32f(b)-\frac12f(a)
=\frac12\bigl(g(a)-3g(b)\bigr).
\]
Hence
\[
u^2-u^1<0\quad\Longleftrightarrow\quad 3g(b)<g(a).
\]

The exact starter \(b(h)\) is strictly increasing from \(a\) to \(1\). The function \(g(x)=x(1-x^2)\) is strictly increasing on \((0,1/\sqrt3)\), strictly decreasing on \((1/\sqrt3,1)\), and tends to zero as \(x\uparrow1\). If \(a\ge1/\sqrt3\), the trajectory begins on the decreasing branch and crosses the level \(g(a)/3\) once. If \(a<1/\sqrt3\), it first rises to the maximum of \(g\), remaining strictly above \(g(a)/3\), and then crosses that level once on the decreasing branch. Thus the unique crossing state is \(b_*>1/\sqrt3\) with \(3g(b_*)=g(a)\).

Solving the exact-flow relation for \(h\) gives
\[
e^{-2h}=\frac{a^2(1-b^2)}{b^2(1-a^2)},
\]
whence
\[
h=\log\frac{b\sqrt{1-a^2}}{a\sqrt{1-b^2}}.
\]
At the threshold, \(1-b_*^2=a(1-a^2)/(3b_*)\), giving
\[
h_*=\frac12\log\frac{3b_*^3}{a^3}.
\]
The cubic \(b_*^3-b_*+a(1-a^2)/3=0\) gives the displayed trigonometric formula for the root in \((1/\sqrt3,1)\).

The crossing is transverse. If
\[
E(h):=\frac32f(b(h))-\frac12f(a)=\frac12\bigl(g(a)-3g(b(h))\bigr),
\]
then \(b'(h)=g(b(h))\) and
\[
E'(h_*)
=\frac{g(a)}2\bigl(3b_*^2-1\bigr)>0.
\]
Thus the sign reversal is not a tangential or multiple-root artifact.

## Over-extrapolation mechanism

The same calculation identifies the mechanism independently of the AB2 coefficients. Suppose a homogeneous two-step nonlinear forcing uses
\[
\alpha f(u^1)+(1-\alpha)f(u^0),\qquad \alpha>1,
\]
multiplied in the update by any positive scalar factor. Put
\[
q:=\frac{\alpha-1}{\alpha}\in(0,1).
\]
With the same exact increasing starter \(b(h)\), the update reverses sign exactly when
\[
g(b)<qg(a).
\]
There is a unique threshold state \(b_q\in(1/\sqrt3,1)\) satisfying
\[
\boxed{b_q(1-b_q^2)=q\,a(1-a^2),}
\]
and the sharp dimensionless threshold is
\[
\boxed{
h_q(a)=\frac12\log\frac{b_q^3}{q a^3}.}
\]
Equivalently,
\[
b_q=\frac{2}{\sqrt3}\cos\!\left[
\frac13\arccos\!\left(-\frac{3\sqrt3}{2}q a(1-a^2)\right)
\right].
\]
The argument of \(\arccos\) lies strictly inside \([-1,1]\), since \(a(1-a^2)\le2/(3\sqrt3)\) and \(q<1\).

Two limiting laws make the extrapolation penalty explicit:
\[
\boxed{\lim_{a\uparrow1}h_q(a)=\frac12\log\frac1q
=\frac12\log\frac{\alpha}{\alpha-1},}
\]
and
\[
h_q(a)=-\frac32\log a-\frac12\log q+o(1)
\qquad(a\downarrow0).
\]
For AB2, \(\alpha=3/2\) and \(q=1/3\), so the near-equilibrium reversal threshold tends to
\[
\frac12\log3=0.5493061443340548\ldots.
\]
This shows that the finite reversal threshold is intrinsic to the over-extrapolated nonlinear forcing: multiplying it by a positive stabilizing/resolvent factor can damp the increment but cannot alter the sign threshold.

## Persistence with active diffusion

Li and Wang's Proposition 5.2 proves persistence of the stabilized-CN/AB sign reversal under sufficiently small smooth admissible nonhomogeneous perturbations by continuous dependence of the exact PDE starter and the elliptic CN/AB update. The proof only requires that the reference homogeneous increment be strict. Therefore the same argument applies for every fixed finite
\[
\tau>\tau_*^{\rm sharp}(a,\varepsilon),
\]
not merely for the larger sufficient threshold used in their statement. For such a step, there are arbitrarily small admissible perturbations with nonzero Laplacian for which the exact Allen–Cahn trajectory remains pointwise nondecreasing while the numerical second increment is strictly negative everywhere.

The same continuity argument is two-sided away from the crossing: for any fixed finite \(\tau<\tau_*^{\rm sharp}\), sufficiently small admissible perturbations preserve the positive sign of this particular second numerical increment. This does not assert a global monotonicity theorem for all later steps or for arbitrary nonhomogeneous data; it identifies the sharp homogeneous bifurcation around which the local PDE perturbation picture is organized.

## Reproducibility

`artifacts/verify_threshold.py` uses only the Python standard library. It evaluates the closed-form threshold state, checks the cubic/level equation and exact-starter identity, verifies opposite signs on the two sides of the crossing, compares the published sufficient threshold with the sharp one, and checks several general extrapolation coefficients. `artifacts/verification_output.txt` records the deterministic output.

## Originality boundary

The source paper arXiv:2609.19023 introduces the PDE pointwise-monotonicity framework, derives the stabilized CN/AB homogeneous recurrence and exact starter, proves large-step reversal, provides the sufficient threshold \(\frac{\varepsilon^2}{2}\log(3/a^3)\), and proves persistence under small nonhomogeneous perturbations. Those results are prior work. Feng, Tang and Yang (2013) introduced/analyzed the stabilized CN/AB phase-field scheme from the energy-stability and error-estimate viewpoint. Li and Wang's earlier asymptotic-stability work studies critical step sizes for several other Allen–Cahn ODE discretizations.

The contribution here is restricted to the exact if-and-only-if first-reversal threshold for the stabilized CN/AB counterexample, its closed form and transversality, the exact improvement over the published sufficient certificate, the corresponding strengthening of the perturbative active-diffusion regime, and the general over-extrapolation threshold law. Searches by the source paper, scheme name, pointwise monotonicity, exact/critical step-size terminology, Adams–Bashforth extrapolation, and equivalent scalar level-crossing formulations found no inspected prior statement of these formulas. Originality is claimed only to the best of our knowledge.

## Limitations

The sharp threshold assumes the exact homogeneous starter used in the source theorem. A numerical starter can shift the crossing. The if-and-only-if statement classifies only the first CN/AB increment after that starter; it is not a characterization of the entire discrete orbit. The nonhomogeneous result is perturbative and does not provide a universal sharp threshold for arbitrary spatial data. The general \(\alpha>1\) result concerns a homogeneous over-extrapolated nonlinear forcing multiplied by a positive update factor; it is not a blanket theorem for every multistep PDE scheme. The analysis is for the cubic Allen–Cahn nonlinearity on the positive branch \(0<a<1\), under periodic or homogeneous Neumann boundary conditions, in exact arithmetic.

## References

1. P. Li and D. Wang, *Pointwise Monotonicity of the Allen–Cahn Flow and Dynamical Limitations of Energy-Stable Schemes*, arXiv:2609.19023 (2026). https://arxiv.org/abs/2609.19023
2. X. Feng, T. Tang and J. Yang, *Stabilized Crank-Nicolson/Adams-Bashforth Schemes for Phase Field Models*, East Asian Journal on Applied Mathematics 3(1), 59–80 (2013). https://doi.org/10.4208/eajam.200113.220213a
3. P. Li and D. Wang, *Asymptotic Stability of Many Numerical Schemes for Phase-Field Modeling*, Journal of Scientific Computing 106, 6 (2026); arXiv:2411.06943. https://arxiv.org/abs/2411.06943
4. J. Xu and X. Xu, *Lack of robustness and accuracy of many numerical schemes for phase-field simulations*, Mathematical Models and Methods in Applied Sciences 33(8), 1721–1746 (2023). https://doi.org/10.1142/S0218202523500409
