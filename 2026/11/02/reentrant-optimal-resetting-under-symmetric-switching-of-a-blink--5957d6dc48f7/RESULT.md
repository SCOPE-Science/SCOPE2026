# Reentrant optimal resetting under symmetric switching of a blinking Brownian target

## Finding

For one-dimensional Brownian search with Poisson resetting and a target that switches symmetrically between perfectly active and transparent states, the optimal resetting rate is necessarily **nonmonotone** in the target's switching speed, although its stationary active duty cycle stays exactly one half. The result provides rigorous singular-limit optimizer asymptotics, not merely numerical minimizers.

Let \(x_b\) be the unique positive zero of \(e^{x_b}(x_b-2)+2=0\), and let \(x_s\) be the unique positive zero of \(2e^{x_s}(x_s-2)+3+x_s/2=0\). Then \(x_s>x_b\), with \(x_b=1.5936242600\ldots\) and \(x_s=1.6244614337\ldots\).

Writing \(h=\gamma \ell^2/D\) for the dimensionless gate-switching speed and \(x_h=\ell\sqrt{r_*/D}\) for an optimal Poisson reset rate, the global minimizer is unique for sufficiently small positive \(h\) and for sufficiently large \(h\), and satisfies

\[
x_h=x_s-d_s h+O(h^2)\quad(h\downarrow0),\qquad
x_h=x_b-\frac{x_b}{\sqrt{2h}}+O(h^{-1})\quad(h\to\infty),
\]
where
\[
d_s=\frac{x_s^2+2x_s-4}{2x_s(2-x_s)\,[2e^{x_s}(x_s-1)+1/2]}>0
=0.2262351716\ldots.
\]
In particular, every optimal choice is above \(x_b\) in the slow-switching limit but below \(x_b\) for sufficiently fast finite switching; it subsequently approaches \(x_b\) from below. This proves reentrant dependence without claiming a unique intermediate turning point or uniqueness for every finite \(h\).

## Assumptions and scope

A particle follows Brownian motion of generator \(D\partial_{xx}\) on the real line, where \(D>0\), starting at and independently resetting to a fixed position \(\ell>0\) at Poisson rate \(r>0\). A target at the origin switches between an active absorbing state and an inactive transparent state at equal, strictly positive continuous-time transition rates \(\gamma\). Its initial state is stationary (active probability one half). The target's internal state is **not** changed at particle resets. Particle motion, resets, and target switching are independent until absorption. Define \(x=\ell\sqrt{r/D}\) and \(h=\gamma\ell^2/D\). The dimensionless mean absorption time is \(T_h(x)=(D/\ell^2)\mathbb E\tau\).

The exact mean-time formula is already known from Mercado-Vásquez and Boyer (2021, Eq. 26); in these symmetric coordinates it reads, for \(x,h>0\), with \(s=\sqrt{x^2+2h}\),
\[
T_h(x)=\frac{(1+x/s)e^x-1}{x^2}+\frac{x e^{x-s}}{2hs}
=\frac{e^x-1}{x^2}+\frac{e^x}{xs}+\frac{x e^{x-s}}{2hs}.
\]
The **new evaluated claim** concerns the global minimizer's two boundary regimes and their rigorous incompatibility with monotone variation under *simultaneous equal-rate changes* of the two gate transitions. It does not claim discovery of the known mean-time formula.

## Proof

**1. Existence and uniform coercivity.** Put \(B(x)=(e^x-1)/x^2\), which diverges both as \(x\downarrow0\) and \(x\to\infty\). The exact formula shows \(T_h(x)\ge B(x)\), so for fixed \(h>0\), at least one global minimizer exists. For the rare-switch limit one must control minimizers even though \(T_h\) diverges as \(1/(2h)\). Write \(E_h=T_h-1/(2h)\) and \(\delta=s-x=2h/(s+x)\). Since \(e^{-\delta}\ge1-\delta\),
\[
\frac{1-(x/s)e^{-\delta}}{2h}\le \frac{1+x}{s(s+x)},
\]
so
\[
E_h(x)-B(x)=\frac{e^x}{xs}-\frac{1-(x/s)e^{-\delta}}{2h}
\ge\frac{e^x(s+x)-x(1+x)}{xs(s+x)}\ge0.
\]
The last inequality holds because \(s+x>x\) and \(e^x\ge1+x\). Thus \(E_h\ge B\) uniformly; since \(E_h(x_s)\) is bounded as \(h\downarrow0\), all global rare-limit minimizers lie in one compact subinterval of \((0,\infty)\). For \(h\to\infty\), the same argument with \(T_h\ge B\) and \(T_h(x_b)\to B(x_b)\) gives a compact family of minimizers.

**2. Rare-switching limit.** Uniformly on each compact positive \(x\)-interval, with two derivatives in \(x\), Taylor expansion in \(h\) yields
\[
E_h(x)=H(x)+hJ(x)+O(h^2),\quad
H(x)=\frac{2e^x-3/2}{x^2}-\frac1{2x},\quad
J(x)=\frac{x^2+3x+3-4e^x}{4x^4}.
\]
Set \(N(x)=2e^x(x-2)+3+x/2\). Then \(H'(x)=N(x)/x^3\), \(N(0)=-1\), \(N'(0)=-3/2\), \(N''(x)=2xe^x>0\) for \(x>0\), and \(N(2)=4\). Therefore \(N\) first decreases and then increases across exactly one positive zero \(x_s\in(3/2,2)\). The function \(H\) has a unique strict global minimum there, with \(H''(x_s)=N'(x_s)/x_s^3>0\). Compactness and convergence of \(E_h\) imply every global minimizer tends to \(x_s\). The implicit-function theorem applied to \(\partial_x E_h=0\), plus strict local convexity and global compactness, gives its uniqueness for sufficiently small \(h\). Expanding the stationarity equation gives \(x_h=x_s-J'(x_s)h/H''(x_s)+O(h^2)\). Substitution of \(N(x_s)=0\) simplifies the coefficient to the displayed \(d_s\); because \(x_s>\sqrt5-1\) and \(x_s<2\), all factors proving \(d_s>0\) are positive.

**3. Fast-switching limit.** Uniformly with two \(x\)-derivatives on compact positive intervals,
\[
T_h(x)=B(x)+\frac{e^x}{x\sqrt{2h}}+O(h^{-3/2}).
\]
The derivative of \(B\) is \(B'(x)=[e^x(x-2)+2]/x^3\). Its numerator decreases once and increases once, has the unique positive zero \(x_b\in(1,2)\), and \(B''(x_b)=e^{x_b}(x_b-1)/x_b^3>0\). Compactness, uniform convergence and the implicit-function theorem imply uniqueness of the global minimizer for sufficiently large \(h\) and its expansion
\[
x_h=x_b-\frac{1}{\sqrt{2h}}
\frac{(e^x/x)'\vert_{x=x_b}}{B''(x_b)}+O(h^{-1})
=x_b-\frac{x_b}{\sqrt{2h}}+O(h^{-1}).
\]
The last identity is exact, not a numerical approximation.

**4. Genuine reentrance.** At \(x_b\), the rare-limit derivative numerator satisfies \(N(x_b)=x_b/2-1<0\), using the defining equation for \(x_b\); hence \(x_s>x_b\). All sufficiently small positive \(h\) have a unique minimizer above \(x_b\), while all sufficiently large finite \(h\) have a unique minimizer below \(x_b\) and converge to \(x_b\) from below. No monotone selection of optimal rates over the full positive \(h\)-axis is possible. The conclusion requires no claim about a single minimum or uniqueness throughout intermediate switching speeds.

## Verification

The standalone standard-library program `verify.py` reproduces the source mean-time formula in two algebraically different forms, checks its independent derivative across randomized parameters, tests the compact asymptotic expansions and numerical optimizer predictions, and checks representative intermediate global values. Its completed run passed **1411 finite assertions**. These tests do not replace any analytic argument for global uniqueness or the singular limits. They do not certify exhaustive behavior for intermediate \(h\).

## Relationship to prior work

Mercado-Vásquez and Boyer (2021, Eq. 26) already derive the exact mean first-passage time for the equivalent 1D reflecting/transparent gate specialization. They discuss numerical optimal resetting and nonmonotonic optimal-rate behavior when one transition rate changes with the other held fixed. Those results are not claimed here. Żbik and coauthors (2025) analyze the full-line blinking-target resetting setting and its hitting-time laws, including the exact mean-time formula, without establishing the symmetric fixed-duty-cycle optimizer's rare/fast-switching expansions or the above analytic reentrance. The novel part is precisely the simultaneous symmetric-speed perturbation with stationary gate occupation held fixed at one half and the uniform/global proof for the two singular optimizer branches.

## Limitations

There is no proof here of uniqueness or of a unique turning point for arbitrary intermediate switching speed. The asymptotics hold for fixed \(D,\ell\) and equal gate transition rates; they are not uniform as \(D\) or \(\ell\) vary in singular ways. No resetting of the gate state, partial absorption, drift, finite interval, or non-Poisson resetting is covered. Reentrance follows from comparison of proven singular limits and does not assert a full finite-parameter phase diagram. Other general renewal-optimization results could imply special cases; mathematical priority remains subject to independent literature review.

## References

1. A. G. Mercado-Vásquez and D. Boyer, *Search of stochastically gated targets with diffusive particles under resetting*, arXiv:2107.02148 (first submitted 2021), particularly Eq. 26 and its reset-rate optimization discussion; https://arxiv.org/abs/2107.02148.
2. K. Żbik, B. Dybiec, K. Capała, Z. Palmowski and I. M. Sokolov, *Hitting the blinking target under stochastic resetting*, arXiv:2512.09739v1 (2025-12-10), main text and Appendix B; https://arxiv.org/abs/2512.09739.
