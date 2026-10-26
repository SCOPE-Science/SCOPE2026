# Sharp homoclinic extinction threshold and logarithmic critical tails in a three-reaction network

## Finding
Consider the mass-action network \(2X\to3X\), \(X+Y\to2Y\), \(2Y\to Y\), with respective strictly positive rate constants \(a,b,c\). Its concentration dynamics is
\[
\dot x=x(ax-by),\qquad \dot y=y(bx-cy),\qquad x(0),y(0)>0.
\]
**Theorem.** Every strictly positive initial condition generates a complete, nonconstant, two-sided homoclinic trajectory to the origin (both limits as \(t\to\pm\infty\) vanish) if and only if
\[
b\ge\max\{a,c\}\quad\text{and}\quad b>\min\{a,c\}.
\]
Under precisely these assumptions the dominant concentration has universal one-sided tails
\[
\lim_{t\to-\infty}|t|x(t)=\frac1a,\qquad
\lim_{t\to+\infty}t\,y(t)=\frac1c.
\]
When \(b>a\) the incoming minority species obeys \(y(t)\sim K_-|t|^{-b/a}\), for some orbit-dependent \(K_->0\); at the threshold \(b=a>c\) this changes to the universal logarithmic law
\[
\lim_{t\to-\infty}(a-c)|t|\log|t|\,y(t)=1.
\]
When \(b>c\) the outgoing minority species obeys \(x(t)\sim K_+t^{-b/c}\), for some orbit-dependent \(K_+>0\); at the other threshold \(b=c>a\) it changes to
\[
\lim_{t\to+\infty}(c-a)t\log t\,x(t)=1.
\]
If \(b<a\), an open set of positive initial states blows up in finite *forward* time. If \(b<c\), an open set blows up in finite *backward* time. When \(a=b=c\), the positive diagonal consists of equilibria and other positive states are incomplete in at least one time direction. These alternatives make the threshold exact.

## Assumptions and scope
Rates \(a,b,c\) are fixed positive real numbers, interpreted in ordinary mass-action kinetics. Solutions are maximal classical solutions in the strictly positive quadrant; "complete" means defined at every real time; "homoclinic" refers to both time limits at the nonhyperbolic equilibrium \((0,0)\). Time is original kinetic time; no rescaling is implicit in the asymptotic coefficients. This is a classification of a single three-reaction rate family, not of all planar chemical networks.

## Proof
**1. Exact projective equation.** Positivity is invariant by uniqueness. Set \(r=y/x>0\). Direct differentiation gives
\[
\dot r=xrD(r),\qquad D(r)=(b-a)+(b-c)r,
\qquad \frac{d\log x}{dr}=\frac{a-br}{rD(r)}
\]
whenever \(D(r)\ne0\). If \(b\ge\max\{a,c\}\) and \(b>\min\{a,c\}\), then \(D(r)>0\) for all \(r>0\). Thus \(r\) strictly increases.

**2. An exact parametrization of every interior trajectory.** With an arbitrary orbit-dependent \(K>0\), integration of the preceding rational differential yields \(x=K\Phi(r)\), \(y=rK\Phi(r)\), where
\[
\Phi(r)=
\begin{cases}
 r^{a/(b-a)}D(r)^{-(b^2-ac)/((b-a)(b-c))},&b>a,\ b>c,\\
 r^{-a/(a-c)}\exp[-a/((a-c)r)],&b=a>c,\\
 r^{a/(c-a)}\exp[-cr/(c-a)],&b=c>a.
\end{cases}
\]
For example, the first line follows by partial fractions:
\[
\frac{a-br}{rD(r)}=
\frac{a}{(b-a)r}
-\frac{b^2-ac}{(b-a)D(r)}.
\]
In every one of the three cases, both \(\Phi(r)\) and \(r\Phi(r)\) tend to zero as \(r\downarrow0\) and as \(r\to\infty\); they are continuous and bounded between those ends. Hence both concentrations are bounded along the maximal trajectory. Polynomial local existence, continuation, and uniqueness rule out finite-time endpoint arrival at the origin, so the trajectory is complete in both directions. Because \(r\) strictly increases, it cannot have a finite positive limit at either time end: at such a limit \(x(r)>0\) and \(\dot r>0\). Therefore \(r\to0\) as \(t\to-\infty\), and \(r\to\infty\) as \(t\to+\infty\), which proves homoclinicity.

**3. Dominant tails.** As \(t\to-\infty\), \(r\to0\) and \((1/x)'=-a+br\to-a\), while \(1/x\to\infty\). Integrating that derivative backwards and dividing by \(|t|\) gives \(|t|x(t)\to1/a\). Similarly \((1/y)'=c-b/r\to c\) at \(+\infty\), so \(t y(t)\to1/c\).

**4. Minority tails and critical logarithms.** If \(b>a\), the first or third formula for \(\Phi\) gives \(x\sim C_0r^{a/(b-a)}\) as \(r\downarrow0\), with \(C_0>0\). Combining this with the dominant incoming tail yields \(r\sim C|t|^{-(b-a)/a}\) and hence \(y\sim K_-|t|^{-b/a}\), \(K_->0\). If \(b>c\), the first or second formula gives \(y\sim C_\infty r^{-c/(b-c)}\) as \(r\to\infty\), so \(x\sim K_+t^{-b/c}\), \(K_+>0\).

At \(b=a>c\), the exact ratio equation becomes \((1/r)'=-(a-c)x\). Its integral over a long negative-time interval, together with \(x(t)\sim1/(a|t|)\), shows
\[
\frac{1}{r(t)\log|t|}\longrightarrow\frac{a-c}{a}
\quad(t\to-\infty).
\]
Multiplying by \(|t|x(t)\to1/a\) gives the first critical logarithmic law. At \(b=c>a\), \(r'=(c-a)y\); integrating with \(y(t)\sim1/(ct)\) gives \(r(t)/\log t\to(c-a)/c\) and therefore the second logarithmic law.

**5. Sharp converse.** If \(b<a\), choose an initial ratio \(r_0>0\) sufficiently small that \(D(r)<0\) and \(a-br\ge a/2\) whenever \(0<r\le r_0\). The ratio decreases forward in time and \(\dot x\ge(a/2)x^2\), forcing finite forward blow-up. These initial conditions form an open set. If \(b<c\), choose \(r_0\) sufficiently large that \(D(r)<0\) and \(c-b/r\ge c/2\) whenever \(r\ge r_0\). Backwards in time \(r\) increases and \(d y/d(-t)\ge(c/2)y^2\), forcing finite backward blow-up on an open set. Finally, if \(a=b=c\), then \(r'=0\) and \(\dot x=a(1-r)x^2\): \(r=1\) is the positive equilibrium diagonal, while every other ratio causes a finite-time blow-up in one direction. Thus the stated condition is necessary.

## Verification
The standalone `verify.py` performs 56 exact rational parameter-and-ratio checks of the projective quadrature, four exact symbolic identities for the published \(a=c=1,b=3\) homoclinic example, and 58 exact endpoint-sign tests across positive integer rates. The recorded output is in `CHECKS.txt`. These finite calculations check critical algebra only; completeness, every-initial-condition quantifiers, and the logarithmic limits follow from the preceding proof, not from sampling.

As a consistency check, the published example \(a=c=1,b=3\) has the conserved quantity \(h=xy/(x+y)^4\). When \(x(0)=y(0)=1\), the exact solution reproduced by the checker is
\[
R(t)=\sqrt{t^2+1/4},\qquad
x(t)=\frac{R(t)-t}{2R(t)^2},\qquad y(t)=\frac{R(t)+t}{2R(t)^2}.
\]
This agrees with the source's homoclinic phase portrait; the new all-rate threshold and critical logarithms are not inferred from this one special orbit.

## Relationship to prior work
Yeung and Erban, arXiv:2610.06130v1 (first public October 5, 2026), Example 2.1, introduce exactly the \(a=c=1,b=3\) three-reaction system, give its first integral \(xy/(x+y)^4\), and identify positive homoclinic trajectories. Their work classifies local quadratic phase portraits under chemical constraints; the example and its first integral are prior work. The present theorem varies **all three positive reaction rates**, proves a sharp if-and-only-if global homoclinic criterion, and distinguishes the algebraic and logarithmic original-time extinction laws.

Algaba, García and Reyes, arXiv:1805.02873v1 (2018), analyze analytic integrability of perturbations of homogeneous quadratic Lotka–Volterra systems and identify invariant factors/first-integral structures. Those are relevant general algebraic techniques, not a statement of the all-rate global kinetic threshold and critical log tails. Classical planar quadratic-sector classifications supply broader qualitative background and may imply the homoclinic topology under specialization, but do not by themselves determine original-time asymptotic coefficients. Historical priority for every component has not been independently established.

## Limitations
The theorem applies only to the specified irreversible three-reaction mass-action family with strictly positive rate constants and initial concentrations. Its homoclinic orbits approach a degenerate equilibrium and are not periodic cycles. Claims of universality refer to the explicitly stated time coefficients and parameter ranges, not arbitrary perturbations. The result does not treat boundary initial states, stochastic chemical kinetics, or spatial diffusion. Independent validation and a comprehensive historical-priority audit have not been performed.

## References
- N. Yeung and R. Erban, *Classification of strongly non-hyperbolic critical points of planar second-order chemical reaction systems*, arXiv:2610.06130v1, October 5, 2026; https://arxiv.org/html/2610.06130v1 , especially Example 2.1 and Section 4.
- A. Algaba, C. García and M. Reyes, *The analytic integrability problem for perturbations of homogeneous quadratic Lotka–Volterra systems*, arXiv:1805.02873v1, May 8, 2018; https://arxiv.org/html/1805.02873v1 , especially Proposition 1.6 and Section 4.
