# Two-sided counting-edge laws in a commonly reset harmonic Brownian gas

## Finding

For an ensemble of independent Ornstein–Uhlenbeck particles subjected to one common Poisson clock that resets all their positions to zero, the number of particles in a fixed central observation window has an explicit stationary full counting law. Its large-population fraction has a compact, nondegenerate distribution with two fundamentally different edges. The lower edge has an adjustable power-law singularity and a finite-population Gaussian rounding scale, whereas the probability of observing **every particle** inside the window decays only as the inverse logarithm of population size.

More precisely, fix \(\mu,D,r,a>0\), and let \(K_N\) count particles in \([-a,a]\) at stationarity. Set
\[
A=a\sqrt{\frac{\mu}{2D}},\qquad \theta=\frac{r}{2\mu},\qquad p_*=\operatorname{erf}(A),\qquad B=\frac{A e^{-A^2}}{\sqrt\pi},\qquad s_*^2=p_*(1-p_*).
\]
Let \(H_N=K_N/N\). As \(N\to\infty\), \(H_N\) converges in distribution to a continuous random variable \(H\) with support \([p_*,1]\) and CDF
\[
\Pr(H\le x)=\left[1-\left(\frac{A}{\operatorname{erf}^{-1}(x)}\right)^2\right]^\theta,
\qquad p_*<x<1.
\]
The CDF is zero to the left and one to the right of that interval. At the lower edge, its density obeys
\[
f_H(p_*+u)\sim\frac{\theta}{B^\theta}u^{\theta-1}\qquad(u\downarrow0).
\]
Thus the density diverges, tends to \(1/B\), or vanishes at the lower edge according as \(r<2\mu\), \(r=2\mu\), or \(r>2\mu\). At the upper edge,
\[
\Pr(H>1-u)\sim\frac{\theta A^2}{\log(1/u)}\qquad(u\downarrow0).
\]

The finite-population lower-edge profile has a sharper form. For every fixed real \(x\), with \(\Phi\) the standard normal CDF,
\[
\lim_{N\to\infty}N^{\theta/2}\Pr\bigl\{K_N\le\lfloor Np_*+x\sqrt N\rfloor\bigr\}
=\frac{\theta}{B^\theta}\int_0^\infty z^{\theta-1}\Phi\!\left(\frac{x-z}{s_*}\right)\,dz.
\]
In particular,
\[
\Pr\bigl\{K_N\le\lfloor Np_*\rfloor\bigr\}
\sim \left(\frac{s_*}{B}\right)^\theta
\frac{2^{\theta/2-1}\Gamma((\theta+1)/2)}{\sqrt\pi}\,N^{-\theta/2}.
\]
In sharp contrast, the extreme all-inside event satisfies
\[
\boxed{\Pr(K_N=N)\sim \frac{r a^2}{4D\log N}.}
\]
These are asymptotic statements at fixed positive \(\mu,D,r,a\); they do not assert uniformity as parameters depend on \(N\).

## Assumptions and scope

For each integer \(N\ge1\), let \(W_1,\ldots,W_N\) be independent standard Brownian motions. Between successive jumps of an independent common rate-\(r\) Poisson process, the positions evolve as
\[
dX_i(t)=-\mu X_i(t)\,dt+\sqrt{2D}\,dW_i(t),\qquad i=1,\ldots,N.
\]
At every jump, all positions are simultaneously set to zero. Observe the unique stationary regime and define
\[
K_N=\sum_{i=1}^N {\bf1}\{|X_i|\le a\}.
\]
The interval is symmetric around the reset location. No particle interactions, partial resets, moving windows, or non-Poisson resetting are included. The equilibrium trap variance is \(D/\mu\), and the resetting age is shared by the whole ensemble.

## Proof

**Stationary mixture and finite-population law.** At a stationary observation time, the backward age \(T\) since the most recent common reset has density \(r e^{-rt}\) on \((0,\infty)\). Conditional on \(T=t\), the \(N\) positions are independent centered Gaussians with variance
\[
v(t)=\frac{D}{\mu}(1-e^{-2\mu t}).
\]
Consequently the conditional probability of a position lying in \([-a,a]\) is
\[
p(t)=\operatorname{erf}\!\left(\frac{A}{\sqrt{1-e^{-2\mu t}}}\right),
\]
and \(K_N\mid T=t\) is binomial with parameters \(N,p(t)\). Put \(Y=e^{-2\mu T}\). Direct transformation gives
\[
\Pr(Y\le y)=y^\theta,\quad 0<y<1;
\qquad q(y)=\operatorname{erf}\!\left(\frac A{\sqrt{1-y}}\right).
\]
Thus \(Y\) has density \(\theta y^{\theta-1}\), and the exact finite-population counting law is, for \(k=0,\ldots,N\),
\[
\Pr(K_N=k)=\binom Nk\,\theta\int_0^1 y^{\theta-1}q(y)^k[1-q(y)]^{N-k}\,dy.
\]
All terms are nonnegative and sum to one by the binomial theorem.

**Macroscopic fraction and its edges.** Couple every \(N\) to the same \(Y\), and conditional on \(Y\) use an infinite IID sequence of the corresponding Bernoulli indicators. The conditional strong law gives \(H_N\to q(Y)\) almost surely. The map \(q\) is continuous and strictly increasing from \(p_*\) to \(1\). Inverting \(x=q(y)\) yields
\[
y(x)=1-\left(\frac A{\operatorname{erf}^{-1}(x)}\right)^2,
\]
which proves the stated CDF. Taylor expansion at \(y=0\) gives
\[
q(y)=p_*+By+O(y^2),\qquad B=\frac{Ae^{-A^2}}{\sqrt\pi}>0.
\]
It follows that \(F_H(p_*+u)\sim(u/B)^\theta\). Differentiating the smooth inverse CDF on \((p_*,1)\) proves the asserted density law. For the other edge, write \(z=\operatorname{erf}^{-1}(1-u)\). The standard Gaussian tail expansion \(u=\operatorname{erfc}(z)\sim e^{-z^2}/(\sqrt\pi z)\) implies \(z^2\sim\log(1/u)\). Since
\[
1-F_H(1-u)=1-(1-A^2/z^2)^\theta\sim\theta A^2/z^2,
\]
the upper-edge logarithmic law follows.

**Gaussian rounding at the lower edge.** Denote \(k_N(x)=\lfloor Np_*+x\sqrt N\rfloor\) and \(g_N(y)=\Pr\{\mathrm{Bin}(N,q(y))\le k_N(x)\}\). The exact mixture formula gives
\[
N^{\theta/2}\Pr(K_N\le k_N(x))
=\frac{\theta}{B^\theta}\int_0^{B\sqrt N}
 z^{\theta-1}\,g_N\!\left(\frac z{B\sqrt N}\right)dz.
\]
For fixed \(z\), the expansion of \(q\), the binomial central limit theorem, and \(s_*^2>0\) show that the last integrand's probability converges to \(\Phi((x-z)/s_*)\). Here is the needed domination argument. On a small fixed interval \(0\le y\le\delta\), the strict positivity of \(q'(0)=B\) gives \(q(y)-p_*\ge (B/2)y\). Hoeffding's inequality then bounds \(g_N(y)\) by \(\exp[-c(z-x)_+^2]\) for all sufficiently large \(z\), uniformly in \(N\) on that interval. On \(y\ge\delta\), monotonicity gives an exponentially small bound \(e^{-c_\delta N}\), whose contribution after multiplication by \(N^{\theta/2}\) vanishes. The small-\(z\) integrability follows from \(\theta>0\). Dominated convergence yields the claimed finite-size profile for every real \(x\).

For \(x=0\), integration by parts and \(\int_0^\infty u^\theta e^{-u^2/2}du=2^{(\theta-1)/2}\Gamma((\theta+1)/2)\) evaluate the integral, giving the displayed coefficient.

**All-inside event.** Conditional independence gives \(\Pr(K_N=N)=\mathbb E[H^N]\). Let \(U=1-H\). The upper-edge result reads \(\Pr(U\le u)\sim c/\log(1/u)\), where \(c=\theta A^2\). For arbitrary fixed \(0<\varepsilon<1\), split the expectation of \((1-U)^N\) at \(U=N^{-(1+\varepsilon)}\) and \(U=N^{-(1-\varepsilon)}\). Below the first threshold the integrand is at least \(1-N^{-\varepsilon}\), and above the second it is at most \(e^{-N^\varepsilon}\). Therefore
\[
\frac{c}{1+\varepsilon}\le\liminf_{N\to\infty}(\log N)\mathbb E[(1-U)^N]
\le\limsup_{N\to\infty}(\log N)\mathbb E[(1-U)^N]\le\frac{c}{1-\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) proves \(\Pr(K_N=N)\sim c/\log N\). Finally \(\theta A^2=ra^2/(4D)\). This completes the proof.

## Verification

The standalone program `verify_counting.py` checks the OU-to-beta transformation, the exact CDF and finite-population normalization, left-edge coefficient, lower-edge Gaussian rounding at several independent parameters, and the slow convergence of the all-inside law. Run using `python verify_counting.py` with Python 3 and SciPy. Numerical evidence is supplementary: the infinite-population and asymptotic statements follow from the proof above. The program uses deterministic quadrature rather than random simulation.

## Relationship to prior work

The conditional IID representation and stationary harmonic Gaussian propagator are established methods, not contributions claimed here. De Mauro, Majumdar and Schehr (arXiv:2606.31634, 2026) analyze a simultaneously reset gas in harmonic and box confinement, deriving its stationary joint state and edge observables; the accessible abstract discusses density, correlations, maximum and gap rather than this counting-edge theorem. Their complete primary full text was unavailable to the present comparison, so any overlap in uninspected sections is a remaining priority risk. De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658, 2025) derive full counting statistics for **unconfined** commonly reset Brownian gases using general resetting-time distributions. That work supplies the general conditional-mixture approach but not the positive equilibrium fraction floor, its reset-to-relaxation dependent finite-population rounding exponent, or this two-edge comparison for a confined OU ensemble. Biroli, Majumdar and Schehr (arXiv:2503.14733, 2025) investigate full counting statistics for a **repulsively interacting Dyson** gas under resetting, not the independent OU model treated here. Neither generic conditional independence nor a title-only comparison establishes originality by itself; the distinguishing quantitative claim is the full paired edge theorem with its finite-\(N\) crossover.

## Limitations

The result assumes independent particles conditional on one globally shared Poisson reset age, stationary observation, a centered fixed interval, positive fixed parameters, and a harmonic trap. It does not cover finite-time startup, interacting gases, hard walls, asymmetric windows, separate reset clocks, or uniform parameter–population limits. No independent mathematical audit or publication-priority certification has been performed. The exact macroscopic CDF is a direct consequence of the known mixture representation; the substantive additional statements are the finite-population lower-edge profile and sharp comparison with the upper-edge logarithmic event. Highly relevant primary manuscripts could not all be inspected in full, and a general theorem on conditional-binomial mixtures might imply parts of these asymptotics without matching the model's wording.

## References

1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first submitted 2026-06-30), https://arxiv.org/abs/2606.31634.
2. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first submitted 2025-09-08), https://arxiv.org/abs/2509.06658; *Physical Review E* **113**, 014120 (2026).
3. M. Biroli, S. N. Majumdar, and G. Schehr, *Resetting Dyson Brownian motion*, arXiv:2503.14733 (first submitted 2025-03-18), https://arxiv.org/abs/2503.14733; *Physical Review E* **112**, 014101 (2025).
