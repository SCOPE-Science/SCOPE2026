# Dilogarithmic rare-excursion law for a Brownian gas with frequent weak common resetting

## Finding
For any fixed integer \(N\geq1\), consider \(N\) independent Brownian particles with diffusivity \(D>0\), all subjected to the **same** Poisson reset clock of rate \(\lambda/s\). At each reset, every position is multiplied by \(1-s\), where \(0<s<1\) and \(\lambda>0\). Let \(\mathbf X^{(s)}\) have the unique stationary distribution.

Define \(\operatorname{Li}_2(t)=\sum_{j\ge1}t^j/j^2\) for \(0\le t\le1\). For \(c>0\), there exists a unique \(y(c)>0\) satisfying
\[
\frac{y(c)^2}{1-e^{-y(c)}}=c.
\]
Define \(H(0)=0\) and
\[
H(c)=y(c)-\tfrac12\operatorname{Li}_2(1-e^{-y(c)})\qquad(c>0).
\]
As \(s\downarrow0\), the rescaled stationary vector \(\sqrt{s}\,\mathbf X^{(s)}\) satisfies a full good large-deviation principle at speed \(s^{-1}\), with the explicit radial rate function
\[
\boxed{\mathcal I(\mathbf z)=H\!\left(\frac{\lambda}{D}\|\mathbf z\|_2^2\right),\qquad\mathbf z\in\mathbb R^N.}
\]
Thus, for every fixed \(1\le k\le N\) and \(L>0\),
\[
\boxed{\lim_{s\downarrow0}s\log\Pr\{X^{(s)}_1\ge L/\sqrt{s},\ldots,X^{(s)}_k\ge L/\sqrt{s}\}
=-H\!\left(\frac{k\lambda L^2}{D}\right).}
\]
The function \(H\) is strictly increasing and strictly concave on \((0,\infty)\), and \(H(0)=0\). In particular, for \(k\ge2\), the simultaneous-reset joint rate \(H(kc)\) is **strictly smaller** than the independent-reset joint rate \(kH(c)\), with \(c=\lambda L^2/D\). Nevertheless, for fixed spatial scales, the stationary coordinates converge jointly to independent centered Gaussians of variance \(D/\lambda\).

The boundary profiles are
\[
H(c)\sim c/2\quad(c\downarrow0),\qquad
H(c)=\sqrt c-\pi^2/12+o(1)\quad(c\to\infty).
\]
These formulas expose a non-Gaussian collective rare-excursion regime beyond the fixed-scale Gaussian approximation.

## Assumptions and scope
Each coordinate obeys \(dX_i(t)=\sqrt{2D}\,dB_i(t)\) between resets, with independent standard Brownian drivers \(B_i\); at rate \(\lambda/s\), a common reset acts as \(\mathbf X\mapsto(1-s)\mathbf X\). The reset clock is independent of all Brownian motions. The integers \(N,k\), the constants \(D,\lambda,L\), and the number of tested coordinates are fixed as \(s\downarrow0\). There is no external drift, interaction, or particle-dependent reset clock. The stationary law is unique for each \(s\in(0,1)\). The full LDP concerns Borel events with the usual interior and closure bounds; the displayed orthant event has matching bounds by continuity and strict radial monotonicity of the rate.

## Proof
**1. Exact stationary Gaussian mixture.** Fix \(s\in(0,1)\) and put \(q_s=(1-s)^2\). Looking backward from a stationary observation epoch, the successive Poisson gap lengths are independent exponentials \(E_j\sim\operatorname{Exp}(\lambda/s)\), indexed by \(j\ge0\). Disjoint Brownian increments are independent, and a gap \(j\) resets by the factor \((1-s)^j\) before observation. Conditional on the gaps, all coordinates are independent centered Gaussian variables with common variance
\[
V_s=2D\sum_{j=0}^{\infty}q_s^jE_j.
\]
This sum converges almost surely and in expectation because \(q_s<1\). Coupling solutions with identical Brownian paths and identical reset epochs multiplies their initial displacement by \((1-s)^{N_t}\), which tends to zero almost surely. Thus the constructed stationary law is unique.

Writing \(E_j=(s/\lambda)Z_j\), where the \(Z_j\) are independent unit-rate exponentials, gives
\[
V_s=\frac D\lambda W_s,\qquad W_s=2s\sum_{j\ge0}q_s^j Z_j.
\]
The explicit moments \(\mathbb EW_s=2s/(1-q_s)\to1\) and \(\operatorname{Var}W_s=4s^2/(1-q_s^2)\to0\) prove \(W_s\to1\) in \(L^2\), hence the stated fixed-scale joint Gaussian limit.

**2. Exact scaled cumulant generating function.** Set \(\mathbf Y_s=\sqrt{s}\,\mathbf X^{(s)}\). For every \(\boldsymbol\theta\in\mathbb R^N\) with \(t=(D/\lambda)\|\boldsymbol\theta\|_2^2<1\), Gaussian conditioning and the exponential transform yield the exact identity
\[
\Lambda_s(\boldsymbol\theta):=s\log\mathbb E\exp\!\left(\frac{\boldsymbol\theta\cdot\mathbf Y_s}{s}\right)
=-s\sum_{j=0}^{\infty}\log(1-tq_s^j).
\]
For \(t\ge1\) this moment is infinite (the term involving \(Z_0\) diverges). Since \(-\log q_s=-2\log(1-s)\sim2s\), Riemann-sum convergence, uniform with derivatives on compact subsets of \(t<1\), gives
\[
\Lambda_s(\boldsymbol\theta)\longrightarrow \Lambda(\boldsymbol\theta)
=\frac12\int_0^{\infty}-\log(1-te^{-u})\,du
=\frac12\operatorname{Li}_2(t).
\]
Here the dilogarithm is extended to real \(t<1\) by its integral, so the expression also covers every admissible vector \(\boldsymbol\theta\), for which \(t\ge0\). The limiting \(\Lambda\) is smooth and strictly convex on \(t<1\). With \(w(t)=-\log(1-t)/t\) (continuous at \(t=0\) with value 1),
\[
\nabla\Lambda(\boldsymbol\theta)=\frac D\lambda w(t)\boldsymbol\theta.
\]
As \(\|\boldsymbol\theta\|_2\uparrow\sqrt{\lambda/D}\), its gradient norm tends to infinity. The gradient is radial, strictly increasing in radius, and maps the open parameter ball onto \(\mathbb R^N\).

**3. Full stationary large deviations.** The exact moment identity yields exponential tightness of \(\mathbf Y_s\) using the exponentially small Chernoff bounds for the finitely many coordinate signs at any fixed interior parameter. For every \(\mathbf z\), choose the unique interior \(\boldsymbol\theta\) such that \(\nabla\Lambda(\boldsymbol\theta)=\mathbf z\). The exponential tilt with density \(\exp[(\boldsymbol\theta\cdot\mathbf Y_s-\Lambda_s(\boldsymbol\theta))/s]\) has mean \(\nabla\Lambda_s(\boldsymbol\theta)\to\mathbf z\) and covariance \(s\nabla^2\Lambda_s(\boldsymbol\theta)\to0\). Therefore the tilted probability of every ball around \(\mathbf z\) tends to one. Undoing the tilt gives the local large-deviation lower bound with exponent \(-\boldsymbol\theta\cdot\mathbf z+\Lambda(\boldsymbol\theta)\). The Chernoff bound with the same parameter gives the matching local upper bound. Finite coverings on compact sets and exponential tightness upgrade these local bounds to the full good LDP, whose rate is the Legendre transform \(\mathcal I(\mathbf z)=\sup_{t<1}[\boldsymbol\theta\cdot\mathbf z-\Lambda(\boldsymbol\theta)]\), with the supremum taken over \(\boldsymbol\theta\) satisfying \((D/\lambda)\|\boldsymbol\theta\|_2^2<1\). The limit is not asserted to be finite at the moment-generating boundary itself; only interior parameters were used.

**4. Explicit radial rate.** For \(\mathbf z\ne0\) the maximizing \(\boldsymbol\theta\) is parallel to \(\mathbf z\). Set \(c=(\lambda/D)\|\mathbf z\|_2^2\), \(t=(D/\lambda)\|\boldsymbol\theta\|_2^2\in(0,1)\), and \(y=-\log(1-t)\). The gradient equation is \(c=t w(t)^2=y^2/(1-e^{-y})\). This right-hand side increases strictly from zero to infinity as \(y\) runs over positive values. Moreover, the optimal dual product is \(\boldsymbol\theta\cdot\mathbf z=tw(t)=y\). Consequently \(\mathcal I(\mathbf z)=y-\operatorname{Li}_2(1-e^{-y})/2=H(c)\), as stated.

**5. Joint orthant probabilities and strict dependence.** The rate is radial and strictly increasing in radius. In the closed orthant \(\{\mathbf z:z_i\ge L,\ i\le k\}\), the unique minimum occurs at \((L,\ldots,L,0,\ldots,0)\), whose squared norm is \(kL^2\). The same infimum is approached from the open orthant. Thus upper and lower LDP bounds agree, yielding the joint-tail formula. If clocks were independent rather than common, each stationary coordinate has the same one-particle law but their joint probabilities factor, giving exponent \(kH(c)\). Differentiating the optimized rate yields \(H'(c)=1/[2w(t(c))]>0\). Since \(w(t)\) and \(t(c)\) increase strictly, \(H'\) decreases strictly. Hence \(H\) is strictly concave with \(H(0)=0\), so \(H(kc)<kH(c)\) for \(k>1\) and \(c>0\).

**6. End-regime checks.** As \(c\downarrow0\), \(y\sim c\), \(\operatorname{Li}_2(1-e^{-y})\sim y\), giving \(H(c)\sim c/2\). As \(c\to\infty\), \(y=\sqrt c+o(1)\) and \(\operatorname{Li}_2(1-e^{-y})\to\pi^2/6\), giving \(H(c)=\sqrt c-\pi^2/12+o(1)\).

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy installed. The script independently evaluates the **exact finite-reset** cumulant series at three parameter values and four strengths, compares it with the predicted dilogarithm limit, reconstructs the rate both from its scalar defining equation and an independently optimized Legendre transform, and checks strict multi-particle rate separation and both endpoint expansions. All programmed comparisons passed. These computations are finite cross-checks, not a substitute for the proof of the LDP or its limiting quantifiers.

## Relationship to prior work
Galla's 2026 work treats weak simultaneous partial resetting and derives a diffusion approximation with shared extrinsic noise; the present theorem describes a **non-Gaussian rare-event scale outside fixed-coordinate Gaussian convergence**. Biroli, Feld, Hartmann, Majumdar and Schehr (2024) obtain one-particle stationary distributions and fixed-rescaling spatial tails. Grzywny, Palmowski, Szczypkowski and Trojan (2024) establish a general multidimensional stationary density, including a fixed-contraction radial tail in their Lemma 2.27; this is the closest broader exact-density result. Their stated asymptotic keeps the contraction factor fixed and does not provide the coupled weak-rescaling/large-position LDP developed here. De Mauro, Biroli, Majumdar and Schehr (2025) establish full-reset Brownian-gas correlations and renewal observables, for resetting **to the origin**, not fractional rescaling. The present result does not claim novelty for the stationary representation, the exact product generating function, or general large-deviation principles; the assessed mathematical claim is the explicit dilogarithmic double-scaling rate and its strict many-particle consequence.

## Limitations
The limit holds for fixed particle count, fixed positive \(D,\lambda,L\), and proportional common reset factor \(1-s\) at rate \(\lambda/s\). It does not address growing particle count, mixed reset batches, nonlinear drifts, interacting particles, random reset amplitudes, or uniformity in all large-deviation thresholds. The primary motivation is a preprint, and no independent validation is asserted.

## References
1. T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635v1, submitted 2026-02-25; full text and supplementary multi-particle sections: https://arxiv.org/html/2602.21635v1 .
2. T. Grzywny, Z. Palmowski, K. Szczypkowski, B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626v1, 2024-12-20, especially Theorem A and Lemma 2.27: https://arxiv.org/pdf/2412.15626 .
3. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1, 2024-06-12: https://arxiv.org/html/2406.08387v1 .
4. G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658v1, 2025-09-08, focusing on full resets: https://arxiv.org/pdf/2509.06658 .
5. M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, 2022-11-01: https://arxiv.org/abs/2211.00563 .
