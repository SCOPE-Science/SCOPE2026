# Exact Green-function tail at the double-logarithmic critical rate for adaptive Brownian resetting

## Finding

Let Brownian motion on \(\mathbb R^d\), \(d\ge1\), have generator \(D\Delta\), \(D>0\). It resets instantaneously to the origin at continuous positive radial rate \(\kappa(r)\). Let \(G\) be the unnormalized occupation density for the trajectory started at the origin and stopped at its first reset. Suppose, for real \(b,c\), that
\[
\kappa(r)=\frac D{r^2}\left(2d+\frac b{\log r}+\frac c{\log r\,\log\log r}+O((\log r)^{-2})\right),\qquad r\to\infty.
\]
Write \(\beta=b/(d+2)\), \(\gamma=c/(d+2)\). Then there exists \(C\in(0,\infty)\) such that the *density per unit volume* satisfies
\[
G(r)=C r^{-d}(\log r)^{-\beta}(\log\log r)^{-\gamma}\bigl(1+O((\log r)^{-1})\bigr).
\]
In particular, the ratio to the displayed power and logarithms tends to a strictly positive finite constant, including when no stationary probability exists. Only a bound on the coefficient remainder is needed; its derivative is not used.

As consequences, the unique stationary law exists exactly when \(\beta>1\) or \(\beta=1,\gamma>1\), and has density \(G/M\) where \(M=\int_{\mathbb R^d}G(x)\,dx\). In these two regimes respectively, its precise tail mass is
\[
\mathbb P_*(|X|>R)\sim \frac{|\mathbb S^{d-1}|C}{M}
\begin{cases}
\dfrac{(\log R)^{1-\beta}(\log\log R)^{-\gamma}}{\beta-1},&\beta>1,\\[4pt]
\dfrac{(\log\log R)^{1-\gamma}}{\gamma-1},&\beta=1,\ \gamma>1.
\end{cases}
\]
The exact occupation-density equivalent is the contribution of this result; the stationarity thresholds are stated for context and are not asserted to be new.

## Assumptions and scope

Along a Brownian excursion \(B\), the conditional survival to time \(s\) is \(\exp(-\int_0^s\kappa(|B_v|)\,dv)\). Brownian paths and exponential clocks are renewed after each reset. The asymptotic hypothesis applies beyond a fixed radius. Continuity, positivity, and the stated asymptotics imply global boundedness, so reset times cannot accumulate in finite time. There is no differentiability requirement on the rate, uniformity in the parameters, or assertion about anisotropic rates or mixing.

## Proof

**1. The physical Green equation and killing mass.** For \(A_s=\int_0^s\kappa(|B_v|)\,dv\), the killed occupation measure is defined by integrating \(\mathbb E_0[e^{-A_s}\mathbf 1_{\{B_s\in dx\}}]\) over time. It is absolutely continuous since each killed transition is dominated by Brownian transition measure. Tonelli's theorem gives
\[
\int\kappa(|x|)G(x)\,dx=\mathbb E_0\int_0^\infty\kappa(|B_s|)e^{-A_s}\,ds=1-\mathbb E_0[e^{-A_\infty}]\le1.
\]
On compact sets \(\kappa\) has a positive minimum, so \(G\) is locally integrable. For any smooth compactly supported test function \(\phi\), apply the product rule to \(e^{-A_s}\phi(B_s)\), take expectations and integrate in time. The terminal expectation tends to zero by domination by \(\mathbb E_0|\phi(B_s)|=O(s^{-d/2})\). This proves \((-D\Delta+\kappa)G=\delta_0\) in distributions. Spherical symmetry gives a radial solution; on any annulus the equation \((r^{d-1}G')'=(\kappa/D)r^{d-1}G\) gives a \(C^2\) representative by integrating the locally integrable right-hand side and then using continuity. It is strictly positive there: on any finite time interval, the killed transitions dominate the free transitions multiplied by \(e^{-s\sup\kappa}>0\).

**2. The slow asymptotic solution.** Set \(z=\log r\), \(a=d+2\), and \(G(r)=r^{-d}h(z)\). Direct differentiation gives
\[
r^{d+2}\bigl(G''+(d-1)G'/r\bigr)=h''-a h'+2dh.
\]
Thus for large \(z\) the equation is \(h''-a h'-q(z)h=0\), where \(q(z)=b/z+c/(z\log z)+O(z^{-2})\). With \(g(z)=z^{-\beta}(\log z)^{-\gamma}\), set \(h=gu\). Then
\[
u''-A(z)u'+f(z)u=0,\qquad A=a-2g'/g,\qquad f=g''/g-a g'/g-q.
\]
Here \(g'/g=-\beta/z-\gamma/(z\log z)\), so \(f=O(z^{-2})\) and \(A=a+O(z^{-1})\). In particular \(A>a/2\) for sufficiently large \(z_0\). On bounded continuous functions on \([z_0,\infty)\), use the equation
\[
u(z)=1-\int_z^\infty\int_s^\infty e^{-\int_s^t A(w)\,dw}\,f(t)u(t)\,dt\,ds.
\]
The norm of the integral operator is at most \((2/a)\int_{z_0}^{\infty}|f(t)|dt=O(z_0^{-1})\). For large \(z_0\) the contraction theorem gives a bounded solution. The same estimate with lower limit \(z\) gives \(u(z)=1+O(z^{-1})\), and differentiating once gives \(u'(z)=O(z^{-2})\) by the exponential kernel bound. The second derivative gives the ODE, with no derivative of \(f\). Thus \(h_s=gu\) is positive on a tail and \(h_s'/h_s=O(z^{-1})\).

**3. The occupation density selects this solution.** An independent solution is \(h_s(z)\int_{z_0}^z e^{at}h_s(t)^{-2}\,dt\), starting sufficiently far out that \(h_s>0\). Since the logarithmic derivative of the integrand tends to \(a\), the integral is asymptotic to \(a^{-1}e^{az}h_s(z)^{-2}\), by l'Hôpital's rule. The corresponding radial branch is asymptotic to \(a^{-1}r^2(\log r)^\beta(\log\log r)^\gamma\). A negative coefficient of this branch would make the density eventually negative. A positive coefficient would give \(\int\kappa G\,dx=\infty\) since \(\kappa(r)\sim 2dD/r^2\), contradicting step 1. Therefore the positive physical density is a strictly positive multiple of the slow branch on the tail, proving the claimed equivalent and relative error.

**4. Stationary consequences.** In the Green equation use a smooth cutoff equal to one in \(|x|\le R\) and zero in \(|x|\ge2R\), with Laplacian bounded by a constant times \(R^{-2}\). The term testing \(G\) against the Laplacian tends to zero by the tail estimate on that annulus. Dominated convergence for the \(\kappa G\) term now gives \(\int\kappa G\,dx=1\), hence an almost surely finite first reset. The mean cycle length is \(M\). Local integrability and the substitution \(z=\log r\) reduce finiteness of \(M\) to the integral of \(z^{-\beta}(\log z)^{-\gamma}\) at infinity. It converges exactly in the stated regimes; the integrals from \(\log R\) to infinity have the two displayed equivalents (by the integral test and l'Hôpital's rule in the first regime, and an exact substitution in the second). Positivity and ratio convergence allow integration of the density equivalent in each convergent case.

For finite \(M\), the regenerative occupation formula gives the invariant probability \(G/M\). For necessity and uniqueness, let \(P_t^\kappa\) be the killed transition semigroup and let \(\mu\) be any invariant probability for the reset process. The reset generator is the killed generator plus the bounded operator \(f\mapsto\kappa(\cdot)f(0)\). Variation of constants and invariance give, for any smooth compactly supported \(\phi\),
\[
\int\phi\,d\mu=\mu P_t^\kappa\phi+\left(\int\kappa\,d\mu\right)\int_0^t P_s^\kappa\phi(0)\,ds.
\]
The first term tends to zero by the uniform all-starting-points Gaussian bound \(\|P_t^\kappa\phi\|_\infty\le(4\pi Dt)^{-d/2}\|\phi\|_1\). Thus \(\mu\) is a positive multiple of \(G(x)dx\), which is impossible for infinite \(M\) and forces \(\mu=G(x)dx/M\) otherwise.

## Verification

The proof uses exact radial conjugation and an explicit tail contraction of norm \(O(1/z_0)\). The accompanying `verify.py` checks the radial derivative identities and cancellation of the two leading terms in representative dimensions. It does not test the infinite-domain asymptotics, branch selection, or stationary equivalence; these follow from the proof.

## Relationship to prior work

Keidar and Reuveni [1] derive the leading inverse-square resetting boundary using power-law tails. A prior one-dimensional analysis [2] explicitly gives the thresholds at coefficients \(3\) and \(3\) in the first and second logarithmic corrections, with the corresponding nonintegrable equality cases and logarithmic limits of the stationary tails. It uses comparison exponents rather than giving a finite nonzero limit of the density ratio to its proposed profile. The threshold portion also transfers at the level of the radial ODE: in step 2 the change \(s=az/3\) sends the drift coefficient to \(3\), the first and second log coefficients to \(3b/a\) and \(3c/a\), and \(\int h(z)dz\) to a constant multiple of the transformed integral. Away from \(b=a\), the first-order comparison exponents suffice; at \(b=a\) the induced error is \(O(1/[s(\log s)^2])\), within the prior second-boundary comparison. The distinction here is the exact Green equivalent in all dimensions, including its positive amplitude and the resulting equivalent, rather than only logarithmic order, of a finite stationary tail. The contraction argument is a direct application of standard asymptotic-ODE ideas after the logarithmic conjugation. The inverse-square Schrödinger asymptotics of Ishige, Kabeya and Ouhabaz [3] assume power-rate control of the coefficient error, not the two slow corrections treated here. Pinsky [4] uses related positive-solution methods for first-passage times under resetting.

## Limitations

The amplitude \(C\) depends on the full hazard and is not evaluated here. The theorem assumes the stated controlled remainder; an unspecified smaller-order term than \(1/(\log r\,\log\log r)\) can decide integrability at the double equality. No historical priority beyond the compared sources is asserted.

## References

1. O. Keidar and S. Reuveni, *Localization–Delocalization Transition in Diffusion with Adaptive Resetting*, arXiv:2608.27090, especially equations (14)–(15).
2. [*Nested logarithmic localization thresholds for critically adaptive Brownian resetting*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-nested-logarithmic-localization-thresholds-for-critically-adapti--06919c67c871/RESULT.md), 18 October 2026, Finding and proof steps 2–5.
3. K. Ishige, Y. Kabeya and E. M. Ouhabaz, *The heat kernel of a Schrödinger operator with inverse square potential*, arXiv:1602.04172, assumption (1.2) and Theorem 1.1.
4. R. G. Pinsky, *Diffusive Search with Spatially Dependent Resetting*, arXiv:1805.00320, Theorem 3.
