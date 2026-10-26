# Quorum-dependent bottleneck and quorum-independent critical relaxation in a coevolving collective-risk game

## Finding

For the three-variable collective-risk game of Wang et al. (2026), an invariant maximal-risk, minimum-cost face has a sharp cooperation-loss threshold. At the threshold, the critical cooperative state attracts from above only at inverse-time speed, with a coefficient that does **not** depend on the quorum after normalization by the critical cost. Just above the threshold, the time required for cooperation to fall through any fixed neighborhood diverges as the inverse square root of the excess cost, with an explicit quorum-dependent coefficient.

Put \(n=N-1\), \(a=M-1\), \(d=N-M\), \(p=a/n\), and
\[
B(x)=b\binom{n}{a}x^a(1-x)^d,\qquad
\beta_*=B(p)=b\binom{n}{a}(a/n)^a(d/n)^d.
\]
For the invariant face \(r=1,c=\beta\), at \(\beta=\beta_*\) every trajectory starting at \(p<x(0)<1\) satisfies
\[
\lim_{t\to\infty} t\,[x(t)-p]=\frac{2}{(N-1)\beta_*}.
\]
For \(\beta=\beta_*+\epsilon\), where \(\epsilon>0\), fix \(0<\eta<\min\{p,1-p\}\). The time \(T_\eta(\epsilon)\) for the face trajectory to descend from \(p+\eta\) to \(p-\eta\) satisfies
\[
\lim_{\epsilon\downarrow0}\sqrt\epsilon\,T_\eta(\epsilon)
=\pi\sqrt{\frac{2(N-1)}{\beta_*(M-1)(N-M)}}.
\]
Under the explicit transverse-stability inequalities stated below, this fold is a nondegenerate one-dimensional center bifurcation of the entire three-variable game, not an artifact of an unrelated scalar approximation.

## Assumptions and scope

All calculations use the unit strategy-update time convention of Wang et al., equation (10). Take integers \(N\ge3\), \(2\le M\le N-1\), endowment \(b>0\), cost bounds \(0<\beta<\alpha\), and positive feedback coefficients \(\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4\). The full game is
\[
\begin{aligned}
\dot x&=x(1-x)[rB(x)-c],\\
\dot r&=r(1-r)[\mu_1(1-x)-\mu_2x],\\
\dot c&=(\alpha-c)(c-\beta)[\theta_1(1-x)-\theta_2x+\theta_3r-\theta_4(1-r)].
\end{aligned}
\]
Here \(x\in[0,1]\), \(r\in[0,1]\), and \(c\in[\beta,\alpha]\). Vary \(\beta\) while holding the other coefficients fixed and choosing \(\alpha>\beta_*+\epsilon\) in a small neighborhood of zero. The face \(r=1,c=\beta\) is invariant; its scalar equation is \(\dot x=x(1-x)[B(x)-\beta]\). For the three-variable center-manifold statement also impose
\[
\frac{\theta_1+\theta_3}{\theta_1+\theta_2}<p<\frac{\mu_1}{\mu_1+\mu_2}.
\]
The asymptotic relaxation and passage statements apply to trajectories **on the invariant face**. No off-face passage-time equivalence is asserted.

## Proof

**Peak and curvature.** Logarithmic differentiation on \((0,1)\) gives \(B'(x)/B(x)=a/x-d/(1-x)\). Thus \(B\) has a unique global maximum at \(p=a/n\). Differentiating once more at the maximum,
\[
B''(p)=-\beta_*\left(\frac{a}{p^2}+\frac{d}{(1-p)^2}\right)
=-\frac{\beta_*n^3}{ad}.
\]
Write \(h=p(1-p)=ad/n^2\) and \(D=-B''(p)/2=\beta_*n^3/(2ad)>0\). Taylor expansion shows
\[
B(p+y)=\beta_*-Dy^2+O(y^3),\qquad
(p+y)(1-p-y)=h+O(y).
\]
The coefficient of \(y^2\) in the critical face field is therefore \(-hD=-\beta_*n/2\). Its cancellation of \(a\) and \(d\) establishes the claimed quorum-independence.

**Critical relaxation.** At \(\beta=\beta_*\), \(B(x)<\beta_*\) away from \(p\) in the interior. For \(p<x(0)<1\), the scalar trajectory decreases monotonically and converges to \(p\), without crossing an equilibrium in finite time. With \(y(t)=x(t)-p>0\),
\[
\dot y=-\frac{\beta_*n}{2}y^2+O(y^3).
\]
Consequently \(\frac{d}{dt}(1/y)=\beta_*n/2+O(y)\to\beta_*n/2\). Integrating and dividing by \(t\) yields \(1/[t y(t)]\to\beta_*n/2\), proving the first limit. Trajectories strictly below \(p\) instead decrease toward the boundary \(x=0\).

**Passage above the critical cost.** At \(\beta=\beta_*+\epsilon\), the face field is strictly negative for \(x\in(0,1)\). The crossing time is therefore the finite integral
\[
T_\eta(\epsilon)=\int_{p-\eta}^{p+\eta}
\frac{dx}{x(1-x)[\epsilon+\beta_*-B(x)]}.
\]
Outside any small fixed neighborhood of \(p\), this integral is bounded uniformly in \(\epsilon\). Inside that neighborhood, \(\beta_*-B(p+y)=Dy^2[1+O(y)]\), and \(x(1-x)=h+O(y)\). Substitute \(y=\sqrt\epsilon\,u\); elementary dominated comparison using positive quadratic upper/lower bounds, followed by taking the inner neighborhood to zero, proves
\[
\lim_{\epsilon\downarrow0}\sqrt\epsilon\,T_\eta(\epsilon)
=\frac1h\int_{-\infty}^{\infty}\frac{du}{1+Du^2}
=\frac{\pi}{h\sqrt D}
=\pi\sqrt{\frac{2n}{\beta_*ad}}.
\]
For \(\beta=\beta_*-\epsilon\), the two nearby face equilibria also satisfy the sharp split
\[
x_\pm=p\pm\sqrt{\frac{2ad}{\beta_*n^3}}\,\sqrt\epsilon+O(\epsilon),
\]
which follows by dividing \(B(p+y)-\beta_*=-Dy^2+O(y^3)\) by \(\epsilon\) and using monotonicity on either side of \(p\).

**Transverse dynamical relevance.** At the critical equilibrium \((p,1,\beta_*)\), the Jacobian is upper triangular because the risk and cost feedback prefactors vanish on the invariant face. Its eigenvalues are
\[
0,\quad -[\mu_1-(\mu_1+\mu_2)p],\quad
(\alpha-\beta_*)[\theta_1+\theta_3-(\theta_1+\theta_2)p].
\]
Both nonzero eigenvalues are strictly negative under the scope inequalities. The invariant face is tangent to the unique center eigendirection, so the scalar dynamics just proved is an *exact* center-manifold restriction. Its nonzero quadratic coefficient and its nonzero derivative with respect to \(\beta\), namely \(-p(1-p)\), establish a nondegenerate fold in the full system. By continuity the upper near-critical edge root is locally attracting in all three directions just below \(\beta_*\), while the lower root has an unstable strategy direction.

## Verification

The included standalone \`verify.py\` checks, using exact rational arithmetic, the curvature identity and normalized relaxation coefficient for all \(N=3,\ldots,30\) and every interior quorum \(M=2,\ldots,N-1\). It also numerically integrates the exact passage-time integral for five disparate group/quorum pairs at two positive excess costs, checking convergence toward the analytical coefficient. Running \`python verify.py\` produces \`PASS: 1639 exact/numerical assertions\`. Numerical integration is corroboration only; the limits are proved by the arguments above.

For example, \(N=5\), \(M=3\), \(b=1\) gives \(p=1/2\), \(\beta_*=3/8\), critical decay coefficient \(4/3\), and passage coefficient \(4\pi/\sqrt3\). Positive feedback parameters \(\mu_1=9\), \(\mu_2=1\), \(\theta_1=1\), \(\theta_2=5\), \(\theta_3=1/10\), \(\theta_4=1\) satisfy the transverse inequalities; choose \(\alpha=1\).

## Relationship to prior work

Wang, Hua, Liu, Zhang, Liu, and Szolnoki, *PLoS Computational Biology* 22 (2026), e1013512, equation (10), derive the three-variable model. Their equilibrium and stability analysis identifies the two edge equilibria when the peak binomial benefit exceeds the lower cooperation cost, and gives conditions for the upper equilibrium's stability. The present claim does **not** count the already-known fold existence or that stability condition as a new discovery. It supplies the critical inverse-time coefficient, the explicit above-threshold loss-of-cooperation crossing constant, the cancellation of the quorum in the normalized critical decay, and the precise center reduction that connects those timing laws to the full game.

Ordinary saddle-node normal-form theory explains the two universal *exponents*; that general theory is not presented here as new. The exact coefficients and their contrasting quorum dependence are computations specific to the published collective-risk payoff geometry.

## Limitations

The timing formulae describe the exactly invariant maximal-risk/minimal-cost face, not all initial states of the three-dimensional system. The nonzero transverse-eigenvalue conditions allow a center-manifold interpretation, but do not prove identical timing constants for off-face trajectories. The parameter interval requires interior thresholds, strictly positive model coefficients, and the strategy update time scale normalized to one. Generic saddle-node theory covers the scaling exponents; the model-specific coefficients may have been independently derived in unindexed work. The supplementary stability analyses of the source were identified but could not be inspected completely; the absence of an analogous timing calculation there is not asserted.

## References

1. L. Wang, S. Hua, Y. Liu, L. Zhang, L. Liu, A. Szolnoki, “Coevolutionary dynamics of cooperation, risk, and cost in collective risk games,” *PLoS Computational Biology* **22** (2026), e1013512, first public journal version 20 February 2026, DOI: 10.1371/journal.pcbi.1013512. Public full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC12923141/ .
2. The authors' arXiv version 2603.20706v1, 21 March 2026: https://arxiv.org/html/2603.20706v1 .
