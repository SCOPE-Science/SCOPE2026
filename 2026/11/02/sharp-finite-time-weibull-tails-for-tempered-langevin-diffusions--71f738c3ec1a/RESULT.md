# Sharp finite-time Weibull tails for tempered Langevin diffusions

## Finding
Let \(X\) be the tempered Langevin diffusion defined below with a polynomially decaying target and any subcritical temperature. For every fixed starting point \(x\) and time \(t>0\), its one-time radial tail has the exact logarithmic asymptotic
\[
\lim_{R\to\infty}\frac{\log\mathbb P_x(\lVert X_t\rVert>R)}{R^{2a}}
=-\frac{c_\pi^{2\ell}}{4a^2t},\qquad a=1-\ell(d+r)>0.
\]
Consequently the critical exponential-moment coefficient is \(\kappa_t=c_\pi^{2\ell}/(4a^2t)\): for every \(\theta\ge0\),
\[
\mathbb E_x\exp\big(\theta\lVert X_t\rVert^{2a}\big)
\begin{cases}<\infty,&0\le\theta<\kappa_t,\\=\infty,&\theta>\kappa_t.\end{cases}
\]
The behavior at equality \(\theta=\kappa_t\) is not asserted. In particular the expectation with unit coefficient is finite for \(t<c_\pi^{2\ell}/(4a^2)\) and infinite for \(t>c_\pi^{2\ell}/(4a^2)\). This determines the precise time separating the two strict regimes previously bounded by nonmatching constants.

## Assumptions and scope
Fix an integer \(d\ge1\), a real \(r>0\), and a strictly positive \(C^2\) function \(\pi:\mathbb R^d\to(0,\infty)\) with locally Hölder-continuous second derivatives. Suppose uniformly in direction as \(\lVert y\rVert\to\infty\) that
\[
\lVert y\rVert^{d+r}\pi(y)\to c_\pi\in(0,\infty),\qquad
\langle y,\nabla\log\pi(y)\rangle\to-(d+r).
\]
For \(0\le\ell<1/(d+r)\), start at any deterministic \(X_0=x\in\mathbb R^d\) the nonexplosive Itô diffusion
\[
 dX_t=(1-2\ell)\pi(X_t)^{-2\ell}\nabla\log\pi(X_t)\,dt
 +\sqrt2\,\pi(X_t)^{-\ell}\,dB_t.
\]
Here \(B\) is standard \(d\)-dimensional Brownian motion, and \(\pi\) is the actual coefficient function, not a normalization-free probability density: multiplying \(\pi\) by a constant changes time at \(\ell>0\). The parameter \(c_\pi\) records that convention. Nonexplosion in this parameter regime follows also from the bounded martingale coefficients constructed in the proof.

## Proof
**Radial clock.** Write \(q=d+r\), \(a=1-\ell q\), and take a positive \(C^2\) radial function \(\Phi\) such that \(\Phi(y)=\lVert y\rVert^a/(\sqrt2a)\) whenever \(\lVert y\rVert\ge2\). By Itô's formula,
\[
\Phi(X_s)=\Phi(x)+M_s+\int_0^s g(X_u)\,du,
\qquad \langle M\rangle_s=\int_0^s v(X_u)\,du,
\]
where, for \(\rho=\lVert y\rVert\ge2\),
\[
 v(y)=(\rho^q\pi(y))^{-2\ell},\qquad
 g(y)=\frac{\rho^{-a}}{\sqrt2}(\rho^q\pi(y))^{-2\ell}
 [d+a-2+(1-2\ell)\langle y,\nabla\log\pi(y)\rangle].
\]
Indeed the generator is \(\mathcal L=\pi^{-2\ell}(\Delta+(1-2\ell)\nabla\log\pi\cdot\nabla)\). The bracket tends to \(-(r+a)\). The stated assumptions therefore give
\[
 v(y)\to v_\infty=c_\pi^{-2\ell}>0,\qquad g(y)\to0.
\]
Both \(v\) and \(g\) are globally bounded after the smooth interior extension. Let \(K=\sup|g|<\infty\). In particular \(\Phi(X_s)\) cannot reach infinity in finite time because its drift and quadratic variation rates are bounded, verifying nonexplosion directly.

**Upper logarithmic bound.** Fix \(\varepsilon\in(0,v_\infty)\). Choose \(R_0\ge2\) so that \(v(y)\le v_\infty+\varepsilon\) outside the closed ball of radius \(R_0\). Choose a smooth nondecreasing cutoff \(\psi:\mathbb R\to[0,\infty)\), with \(0\le\psi'\le1\), which vanishes on the entire range \(\{\Phi(y):\lVert y\rVert\le R_0\}\), and satisfies \(\psi(z)=z-C\) for all sufficiently large \(z\). The function \(Z_s=\psi(\Phi(X_s))\) has a bounded drift rate \(\psi'g+\tfrac12\psi''v\) and quadratic variation rate \((\psi')^2v\le v_\infty+\varepsilon\) globally. If \(K_0\) bounds the absolute drift, the Dambis–Dubins–Schwarz representation and Brownian reflection inequality imply, for a constant \(C_0\) independent of \(R\),
\[
 \mathbb P_x(\lVert X_t\rVert>R)
 \le\mathbb P\Big(\sup_{0\le u\le(v_\infty+\varepsilon)t}W_u\ge\Phi(R)-C_0\Big).
\]
The Gaussian reflection tail has logarithmic coefficient \(-1/[2(v_\infty+\varepsilon)t]\) relative to \(\Phi(R)^2\). Hence
\[
\limsup_{R\to\infty}\frac{\log\mathbb P_x(\lVert X_t\rVert>R)}{\Phi(R)^2}
\le-\frac1{2(v_\infty+\varepsilon)t}.
\]
Send \(\varepsilon\downarrow0\).

**Lower logarithmic bound.** Fix \(\varepsilon\in(0,v_\infty)\), a time \(s\in(0,t)\), and a radius \(R_0\ge2\) so large that \(v_-=v_\infty-\varepsilon\le v(y)\le v_+=v_\infty+\varepsilon\) for all \(\lVert y\rVert\ge R_0\). Choose \(B>0\) and a compact annulus \(U\) beyond \(R_0\) such that
\[
 \min_{y\in U}\Phi(y)>\Phi(R_0)+Ks+B.
\]
For every initial point \(y\in U\) let \(\tau\) be the first time the process enters the ball of radius \(R_0\). Represent \(M_u=W_{\langle M\rangle_u}\) by a standard Brownian motion. For a large target radius \(R\), set \(H_R=\Phi(R)+Ks-\min_{y\in U}\Phi(y)\). Consider the Brownian event
\[
 E_R=\left\{\inf_{0\le z\le v_+s}W_z>-B,\ \inf_{v_-s\le z\le v_+s}W_z\ge H_R\right\}.
\]
On \(E_R\), the path cannot reach \(R_0\) by time \(s\): at a first entrance \(\tau\le s\), its martingale would satisfy
\[
 W_{\langle M\rangle_\tau}=\Phi(R_0)-\Phi(y)-\int_0^\tau g(X_u)\,du<-B,
\]
whereas before entrance \(\langle M\rangle_\tau\le v_+s\). Thus \(\tau>s\), so \(\langle M\rangle_s\in[v_-s,v_+s]\), and \(E_R\) implies \(\Phi(X_s)\ge\Phi(R)\). Therefore
\[
\inf_{y\in U}\mathbb P_y(\lVert X_s\rVert\ge R)\ge\mathbb P(E_R).
\]
For each fixed \(s,v_-,v_+,B\), the standard Gaussian bridge/reflection argument gives
\[
 \lim_{H\to\infty}\frac{\log\mathbb P\{\inf_{z\le v_+s}W_z>-B,\ \inf_{v_-s\le z\le v_+s}W_z\ge H\}}{H^2}
 =-\frac1{2v_-s}.
\]
For completeness, the upper estimate follows from \(W_{v_-s}\ge H\). For the lower estimate require \(W_{v_-s}\in[H+\sqrt H,H+2\sqrt H]\). Its Gaussian probability has the displayed exponent; conditional on that endpoint the preceding Brownian bridge remains above \(-B\) with probability tending to one by reflection, and the subsequent increments remain above \(-\sqrt H\) throughout the fixed remaining interval with probability tending to one. This proves the stated Brownian exponent without an unjustified assumption of independence between time change and Brownian motion.

By local nondegenerate ellipticity, a diffusion started at any \(x\) has positive probability of belonging to the open interior of \(U\) at time \(t-s>0\); this also follows from the support theorem with paths confined to a compact region. The Markov property therefore gives a strictly positive factor multiplying the preceding uniform lower bound, independent of \(R\). Since \(H_R=\Phi(R)+O(1)\),
\[
 \liminf_{R\to\infty}\frac{\log\mathbb P_x(\lVert X_t\rVert>R)}{\Phi(R)^2}\ge-\frac1{2v_-s}.
\]
Now send \(s\uparrow t\) and \(\varepsilon\downarrow0\). Upper and lower bounds coincide, yielding \(-1/(2v_\infty t)\) per squared \(\Phi(R)\). Because \(\Phi(R)^2=R^{2a}/(2a^2)\), the asserted constant is \(-c_\pi^{2\ell}/(4a^2t)\).

**Exponential-moment cutoff.** For \(Y=\lVert X_t\rVert^{2a}\) and \(\theta>0\), Tonelli's identity
\[\mathbb E_xe^{\theta Y}=1+\theta\int_0^\infty e^{\theta u}\mathbb P_x(Y>u)\,du\]
turns the logarithmic tail asymptotic into finiteness for \(\theta<\kappa_t\) and divergence for \(\theta>\kappa_t\). At \(\theta=0\) the moment equals one. No boundary claim at equality is needed.

## Verification
The analytical argument is self-contained apart from standard Itô calculus, Dambis–Dubins–Schwarz, Gaussian reflection/bridge identities, and the standard local support property for a nondegenerate diffusion. The accompanying pure-Python checker verifies the symbolic exponents and generator identities on a nontrivial rational grid, and checks the moment-cutoff constant in its Brownian normalization. These finite checks do not establish the theorem; the stopped-path argument above handles all dimensions and admissible targets. Run `python3 verification/check_radial_clock.py` in a standard Python installation. The recorded output is in `verification/check_radial_clock.out`.

## Relationship to prior work
Mijatović and Xie, *Tempered Langevin diffusions with polynomial-tailed targets: explosions, moment thresholds and ergodicity* (arXiv:2610.30024v1, publicly posted 21 October 2026), establish nonexplosion and the qualitative critical exponential-moment power. Their Theorem 2.2(1) leaves two nonmatching time bounds when the moment order equals that critical power, and their Section 4.1 uses a bounded-drift, bounded-quadratic-variation radial transform. The present argument refines that transform by localizing quadratic variation **outside a large ball** and uses a near-full-duration Brownian bridge event, giving an exact coefficient and exact strict time dividing point. Earlier Fort–Roberts and Brešar–Mijatović ergodicity results concern convergence-to-stationarity rates and do not themselves supply the stated fixed-time logarithmic marginal-tail identity. Standard Gaussian large-deviation methods are conceptually related but require an additional localization argument under the stated asymptotic, potentially anisotropic coefficients.

## Limitations
The equality case \(\theta=\kappa_t\) is not classified; it can depend on lower-order radial information and is not implied by a logarithmic tail limit. The theorem excludes the critical temperature \(\ell=1/(d+r)\), higher temperatures, jump diffusions, and targets failing the two stated asymptotic assumptions. It makes no claim of a density-level prefactor, a uniform-in-time error, or historical independence from all possible general heat-kernel theorems. Independent priority and proof review have not been performed.

## References
1. A. Mijatović and H. Xie, *Tempered Langevin diffusions with polynomial-tailed targets: explosions, moment thresholds and ergodicity*, arXiv:2610.30024v1, 21 October 2026, especially Theorem 2.2(1) and Section 4.1; https://arxiv.org/abs/2610.30024.
2. G. Fort and G. O. Roberts, *Subgeometric ergodicity of strong Markov processes*, Annals of Applied Probability 15 (2005), 1565–1589, arXiv:math/0505260.
3. M. Brešar and A. Mijatović, *Subexponential lower bounds for f-ergodic Markov processes*, originally available in 2024, arXiv:2403.14826; Probability Theory and Related Fields 194 (2026), 997–1054.
4. D. Revuz and M. Yor, *Continuous Martingales and Brownian Motion*, for Dambis–Dubins–Schwarz and Brownian reflection identities.
