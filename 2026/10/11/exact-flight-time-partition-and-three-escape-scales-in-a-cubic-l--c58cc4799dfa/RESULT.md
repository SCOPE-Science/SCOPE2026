# Exact flight-time partition and three escape scales in a cubic \(\Lambda\)–\(\Omega\) flow

## Finding

For \(\mu>0\) and \(\kappa>0\), consider the *physical-time* polynomial system
\[
\dot x=-y(1+\mu y)+x(\mu x-\kappa xy),\qquad
\dot y=x(1+\mu y)+y(\mu x-\kappa xy).
\]
Put \(q=\mu^2+\kappa\), \(y_-=-1/(\mu+\sqrt q)\), \(y_+=1/(\sqrt q-\mu)\), and \(b(x)=-(\kappa x^2+1)/(2\mu)\).

The only equilibria are \((0,0)\) and \((0,-1/\mu)\). Every point of \(\{y_-<y<y_+\}\setminus\{(0,0)\}\) lies on a periodic ellipse with minimal period \(T_0=2\pi\). Every point of \(\{y<b(x)\}\setminus\{(0,-1/\mu)\}\) lies on a periodic ellipse with minimal period \(T_1=2\pi\mu/\sqrt q\). There are no other periodic trajectories. Every other non-equilibrium real trajectory blows up in finite time in *both* directions.

The two invariant straight lines \(y=y_-\) and \(y=y_+\) consist of infinity-to-infinity trajectories of respective full maximal physical-time lifetimes
\[
F_- =\pi\left(1+\frac\mu{\sqrt q}\right),\qquad
F_+ =\pi\left(1-\frac\mu{\sqrt q}\right).
\]
The invariant parabola \(y=b(x)\) also consists of one entire infinity-to-infinity trajectory, with lifetime \(F_{\mathrm p}=2\pi\mu/\sqrt q\). Thus the four natural durations obey the **exact time-partition identities**
\[
\boxed{\quad T_0=F_-+F_+,\qquad T_1=F_{\mathrm p}=F_--F_+.\quad}
\]
Their equality is in the displayed original time variable, not up to a time rescaling or orbital equivalence.

The three escaping orbit classes also have distinct exact blow-up exponents. On either invariant line, at either finite endpoint \(t_*\), \(|x(t)|\,|t-t_*|\to1/\sqrt q\). On the invariant parabola,
\[
|x(t)|\,|t-t_*|^{1/3}\to\left(\frac{4\mu}{3\kappa^2}\right)^{1/3},\qquad
\frac{y(t)}{x(t)^2}\to-\frac{\kappa}{2\mu}.
\]
Finally every remaining, non-line, non-parabola, nonperiodic orbit has \(H=-h\) with \(h>1/\kappa\), and at both maximal time endpoints obeys
\[
\lim_{t\uparrow t_+}(t_+-t)y(t)^2
=\lim_{t\downarrow t_-}(t-t_-)y(t)^2
=\frac1{2\kappa\sqrt{\kappa h-1}},
\]
with \(x(t)/y(t)\to-\sqrt{\kappa h-1}\) at \(t_+\) and \(+\sqrt{\kappa h-1}\) at \(t_-\).

## Assumptions and scope

All assertions concern classical maximal solutions of the stated autonomous cubic polynomial ODE, with \(\mu,\kappa\) arbitrary fixed strictly positive *real* constants. No statements are made for the singular parameter axes, for complex trajectories, or for time-reparameterized dynamics. The plane is partitioned into the two equilibrium points, the two disjoint open periodic regions in the Finding, the two invariant horizontal lines, the invariant separating parabola, and the remaining hyperbolic sectors. The strict domains remove all ambiguity at the boundaries. At \(y=y_\pm\), the rational first integral below is undefined; these lines are treated independently.

## Proof

**First integral and invariant sets.** Define \(p(y)=1+2\mu y-\kappa y^2\). Directly collecting terms gives
\[
\dot x=-y(1+\mu y)+(\mu-\kappa y)x^2,\qquad
\dot y=xp(y).
\]
Also \(\frac{d}{dt}(x^2+y^2)=2x(\mu-\kappa y)(x^2+y^2)\), while \(\frac{d}{dt}p(y)=2x(\mu-\kappa y)p(y)\). Hence wherever \(p(y)\ne0\),
\[
H(x,y)=\frac{x^2+y^2}{p(y)}
\]
is constant. The simple zeros of \(p\) are exactly \(y_-\) and \(y_+\); \(p>0\) only between them. The invariant horizontal lines \(y=y_\pm\) follow from \(\dot y=xp(y)\). On any constant nonzero level \(H=E\), the level curve has conic equation
\[
x^2+(1+\kappa E)y^2-2\mu E y-E=0.\tag{1}
\]
Stationarity requires \(x=0\) away from \(p=0\) and then \(-y(1+\mu y)=0\); on \(p=0\) the explicit nonvanishing Riccati equation below excludes equilibrium. Thus the two listed equilibria are exhaustive.

For \(p>0\), \(E>0\), \(1+\kappa E>0\) and (1) is a regular ellipse except at the origin. Its connected level set lies in the central strip, contains no critical point, and is therefore one periodic orbit. In a region where \(p<0\), write \(E=-h\), \(h>0\). The identity
\[
H+\frac1q=\frac{q x^2+(1+\mu y)^2}{q p(y)}
\]
shows \(h\ge1/q\), with equality only at the second equilibrium. Moreover
\[
H+\frac1\kappa=\frac{\kappa x^2+1+2\mu y}{\kappa p(y)}.
\]
For the lower strip \(y<y_-\), this proves \(1/q<h<1/\kappa\) precisely inside \(y<b(x)\): (1) is then a regular ellipse entirely in the lower region, with no other critical point. On the parabola, \(h=1/\kappa\); outside it below \(y_-\), and throughout \(y>y_+\), one has \(h>1/\kappa\), so (1) is a hyperbola. This proves the claimed global partition of periodic and nonperiodic orbits.

**Exact ellipse periods.** For an elliptical level \(H=E\), set \(a=1+\kappa E>0\), \(c=\mu E/a\), \(R^2=E(1+qE)/a>0\), and \(B=R/\sqrt a\). Parameterize \(x=R\cos\phi\), \(y=c+B\sin\phi\). The original ODE gives \(\dot\phi=\sqrt a\,p(c+B\sin\phi)\). Using
\[
\frac1{p(y)}=\frac1{2\sqrt q}\left(\frac1{y-y_-}-\frac1{y-y_+}\right),\qquad
(c-y_\pm)^2-B^2=\frac{y_\pm^2}{a},
\]
and the elementary integral \(\int_0^{2\pi}(d+B\sin\phi)^{-1}d\phi=2\pi\operatorname{sgn}(d)/\sqrt{d^2-B^2}\) for \(|d|>B\), obtain
\[
T(E)=\frac1{\sqrt a}\int_0^{2\pi}\frac{d\phi}{|p(c+B\sin\phi)|}
=\begin{cases}2\pi,&E>0,\\2\pi\mu/\sqrt q,&-1/\kappa<E<-1/q.\end{cases}
\]
Each ellipse is a simple closed orbit with nonvanishing speed, so this is its minimal period.

**Invariant lines and parabola.** At either root \(y=y_\pm\), the root identity \(1+\mu y=-y(\mu-\kappa y)\) yields
\[
\dot x=(\mu-\kappa y_\pm)(x^2+y_\pm^2)
=\begin{cases}\sqrt q(x^2+y_-^2),&y=y_-,\\-\sqrt q(x^2+y_+^2),&y=y_+.\end{cases}
\]
The full time from one infinite endpoint to the other is therefore \(F_\pm=\pi/(\sqrt q\,|y_\pm|)\), giving the two stated values. Their one-sided Riccati expansion at infinity proves the \(|t-t_*|^{-1}\) blow-up with coefficient \(1/\sqrt q\).

On \(y=b(x)\), substitution into the polynomial ODE yields
\[
\dot x=\frac{(1+\kappa x^2)^2+4\mu^2x^2}{4\mu}>0,\qquad
y=-\frac{1+\kappa x^2}{2\mu}.
\]
Thus this entire parabola is one maximal orbit and
\[
F_{\mathrm p}=4\mu\int_{-\infty}^{\infty}\frac{dx}{(1+\kappa x^2)^2+4\mu^2x^2}
=\frac{2\pi\mu}{\sqrt q}.
\]
The last equality follows by \(z=\sqrt\kappa x\) and \(\int_{-\infty}^{\infty}(z^4+az^2+1)^{-1}dz=\pi/\sqrt{a+2}\) for \(a>-2\). This integral identity follows, for example, from splitting the even integral under the substitution \(z\mapsto1/z\) and then using \(w=z-1/z\). The quartic leading term gives \(\dot x\sim\kappa^2x^4/(4\mu)\), and hence the exact \(|t-t_*|^{-1/3}\) coefficient, with the stated quadratic relation for \(y\).

**All other orbits and sharp hyperbolic blow-up.** For \(E=-h\), \(h>1/\kappa\), equation (1) becomes \(x^2-(\kappa h-1)y^2+2\mu h y+h=0\). Each connected branch has one point at which \(x=0\) and then extends at both ends to \(|y|=\infty\); it lies entirely either above \(y_+\) or between the lower invariant line and the parabola. There is no finite equilibrium on the branch. At infinity, \(x/y\to\pm\sqrt{\kappa h-1}\) and
\[
\dot y=x\bigl(1+2\mu y-\kappa y^2\bigr)\sim-\kappa x y^2.
\]
The forward-going end has \(x/y\to-\sqrt{\kappa h-1}\), giving \(\dot y\sim\kappa\sqrt{\kappa h-1}\,y^3\); the backward-going end has the opposite ratio. Integrating the differential equation for \(y^{-2}\) proves that each endpoint is reached in finite time and yields the two displayed limits, with no assumption on initial position beyond the stated hyperbolic domain.

Finally, direct substitution into \(F_\pm\), \(F_{\mathrm p}\) and the elliptical period formulas gives \(T_0=F_-+F_+\) and \(T_1=F_{\mathrm p}=F_--F_+\). All comparisons are in physical time.

## Verification

A standalone symbolic checker, `verify.py`, checks the polynomial first-integral derivative, both linearized centers, the invariant-line Riccati reductions, the parabolic polynomial identity and velocity, and the exact time-partition constants. It runs with SymPy and prints `CHECK_OK` upon success. The analytic trigonometric and quartic integral identities, global conic classification, and endpoint asymptotic comparison are proved above and are not inferred from a finite numerical experiment.

## Relationship to prior work

Zhou's 2023 article introduces the analytic-commutator conditions for the broader \(\Lambda\)–\(\Omega\) family and proves local isochronicity of the origin for the specialization \(\lambda=\mu\), \(h_2=-\lambda_2xy\). We use the same family with \(\kappa=\lambda_2>0\) and do not claim the originating family or its local origin isochronicity as new. Earlier cubic/quartic reversible bi-center papers already study simultaneous centers and, in some cases, global topological phase portraits. The present claim is the original-physical-time **sum/difference of three infinity-to-infinity flight durations with the two center periods**, plus the exhaustive finite-time escape division and its three distinct sharp rates. Such time data are not fixed by a topological phase portrait or local center classification. See limitations about unresolved source access.

## Limitations

The theorem is restricted to \(\mu,\kappa>0\). No statement is made about perturbation robustness, limit cycles outside this exact family, or complex dynamics. Prior literature may contain equivalent time identities under different coordinates; the relevant Fernandes–Valério–Tempesta 2022 full text was access restricted and could not be inspected. Its abstract confirms classifications of global portraits and isochronous bi-centers, which are therefore not claimed as independent contributions. The originality comparison cannot certify exhaustive priority. The proof supplies no separate independent audit.

## References

1. Zhengxin Zhou, *On the analytic commutator for \(\Lambda\)–\(\Omega\) differential systems*, Electronic Journal of Qualitative Theory of Differential Equations 2023, No. 25, 1–14, first appeared 2023-07-06, DOI: 10.14232/ejqtde.2023.1.25. Full PDF: https://www.math.u-szeged.hu/ejqtde/p10349.pdf.
2. Maša Dukarić, Wilker Fernandes and Regilene Oliveira, *Symmetric centers on planar cubic differential systems*, Nonlinear Analysis 197 (2020), 111868, DOI: 10.1016/j.na.2020.111868.
3. Wilker Fernandes, Viviane Pardini Valério and Patricia Tempesta, *Isochronicity of bi-centers for symmetric quartic differential systems*, Discrete and Continuous Dynamical Systems B 27 (2022), 3991–4006, DOI: 10.3934/dcdsb.2021215.
4. Marco Sabatini, *Centers with equal period functions*, Journal of Mathematical Analysis and Applications (2015), DOI: 10.1016/j.jmaa.2015.04.065.
