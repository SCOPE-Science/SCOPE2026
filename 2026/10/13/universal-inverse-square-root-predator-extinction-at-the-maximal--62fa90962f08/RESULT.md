# Universal inverse-square-root predator extinction at the maximal Holling-IV response threshold

## Finding
At the maximum of the Holling-IV predator numerical response, positioning the prey carrying capacity exactly at that maximum and setting predator mortality equal to maximal reproduction makes the predator-free state globally attracting **but not exponentially attracting**. All strictly positive trajectories have the same sharp critical law:
\[
\begin{aligned}
\lim_{t\to\infty}\sqrt t\,y(t)&=\frac{(1+2c\sqrt b)^2}{\sqrt{2\beta(c-\xi)b^{3/2}}},\\
\lim_{t\to\infty}\sqrt t\,(\gamma-x(t))&=\frac{1+2c\sqrt b}{\sqrt{2\beta(c-\xi)b^{3/2}}}.
\end{aligned}
\]
The exponent and the coefficients are independent of the positive initial densities.

## Assumptions and scope
Consider the continuous-time predator--prey equations
\[
\begin{aligned}
\dot x&=x(1-x/\gamma)-f(x)y,\\
\dot y&=(\beta g(x)-\delta)y,\\
f(x)&=\frac{x}{c(1+bx^2)+x},\\
g(x)&=\frac{x+\xi(1+bx^2)}{c(1+bx^2)+x},\\
c&=1+\alpha\xi.
\end{aligned}
\]
The variables \(x(t)\) and \(y(t)\) are nonnegative prey and predator densities. Fix arbitrary \(\alpha,\xi,b,\beta>0\) satisfying \(c>\xi\), and impose the **two exact threshold constraints**
\[
\gamma=\frac1{\sqrt b},\qquad
\delta=\beta m,\qquad
m=\frac{1+2\xi\sqrt b}{1+2c\sqrt b}.
\]
The initial data are any finite \(x(0)>0\) and \(y(0)>0\). No upper bound on either initial density is imposed. The functional responses and time scaling are exactly those in Section 4, equations (14)--(16), of Verma et al. [1]. The subject is deterministic population dynamics (MSC 2020: 92D25).

## Proof
**1. A global, quadratic mortality gap.** Write \(Q(x)=1+bx^2\), \(z(x)=x/Q(x)\), and \(c=1+\alpha\xi\). Then
\[
g(x)=\frac{z(x)+\xi}{z(x)+c},\qquad z(x)\le\frac1{2\sqrt b}\quad(x\ge0).
\]
The inequality is sharp only at \(x=\gamma=1/\sqrt b\), since \(1+bx^2-2\sqrt b\,x=(\sqrt b\,x-1)^2\). As \(c>\xi\), the displayed fractional-linear response is strictly increasing in \(z\). Therefore \(g(x)\le m=g(\gamma)\), with equality only at \(x=\gamma\). Direct subtraction yields the exact identity
\[
a(x):=\beta\bigl(m-g(x)\bigr)
=\frac{\beta(c-\xi)b(x-\gamma)^2}
{(1+2c\sqrt b)\,[c(1+bx^2)+x]}\ge0.
\tag{1}
\]
In particular, with
\[
F=f(\gamma)=\frac1{1+2c\sqrt b},\qquad
G=-g''(\gamma)=\frac{2(c-\xi)b^{3/2}}{(1+2c\sqrt b)^2}>0,
\]
we have \(a(x)=(\beta G/2)(x-\gamma)^2+o((x-\gamma)^2)\) as \(x\to\gamma\).

**2. Global existence and boundedness.** For \(x>0\), \(f(x)/x=[c(1+bx^2)+x]^{-1}\le1/c\). Thus
\[
\dot x=x\left(1-\frac{x}{\gamma}-\frac{y}{c(1+bx^2)+x}\right),
\qquad \dot y=-a(x)y.
\]
Both coordinates remain strictly positive for every finite time. Since \(\dot y\le0\), \(0<y(t)\le y(0)\); since \(\dot x\le x(1-x/\gamma)\), \(0<x(t)\le\max\{x(0),\gamma\}\). These bounds and the regular vector field prevent finite-time blow-up, so the solution is global.

**3. The predator must vanish.** Monotonicity gives \(y(t)\downarrow L\ge0\). If \(L>0\), integrating \(\dot y/y=-a(x)\) gives \(\int_0^\infty a(x(t))\,dt=\log(y(0)/L)<\infty\). The function \(a(x(t))\) is nonnegative and uniformly continuous: \(x(t)\) and \(\dot x(t)\) are bounded, and \(a\) is continuously differentiable on their compact range. Hence \(a(x(t))\to0\). Indeed, otherwise uniform continuity supplies disjoint intervals of a fixed positive width and height, contradicting integrability. By (1) and boundedness, \(x(t)\to\gamma\). But the prey equation would then give \(\dot x(t)\to-f(\gamma)L<0\), contradicting convergence of \(x(t)\). Hence \(L=0\).

**4. The prey tends to carrying capacity.** The logistic upper comparison gives \(\limsup_{t\to\infty}x(t)\le\gamma\). For any \(0<\varepsilon<1\), Step 3 gives \(y(t)/c<\varepsilon\) eventually, and then
\[
\dot x\ge x(1-\varepsilon-x/\gamma).
\]
Positive logistic lower comparison implies \(\liminf_{t\to\infty}x(t)\ge\gamma(1-\varepsilon)\). Letting \(\varepsilon\downarrow0\) proves \(x(t)\to\gamma\).

**5. The prey deficit is slaved to predator density.** Put \(u=x-\gamma\), \(w=u/y\). The prey and predator equations give the **exact** scalar linear nonautonomous equation
\[
\dot w=-\left(1+\frac{u}{\gamma}-a(x)\right)w-f(x).
\tag{2}
\]
By Steps 3--4, the coefficient of \(w\) tends to \(1\) and \(f(x(t))\to F\). Variation of constants in (2) proves \(w(t)\to-F\): after a fixed large time the coefficient is positive and bounded away from zero, and the forcing tends to its constant limit. Therefore
\[
\frac{\gamma-x(t)}{y(t)}\longrightarrow F>0.
\tag{3}
\]
In particular, \(x(t)<\gamma\) for all sufficiently large times, regardless of the initial prey density.

**6. The sharp coefficient.** The exact gap (1) and (3) imply
\[
\frac{d}{dt}\frac1{y(t)^2}
=\frac{2a(x(t))}{y(t)^2}
\longrightarrow\beta G F^2>0.
\]
Since \(y(t)>0\) and the derivative has a finite positive limit, averaging over time yields
\[
\lim_{t\to\infty}\frac1{t\,y(t)^2}=\beta G F^2.
\]
Taking positive square roots and using (3) gives
\[
\begin{aligned}
\lim_{t\to\infty}\sqrt t\,y(t)&=\frac1{F\sqrt{\beta G}}
=\frac{(1+2c\sqrt b)^2}{\sqrt{2\beta(c-\xi)b^{3/2}}},\\
\lim_{t\to\infty}\sqrt t\,(\gamma-x(t))&=\frac1{\sqrt{\beta G}}
=\frac{1+2c\sqrt b}{\sqrt{2\beta(c-\xi)b^{3/2}}}.
\end{aligned}
\]
All limits hold for **every** strictly positive initial condition. This completes the proof.

## Verification
The bundled `verifier.py` checks (1) as a rational-function identity for symbolic parameters, the formulas for \(F\) and \(G\), the differential identity (2), and an exact rational parameter witness. Run `python verifier.py` with SymPy installed; the expected terminal line is `VERIFY_OK`. The proof of global convergence and the asymptotic limits is analytic, not based on simulations or a finite grid.

For the exact witness \(\alpha=\xi=b=\gamma=1\), \(c=2\), \(\beta=5\), \(\delta=3\), the theorem specializes to
\[
\lim_{t\to\infty}\sqrt t\,y(t)=\frac{25}{\sqrt{10}},\qquad
\lim_{t\to\infty}\sqrt t\,(1-x(t))=\frac5{\sqrt{10}}.
\]
The special choice is only a consistency check; the theorem has the continuous parameter range stated above.

## Relationship to prior work
Verma et al. [1], Section 4.1, identify the double root of the interior predator-nullcline equation at \(d=d^*=(1+2\xi\sqrt b)/(1+2c\sqrt b)\) and \(x=1/\sqrt b\). Their Theorem 4 in Section 3 gives strict local predator-free criteria \(\beta g(\gamma)<\delta\) and \(\beta g(\gamma)>\delta\), leaving the equality case unresolved. Their Theorem 8 addresses a **positive coexistence** cusp at \(\gamma=2/\sqrt b\), not the **predator-free collision** at \(\gamma=1/\sqrt b\) proved here. Their Theorem 7 concerns a positive coexistence equilibrium and does not imply this boundary extinction rate.

Prakash and Vamsi [2] study an additional-food Holling-IV response with a nonzero explicit intrapredator competition term proportional to the **square of predator density**. The present model [1] lacks that term, and its critical predator decay is controlled instead by a cubic effective drift; the two systems are not equivalent at the threshold. The earlier inhibitory-prey study of Vamsi, Kanumoori, and Chhetri [3] concerns related additional-food ecological dynamics, but its accessible abstract does not establish the present sharp all-initial-data law. General normal-form intuition about cubic critical slowing is not a substitute for the global result and exact model-specific coefficients.

## Limitations
The conclusions require \(c>\xi\), exact equality of mortality to the maximum numerical response, and exact coincidence of the prey carrying capacity with the numerical-response maximizer. The result excludes \(x(0)=0\) and \(y(0)=0\): their invariant boundary trajectories have different asymptotics. The analysis is deterministic, homogeneous, without direct predator crowding, diffusion, delay, or time-dependent forcing. It does not assert robustness of the exponent away from the tuned parameter surface or infer any intervention efficacy from the idealized model. The exact source-specific half-power law is not shown to be independent of every general center-manifold theorem in the literature; generic local cubic asymptotics may be known, but do not supply this global theorem by themselves.

## References
[1] U. Verma, K. Goyal, S. Biswas, J. I. Lathrop, and R. D. Parshad, *An Investigation of Additional Food Models with Generalised Functional Response*, arXiv:2606.26340v1 (first submitted June 24, 2026), Section 3 Theorems 4 and 7; Section 4 Equations (14)--(27) and Theorem 8. https://arxiv.org/abs/2606.26340 ; accessible full text: https://www.researchgate.net/publication/408106658_An_Investigation_of_Additional_Food_Models_with_Generalised_Functional_Response .

[2] D. Bhanu Prakash and D. K. K. Vamsi, *Role of Intra-specific Competition and Additional Food on Prey-Predator Systems exhibiting Holling Type-IV Functional Response*, arXiv:2504.09078v1 (April 12, 2025), Sections 2, 5--7. https://arxiv.org/html/2504.09078v1 .

[3] D. K. K. Vamsi, D. S. S. M. Kanumoori, and B. Chhetri, *Additional Food Supplements as a Tool for Biological Conservation of Biosystems in the Presence of Inhibitory Effect of the Prey*, *Acta Biotheoretica* 68 (2020), 321--355, DOI:10.1007/s10441-019-09371-x (first public November 26, 2019; abstract inspected). https://pubmed.ncbi.nlm.nih.gov/31773436/ .
