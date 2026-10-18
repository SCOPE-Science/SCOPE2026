# Sharp finite-size counting edge in a harmonically confined resetting gas

## Finding

Fix \(D,\mu,r,a>0\). In the stationary state of \(N\) independent Ornstein--Uhlenbeck particles driven by independent Brownian noises but reset **simultaneously** to the origin at Poisson rate \(r\), let \(K_N\) count the particles inside \([-a,a]\). Define
\[
\beta=\frac r{2\mu},\qquad b=a\sqrt{\frac\mu{2D}},\qquad p_*=\operatorname{erf}(b),\qquad c=\frac{b e^{-b^2}}{\sqrt\pi},\qquad \sigma=\sqrt{p_*(1-p_*)}.
\]
For every fixed \(s\in\mathbb R\),
\[
\boxed{\lim_{N\to\infty}N^{\beta/2}\,\mathbb P\left\{K_N\le\lfloor Np_*+s\sqrt N\rfloor\right\}=\mathcal E_\beta(s):=\beta\int_0^\infty w^{\beta-1}\Phi\left(\frac{s-cw}{\sigma}\right)dw,}
\]
where \(\Phi\) is the standard normal distribution function. The integral is finite and strictly positive for every finite \(s\). At the equilibrium-count threshold,
\[
\boxed{\mathbb P\{K_N\le\lfloor Np_*\rfloor\}\sim \frac{2^{\beta/2-1}\Gamma((\beta+1)/2)}{\sqrt\pi}\left(\frac\sigma c\right)^\beta N^{-\beta/2}.}
\]
The exponent is therefore \(r/(4\mu)\). A related infinite-particle statement is that \(K_N/N\) converges in distribution to a random fraction supported on \([p_*,1]\), whose density behaves as \(\beta c^{-\beta}(z-p_*)^{\beta-1}\) as \(z\downarrow p_*\). The limiting density diverges for \(r<2\mu\), approaches \(1/c\) for \(r=2\mu\), and vanishes for \(r>2\mu\).

## Assumptions and scope

Between common reset events, particle positions satisfy \(dX_i(t)=-\mu X_i(t)dt+\sqrt{2D}\,dB_i(t)\), with independent standard Brownian motions \(B_i\). Common resets send every coordinate to zero. The resetting clock is Poisson with fixed rate \(r>0\), and the system is observed in its stationary regime. The observation interval \([-a,a]\) has fixed positive half-width \(a\); all other parameters are fixed as \(N\to\infty\). The result concerns a count **across particles at one stationary time**, not occupation time along one trajectory.

The equilibrium comparison fraction is \(p_*=\Pr\{|Z|\le a\}\) for \(Z\sim N(0,D/\mu)\), and \(0<p_*<1\). The distinction between the fixed positive reset rate and the equilibrium case \(r=0\) matters: the theorem does not cover a joint scaling of \(r\) with \(N\).

## Proof

**Exact mixture.** At a stationary observation time, the time \(T\) since the last Poisson reset is exponential with rate \(r\). Conditional on \(T=t\), the \(X_i\) are independent centered Gaussians with variance \((D/\mu)(1-e^{-2\mu t})\). Consequently, setting \(V=e^{-2\mu T}\), one has
\[
\Pr\{V\le v\}=v^\beta\quad(0<v<1),\qquad
p(v)=\Pr\{|X_i|\le a\mid V=v\}=\operatorname{erf}\!\left(\frac b{\sqrt{1-v}}\right).
\]
Thus \(V\) has density \(\beta v^{\beta-1}\) and \(K_N\mid V=v\sim\operatorname{Bin}(N,p(v))\). The exact finite-size formula is
\[
\Pr\{K_N\le k\}=\beta\int_0^1 v^{\beta-1}\Pr\{\operatorname{Bin}(N,p(v))\le k\}\,dv\quad(0\le k\le N).
\]

**Boundary expansion and conditional normal fluctuations.** The function \(p\) is continuous on \([0,1]\), strictly increasing, satisfies \(p(0)=p_*\), \(p(1)=1\), and has expansion
\[
p(v)=p_*+cv+O(v^2)\quad(v\downarrow0),\qquad c=\frac{b e^{-b^2}}{\sqrt\pi}>0.
\]
For fixed \(w\ge0\) put \(v=w/\sqrt N\). The conditional binomial mean is \(Np_*+cw\sqrt N+O(1)\), and its variance divided by \(N\) tends to \(\sigma^2=p_*(1-p_*)>0\). The binomial central limit theorem therefore gives, for each fixed real \(s\),
\[
\Pr\{\operatorname{Bin}(N,p(w/\sqrt N))\le\lfloor Np_*+s\sqrt N\rfloor\}\longrightarrow\Phi((s-cw)/\sigma).
\]
The floor changes the standardized threshold by at most \(N^{-1/2}\).

**Uniform domination.** Define \(g(v)=(p(v)-p_*)/v\) for \(0<v\le1\) and \(g(0)=c\). This extends to a continuous, strictly positive function on \([0,1]\); at its right endpoint \(g(1)=1-p_*>0\). Let \(\delta=\min_{[0,1]}g>0\). For \(w\) larger than a fixed number depending on \(s,\delta\), and \(0\le w\le\sqrt N\), the binomial mean exceeds \(\lfloor Np_*+s\sqrt N\rfloor\) by at least \(\delta w\sqrt N/2\). Hoeffding's inequality therefore bounds the conditional left tail by \(\exp(-\delta^2w^2/2)\). For bounded \(w\), the tail is at most one. Hence \(w^{\beta-1}\) times the conditional probability has an integrable majorant on \([0,\infty)\) for every \(\beta>0\). Substituting \(v=w/\sqrt N\) in the exact mixture and invoking dominated convergence proves
\[
N^{\beta/2}\Pr\{K_N\le\lfloor Np_*+s\sqrt N\rfloor\}
\longrightarrow\beta\int_0^\infty w^{\beta-1}\Phi((s-cw)/\sigma)dw.
\]

**Exact threshold constant.** At \(s=0\), changing variables to \(y=cw/\sigma\) and integrating the normal survival function by layers yields
\[
\beta\int_0^\infty w^{\beta-1}\Phi(-cw/\sigma)\,dw
=\left(\frac\sigma c\right)^\beta\mathbb E[(Z_+)^\beta]
=\left(\frac\sigma c\right)^\beta\frac{2^{\beta/2-1}\Gamma((\beta+1)/2)}{\sqrt\pi},
\]
where \(Z\) is standard normal and \(Z_+=\max(Z,0)\).

**Macroscopic fraction and its edge.** Conditional binomial concentration gives \(K_N/N\to p(V)\) in probability conditional on \(V\), hence in distribution unconditionally. For \(\varepsilon\downarrow0\), the inverse of \(p(v)=p_*+cv+O(v^2)\) satisfies \(v=(\varepsilon/c)(1+O(\varepsilon))\). Therefore
\[
\Pr\{p(V)\le p_*+\varepsilon\}=\left(\frac\varepsilon c\right)^\beta(1+O(\varepsilon)),
\]
and differentiation of the smooth monotone inverse gives the claimed density asymptotic and the three regimes.

## Verification

The accompanying `verify.py` computes the exact binomial-mixture integral and the limiting Gaussian integral using independent numerical quadratures. With \(D=\mu=a=1\), its checks cover \(\beta=1/2,1,2\), \(N=300,1500,6000\), and nonzero offsets \(s=\pm0.3\). At \(N=6000\) the scaled probabilities divided by their predicted limits are approximately \(1.0005,0.9908,0.9641\) for those three \(\beta\) values, respectively; convergence is slowest in this sample at \(\beta=2\). An independent integral over physical reset age agrees with the transformed beta integral for \(N=300\), \(\beta=1\) to within floating-point quadrature accuracy. These are finite checks, not substitutes for the dominated-convergence proof.

To reproduce: run `python verify.py` with Python, NumPy/SciPy installed. The code uses the precise conditional binomial CDF rather than simulated paths.

## Relationship to prior work

The Poisson resetting and conditional-independence representation is established for the confined ideal gas by de Mauro, Majumdar and Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations* (arXiv:2606.31634, §§II and V). Its conclusion expressly identifies full counting statistics in a fixed interval as a prospective direction, rather than giving the finite-\(N\) equilibrium-edge law.

The earlier unconstrained-diffusion work of de Mauro, Biroli, Majumdar and Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols* (arXiv:2509.06658, §III, full-counting equations (52)–(55), and §V), establishes a binomial-mixture formula and macroscopic counting scaling for **free** Brownian particles under general renewal resetting. The new contribution is not that generic mixture identity, nor the already known upper counting-edge logarithm, but the explicit lower-edge finite-size probability, its rate-dependent exponent, and the full Gaussian boundary layer created by **harmonic confinement**.

Biroli, Majumdar and Schehr, *Resetting Dyson Brownian motion* (arXiv:2503.14733, §III.D), obtain full counting results in a harmonically trapped **logarithmically repulsive** Dyson gas. Their conditional particle-count fluctuations are on a \(\sqrt{\log N}\) scale, in contrast to the \(\sqrt N\) binomial fluctuations here; their large-particle-number and window scalings do not imply the present independent-particle boundary layer.

## Limitations

All asymptotics hold for a fixed positive reset rate, trap stiffness, diffusion constant, and window width as \(N\to\infty\). The formula does not cover correlated microscopic Brownian noises, non-Poisson reset clocks, interactions, spatially asymmetric windows, or simultaneous limits involving vanishing resetting/trapping parameters. The finite-size probability is not an independent-particle equilibrium large-deviation probability: the particles are dependent after averaging over the common reset age. The literature comparisons do not prove absolute uniqueness; implicit results in the general theory of exchangeable binomial mixtures remain a residual originality risk. No external independent validation is claimed.

## References

- G. de Mauro, S. N. Majumdar, G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first posted 2026-06-30), https://arxiv.org/abs/2606.31634.
- G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first posted 2025-09-08), https://arxiv.org/abs/2509.06658.
- M. Biroli, S. N. Majumdar, G. Schehr, *Resetting Dyson Brownian motion*, arXiv:2503.14733 (first posted 2025-03-18), https://arxiv.org/abs/2503.14733.
