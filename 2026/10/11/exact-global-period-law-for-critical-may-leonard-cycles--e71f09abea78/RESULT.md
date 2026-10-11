# Exact global period law for critical May–Leonard cycles

## Finding
For the classical May–Leonard flow below, every positive nonconstant periodic orbit has a real product parameter \(0<p<1/27\). Its least period is
\[
T_\delta(p)=\frac{2\pi\sqrt3}{\delta}{}_2F_1\left(\frac13,\frac23;1;1-27p\right).
\]
The function \(p\mapsto T_\delta(p)\) is strictly decreasing and maps \((0,1/27)\) bijectively onto \((2\pi\sqrt3/\delta,\infty)\). In the nearly heteroclinic regime,
\[
T_\delta(p)=\frac3\delta\left(\log\frac1p+6p\left(\log\frac1p-\frac52\right)+O\left(p^2|\log p|\right)\right),\qquad p\downarrow0.
\]
The absence of an additive constant after the leading logarithm and the explicit first logarithmic correction are parts of the assertion.

## Assumptions and scope
Consider positive solutions of
\[
\begin{aligned}
\dot x&=x(1-x-\alpha y-\beta z),\\
\dot y&=y(1-\beta x-y-\alpha z),\\
\dot z&=z(1-\alpha x-\beta y-z),
\end{aligned}
\qquad \alpha=1-\delta,\quad \beta=1+\delta,\quad 0<\delta<1.
\]
Time is the unrescaled time in these equations; \(p\) means the product \(xyz\) **on** the invariant plane \(x+y+z=1\). The Gauss hypergeometric function is defined by its convergent Taylor series at zero. Only strictly positive, nonconstant periodic solutions are classified. The invariant equilibrium \((1/3,1/3,1/3)\), corresponding to \(p=1/27\), is not counted as a periodic orbit of positive least period.

## Proof
**1. Restriction to the simplex and complete orbit labeling.** Put \(s=x+y+z\). The cancellation \(\alpha+\beta=2\) gives \(\dot s=s(1-s)\). Thus every strictly positive periodic trajectory must lie in \(s=1\). Moreover
\[
\frac{d}{dt}\log\frac{xyz}{s^3}=0
\]
for every positive trajectory. On the simplex, \(p=xyz\) is conserved. By strict concavity of \(\log x+\log y+\log z\) on the positive simplex, for each \(0<p<1/27\) its level set is one smooth embedded circle enclosing the barycenter. The restricted vector field is
\[
\dot x=\delta x(y-z),\qquad
\dot y=\delta y(z-x),\qquad
\dot z=\delta z(x-y).
\]
It has no zeros on any regular circle because the only positive equilibrium is the barycenter. Therefore each level circle is one nonconstant periodic orbit, and there are no other positive periodic orbits.

**2. Quadrature and differential equation.** On \(s=1\), \(y+z=1-x\), \(yz=p/x\), hence
\[
\dot x^2=\delta^2 P(x,p),\qquad P(x,p)=x^2(1-x)^2-4px.
\]
The cubic equation \(x(1-x)^2=4p\) has three real positive roots \(0<r_1<1/3<r_2<1<r_3\) for \(0<p<1/27\). Therefore
\[
T_\delta(p)=\frac2\delta\int_{r_1}^{r_2}\frac{dx}{\sqrt{P(x,p)}}.
\]
On the nonsingular elliptic curve \(w^2=P(x,p)\), take \(\omega_p=dx/w\) and integrate around the real cycle surrounding the interval \([r_1,r_2]\). The following **exact rational differential identity** holds for \(P=x^2(1-x)^2-4px\) and
\(B=6x^5-15x^4+11x^3-(6p+2)x^2\):
\[
\left[p(1-27p)\partial_p^2+(1-54p)\partial_p-6\right]\omega_p
=d_x\left(\frac{B(x,p)}{P(x,p)^{3/2}}\right).
\]
Indeed this identity is equivalent, after multiplication by \(P^{5/2}\), to the polynomial equality
\[
12p(1-27p)x^2+2(1-54p)xP-6P^2=B_xP-\frac32 BP_x.
\]
Integrating the exact differential around the closed elliptic cycle yields
\[
p(1-27p)T_\delta''+(1-54p)T_\delta'-6T_\delta=0.
\]
The derivative under the moving-cycle integral is justified by transporting the homology cycle through smooth nonsingular fibers; the right side is a globally exact meromorphic differential. In \(u=1-27p\), this is the Gauss equation
\[
u(1-u)f''+(1-2u)f'-\frac29 f=0.
\]

**3. Selection and normalization of the real period.** As \(p\uparrow1/27\), \(r_1,r_2\to1/3\) and \(r_3\to4/3\). Set \(x=r_1+(r_2-r_1)\sin^2\theta\). Factoring \(P=x(x-r_1)(r_2-x)(r_3-x)\) gives
\[
T_\delta(p)=\frac4\delta\int_0^{\pi/2}\frac{d\theta}{\sqrt{x(\theta)[r_3-x(\theta)]}},
\quad x(\theta)=r_1+(r_2-r_1)\sin^2\theta.
\]
Thus \(T_\delta\to2\pi\sqrt3/\delta\). The coalescing-root quadrature is analytic in \(u\) near zero: in centered coordinates, the root separation is an analytic odd function of \(\sqrt{u}\) and the integral is invariant under exchange of the two merging roots, so only even powers occur. The regular singular Gauss equation has a unique solution analytic at \(u=0\) with prescribed constant term, namely \({}_2F_1(1/3,2/3;1;u)\). This proves the exact period formula for the full interval \(0<u<1\) by analytic continuation along the real interval.

**4. Global monotonicity and endpoint expansion.** Every coefficient of the hypergeometric series at \(u=0\) after the constant term is strictly positive:
\[
{}_2F_1\left(\frac13,\frac23;1;u\right)
=\sum_{n=0}^\infty\frac{(1/3)_n(2/3)_n}{(n!)^2}u^n.
\]
Consequently \(dT_\delta/dp<0\) on the entire open interval. The zero-balanced hypergeometric continuation at \(u=1-z\) has the expansion
\[
{}_2F_1\left(\frac13,\frac23;1;1-z\right)
=\frac{\sqrt3}{2\pi}\left[
\log\frac{27}{z}+\frac{2z}{9}\left(\log\frac{27}{z}-\frac52\right)
+O(z^2|\log z|)\right].
\]
Substituting \(z=27p\) gives the asserted asymptotic, including its exact constant term. The opposite endpoint limit is already determined in step 3, so the strict range follows.

## Verification
The standalone `verify.py` recomputes the conserved ratio and the polynomial differential identity symbolically, evaluates the real period integral using a nonsingular fixed-interval substitution at four product levels, and compares it with the hypergeometric formula at 65-digit precision. It also tests positive hypergeometric coefficients and the first two logarithmic terms numerically. Run `python verify.py` with SymPy and mpmath installed; its final line is `CHECKS_PASS`. The infinite-interval and all-parameter statements are proved above, not inferred from numerical samples.

## Relationship to prior work
May and Leonard's founding 1975 paper derives the critical neutral cycles using total population and triple product, but does not supply the physical-time hypergeometric period or strict global monotonicity. Leach and Miritzis (2006) study integrability and symmetry for the same equations, while Chi, Hsu, and Wu (1998) characterize neutrally stable cycles in a broader asymmetric class; neither inspected text establishes this exact real-time period law. The 2016 preprint of Zhou gives a related hypergeometric Picard–Fuchs system for the Hesse family of plane cubics, an important general elliptic-period antecedent. The present proof identifies the dynamical time differential, real cycle, exact product normalization, strict monotonicity, and corner asymptotics for the May–Leonard flow; the elliptic Picard–Fuchs methodology itself is not claimed new.

## Limitations
The classification is restricted to \(0<\delta<1\), \(\alpha+\beta=2\), and strictly positive trajectories. It does not describe periods in asymmetric perturbations or noncritical parameter regimes, nor does it assert hyperbolic stability of the neutral cycles. Historical priority with respect to all earlier special-function treatments is not conclusively established: the complete Phillipson–Schuster–Johnston (1985) text could not be inspected, and related elliptic-period formulas may admit alternative dynamical interpretations.

## References
- R. M. May and W. J. Leonard, *Nonlinear Aspects of Competition Between Three Species*, SIAM Journal on Applied Mathematics 29 (1975), 243–253, DOI: 10.1137/0129022.
- C.-W. Chi, S.-B. Hsu, and L.-I. Wu, *On the Asymmetric May–Leonard Model of Three Competing Species*, SIAM Journal on Applied Mathematics 58 (1998), 211–226, https://www.math.nthu.edu.tw/~sbhsu/May-Leonard.pdf.
- P. G. L. Leach and J. Miritzis, *Analytic Behaviour of Competition among Three Species*, Journal of Nonlinear Mathematical Physics 13 (2006), 535–548, DOI: 10.2991/jnmp.2006.13.4.8; arXiv:q-bio/0609010.
- P. E. Phillipson, P. Schuster, and R. G. Johnston, *An Analytic Study of the May–Leonard Equations*, SIAM Journal on Applied Mathematics 45 (1985), 541–554, DOI: 10.1137/0145032 (full-text comparison incomplete).
- J. Zhou, *GKZ Hypergeometric Series for the Hesse Pencil, Chain Integrals and Orbifold Singularities*, arXiv:1606.08352, particularly the Picard–Fuchs operator in Section 1.
