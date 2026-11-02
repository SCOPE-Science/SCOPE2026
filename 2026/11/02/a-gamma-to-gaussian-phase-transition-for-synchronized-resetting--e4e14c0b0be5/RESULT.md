# A Gamma-to-Gaussian phase transition for synchronized resetting of Brownian searchers

## Finding

For every integer \(N\ge2\), let \(N\) independent Brownian motions with generator \(D\partial_{xx}\) start at \(d>0\), be absorbed on reaching the origin, and experience **one common** Poisson resetting clock. At each reset, every still-searching particle returns instantaneously to \(d\); the search ends at the first absorption. Set
\[
t_0=\frac{d^2}{4D},\qquad L_N=\log N,\qquad r_N=\frac{aL_N^2}{t_0},\qquad a>0.
\]
Write \(T_N\) for the completion time and \(p_N\) for the probability of completing the search in a single independent reset interval. As \(N\to\infty\), the exact leading laws are
\[
p_N\sim
\begin{cases}
\Gamma(1-a)\,(\pi L_N)^{-a/2}N^{-a},&0<a<1,\\
\frac{1}{2}N^{-1},&a=1,\\
N^{1-2\sqrt a},&a>1.
\end{cases}
\]
The transition admits a nondegenerate **Gaussian critical window**: for each fixed real \(z\), put \(a_N=1+z/\sqrt{L_N}\). Then
\[
\frac{p_N(a_N)}{N^{1-2\sqrt{a_N}}}\longrightarrow
\Phi\!\left(\frac z{\sqrt2}\right),
\]
where \(\Phi\) is the standard normal distribution function. Moreover, at every fixed \(a>0\),
\[
r_Np_N T_N\Longrightarrow\operatorname{Exp}(1),
\qquad
\mathbb E[T_N]=\frac{1-p_N}{r_Np_N}.
\]
Consequently the mean completion time grows on three explicitly different scales:
\[
\mathbb E[T_N]\sim
\begin{cases}
\displaystyle\frac{t_0\pi^{a/2}}{a\Gamma(1-a)}N^a L_N^{a/2-2},&0<a<1,\\
\displaystyle 2t_0N/L_N^2,&a=1,\\
\displaystyle\frac{t_0}{aL_N^2}N^{2\sqrt a-1},&a>1.
\end{cases}
\]
The exponential power \(I(a)=\lim_{N\to\infty}[-\log p_N/\log N]\) equals \(a\) below the threshold and \(2\sqrt a-1\) above it. It is continuously differentiable, but its second derivative jumps at \(a=1\).

## Assumptions and scope

Brownian motions between resets are mutually independent, have variance \(2Dt\), and each starts at the same target distance \(d\). The global reset clock is independent of all Brownian paths, has rate \(r_N\), and causes a simultaneous instantaneous restart of all surviving walkers. Every reset restores fresh independent Brownian driving noise. No particle is required to return after the **first** absorption; completion ends the experiment. Parameters \(d,D\) are fixed positive constants. The fixed-rate coefficient \(a\) belongs to \((0,\infty)\), except in the stated critical-window result, where \(a_N\to1\). The case of no resetting, \(a=0\), is deliberately excluded.

A single unreset Brownian first-passage time \(\tau\) has distribution
\[
\Pr(\tau\le t)=\operatorname{erfc}\!\left(\sqrt{t_0/t}\right),\qquad t>0.
\]
Let \(\tau_1,\ldots,\tau_N\) be independent copies, \(M_N=\min_i\tau_i\), and \(R_N\sim\operatorname{Exp}(r_N)\) independent of them. Then \(p_N=\Pr(M_N<R_N)=\mathbb E[e^{-r_NM_N}]\).

## Proof

**1. An exact representation through maxima of Gamma variables.** Let \(Y_i=t_0/\tau_i\). A change of variables in the Brownian hitting-time density shows that the \(Y_i\) are independent with density
\[
g(y)=\frac{e^{-y}}{\sqrt{\pi y}},\qquad y>0,
\]
i.e. each is Gamma with shape \(1/2\) and unit rate. Put \(Y_{(N)}=\max_iY_i\); then \(M_N=t_0/Y_{(N)}\) and
\[
p_N=\mathbb E\!\left[e^{-aL_N^2/Y_{(N)}}\right]
=\frac{N}{\sqrt\pi}\int_0^\infty
\frac{e^{-y-aL_N^2/y}}{\sqrt y}
\left(1-\operatorname{erfc}\sqrt y\right)^{N-1}\,dy.
\tag{1}
\]
An independent integration-by-parts representation, useful for numerical checking, is
\[
p_N=aL_N^2\int_0^\infty y^{-2}e^{-aL_N^2/y}
\left[1-\left(1-\operatorname{erfc}\sqrt y\right)^N\right]dy.
\tag{2}
\]
Both identities hold for each finite \(N\) and positive \(a\). Such finite-population renewal formulas belong to the established resetting literature; novelty is not claimed for (1) or (2).

**2. The Gumbel regime \(0<a<1\).** Define \(b_N>0\) by \(N\operatorname{erfc}(\sqrt{b_N})=1\). The standard Gaussian-tail expansion gives
\[
b_N=L_N-\tfrac12\log L_N-\tfrac12\log\pi+o(1).
\]
For each real \(u\), \(N\operatorname{erfc}\sqrt{b_N+u}\to e^{-u}\), so \(Y_{(N)}-b_N\) converges to the standard Gumbel law \(G\) with \(\Pr(G\le u)=e^{-e^{-u}}\). The Mills-ratio upper bound also gives a uniform bound \(\Pr(Y_{(N)}-b_N>u)\le C e^{-u}\) for \(u\ge0\) and all sufficiently large \(N\). Consequently \(e^{a(Y_{(N)}-b_N)}\) is uniformly integrable for \(0<a<1\), and its expectation tends to \(\mathbb E[e^{aG}]=\Gamma(1-a)\).

The **exact** algebraic identity
\[
\frac{L_N^2}{Y_{(N)}}
=L_N-(Y_{(N)}-L_N)+\frac{(Y_{(N)}-L_N)^2}{Y_{(N)}}
\]
gives
\[
e^{aL_N-aL_N^2/Y_{(N)}}
=e^{a(Y_{(N)}-L_N)}
\exp\!\left[-a\frac{(Y_{(N)}-L_N)^2}{Y_{(N)}}\right].
\]
The last factor tends to one in probability, because \(Y_{(N)}=L_N+O_{\mathbb P}(\log L_N)\), and is bounded above by one. The preceding uniform-integrability bound therefore yields
\[
p_N\sim e^{-aL_N+a(b_N-L_N)}\Gamma(1-a)
=\Gamma(1-a)(\pi L_N)^{-a/2}N^{-a}.
\]

**3. The tilted-Gamma saddle and its Gaussian edge.** Equation (1) can be rewritten **exactly** as
\[
\frac{p_N}{N e^{-2\sqrt a L_N}}
=\mathbb E_{Q_{a,L_N}}
\left[\left(1-\operatorname{erfc}\sqrt Y\right)^{N-1}\right],
\tag{3}
\]
where the probability measure \(Q_{a,L}\) has density
\[
q_{a,L}(y)=\frac{e^{2\sqrt a L}}{\sqrt{\pi y}}
 e^{-y-aL^2/y},\qquad y>0.
\]
Its normalization follows from the exact Gamma integral
\(\int_0^\infty y^{-1/2}e^{-y-c/y}\,dy=\sqrt\pi e^{-2\sqrt c}\). Its moment-generating function, for \(t<1\), is
\[
\mathbb E_{Q_{a,L}}e^{tY}
=(1-t)^{-1/2}\exp\!\left[2\sqrt a L(1-\sqrt{1-t})\right].
\]
Expanding this identity at \(t=u/\sqrt L\) proves, for any sequence \(a_L\to a>0\),
\[
\frac{Y-\sqrt{a_L}L}{\sqrt L}
\Longrightarrow\mathcal N\!\left(0,\frac{\sqrt a}{2}\right).
\tag{4}
\]
Write \(h_N(y)=(1-\operatorname{erfc}\sqrt y)^{N-1}\). The location where \(h_N\) changes from near zero to near one is \(b_N=L_N+O(\log L_N)\). More precisely, for any fixed \(\delta>0\), \(h_N(y)\to0\) uniformly for \(y\le L_N-\delta\sqrt{L_N}\), and \(h_N(y)\to1\) uniformly for \(y\ge L_N+\delta\sqrt{L_N}\). This follows from the Gamma-tail expansion, and is sufficient with (4) to pass to the limit in (3).

If \(a>1\), the center \(\sqrt a L_N\) lies a positive linear distance above \(b_N\), so the right side of (3) tends to one. If \(a=1\), it tends to \(\Pr(Z>0)=1/2\) with centered normal \(Z\), giving the exact critical prefactor. More generally, for \(a_N=1+z/\sqrt{L_N}\),
\[
\frac{Y-L_N}{\sqrt{L_N}}
\Longrightarrow\mathcal N\!\left(\frac z2,\frac12\right),
\]
and hence (3) tends to \(\Pr(\mathcal N(z/2,1/2)>0)=\Phi(z/\sqrt2)\). This proves the Gaussian crossover without extrapolating finite numerical data.

**4. Exact mean and exponential completion law.** The independent attempts consist of \(M_N\) racing against an independent exponential clock. Their success probability is \(p_N\), while their mean duration is \((1-p_N)/r_N\). The renewal equation gives the exact stated mean \((1-p_N)/(r_Np_N)\). More generally, if \(p_N(q)=\mathbb E[e^{-qM_N}]\) with the same Brownian population but arbitrary \(q>0\), the Laplace transform of total completion time is
\[
\mathbb E[e^{-sT_N}]
=\frac{(r_N+s)p_N(r_N+s)}{s+r_Np_N(r_N+s)},\qquad s\ge0.
\tag{5}
\]
The three asymptotic regimes imply \(p_N\to0\) and \(p_NL_N\to0\). For each fixed \(a>0\), there is a small constant \(c>0\) such that the contribution of \(Y_{(N)}<cL_N\) to \(p_N\) is negligible: it is bounded by \(e^{-aL_N/c}\), whereas the proved asymptotic exponent of \(p_N\) is either \(a\) or \(2\sqrt a-1\); choose \(c\) so that \(a/c\) exceeds that exponent. Under the tilted law proportional to \(e^{-aL_N^2/Y_{(N)}}\), therefore, \(Y_{(N)}\ge cL_N\) with probability tending to one. For \(s=\theta r_Np_N\), this ensures
\[
sM_N=\theta p_N\,aL_N^2/Y_{(N)}
\le \theta a p_NL_N/c\to0
\]
in tilted probability. Bounded convergence yields \(p_N(r_N+s)/p_N(r_N)\to1\). Substituting into (5) proves \(\mathbb E[e^{-\theta r_Np_NT_N}]\to(1+\theta)^{-1}\), hence convergence to an exponential variable. Substitution in the exact mean gives its three asymptotic formulas.

## Verification

The accompanying standalone `verify.py` evaluates both independent finite-population integral formulas (1) and (2), checks probability bounds and the geometric-attempt renewal identity, and compares numerically normalized probabilities against all three asymptotic regimes and the critical Gaussian crossover. Run `python verify.py` with Python, NumPy and SciPy. In its recorded execution it passed 101 deterministic numerical consistency assertions. These are finite checks only: the infinite-population results are proved by the preceding analytical argument.

## Relationship to prior work

Biroli, Majumdar and Schehr (2023) derive the exact mean first-passage law for both independent and simultaneous resetting of finitely many Brownian walkers. In particular their protocol B equations (21)–(26) imply the finite-population renewal representation used here. They analyze finite-population optimization and small-reset-rate asymptotics; the increasing-population, diverging-rate \(r_N\propto(\log N)^2\) Gamma/saddle transition and its Gaussian critical window are not stated in the inspected primary preprint.

Vatash, Goldfarb, Rudyak and Roichman (2026) analyze optimal ordered-arrival resetting across ranks, including a finite-population common-reset comparison; their asymptotic discussion concerns fixed rank fractions and independently resetting searchers, not this joint high-reset-rate common-clock limit. Linn and Lawley (2023) develop general frequent-resetting completion-time laws, which overlap with the generic exponential-renewal mechanism but do not provide the population-dependent success probabilities and crossover established here. Independent Poisson clocks have a different renewal structure; their results cannot be carried across to a shared clock by changing a parameter.

## Limitations

The conclusion is for identical independent Brownian excursions in one dimension and an exact globally synchronized Poisson clock. It does not cover spatially heterogeneous reset distances, interactive walkers, per-particle reset clocks, resetting overheads, arbitrary restart-time distributions, the no-reset boundary \(a=0\), or all ordered arrival ranks. The Gaussian statement applies to fixed \(z\) and the window \(a_N=1+z/\sqrt{\log N}\); no uniform-in-\(z\) error bounds are claimed. General rare-event theorems may offer alternative proofs; publication priority beyond the sources inspected is not established.

## References

1. R. Vatash, E. Goldfarb, V. Yu. Rudyak and Y. Roichman (2026), *Rank-dependent optimal resetting in multiparticle search*, arXiv:2609.23542, first submitted 2026-09-20, https://arxiv.org/abs/2609.23542.
2. M. Biroli, S. N. Majumdar and G. Schehr (2023), *Critical number of walkers for diffusive search processes with resetting*, *Physical Review E* 107, 064141; arXiv:2303.18012, https://arxiv.org/abs/2303.18012.
3. S. Linn and S. D. Lawley (2023), *First-passage times under frequent stochastic resetting*, *Physical Review E* 108, 024114, https://doi.org/10.1103/PhysRevE.108.024114.
4. M. Biroli, S. N. Majumdar and G. Schehr (2026), *First-passage resetting gas*, *EPL* 153, 31002, https://doi.org/10.1209/0295-5075/ae3f4f (different event-triggered protocol).
