# Quadratic unlocking and a sharp harmonic threshold at the degenerate half-turn resonance

## Finding
For \(a>0\), \(b\in\mathbb R\), and sufficiently small real \(\mu\), consider the orientation-preserving circle-diffeomorphism lift
\[
F_\mu(x)=x+\frac12+\mu\bigl[a(1+\cos(4\pi x))+b\sin(2\pi x)\bigr].
\]
Let \(\rho(\mu)\) be its real translation number, normalized by \(\rho(0)=1/2\). There is a sharp dichotomy:
\[
\rho(\mu)=\begin{cases}
\displaystyle \frac12+\frac{\pi |b|}{2}\sqrt{16a^2-b^2}\,\mu|\mu|+o(\mu^2),&0<|b|<4a,\\[3pt]
\displaystyle\frac12,&b=0\text{ or }|b|\ge4a,
\end{cases}\qquad \mu\to0.
\]
The second line holds **identically** for all sufficiently small \(\mu\), not only asymptotically. In the open unlocking interval, the drift has the sign of \(\mu\); its second-order coefficient is positive and maximized at \(|b|=2\sqrt2a\), with maximum \(4\pi a^2\). At \(\mu=0\), \(\rho\) is differentiable with derivative zero but is not twice differentiable in the usual two-sided sense when \(0<|b|<4a\).

## Assumptions and scope
Here \(\rho(F)=\lim_{n\to\infty}(F^n(x)-x)/n\), independent of \(x\), for an increasing degree-one lift. Both signs of \(\mu\) are included, with \(a,b\) held fixed. The smallness requirement may depend on \(a,b\); it ensures that \(F_\mu\) is an orientation-preserving smooth diffeomorphism. The result is specific to the rational half-turn and the indicated two harmonics on the marginal line where the first-order averaged displacement has quadratic zeros.

## Proof
Set \(f(x)=a(1+\cos(4\pi x))+b\sin(2\pi x)\), and write the one-period lift of the two-step map as
\[
G_\mu=F_\mu^2-1,\qquad \Delta_\mu(x)=G_\mu(x)-x
=\mu\bigl[f(x)+f(x+\tfrac12+\mu f(x))\bigr].
\]
Its leading term, uniform in \(x\), is
\[
\Delta_\mu(x)/\mu=2a(1+\cos4\pi x)+O(|\mu|),
\]
which vanishes only at \(x_+=1/4\) and \(x_-=3/4\) modulo one, with quadratic contact. Put \(x=x_\pm+\delta\). Taylor's formula gives, uniformly as \((\delta,\mu)\to(0,0)\),
\[
\begin{aligned}
\frac{\Delta_\mu(x_++\delta)}\mu&=
16\pi^2a\delta^2+4\pi^2b(4a+b)\mu\delta
+2\pi^2b^2(4a+b)\mu^2+O((|\delta|+|\mu|)^3),\\
\frac{\Delta_\mu(x_-+\delta)}\mu&=
16\pi^2a\delta^2-4\pi^2b(4a-b)\mu\delta
+2\pi^2b^2(4a-b)\mu^2+O((|\delta|+|\mu|)^3).
\end{aligned}
\]
Call the homogeneous quadratic terms \(Q_+(\delta,\mu)\) and \(Q_-(\delta,\mu)\). The same completed-square discriminant occurs in both:
\[
4A C_\pm-B_\pm^2=16\pi^4 b^2(16a^2-b^2),\qquad A=16\pi^2a.
\]
If \(0<|b|<4a\), each quadratic form is positive definite. The cubic remainder and positivity away from the two contact points then yield some \(c>0\) such that, for small nonzero \(\mu\),
\[
\frac{\Delta_\mu(x)}\mu\ge c\bigl(\operatorname{dist}(x,\{x_+,x_-\}+\mathbb Z)^2+\mu^2\bigr)>0.
\]
Consequently \(G_\mu\) moves every point in the direction \(\operatorname{sgn}\mu\), and there is no two-cycle of \(F_\mu\).

For this case put \(T_\mu=\int_0^1|\Delta_\mu(u)|^{-1}\,du\). Because \(\|\Delta_\mu'\|_\infty=O(|\mu|)\), the integral along one \(G_\mu\)-step obeys
\[
\int_x^{G_\mu(x)}\frac{du}{|\Delta_\mu(u)|}
=\operatorname{sgn}(\mu)\bigl(1+O(|\mu|)\bigr)
\]
uniformly in \(x\). Indeed, for \(u\) between \(x\) and \(x+\Delta_\mu(x)\), the mean-value theorem gives \(|\Delta_\mu(u)/\Delta_\mu(x)-1|\le C|\mu|\). The increasing primitive of \(|\Delta_\mu|^{-1}\) has period increment \(T_\mu\); telescoping the preceding identity along orbits and using the bounded periodic part of this primitive shows
\[
\rho(G_\mu)=\frac{\operatorname{sgn}\mu}{T_\mu}\bigl(1+O(|\mu|)\bigr).
\]
At \(x=x_\pm+\mu s\) the local expansion is \(\Delta_\mu=\mu^3(Q_\pm(s,1)+o(1))\), uniformly for bounded \(s\). The displayed uniform positive lower bound controls rescaled tails by \(\int_{|s|>R}(s^2+1)^{-1}\,ds\); away from the zeros the contribution to \(\mu^2 T_\mu\) vanishes. Therefore
\[
\begin{aligned}
\lim_{\mu\to0}\mu^2 T_\mu
&=\sum_{\sigma\in\{+,-\}}\int_{\mathbb R}\frac{ds}{Q_\sigma(s,1)}\\
&=2\cdot\frac{2\pi}{\sqrt{16\pi^4b^2(16a^2-b^2)}}
=\frac1{\pi|b|\sqrt{16a^2-b^2}}.
\end{aligned}
\]
Since \(\rho(G_\mu)=2\rho(F_\mu)-1\), the quadratic two-sided sign law follows.

If \(|b|>4a\), one local constant coefficient \(Q_\pm(0,\mu)/\mu^2=2\pi^2b^2(4a\pm b)\) is negative, whereas \(\Delta_\mu/\mu\) is positive at, for example, \(x=0\) for small \(\mu\). Thus \(\Delta_\mu\) has a zero, so \(G_\mu\) has a fixed point and \(\rho(F_\mu)=1/2\). At \(b=0\), the orbit \(1/4\mapsto 3/4\mapsto5/4\) is exact. For \(b=4a\), direct substitution at \(x_-=3/4\) gives the **exact identity**
\[
\Delta_\mu(3/4)=-2a\mu[1-\cos(8\pi a\mu)]^2.
\]
Since \(\Delta_\mu(0)/\mu>0\) for small \(\mu\), continuity again gives a fixed point of \(G_\mu\). The case \(b=-4a\) is conjugate by translation \(x\mapsto x+1/2\). This proves locking at both endpoints. Finally, maximize \(|b|\sqrt{16a^2-b^2}\) by maximizing its square as a quadratic in \(b^2\).

## Verification
The standalone `verify.py` performs exact rational discriminant, threshold and coefficient identities, checks the endpoint algebra to floating-point accuracy at multiple parameters, tests the invariant symmetry under half-translation, and compares orbit-averaged rotations to the \(\mu|\mu|\) law for smaller parameters. These finite numerical observations are secondary; the proof above establishes the universal result. Run using `python3 verify.py` (Python standard library only).

## Relationship to prior work
Glendinning, *Scaling of the rotation number for perturbations of rational rotations* (2025), Theorem 1.3 and §6, equations (6.34)–(6.36), gives the first-order derivative for the two-harmonic half-turn when the mean coefficient strictly dominates its resonant coefficient; the example explicitly requires \(a>|c|\) and finds no dependence on the nonresonant first-harmonic coefficient at first order. This theorem treats the **excluded equality** \(c=a>0\), obtaining the sharp \(|b|=4a\) transition and second-order asymptotics. Boyland's *Pinched Arnol'd tongues for families of circle maps* gives generic pinching results for a different two-parameter family, without this equality-line coefficient. Parkhe's *One-parameter families of circle diffeomorphisms with strictly monotone rotation number* concerns monotonicity, not the displayed second-order law. Classical perturbative theory of circle maps is relevant background; no general novelty claim is made for its underlying techniques.

## Limitations
The parameter \(a\) is strictly positive; the statement is local in \(\mu\), requires fixed \(a,b\), and applies to this explicit family rather than general circle maps. At \(b\to0\) or \(|b|\to4a\), the asymptotic is not uniform in \(b\); indeed the locking/unlocking transition is singular. The asymptotics do not classify irrational versus rational rotation numbers at individual nonzero \(\mu\). An equivalent implicit statement in older Arnol'd-tongue perturbation literature remains a bibliographic risk; no independent mathematical review has been performed.

## References
- P. Glendinning, *Scaling of the rotation number for perturbations of rational rotations*, arXiv:2506.19508 (first public version 2025-06-24); especially Theorem 1.3 and §6, equations (6.34)–(6.36). https://arxiv.org/abs/2506.19508
- P. Boyland, *Pinched Arnol'd tongues for families of circle maps*, arXiv:2506.02988; especially introduction and Theorem 1.2. https://arxiv.org/abs/2506.02988
- K. Parkhe, *One-parameter families of circle diffeomorphisms with strictly monotone rotation number*, arXiv:1109.3214. https://arxiv.org/abs/1109.3214
