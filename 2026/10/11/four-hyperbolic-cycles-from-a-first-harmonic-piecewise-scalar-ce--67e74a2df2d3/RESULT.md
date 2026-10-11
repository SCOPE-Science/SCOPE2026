# Four hyperbolic cycles from a first-harmonic piecewise scalar center

## Finding

Consider the scalar, \(2\pi\)-periodic differential equation
\[
\dot x=(2\sin t+\varepsilon p)|x|+2\sin t-\varepsilon(r-p),
\qquad 0<p<r,\quad\varepsilon>0.
\]
Define the explicit even response profile
\[
I(s)=\int_0^{2\pi}\exp(-|s-2\cos t|)\,dt,
\qquad s\in\mathbb R.
\]
There is a unique \(s_*\in(0,2)\) at which \(I\) attains its maximum on the positive half-line. Put \(I_0=I(0)\), \(I_*=I(s_*)\), and \(\lambda=2\pi p/r\). The constants satisfy \(0<I_0<I_*<2\pi\), with \(I_0\simeq2.14980156\), \(I_*\simeq2.22266137\), and \(s_*\simeq1.31497\).

For each fixed \(p,r\) with \(0<p<r\) and \(\lambda\notin\{I_0,I_*\}\), there exists \(\varepsilon_0(p,r)>0\) such that, whenever \(0<\varepsilon<\varepsilon_0(p,r)\), the equation has **exactly** the following numbers of \(2\pi\)-periodic solutions (counted as distinct periodic graphs):
\[
\begin{array}{c|ccc}
\lambda& (0,I_0)&(I_0,I_*)&(I_*,2\pi)\\\hline
\text{number}&2&4&0.
\end{array}
\]
Every counted solution is isolated and hyperbolic. In the four-solution regime, all four change sign in one forcing period. Their initial values, after the coordinate transformation below, converge to the four simple roots \(s_1<s_2<s_3<s_4\) of \(I(s)=\lambda\), and their Floquet multipliers obey
\[
\rho_j(\varepsilon)=1-\varepsilon r I'(s_j)+o(\varepsilon).
\]
From left to right, the four periodic solutions alternate **attracting, repelling, attracting, repelling**. The unperturbed equation at \(\varepsilon=0\) is a global center; the result exhibits a nonempty open coefficient wedge with four hyperbolic cycles despite using only the first trigonometric harmonic.

## Assumptions and scope

Time is the original, unrescaled time, and periodicity is imposed over \(2\pi\). The parameters \(p,r\) are held fixed as \(\varepsilon\downarrow0\). The classification excludes the two critical levels \(I_0\) and \(I_*\); it makes no statement about the number or multiplicity of cycles on those levels or for non-small perturbations. The counts include solutions of either fixed sign as well as sign-changing solutions. The scalar right-hand side is globally Lipschitz in the state, so all forward and backward solutions exist uniquely.

## Proof

**1. Exact global-center conjugacy.** Let
\[
 z=\operatorname{sgn}(x)\log(1+|x|),\qquad
 x=\operatorname{sgn}(z)(e^{|z|}-1).
\]
This is a continuously differentiable, strictly increasing bijection of the real line, with positive derivative. Direct division by \(1+|x|=e^{|z|}\) gives the **exact**, not averaged, equation
\[
\dot z=2\sin t+\varepsilon\bigl(p-r e^{-|z|}\bigr).
\]
For \(\varepsilon=0\), every solution is \(z(t)=s-2\cos t\) for some \(s\in\mathbb R\), so every original-state solution is \(2\pi\)-periodic. Write \(z_\varepsilon(0;s)=s-2\); then
\[
 z_\varepsilon(2\pi;s)-(s-2)
 =\varepsilon\left(2\pi p-r J_\varepsilon(s)\right),\quad
 J_\varepsilon(s)=\int_0^{2\pi}e^{-|z_\varepsilon(t;s)|}\,dt.
\]
Because \(|p-r e^{-|z|}|\le p+r\), the integral equation and the global \(1\)-Lipschitz property of \(e^{-|z|}\) imply, for all real \(s\),
\[
\sup_{0\le t\le2\pi}|z_\varepsilon(t;s)-(s-2\cos t)|
\le2\pi\varepsilon(p+r),\qquad
\sup_{s\in\mathbb R}|J_\varepsilon(s)-I(s)|
\le(2\pi)^2\varepsilon(p+r).
\]
Consequently the normalized return displacement converges **uniformly on the entire real line** to \(r(\lambda-I(s))\). In particular, no additional periodic solutions can escape to unbounded initial conditions while the four roots persist.

**2. Exact shape of the response profile.** The change of variables \(u=2\cos t\) gives
\[
 I(s)=2\int_{-2}^{2}\frac{e^{-|s-u|}}{\sqrt{4-u^2}}\,du.
\]
Hence \(I\) is even, continuously differentiable, strictly positive, and tends to zero as \(|s|\to\infty\). For \(|s|<2\), differentiation in the distributional convolution identity \((d^2/ds^2-1)e^{-|s|}=-2\delta_0\) yields the ordinary differential equation
\[
 I''(s)-I(s)=-\frac4{\sqrt{4-s^2}}.
\]
In particular, \(I'(0)=0\) and \(I''(0)=I_0-2\). To establish \(I_0>2\) without relying on numerics, use the elementary alternating-Taylor inequality \(\sin u\le u-u^3/7\) for \(0\le u\le\pi/2\). Since \(\pi/2>3/2\) and \(e^v\ge1+v\) for \(v\ge0\),
\[
 \frac{I_0}{4}=\int_0^{\pi/2}e^{-2\sin u}\,du
 >\int_0^{3/2} e^{-2u}\left(1+\frac{2u^3}{7}\right)du
 =\frac{17-53e^{-3}}{28}>\frac12.
\]
(The final strict inequality follows from \(e^3>53/3\), itself immediate from the first six Taylor terms.) We also have \(I'(2)=-I(2)<0\), since for \(s\ge2\) the profile is \(I(s)=I(2)e^{2-s}\).

Set \(h(s)=I'(s)\) on \((0,2)\). Differentiating the profile ODE gives
\[
 h''(s)-h(s)=-\frac{4s}{(4-s^2)^{3/2}}<0.
\]
The Wronskian-like expression \(W(s)=h'(s)\sinh s-h(s)\cosh s\) satisfies
\[
 W'(s)=(h''(s)-h(s))\sinh s<0,\qquad W(0)=0.
\]
Thus \(h(s)/\sinh s\) decreases strictly on \((0,2)\), from the positive limit \(I''(0)\) to a negative value near \(2\). It has exactly one zero \(s_*\in(0,2)\), and \(I\) increases on \((0,s_*)\) and decreases on \((s_*,\infty)\). It follows that \(I_* > I_0>0\). Finally \(I_*<2\pi\), because the integrand is at most one and is strictly less than one except at finitely many phases. This proves precisely the asserted two, four, or zero **simple** profile-root counts at noncritical levels.

For completeness, \(I(2)<2\) can also be proved without numerics: the series expansion gives \(I(2)=2\pi e^{-2}\sum_{k\ge0}(k!)^{-2}\). The positive series is less than \(23/10\), while \(e^2>73/10\) and \(\pi<22/7\), giving \(I(2)<2\). Thus, when \(I_0<\lambda<I_*\), all four profile roots have absolute value less than \(2\), and the corresponding unperturbed trajectories cross zero transversely twice.

**3. Persistence and exact global count.** Let \(s_j\) be a simple zero of \(I(s)-\lambda\). In a sufficiently small compact neighborhood of \(s_j\), all unperturbed zero crossings \(s-2\cos t=0\) are transverse whenever they occur; at such crossings \(2\sin t\ne0\). The standard parameter variational equation, integrated separately between these finitely many transverse crossings, shows that \(J_\varepsilon\to I\) in \(C^1\) on this neighborhood. This can also be seen directly from the integral representation and dominated convergence: the exceptional crossing instants have measure zero and the initial-state derivative of the flow tends uniformly to one. Consequently \(\lambda-J_\varepsilon(s)\) is strictly monotone near each simple root and has exactly one zero there for small \(\varepsilon\). Away from these neighborhoods, \(|\lambda-I(s)|\) is bounded below by a positive constant: this uses both the compact complement and \(I(s)\to0\) at infinity, with \(\lambda>0\). The global uniform displacement estimate from Step 1 therefore excludes all other roots. The number of periodic solutions is exactly the profile-root count.

**4. Hyperbolicity and stability.** The derivative of the exact return map in the transformed initial coordinate exists at every continued solution because its zero crossings are transverse (or absent), and the same variational argument gives
\[
\frac{d z_\varepsilon(2\pi;s)}{ds}\Big|_{s=s_j(\varepsilon)}
=1-\varepsilon r I'(s_j)+o(\varepsilon).
\]
The increasing \(C^1\) change of state coordinates preserves the multiplier. Since all profile zeros are simple, none of these multipliers equals one for sufficiently small positive \(\varepsilon\); moreover they remain positive. Their sign relative to one determines attracting versus repelling. The profile derivative signs for the four roots are \(+, -, +, -\), proving the stated order of stability.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It computes the response profile by midpoint quadrature, checks its local minimum and two symmetric maxima, locates four simple crossings for the **illustrative** coefficient choice \(p=7\), \(r=20\), and numerically brackets four zeros of the exact transformed return displacement when \(\varepsilon=10^{-3}\). It prints `CHECK_OK` when all checks succeed. These numerical checks are **not** the proof that there are no other roots, and they do not certify the illustrative coefficients symbolically; the global exact count rests on Steps 1–4. The exact open parameter wedge is independently nonempty by the analytical inequality \(I_* > I_0\).

## Relationship to prior work

Bravo, Fernández, and Ojeda (first arXiv version July 28, 2023) study exactly the first-harmonic family of scalar piecewise equations containing the system above. Their global-center criterion proves the center interpretation at zero perturbation, and their Theorem 2.14 bounds the number of limit cycles in the general first-harmonic family by \(22\); the same source does not state this four-cycle lower-bound construction or the complete local two–four–zero diagram. Bravo, Fernández, and Tineo (2007) describe general distributions of periodic solutions for piecewise scalar ODEs without an evaluated first-harmonic bifurcation profile. Gasull and Zhao (2023) prove at-most-two results under sign restrictions; here both varying coefficient functions change sign for sufficiently small perturbation and those restrictions do not apply. Tian and Zhao (2024) establish unbounded numbers of cycles when arbitrary smooth time coefficients are permitted, which does not imply the first-harmonic construction or its exact local count. Bravo and Trinidad-Forte (2026) characterize global centers for higher-harmonic coefficients but do not determine the off-center four-cycle wedge.

## Limitations

This is a local small-parameter theorem, not an identification of the global Hilbert number of the entire first-harmonic class. The two critical levels \(I_0\) and \(I_*\) are excluded, and the theorem makes no claims about arbitrary larger perturbations. The numerical example is supporting evidence rather than a rigorous finite-precision parameter certificate. Full text of Tian and Zhao (2024), a broadly relevant paper on scalar piecewise equations with arbitrary smooth coefficients, could not be retrieved and remains a source-priority uncertainty.

## References

1. J. L. Bravo, M. Fernández and I. Ojeda, *Hilbert Number for a Family of Piecewise Nonautonomous Equations*, arXiv:2307.15578v1, July 28, 2023; *Qualitative Theory of Dynamical Systems* **23** (2024), article 119, DOI:10.1007/s12346-023-00922-9. Full preprint: https://arxiv.org/pdf/2307.15578.
2. J. L. Bravo, M. Fernández and A. Tineo, *Periodic solutions of a periodic scalar piecewise ODE*, *Communications on Pure and Applied Analysis* **6** (2007), 213–228, DOI:10.3934/cpaa.2007.6.213.
3. A. Gasull and Y. Zhao, *Existence of at most two limit cycles for some non-autonomous differential equations*, *Communications on Pure and Applied Analysis* **22** (2023), 970–982, DOI:10.3934/cpaa.2023016.
4. R. Tian and Y. Zhao, *The Limit Cycles for a Class of Non-autonomous Piecewise Differential Equations*, *Qualitative Theory of Dynamical Systems* **23** (2024), article 185, DOI:10.1007/s12346-024-01050-8.
5. J. L. Bravo and R. Trinidad-Forte, *Global Centers in Piecewise Linear Equations in the Cylinder*, *Qualitative Theory of Dynamical Systems* **25** (2026), article 26, DOI:10.1007/s12346-025-01425-5.
