# A sharp reset-distance threshold for reentrant first-passage fluctuations

## Finding

Let a Brownian particle on the positive half-line be absorbed upon hitting zero, start at distance \(a>0\), and independently relocate to a *fixed* distance \(b>0\) at Poisson rate \(r>0\). The diffusion generator is \(D\partial_{xx}\), with \(D>0\). Write \(T\) for its absorption time, \(q=b/a\), \(t=a\sqrt{r/D}\), and \(\mathrm{CV}=\sqrt{\operatorname{Var}(T)}/\mathbb E T\).

Set
\[
H_q(t)=t e^{-(q-1)t}\left(q+\frac{1}{e^t-1}\right),\qquad q,t>0.
\]
Then the exact dispersion identity is
\[
\boxed{\mathrm{CV}^2-1=\frac{e^{-t}}{1-e^{-t}}\bigl(2-H_q(t)\bigr).}
\]
There exists one universal constant \(q_c\in(1,2)\), uniquely specified by the tangency system
\[
H_{q_c}(t_c)=2,\quad \partial_tH_{q_c}(t_c)=0,\quad t_c>0,
\]
with numerical values \(q_c\approx1.2286314004819505853\) and \(t_c\approx4.1334526383049528347\), such that the **complete classification of positive reset-rate crossings of \(\mathrm{CV}=1\)** is:

1. For \(0<q\le1\), exactly one simple crossing, from \(\mathrm{CV}>1\) to \(\mathrm{CV}<1\) as \(r\) increases.
2. For \(1<q<q_c\), exactly two simple crossings; the sign pattern is \(\mathrm{CV}>1\), then \(\mathrm{CV}<1\), then \(\mathrm{CV}>1\).
3. For \(q=q_c\), exactly one tangency, at \(r=(D/a^2)t_c^2\); \(\mathrm{CV}\ge1\) for every positive rate.
4. For \(q>q_c\), \(\mathrm{CV}>1\) for every positive rate.

In particular, when \(b/a=6/5\), the two crossover values of \(t\) are approximately \(2.6933350688347923\) and \(7.5670326443933131\). The corresponding physical rates are \(r=(D/a^2)t^2\). The two-crossing phenomenon disappears if the reset site is sufficiently far from the initial site.

## Assumptions and scope

The process evolves as \(dX_s=\sqrt{2D}\,dB_s\) between resets and is stopped upon hitting zero. At each jump of an independent rate-\(r\) Poisson process before absorption, its position is set to \(b\), even though the deterministic initial position is \(a\). All parameters \(a,b,D,r\) are strictly positive. The reset clock is independent of the Brownian motion and the process is absorbing rather than reflecting at zero. Both \(\mathbb ET\) and \(\mathbb ET^2\) are finite for each \(r>0\); this follows, for instance, because every reset-bounded attempt has strictly positive probability of absorption before the next reset.

The initial and post-reset positions are deliberately distinguished. An average over a distribution of initial positions that is identical to the reset distribution is a *different* first-passage ensemble and is not covered by the classification as stated.

## Proof

**1. The two moments.** The free Brownian first-hit Laplace transform from a distance \(x>0\) is \(\exp(-x\sqrt{s/D})\). A first-reset renewal decomposition, with one initial distance \(a\) and every subsequent reset distance \(b\), gives the Laplace transform of the survival function:
\[
\widehat S(s)=\int_0^\infty e^{-su}\mathbb P(T>u)\,du
=\frac{1-e^{-a\sqrt{(s+r)/D}}}{s+r e^{-b\sqrt{(s+r)/D}}},\qquad s\ge0.
\]
In particular, \(\mathbb ET=\widehat S(0)\) and \(\mathbb ET^2=-2\widehat S'(0)\). Differentiation yields
\[
\mathbb ET=\frac{e^{qt}(1-e^{-t})}{r},
\]
\[
\mathbb ET^2=\frac{2e^{2qt}(1-e^{-t})-qt e^{qt}(1-e^{-t})-t e^{(q-1)t}}{r^2}.
\]
Subtracting \(2(\mathbb ET)^2\) from the second moment and dividing by \((\mathbb ET)^2\) gives the claimed identity for \(\mathrm{CV}^2-1\). This step fixes both the dimensional normalization and the sign convention; the prefactor is strictly positive for all \(t>0\).

**2. One crossing for \(q\le1\).** The function \(H_1(t)=t/(1-e^{-t})\) increases strictly from \(1\) to \(\infty\), since \(e^t>1+t\) for positive \(t\). For \(0<q<1\), the exact ratio
\[
\frac{H_q(t)}{H_1(t)}=q e^{(1-q)t}+(1-q)e^{-qt}
\]
has a strictly positive derivative \(q(1-q)(e^{(1-q)t}-e^{-qt})\) for \(t>0\). Thus \(H_q\) also increases strictly from \(1\) to infinity and passes through \(2\) exactly once.

**3. Strict logarithmic concavity for \(q\ge1\).** Put \(z=(e^t-1)^{-1}>0\). Direct differentiation gives
\[
\frac{d^2}{dt^2}\log H_q(t)
=-\frac1{t^2}+\frac{z(1+z)[q(1+2z)+z^2]}{(q+z)^2}.
\]
At each fixed \(z>0\), the rational factor \([q(1+2z)+z^2]/(q+z)^2\) strictly decreases in \(q\ge1\), since its derivative has the sign of \(z-q(1+2z)<0\). Its maximum occurs at \(q=1\), where it equals \(1\). Consequently
\[
\frac{d^2}{dt^2}\log H_q(t)
\le-\frac1{t^2}+z(1+z)
=-\frac1{t^2}+\frac1{4\sinh^2(t/2)}<0,
\]
because \(2\sinh(t/2)>t\). Thus \(H_q\) is strictly log-concave for all \(q\ge1\). For \(q>1\) it starts at \(H_q(0+)=1\), has derivative \(H_q'(0+)=1/2\), and tends to zero at infinity. It therefore has exactly one strict interior maximum. Any level-\(2\) crossings number zero, one tangency, or two simple crossings, according as that maximum is below, equal to, or above \(2\).

**4. Uniqueness of the reset-distance threshold.** For every fixed \(t>0\),
\[
\partial_q\log H_q(t)=\frac1{q+(e^t-1)^{-1}}-t<0\qquad(q\ge1),
\]
using \(1-e^{-t}<t\). Hence \(M(q)=\max_{t>0}H_q(t)\) is continuous and strictly decreasing for \(q>1\). Its limit at \(q\downarrow1\) is infinite: taking a sufficiently large fixed \(t\) in \(H_1(t)\), then letting \(q\downarrow1\), gives an arbitrarily high lower bound. At \(q=2\),
\[
H_2(t)=2t e^{-t}+\frac{t e^{-t}}{e^t-1}<\frac2e+1<2.
\]
The intermediate value theorem and strict monotonicity yield one and only one \(q_c\in(1,2)\) with \(M(q_c)=2\). Strict log-concavity gives a unique associated maximizing \(t_c\). Combining the four regimes with the positive prefactor in step 1 proves the entire classification.

## Verification

The accompanying `verify.py` checks two separate derivations: exact stationary backward-generator equations for the first two moments, and direct derivatives of the renewal survival transform in 48 high-precision parameter cases. It also evaluates the tangency residuals, the sign patterns in all four regimes, and logarithmic-curvature values for a mesh of parameters. The script outputs the approximate critical pair and two illustrative crossing points. These finite calculations verify identities and diagnostics but do not substitute for the analytic global uniqueness proof above.

Run in a Python environment with `sympy` and `mpmath` available:

```bash
python verify.py
```

## Relationship to prior work

Julián-Salgado, Dagdug and Boyer (arXiv:2311.11897, first released 20 November 2023) derive the survival transform and mean passage time for a Brownian searcher with two possible reset points and independently specified initial position. Setting one reset probability to zero produces the transform used in step 1, but their stated optimization results concern the *mean*, not a global coefficient-of-variation crossing classification. Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125, first released 2 January 2024) derive general first-passage transforms and study variation coefficients primarily after averaging the initial location over the same reset distribution. Their equations contain the underlying survival-transform ingredients but not the single-mismatched-start four-regime reset-distance theorem, the strict log-concavity lemma, or its unique universal threshold. Singh and Pal (arXiv:2202.02715v1, first released 6 February 2022) provide a general Feynman–Kac backward-generator framework for Brownian first-passage functionals with potentially distinct initial and reset positions; their Section 5.1 specializes the explicit first-passage density to equal initial/reset positions and does not classify mismatched-position coefficient-of-variation crossings. Abundo (arXiv:2505.19759v1, first released 26 May 2025) studies the same mismatched-position first-passage process, but optimizes only the mean absorption time, not its coefficient of variation. Reuveni's optimal-restart theorem concerns \(\mathrm{CV}=1\) at a mean-optimal *renewal* restart and does not provide the classification across all reset rates when the initial condition differs from the reset state.

The derivation explicitly acknowledges the preexisting full survival transform and does not claim to discover or rederive a new physical process. The candidate contribution is the global exact phase classification of dispersion signs, which requires an additional analytic shape theorem.

## Limitations

The result is confined to one-dimensional unbiased Brownian motion, a single perfectly localized Poisson reset destination, a fixed deterministic initial position, and an absorbing point. It does not classify arbitrary resetting distributions, non-Poisson clocks, biased diffusions, higher-dimensional targets, or observation-time truncations. The threshold and crossing counts follow from exact analysis, whereas displayed decimal numbers are approximations. No claim of independent review or definitive publication priority is made.

## References

1. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897v1 (2023), https://arxiv.org/abs/2311.11897. Relevant material: Sections II–III, especially the full Laplace survival transform (Eq. 3).
2. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1 (2024), https://arxiv.org/abs/2401.01125. Relevant material: Sections II and VII, especially Eqs. 6 and 60–61 and the initial-location averaging assumption.
3. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, J. Phys. A 44, 435001 (2011), arXiv:1107.4225, https://arxiv.org/abs/1107.4225.
4. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715v1 (2022), https://arxiv.org/abs/2202.02715. Relevant material: full Sections 2 and 5.1, Eq. 42 and the initial/reset-site distinction.
5. M. Abundo, *Minimization of the expected first-passage time of a Brownian motion with Poissonian resetting*, arXiv:2505.19759v1 (2025), https://arxiv.org/abs/2505.19759. Relevant material: full Section 2, especially mean Eq. 2.2 and the optimization discussion.
6. S. Reuveni, *Optimal stochastic restart renders fluctuations in first passage times universal*, Phys. Rev. Lett. 116, 170601 (2016), arXiv:1512.01600, https://arxiv.org/abs/1512.01600.
