# Moment-order buckling and oscillatory finite-size thresholds for telegraph-modulated surfaces

## Finding

Consider a linearly elastic height field with positive mean tension and bending rigidity, driven by **spatially uniform, symmetric, two-state tension fluctuations**. Although each nonzero Fourier mode decays exponentially along almost every realization, its ensemble moments have a sharp *order-dependent* transition. The transition is completely classified by an explicit cubic and affects exactly one bounded continuum band of squared wave numbers. On a finite periodic surface, mode quantization creates an exact minimal system size, a singular onset at that size, and an oscillatory quadratic finite-size shift of the moment-order threshold.

Write \(x=|k|^2>0\), let \(p>0\) be the real moment order, and let \(\sigma,\kappa,r>0\) and \(a\ge0\). The exact long-time \(p\)-moment growth exponent is
\[
\Lambda_p(x)=-p(\sigma x+\kappa x^2)-r+\sqrt{r^2+p^2a^2x^2}.
\]
Define
\[
H_p(x)=(\sigma+\kappa x)^2+\frac{2r(\sigma+\kappa x)}{p x}.
\]
For each fixed \(p>0\), there is a unique \(x_p>0\) satisfying
\[
\kappa x_p^2(\sigma+\kappa x_p)=\frac{r\sigma}{p}.
\]
Set \(a_{c,p}=\sqrt{H_p(x_p)}>\sigma\). If \(a<a_{c,p}\), all nonzero modes have negative \(p\)-moment exponents. If \(a=a_{c,p}\), exactly one nonzero squared wave number \(x_p\) has exponent zero. If \(a>a_{c,p}\), the positive exponents occur **exactly** for \(x\in(x_-,x_+)\), where \(0<x_-<x_p<x_+<\infty\) are the two positive solutions of \(H_p(x)=a^2\).

Equivalently, fixing the active tension amplitude instead, there is a **single sharp moment-order threshold**. If \(a\le\sigma\), no positive real moment order has any unstable mode. If \(a>\sigma\), let \(u_*\in(\sigma,a)\) be the unique solution of
\[
2u_*^3-\sigma u_*^2-\sigma a^2=0
\]
and put
\[
p_c=\frac{2r\kappa u_*}{(u_*-\sigma)(a^2-u_*^2)},
\qquad x_* = \frac{u_*-\sigma}{\kappa}.
\]
For \(0<p<p_c\), all nonzero modes have negative exponents; at \(p=p_c\), exactly the mode \(x=x_*\) is neutral; and at \(p>p_c\), exactly one bounded band has positive \(p\)-moment exponent. In the weak-overdrive limit,
\[
p_c\sim\frac{4r\kappa}{(a-\sigma)^2}\qquad(a\downarrow\sigma).
\]
Thus any arbitrarily small excess of fluctuating tension above the mean eventually destabilizes sufficiently high moments, but the critical moment order diverges quadratically as the excess vanishes. At the same time the sample-path growth exponent remains strictly negative for every fixed nonzero Fourier mode.

**Finite-size conclusion.** On a one-dimensional periodic domain of circumference \(L>0\), define
\[
L_0=2\pi\sqrt{\frac{\kappa}{a-\sigma}}\quad(a>\sigma),
\qquad k_*=\sqrt{x_*}.
\]
If \(a\le\sigma\) or \(0<L\le L_0\), no positive moment order can grow at any nonzero allowed Fourier mode. For \(a>\sigma\) and \(L>L_0\), the finite-system critical order is
\[
p_c(L)=\min_{n\ge1:\ \sigma+\kappa(2\pi n/L)^2<a}
\frac{2r[\sigma+\kappa(2\pi n/L)^2]}
{(2\pi n/L)^2\{a^2-[\sigma+\kappa(2\pi n/L)^2]^2\}}.
\]
The set minimized over is nonempty and finite. At equality a listed mode is neutral; at larger orders at least one mode has positive growth. Two sharp boundary laws hold:
\[
\lim_{L\downarrow L_0}(L-L_0)p_c(L)
=\frac{r\kappa L_0}{2(a-\sigma)^2},
\]
\[
p_c(L)=p_c+\frac{2\pi^2\Phi''(k_*)}{L^2}
\operatorname{dist}\left(\frac{Lk_*}{2\pi},\mathbb Z\right)^2+O(L^{-3}),
\qquad L\to\infty,
\]
where \(\Phi(k)=\frac{2r(\sigma+\kappa k^2)}{k^2[a^2-(\sigma+\kappa k^2)^2]}\) on \(0<k<\sqrt{(a-\sigma)/\kappa}\), and \(\Phi''(k_*)>0\). The remainder is uniform in real \(L\) tending to infinity. This supplies an exact physical-size threshold as well as a mode-quantization correction with a nonconvergent rescaled phase: \(\liminf_{L\to\infty}L^2[p_c(L)-p_c]=0\), while \(\limsup_{L\to\infty}L^2[p_c(L)-p_c]=\pi^2\Phi''(k_*)/2\).

## Assumptions and scope

The linear height equation is
\[
\partial_t h=(\sigma+a S_t)\Delta h-\kappa\Delta^2 h.
\]
Here \(S_t\in\{-1,+1\}\) is a continuous-time Markov chain with symmetric flip rate \(r>0\), initially in its stationary distribution \(\mathbb P(S_0=\pm1)=1/2\). The noise is *spatially uniform*: the same \(S_t\) multiplies every Fourier mode, and its sample paths are piecewise constant. The elastic equation is linear, and drag has been normalized to one by rescaling time. For a nonzero Fourier mode with deterministic initial coefficient \(\widehat h_k(0)\ne0\), the moment of interest is \(\mathbb E|\widehat h_k(t)|^p\) for any real \(p>0\). The continuum dispersion classification takes place over all real \(x=|k|^2>0\). For the additional finite-size theorem, specialize to a one-dimensional torus of circumference \(L\), whose nonzero wave numbers are \(k_n=2\pi n/L\) for nonzero integers \(n\). On a fixed torus, instability occurs only for the permitted discrete modes; a sufficiently small domain can exclude every unstable mode at every finite moment order.

The claim does not cover spatially varying tension, nonlinear surface mechanics, additive noise, asymmetric switching, or a noise distribution with unbounded support. The neutral \(k=0\) mode is excluded throughout.

## Proof

**1. Sample paths and almost-sure stability.** Spatial uniformity diagonalizes the equation in Fourier space. With \(x=|k|^2\) and \(A(x)=\sigma x+\kappa x^2\),
\[
\widehat h_k(t)=\widehat h_k(0)\exp\left[-A(x)t-a x\int_0^t S_s\,ds\right].
\]
The symmetric two-state chain is irreducible and ergodic, hence \(t^{-1}\int_0^tS_s\,ds\to0\) almost surely. Therefore
\[
\lim_{t\to\infty}\frac1t\log\frac{|\widehat h_k(t)|}{|\widehat h_k(0)|}=-A(x)<0
\]
for every fixed nonzero mode. Because the random integral is common to every wave number, the same probability-one event gives the limit simultaneously for all real \(x>0\), for modes with nonzero initial coefficient.

**2. Exact finite-time moment.** Let \(Y_t=\int_0^t S_s\,ds\). The usual two-state finite-state Feynman--Kac system for \(\mathbb E e^{-paxY_t}\) has tilted matrix
\[
B=\begin{pmatrix}-r-pax&r\\r&-r+pax\end{pmatrix},
\quad B+rI\text{ has square }(r^2+p^2a^2x^2)I.
\]
Write \(\Omega=\sqrt{r^2+p^2a^2x^2}>0\). Exponentiating the matrix with the stationary initial distribution gives, for every \(t\ge0\),
\[
\frac{\mathbb E|\widehat h_k(t)|^p}{|\widehat h_k(0)|^p}
=e^{-pA(x)t-rt}\left[\cosh(\Omega t)+\frac r\Omega\sinh(\Omega t)\right].
\]
The leading coefficient \((1+r/\Omega)/2\) is strictly positive. Its exponential rate is precisely the claimed \(\Lambda_p(x)\); this argument is valid for all real \(p>0\), including noninteger orders.

**3. Strictly convex amplitude frontier.** Since \(pA(x)+r>0\), squaring the inequality \(\sqrt{r^2+p^2a^2x^2}>r+pA(x)\) is reversible. Dividing by \(p^2x^2\) yields
\[
\Lambda_p(x)>0\iff
 a^2>\left(\sigma+\kappa x\right)^2+\frac{2r}{p}\left(\frac\sigma x+\kappa\right)=H_p(x).
\]
The derivatives satisfy
\[
H_p'(x)=2\kappa(\sigma+\kappa x)-\frac{2r\sigma}{p x^2},\qquad
H_p''(x)=2\kappa^2+\frac{4r\sigma}{p x^3}>0.
\]
Also \(H_p(x)\to+\infty\) at both endpoints \(x\downarrow0\) and \(x\to\infty\). Therefore it has a unique positive minimizer given by the stated cubic equation, and its strict sublevel sets are exactly either empty or a single bounded interval. Since \(H_p(x)>\sigma^2\) for each \(x>0\), \(a_{c,p}>\sigma\). The double-root and two-crossing cases follow by strict convexity.

**4. Strictly ordered moment frontier and its cubic.** For \(a\le\sigma\), the preceding strict inequality rules out positive growth at every order. For \(a>\sigma\), the condition \(a^2>H_p(x)\) requires \(u=\sigma+\kappa x\in(\sigma,a)\) and is equivalent to
\[
p>\phi(u):=\frac{2r\kappa u}{(u-\sigma)(a^2-u^2)}.
\]
The function \(\phi\) tends to infinity at each endpoint. Its logarithmic derivative vanishes exactly when
\[
\frac1u-\frac1{u-\sigma}+\frac{2u}{a^2-u^2}=0
\iff 2u^3-\sigma u^2-\sigma a^2=0.
\]
The cubic is strictly increasing for \(u>\sigma\), because its derivative is \(2u(3u-\sigma)>0\). Its values at the endpoints are negative and positive, respectively: at \(u=\sigma\) it is \(\sigma(\sigma^2-a^2)<0\), and at \(u=a\) it is \(2a^2(a-\sigma)>0\). Consequently it has one and only one root \(u_*\in(\sigma,a)\), which is the unique minimizer of \(\phi\). Taking the strict inequality \(p>\min\phi=p_c\) proves the asserted complete order classification, including uniqueness of the neutral squared wave number at equality.

**5. Sharp weak-overdrive scale.** Put \(a=\sigma+\varepsilon\) with \(\varepsilon\downarrow0\), and let \(u_*(\varepsilon)\) be the cubic root. Implicit differentiation at \((u,a)=(\sigma,\sigma)\) gives \(du_*/da=1/2\); thus \(u_*=\sigma+\varepsilon/2+O(\varepsilon^2)\). The numerator of \(p_c\) is \(2r\kappa\sigma(1+O(\varepsilon))\) and its denominator is \(\sigma\varepsilon^2/2\,(1+O(\varepsilon))\). Hence \(p_c=4r\kappa\varepsilon^{-2}(1+O(\varepsilon))\), establishing the sharp coefficient.

**6. First- versus second-moment separation.** For fixed \(x>0\), \(H_p(x)\) decreases strictly as \(p\) increases. Consequently \(a_{c,2}<a_{c,1}\). Every choice \(a\in(a_{c,2},a_{c,1})\) gives exponential decay of the first absolute moment at every nonzero wave number but exponential growth of the second moment for a nonempty finite band. This is an ensemble intermittency statement and does not contradict sample-path decay.


**7. Finite-size existence and singular onset.** On the circle, the allowed positive squared wave numbers are \(x_n=(2\pi n/L)^2\), \(n=1,2,\ldots\). A positive growth exponent at any order requires \(a>\sigma+\kappa x_n\), since \(H_p(x_n)>\left(\sigma+\kappa x_n\right)^2\). Such a mode exists exactly when \(a>\sigma\) and \(x_1<(a-\sigma)/\kappa\), or \(L>L_0\). For each eligible \(n\), step 4 gives the necessary and sufficient order inequality \(p>\Phi(k_n)\). There are finitely many eligible \(n\), proving the asserted finite-minimum formula, equality case and strict threshold.

For \(L_0<L<2L_0\), only the first positive wave number is eligible. With \(\varepsilon=L-L_0\downarrow0\),
\[
\sigma+\kappa(2\pi/L)^2
=a-\frac{2(a-\sigma)}{L_0}\varepsilon+O(\varepsilon^2).
\]
Substitution into the rational expression defining \(p_c(L)\) gives
\[
p_c(L)=\frac{r\kappa L_0}{2(a-\sigma)^2}\varepsilon^{-1}+O(1),
\]
including the positive constant and the strict-endpoint behavior.

**8. Uniform oscillatory finite-size law.** The function \(\Phi(k)\) is smooth and proper on its eligible positive interval. The unique global minimizer is \(k_*\), since its logarithmic derivative vanishes exactly at the unique root \(u_*\) in step 4. Its second derivative is strictly positive: with \(u=\sigma+\kappa k^2\) and \(G(u)=\log\{u/[(u-\sigma)(a^2-u^2)]\}\), one has
\[
G''(u)=-\frac1{u^2}+\frac1{(u-\sigma)^2}+
\frac{2(a^2+u^2)}{(a^2-u^2)^2}>0,
\]
so at the critical point,
\[
\Phi''(k_*)=p_c(2\kappa k_*)^2G''(u_*)>0.
\]
Let \(h=2\pi/L\). Among the lattice points \(nh\), the closest one to \(k_*\) is at distance \(h\operatorname{dist}(k_*/h,\mathbb Z)\). Properness and strict positivity of \(\Phi''(k_*)\) force every minimizing lattice point into an \(O(h)\) neighborhood of \(k_*\); the minimum of its quadratic Taylor term differs from that at the closest lattice point by at most \(O(h^3)\), uniformly even when two grid points nearly tie. Taylor's formula then gives
\[
p_c(L)-p_c=\frac12\Phi''(k_*)h^2\operatorname{dist}(k_*/h,\mathbb Z)^2+O(h^3),
\]
as claimed. Choosing \(L=2\pi n/k_*\) gives exact resonance \(p_c(L)=p_c\), whereas choosing \(L=2\pi(n+1/2)/k_*\) yields the largest asymptotic quadratic correction. Both sequences diverge, proving the liminf and limsup assertions.

## Verification

The accompanying standard-library `verify.py` independently evaluates the amplitude frontier, the order-frontier cubic, the exact telegraph moment against a two-state fourth-order Runge--Kutta evolution, weak-overdrive scaling, the finite-size onset pole, and the lattice-quantization asymptotic. Reproduce with `python3 verify.py` from the directory containing this document. The tested implementation uses deterministic parameter samples; no random seed or external software service is needed beyond Python's standard library. A successful run prints `PASS 2979 deterministic assertions` and critical values for a reproducible reference parameter set.

For \(\sigma=1\), \(\kappa=1/2\), \(r=0.7\), the first-moment amplitude threshold is approximately \(2.0853111900\), while the second-moment threshold is approximately \(1.7809579460\). Choosing \(a=1.9\) therefore produces an unstable second-moment interval approximately \(0.37951017<|k|^2<1.29922165\), with the first moment still decaying at all nonzero wave numbers. These finite evaluations test the analytic formulae but do not substitute for the proof above.

## Relationship to prior work

Ciarchi, Goychuk and Frey (2026) introduced and analyzed buckling of active surfaces driven by spatially *varying*, time-correlated Gaussian tension fluctuations. Their analysis yields a finite-band ensemble instability with Novikov--Furutsu closure and numerical validation. The present model is an explicitly different **spatially uniform binary-tension** specialization of the underlying elastic operator; the all-positive-real-moment order transition and its sharp cubic boundary are not asserted to follow from their spatially correlated closure. Crucially, the present finite-band instability requires rare intervals of *negative instantaneous tension* when \(a>\sigma\), whereas their mechanism is not claimed to have that property. Neither mechanism is equated to the other.

Classical telegraph-process theory, particularly the occupation-time and Feynman--Kac analysis of Bogachev and Ratanov (2010), supplies the integrated-switching-process framework and general tilted-generator method. More directly, Falkovich and Martins Afonso (2007) calculate the complete moment-growth spectrum of a one-dimensional telegraph-driven multiplicative scalar equation and its (typically negative) Lyapunov exponent. Their formula covers the **single-mode telegraph moment exponent** by parameter substitution and deterministic relaxation shift, so neither that exponent nor the separation of quenched and annealed growth is claimed as new. The candidate new mathematical statement is the joint *all-moment, all-wavenumber and finite-size* phase classification for the elastic operator, with a cubic critical order, quadratic near-threshold law, sharp finite-size cutoff and oscillatory lattice correction. Those prior exact moment formulas are essential inputs; the independent assessed mathematical contribution is the global optimization over the nonlinear bending-dependent continuum dispersion and the sharp finite-size lattice-quantization, system-size cutoff and oscillation laws. Independent priority assessment should determine whether comparable explicit elastic-interface classifications have been given.

## Limitations

This theorem concerns deterministic initial Fourier coefficients under a *global* two-state Markov modulation. Its instability is a growth of ensemble moments, **not** a claim that typical Fourier amplitudes grow; in fact the latter decay almost surely. The active tension must occasionally reverse sign for any moment-order instability. The analysis is linear and cannot predict nonlinear buckled morphology, saturation or finite-size mode availability. On a fixed finite torus, only the actual lattice wave numbers are relevant, and a narrow continuum band can contain no permitted modes. No result is asserted for the spatially correlated Gaussian noise field in the motivating paper, or for nonstationary time-dependent switching laws. Publication-level originality remains subject to external review.

## References

1. M. Ciarchi, A. Goychuk and E. Frey, *Active fluctuations induce buckling of living surfaces*, arXiv:2602.24272, first public version 2026-02-27, https://arxiv.org/abs/2602.24272 . Primary full text (including model and analytic discussion) consulted.
2. G. Falkovich and M. Martins Afonso, *Fluid-particle separation in a random flow described by the telegraph model*, arXiv:nlin/0703054, first public version 2007-03-28, https://arxiv.org/abs/nlin/0703054 . Section II, especially moment-growth equations (7)–(13), consulted as the strongest single-mode scalar precedent.
3. L. Bogachev and N. Ratanov, *Occupation time distributions for the telegraph process*, arXiv:1007.3139, first public version 2010-07-19, https://arxiv.org/abs/1007.3139 . Sections 1, 3 and 4 consulted for telegraph occupation-time and finite-state Feynman--Kac precedent.
