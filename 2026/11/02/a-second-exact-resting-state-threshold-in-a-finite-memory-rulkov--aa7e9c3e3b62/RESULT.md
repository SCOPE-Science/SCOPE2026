# A second exact resting-state threshold in a finite-memory Rulkov neuron

## Finding

The finite-memory, sigmoid-feedback Rulkov neuron has a *second* sharp, algebraically specified threshold for a locally attracting **time-independent** resting state. Its creation of nonzero memory states at \(\kappa=1\) does not imply that a resting fixed point is attracting. For every fixed positive integer \(m\) and fixed \(\tau>0\), the exact equilibrium and weak-slow-feedback classification is governed by
\[
\kappa=\frac{m}{2\tau},\quad s_*=\sqrt5-2,\quad
\kappa_*=\frac{\operatorname{artanh}(s_*)}{s_*}=1.0192230012646086\ldots.
\]
If \(\kappa\le1\), the post-memory-fill map has only one fixed point, which is unstable whenever \(0<\mu<1/64\). If \(\kappa>1\), it has exactly three fixed points, indexed by \(\sigma\in\{0,-s_\kappa,+s_\kappa\}\), where \(s_\kappa\in(0,1)\) uniquely solves \(s_\kappa=\tanh(\kappa s_\kappa)\). The zero and positive branches are unstable for every \(0<\mu<1/64\). The **negative branch** is linearly unstable for all sufficiently small \(\mu>0\) if \(1<\kappa<\kappa_*\), but is a locally exponentially attracting fixed point for all sufficiently small \(\mu>0\) if \(\kappa\ge\kappa_*\), including at equality.

Consequently, for every fixed pair \((m,\tau)\) with \(\kappa>0\), and all sufficiently small positive \(\mu\), there exists a locally exponentially attracting stationary resting state **if and only if** \(\kappa\ge\kappa_*\). The smallness bound on \(\mu\) can depend on \((m,\tau)\); this is not a claim of a uniform finite-\(\mu\) phase boundary.

## Assumptions and scope

Fix an integer \(m\ge1\), positive \(\tau\), and slow update parameter \(\mu>0\). In the post-initialization region (after \(m\) states have filled the finite-memory window), study the autonomous delayed Rulkov map
\[
 x_{n+1}=f(x_n,y_n),\qquad
 y_{n+1}=y_n-\mu(x_n+1-\sigma_n),\qquad
 \sigma_n=\tanh\!\left(\frac{1}{2\tau}\sum_{j=1}^{m}(x_{n-j}+1)\right),
\]
where
\[
 f(x,y)=\begin{cases}
 5/(1-x)+y,&x\le0,\\
 5+y,&0<x<5+y,\\
 -1,&x\ge5+y.
 \end{cases}
\]
The state is \((x_n,y_n,x_{n-1},\ldots,x_{n-m})\in\mathbb R^{m+2}\). Its equilibrium analysis uses only the smooth branch \(x<0\), so none of the piecewise switching boundaries enters the local arguments. A fixed point means *every* state coordinate is time independent, not merely that the average voltage or its neuronal activity type has settled.

At a fixed point, \(\sigma\in(-1,1)\), \(x_*=\sigma-1\in(-2,0)\), \(y_*=x_*-5/(1-x_*)\), all delayed voltages equal \(x_*\), and \(\sigma=\tanh(\kappa\sigma)\). Thus no fixed points on other fast-map branches are omitted.

## Proof

**1. Exact equilibrium census and response slope.** For \(\kappa\le1\), \(\tanh(\kappa s)<s\) for all \(s>0\); hence only \(\sigma=0\) is possible. For \(\kappa>1\), strict concavity of \(s\mapsto\tanh(\kappa s)\) for \(s>0\), its derivative \(\kappa>1\) at zero, and its value below one at \(s=1\) give exactly one root \(s_\kappa\in(0,1)\), along with its negative. The implicit relation \(\kappa=\operatorname{artanh}(s_\kappa)/s_\kappa\) is strictly increasing in \(s_\kappa\). At either nonzero root set
\[
 \rho=\kappa(1-s_\kappa^2).
\]
The strict inequality \(0<\rho<1\) follows from \(\operatorname{artanh}(s)<s/(1-s^2)\), itself obtained by integrating \((1-t^2)^{-1}<(1-s^2)^{-1}\) for \(0\le t<s\).

**2. Exact linearized characteristic polynomial.** At an equilibrium with parameter \(\sigma\), let \(a=5/(2-\sigma)^2\), \(\eta=(1-\sigma^2)/(2\tau)\), and \(\rho=m\eta\). Perturbations satisfy
\[
 \delta x_{n+1}=a\delta x_n+\delta y_n,\qquad
 \delta y_{n+1}=\delta y_n-\mu\delta x_n+\mu\eta\sum_{j=1}^m\delta x_{n-j}.
\]
Together with the shift of the \(m\) lag coordinates, this has the monic degree-\(m+2\) characteristic polynomial
\[
 P_{m,\sigma}(\lambda)=
 \lambda^m\big[(\lambda-1)(\lambda-a)+\mu\big]
 -\mu\eta\sum_{j=0}^{m-1}\lambda^j.
\]
For real \(\lambda\ge1\), division by \(\lambda^m\) gives
\[
 Q(\lambda)=(\lambda-1)(\lambda-a)
 +\mu\left(1-\eta\sum_{j=1}^{m}\lambda^{-j}\right).
\]
These identities are exact for every integer memory length; in particular they retain all lag eigenmodes rather than replacing the memory by an instantaneous mean.

**3. Universal instability of the zero and positive branches.** At \(\sigma=0\), \(a=5/4\) and \(\rho=\kappa\). If \(\kappa>1\), then \(P(1)=\mu(1-\kappa)<0\), while \(P(\lambda)>0\) for sufficiently large positive \(\lambda\); therefore a real eigenvalue exceeds one for every \(\mu>0\). If \(\kappa\le1\), then \(Q(a)>0\) because \(\eta\sum_{j=1}^m a^{-j}<\rho\le1\), and at \(b=(1+a)/2\)
\[
 Q(b)=-\frac{(a-1)^2}{4}+\mu\left(1-\eta\sum_{j=1}^m b^{-j}\right)
 \le-\frac1{64}+\mu<0.
\]
This produces a real eigenvalue in \((b,a)\subset(1,\infty)\). (For \(\kappa<1\), a second is in \((1,b)\).) At the positive outer branch \(\sigma=s_\kappa\), one has \(a>5/4\), \(\rho<1\), \(Q(1)=\mu(1-\rho)>0\), \(Q(a)>0\), and \(Q(b)<0\) for \(0<\mu<1/64\). Hence **two distinct real eigenvalues above one** exist there.

**4. Negative branch below the second threshold.** At \(\sigma=-s_\kappa\), the fast multiplier is \(a=5/(2+s_\kappa)^2\). It exceeds one precisely when \(s_\kappa<s_*=\sqrt5-2\), equivalently \(1<\kappa<\kappa_*\). Since \(\rho<1\), the same three signs \(Q(1)>0\), \(Q((1+a)/2)<0\), and \(Q(a)>0\) hold whenever \(0<\mu<(a-1)^2/4\). Thus the negative equilibrium has two real unstable multipliers throughout that small-\(\mu\) range.

**5. Negative branch above the threshold.** If \(\kappa>\kappa_*\), then \(0<a<1\) and \(0<\rho<1\). At \(\mu=0\), the polynomial is \(\lambda^m(\lambda-1)(\lambda-a)\). The simple root at one continues analytically as
\[
 \lambda_1(\mu)=1-\mu\frac{1-\rho}{1-a}+O(\mu^2).
\]
For sufficiently small \(\mu>0\), this root lies inside the unit circle; all other roots remain near \(a\) or zero, hence are also strictly inside. This proves local exponential attraction.

**6. The endpoint is stable, not excluded.** At \(\kappa=\kappa_*\), one has \(a=1\), \(s_\kappa=s_*\), and \(\rho_*=\kappa_*(1-s_*^2)>8/9>1/2\): indeed \(s_*<1/3\) and \(\kappa_*>1\). Put \(\lambda=1+u\) and expand the exact characteristic equation as
\[
 u^2+\mu\Big[(1-\rho_*)+\tfrac12\rho_*(m+1)u+O(u^2)\Big]=0.
\]
The two roots emerging from the double root at one satisfy
\[
 \lambda_\pm=1\pm i\sqrt{\mu(1-\rho_*)}
 -\frac{\rho_*(m+1)}4\mu+O(\mu^{3/2}),
\]
so
\[
 |\lambda_\pm|^2=1+\mu\left[1-\frac{m+3}{2}\rho_*\right]+O(\mu^{3/2})<1
\]
for sufficiently small positive \(\mu\), because \(m\ge1\) and \(\rho_*>1/2\). The other \(m\) eigenvalues tend to zero. Hence the negative equilibrium is locally exponentially attracting **also at** \(\kappa=\kappa_*\). The strict-on-either-side statements and this endpoint analysis give the advertised if-and-only-if classification.

## Verification

The attached standalone `verify.py` computes the unfolded \((m+2)\)-dimensional Jacobian, checks its degree-\(m+2\) characteristic polynomial symbolically for memory length three, compares direct Jacobian eigenvalues against the polynomial for small memory lengths and varied feedback strengths, and tests the critical double-root expansion. It also prints diagnostic spectral radii at the motivating paper's parameter pair \(m=150\), \(\tau=70\), \(\mu=0.001\), giving approximately \(0.99941266\) for the negative outer fixed point, \(1.24605383\) for the central fixed point, and \(2.04089685\) for the positive outer fixed point. These numerical checks are finite evidence; the all-length and sufficiently-small-\(\mu\) statements rest on the proof above. Run the checker with `python verify.py` using the dependencies documented in `requirements.txt`.

## Relationship to prior work

Moreno, Nieto, and Sanjuán introduce the precise finite-memory sigmoid Rulkov feedback and observe a regime change near \(m=2\tau\). Their reported "stable spiking" and "stable bursting" states concern long-term neuronal activity regimes (often oscillatory), not necessarily time-independent fixed points of the full delayed map. Their intersection graph for the *mean* voltage already motivates \(\sigma=\tanh(\kappa\sigma)\); the scalar intersection count alone is **not** a new contribution here. The contribution is the exact full delayed-state spectrum and the second, boundary-inclusive resting-point stability threshold \(\kappa_*\), which distinguishes an unstable positive fixed point from a potentially stable *spiking regime*.

Earlier discrete-memristor Rulkov studies concern different state/memory feedback laws and do not obviously imply this exact finite-window polynomial and endpoint classification. More general stability ideas for lagged maps do not automatically give its threshold without evaluating the fast branch and the singular double-root perturbation. The result is a local stationary-state theorem, not a reinterpretation or rejection of the published simulations.

## Limitations

The theorem concerns the source's \(\alpha=5\), finite-window, sigmoid \(\sigma\)-feedback variant after the memory window fills; it does not address the separate early-time initialization rule, other fast branches away from the fixed points, arbitrary \(\alpha\), or time-varying memory. Stability is local and applies for each fixed \((m,\tau)\) and sufficiently small positive \(\mu\); no uniform gain ceiling, global basin, spiking/bursting-orbit classification, or stability assertion for all finite \(\mu\) is made. Numerical eigenvalues at \(\mu=0.001\) are diagnostics, not an exhaustive root certificate. Historical priority remains provisional pending independent literature review.

## References

1. M. Moreno, A. R. Nieto, and M. A. F. Sanjuán, *Complex transitions between spiking, bursting and silent regimes in a new memristive Rulkov neuronal model*, arXiv:2601.12139, first public version 2026-01-17; Chaos, Solitons & Fractals 206 (2026), 117928. https://arxiv.org/abs/2601.12139
2. L. J. Liu and D. Q. Wei, *A discrete memristor model and its application in the Rulkov neuron*, arXiv:2112.02738, 2021. https://arxiv.org/abs/2112.02738
3. M. Guo, Y. Bai, and J. Zhang, *Effects of non-ideal characteristics of memristor on the complex dynamics of memristor-coupled discrete Rulkov neurons*, Chaos 36 (2026), 033127, DOI:10.1063/5.0315796. https://doi.org/10.1063/5.0315796
