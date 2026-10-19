# A sharp chirality threshold for reentrant fourth-cumulant signs in a trapped circle swimmer

## Finding

A planar active Brownian particle can change the sign of its *stationary radial fourth cumulant twice* as the rate of stochastic chirality reversal increases. This happens above one sharply defined angular-speed threshold, and never below it, on the physically natural matched-timescale slice where the rotational diffusivity equals the trap relaxation rate. The result is exact for every positive propulsion speed and every nonnegative isotropic translational diffusivity.

**Theorem.** Let \(\kappa>0\) denote a harmonic relaxation rate, let \(v_0>0\) be the propulsion speed, and suppose the rotational diffusivity equals \(\kappa\). Let \(\omega>0\) be the magnitude of angular drift, \(\gamma>0\) the symmetric Poisson reversal rate of that drift, and \(D\geq0\) translational diffusivity. Define
\[
 r=\gamma/\kappa,\qquad u=\omega/\kappa,\qquad x=u^2,
\]
and define the stationary rotationally invariant cumulant
\[
 K_4=\mathbb E[(X_1^2+X_2^2)^2]-2\{\mathbb E[X_1^2+X_2^2]\}^2.
\]
Then
\[
 K_4=-\left(\frac{v_0}{\kappa}\right)^4\frac{P(r,x)}{(3r+x+9)(4r+x+4)^2(8r+x+16)},
\]
where
\[
\begin{aligned}
 P(r,x)={}&80r^4+(28x+560)r^3+(96x+1360)r^2\\
 &+(-4x^2+72x+1360)r+x^2+4x+480.
\end{aligned}
\]
In particular, the sign of \(K_4\) is independent of \(D\) and \(v_0\).

There exists **exactly one** critical dimensionless chirality \(u_c\), with
\[
8<u_c<9,\qquad u_c\approx8.8343988955,
\]
characterized exactly as follows. Put
\[
 B(r)=28r^3+96r^2+72r+4,
\qquad C(r)=80r^4+560r^3+1360r^2+1360r+480
\]
and for \(r>1/4\) put
\[
 x_{\mathrm{crit}}(r)=\frac{B(r)+\sqrt{B(r)^2+4(4r-1)C(r)}}{2(4r-1)},\qquad
 u_c^2=\min_{r>1/4}x_{\mathrm{crit}}(r).
\]
The minimizing \(r_c>1/4\) exists and is unique; numerically \(r_c\approx0.7282702565\).

For \(0<u<u_c\), \(K_4<0\) at every reversal rate \(r>0\). At \(u=u_c\), \(K_4\leq0\), and equality holds at just one (double-root) rate \(r=r_c\). For \(u>u_c\), there are exactly two simple positive thresholds
\[
\frac14<r_-(u)<r_+(u),
\]
and \(K_4\) is negative for \(0<r<r_-\), positive for \(r_-<r<r_+\), and negative for \(r>r_+\). The thresholds have the large-chirality laws
\[
 r_-(u)=\frac14+\frac{455}{64u^2}+O(u^{-4}),\qquad
 \frac{r_+(u)}{u}\longrightarrow\frac1{\sqrt7}\quad(u\to\infty).
\]
As one exact positive-cumulant witness, at \(u=10\) and \(r=1\),
\[
\left(\frac\kappa{v_0}\right)^4K_4=\frac{55}{1446336}>0.
\]
The assertion concerns the sign of the radial fourth *cumulant*, not a necessary-and-sufficient classification of peaks in the full spatial density.

## Assumptions and scope

Let \(W_t\) be standard planar Brownian motion and \(B_t\) an independent scalar Brownian motion. Let \(S_t\in\{-1,1\}\) be an independent symmetric continuous-time chain, flipping at rate \(\gamma\) from either state. On \(\mathbb R^2\times\mathbb S^1\times\{-1,1\}\), consider
\[
\begin{aligned}
 d\mathbf X_t&=(-\kappa\mathbf X_t+v_0(\cos\theta_t,\sin\theta_t))\,dt+\sqrt{2D}\,dW_t,\\
 d\theta_t&=\omega S_t\,dt+\sqrt{2\kappa}\,dB_t\quad(\text{mod }2\pi).
\end{aligned}
\]
All parameters are as in the theorem. The chain is stationary with probabilities one half per sign. Since \(\kappa>0\), the position admits a unique stationary realization as a contracting integral over the infinite past. Since the angle has strictly positive rotational diffusivity, its unique stationary marginal is uniform; the joint angle--sign chain is ergodic. Thus the stationary spatial law is rotation-invariant, centered, and has finite moments of every order. The statement holds for fixed finite positive parameters, not a joint large-time/large-rate limiting procedure.

## Proof

**1. Stationarity and removal of thermal noise.** On a two-sided stationary angle--sign process, the unique stationary position is
\[
 \mathbf X_t=v_0\int_0^\infty e^{-\kappa s}\mathbf n_{t-s}\,ds
 +\sqrt{2D}\int_{-\infty}^t e^{-\kappa(t-s)}\,dW_s,\qquad
 \mathbf n_t=(\cos\theta_t,\sin\theta_t).
\]
The first summand is bounded in norm by \(v_0/\kappa\), and the second is an independent centered isotropic Gaussian. For independent centered isotropic planar vectors \(V,G\), direct fourth-moment expansion gives
\[
 \mathbb E|V+G|^4-2(\mathbb E|V+G|^2)^2
 =\bigl(\mathbb E|V|^4-2(\mathbb E|V|^2)^2\bigr)
 +\bigl(\mathbb E|G|^4-2(\mathbb E|G|^2)^2\bigr).
\]
The last bracket vanishes for an isotropic Gaussian. It suffices to compute the active contribution with \(D=0\), in time units \(\kappa^{-1}\) and position units \(v_0/\kappa\).

**2. Exact stationary moment closure.** Let \(Z=\kappa(X_1+iX_2)/v_0\) be the dimensionless active position. Its generator acts on complex polynomials through
\[
 \dot Z=-Z+e^{i\theta},\qquad d\theta=uS\,dt+\sqrt2\,dB_t,
\]
with sign switches at rate \(r\). For integers \(p,q\geq0\) and signs \(s=\pm1\), set
\[
 F_{p,q}^{s}=\mathbb E\!\left[Z^p\overline Z^q e^{i(q-p)\theta}\mathbf1_{\{S=s\}}\right].
\]
Rotational covariance closes the hierarchy and \(F_{0,0}^{\pm}=1/2\). Applying the stationary generator, including the angular Brownian second derivative and the sign-switching generator, gives for \(p+q>0\), with \(m=q-p\),
\[
 \left(p+q+m^2+r-imu s\right)F_{p,q}^{s}-rF_{p,q}^{-s}
 =pF_{p-1,q}^{s}+qF_{p,q-1}^{s}.
\]
Terms with a negative index are omitted. The determinant of each two-state linear system is
\[
 (p+q+m^2)(p+q+m^2+2r)+m^2u^2>0.
\]
Induction therefore determines all moments uniquely and without any uncontrolled closure assumption. Solving this explicitly up to order four yields
\[
 \begin{aligned}
 \mathbb E|Z|^2&=\frac{2(r+1)}{4r+x+4},\\
 \mathbb E|Z|^4&=\frac{28r^3+(8x+168)r^2+(20x+308)r+7x+168}{(3r+x+9)(4r+x+4)(8r+x+16)}.
 \end{aligned}
\]
Subtracting twice the square of the first formula, factoring, and restoring the original length scale gives the asserted expression for \(K_4\).

**3. One sharp onset and the complete sign diagram.** Write
\[
 P(r,x)=(1-4r)x^2+B(r)x+C(r).
\]
Both \(B(r)\) and \(C(r)\) are strictly positive for \(r\geq0\). Thus \(P(r,x)>0\) for \(0\leq r\leq1/4\) and all \(x\geq0\). When \(r>1/4\), the expression is a downward-opening quadratic in \(x\) with positive value at zero. It crosses zero precisely once at the positive number \(x_{\mathrm{crit}}(r)\) given above: it is positive below this number and negative above it.

The function \(x_{\mathrm{crit}}(r)\) is continuous and goes to infinity both as \(r\downarrow1/4\) and as \(r\to\infty\) (in fact its large-\(r\) leading order is \(7r^2\)). Therefore its strictly positive global minimum \(x_c\) exists. By the preceding sign analysis, \(P(r,x)>0\) for all positive \(r\) when \(x<x_c\); at \(x_c\) it is everywhere nonnegative and zero at least once; above \(x_c\) it becomes strictly negative for some \(r\).

The decisive strict convexity is
\[
 \frac{\partial^2P}{\partial r^2}
 =960r^2+6(28x+560)r+2(96x+1360)>0.
\]
Together with \(P(0,x)>0\) and \(P(r,x)\to+\infty\) as \(r\to\infty\), strict convexity implies: at the critical \(x_c\), precisely one zero, a double root at a unique minimizing rate; above the threshold, precisely two simple positive zeros with \(P<0\) strictly between. This proves all the sign statements.

To rigorously localize the onset, at \(x=64\) one has
\[
 P(r,64)=80r^4+2352r^3+(7504r^2-10416r+4832).
\]
The quadratic in parentheses has positive leading coefficient and discriminant \(-36544256<0\); hence \(P(r,64)>0\) for all \(r\geq0\). Conversely \(P(3/4,81)=-4533/8<0\). Thus \(8<u_c<9\). The quoted decimals arise only from solving the two exact equations \(P=\partial_rP=0\); they are not needed for the theorem.

**4. High-chirality endpoints.** The polynomial identity
\[
 P(r,u^2)=(1-4r)u^4+B(r)u^2+C(r)
\]
shows that, for bounded \(r\), the lower root must tend to \(1/4\). Substitution of \(r=1/4+c/u^2\), followed by division by \(u^2\), gives the limiting coefficient \(455/16-4c\), so \(c=455/64\). Smooth implicit expansion about this simple scaled root gives the stated \(O(u^{-4})\) remainder. For the upper root put \(r=yu\). After division by \(u^5\), the polynomial converges uniformly on compact positive \(y\)-intervals to \(28y^3-4y\). Its positive nonzero simple root is \(1/\sqrt7\); comparison on either side of that root, together with the already-proved two-root classification, gives \(r_+(u)/u\to1/\sqrt7\).

## Verification

The companion `verify.py` uses two mathematically distinct exact moment constructions. It first solves the finite triangular stationary generator hierarchy symbolically in \(r,u\), and checks both moments and the factorization defining \(P\). It then independently evaluates ordered-time correlation integrals: Fourier-mode transition matrices for the two-state angular process are integrated with matrix resolvents over each time gap, and all labeled orderings of the two positive and two negative Fourier charges are summed. At exact rational parameter sets, the independently computed second and fourth moments agree with the generator results. The program also checks polynomial identities, exact sign witnesses, and high-chirality asymptotic coefficients. Its execution reports 34 exact assertions.

These finite automated checks support, but do not replace, the proof of the globally quantified threshold theorem. In particular, positivity and uniqueness over a continuum of rates follow analytically from the concave quadratic in \(x\) and strict convexity in \(r\), not by sampling a grid.

## Relationship to prior work

Das and Basu (arXiv:2301.11194v1, 26 January 2023) established the free chirality-reversing active Brownian model and its dynamical position fluctuations; their conclusion identifies confinement as a further question. Our addition is an isotropic harmonic trap and an exact *stationary* fourth-cumulant sign classification as the rate of angular-drift reversal changes.

Santra, Basu, and Sabhapandit (arXiv:2107.12640v1, 27 July 2021) studied a harmonically trapped particle with **reversals of the propulsion direction**, not reversals of angular drift. Their exact stationary kurtosis concerns a different generator. Pattanayak and collaborators (arXiv:2509.03448v1, 3 September 2025; and arXiv:2603.26967v1, 27 March 2026) derived fourth moments and kurtosis for harmonically trapped chiral particles with **constant** angular velocity, not a switching telegraph angular drift. Their static-chirality result is compatible with the zero-reversal limit here but does not supply the rate-dependent quartic or its two-root theorem. The free constant-chirality exact-moment treatment arXiv:2404.09650v1 also has neither stochastic chirality reversals nor confinement.

The underlying moment-hierarchy technique and the existence of positive and negative kurtosis regimes in other chiral models are prior knowledge. The specific contribution here is the sharp telegraph-chirality onset, the complete two-rate reentrance, and its asymptotic endpoints, not a claim to have originated those broader ideas.

## Limitations

The complete sign classification is proved on the matched-time-scale slice \(D_R=\kappa\); other ratios of rotational diffusion to trap relaxation are not classified. Switching is symmetric, memoryless, and changes the *angular velocity*, not the propulsion sign. The trap is isotropic and harmonic. We do not infer the number of peaks or shoulders in a stationary density from a fourth cumulant, and no collective-particle, arbitrary-trap, or non-Poisson switching claim is made. The critical threshold is defined exactly by a variational algebraic minimum and located numerically; no elementary radical expression is asserted. Independent review of mathematical priority remains outstanding, especially concerning possible general Markov-additive cumulant identities.

## References

1. S. Das and U. Basu, *Chirality Reversing Active Brownian Motion in Two Dimensions*, arXiv:2301.11194v1 (26 January 2023), https://arxiv.org/abs/2301.11194.
2. I. Santra, U. Basu, and S. Sabhapandit, *Direction reversing active Brownian particle in a harmonic potential*, arXiv:2107.12640v1 (27 July 2021), https://arxiv.org/abs/2107.12640.
3. A. Pattanayak, A. Shee, D. Chaudhuri, and A. Chaudhuri, *Chirality, confinement and dimensionality govern re-entrant transitions in active matter*, arXiv:2509.03448v1 (3 September 2025), https://arxiv.org/abs/2509.03448.
4. A. Pattanayak, A. Shee, A. Chaudhuri, and D. Chaudhuri, *Characterizing exact dynamics of a trapped active Brownian particle under torque in two and three dimensions*, arXiv:2603.26967v1 (27 March 2026), https://arxiv.org/abs/2603.26967.
5. A. Pattanayak, A. Shee, D. Chaudhuri, and A. Chaudhuri, *Impact of chirality on active Brownian particle: Exact moments in two and three dimensions*, arXiv:2404.09650v1 (15 April 2024), https://arxiv.org/abs/2404.09650.
