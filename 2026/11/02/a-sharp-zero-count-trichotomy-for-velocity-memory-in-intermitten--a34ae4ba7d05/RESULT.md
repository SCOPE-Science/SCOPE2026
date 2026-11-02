# A sharp zero-count trichotomy for velocity memory in intermittent reversing swimmers

## Finding
For the stationary two-dimensional exponential run--turn process defined below, write \(c\in[-1,1]\) for the mean cosine of the turning-angle jump, \(\alpha,\beta>0\) for the run-to-turn and turn-to-run rates, and \(d_r,d_t\geq0\) for angular diffusivities in the two states. Set
\[
a=\alpha+d_r,\qquad b=\beta+d_t,\qquad
\Delta=(a-b)^2+4\alpha\beta c.
\]
The active-velocity autocorrelation \(C(t)\), for positive lag \(t\), has the following **exhaustive zero-count classification**:

1. If \(c\geq0\), or \(c<0\), \(a<b\), and \(\Delta\geq0\), then \(C(t)>0\) at every finite \(t\geq0\), with no zeros.
2. If \(\Delta<0\), then \(c<0\), and \(C(t)\) has infinitely many simple positive zeros, alternating its sign across consecutive zeros. They are equally spaced by \(2\pi/\sqrt{-\Delta}\).
3. If \(c<0\), \(a>b\), and \(\Delta\geq0\), then \(C(t)\) has exactly one simple positive zero, changing from positive to negative.

In particular, for exact reversal by angle \(\pi\) at each resumption, and no angular diffusion, put \(h=\alpha/\beta\). The complete trichotomy is
\[
\begin{cases}
0<h\leq3-2\sqrt2 &: \text{no zero},\\
3-2\sqrt2<h<3+2\sqrt2 &: \text{infinitely many zeros},\\
h\geq3+2\sqrt2 &: \text{exactly one zero}.
\end{cases}
\]
For instance, at \(\alpha=\beta=1\), \(c=-1\), and \(d_r=d_t=0\), the normalized correlation is \(e^{-t}\cos t\), exhibiting an infinite sequence of sign reversals despite memoryless run and pause durations. These sharp boundaries hold for every positive swimming speed and any independent nonnegative translational diffusivity. Since the equilibrium mean-squared displacement obeys \(m_2''(t)=2C(t)\) for \(t>0\), they also classify sign changes of the mean-squared displacement's curvature.

## Assumptions and scope
Let \(S_t\in\{r,t\}\) be an irreducible two-state continuous-time Markov chain, changing from a run to a turn at rate \(\alpha>0\) and back at rate \(\beta>0\). While running, the particle has deterministic propulsion velocity \(v(\cos\theta_t,\sin\theta_t)\), where \(v>0\); during turns the propulsion velocity is zero. Within state \(j\in\{r,t\}\), the orientation obeys angular Brownian diffusion \(d\theta=\sqrt{2d_j}\,dB_t\), with \(d_j\geq0\). Run-to-turn transitions preserve the orientation. At each turn-to-run transition the orientation receives a fresh independent angular increment \(\chi\) with a symmetric distribution on the circle, independent of the state chain and Brownian motions. Its first cosine moment is \(c=\mathbb E[\cos\chi]\in[-1,1]\), and symmetry ensures \(\mathbb E[\sin\chi]=0\). Independent planar translational Brownian diffusion with diffusivity \(D\geq0\) may be included in the position without altering the regular active-velocity correlation at nonzero lag.

The internal state is initialized stationarily, with \(\mathbb P(S_0=r)=\beta/(\alpha+\beta)\), and the initial orientation is uniform on the circle. Write \(V_t=v\mathbf 1_{\{S_t=r\}}(\cos\theta_t,\sin\theta_t)\) and \(C(t)=\mathbb E[V_0\cdot V_t]\) for \(t\geq0\); delta-correlated translational noise is excluded from this regular correlation. No bounded domain, interaction, external torque, or confinement is assumed.

## Proof
**1. First angular harmonic.** Starting from a run, define \(u_r(t)\) as the expectation of \(\cos(\theta_t-\theta_0)\mathbf 1_{\{S_t=r\}}\). Starting from a turn, define \(u_t(t)\) analogously, with the same future-event rules. The first Fourier mode decays at rate \(d_r\) or \(d_t\) within each motility state and is multiplied by \(c\) at each turn-to-run jump. Backward conditioning on the first transition therefore gives the exact linear system
\[
\frac{d}{dt}\binom{u_r}{u_t}=
\begin{pmatrix}-a&\alpha\\\beta c&-b\end{pmatrix}
\binom{u_r}{u_t},\qquad (u_r(0),u_t(0))=(1,0).
\]
The stationary speed prefactor consequently gives
\[
C(t)=v^2\frac{\beta}{\alpha+\beta}u_r(t).
\]
The elimination equation is \(u_r''+(a+b)u_r'+(ab-\alpha\beta c)u_r=0\), with \(u_r(0)=1\), \(u_r'(0)=-a\). Equivalently, its Laplace transform is
\[
\widehat u_r(z)=\frac{z+b}{(z+a)(z+b)-\alpha\beta c}.
\]

**2. Complete exact correlation.** For \(\Delta>0\), with \(\delta=\sqrt\Delta\), inverse transformation yields
\[
u_r(t)=e^{-(a+b)t/2}\left[\cosh\frac{\delta t}{2}+\frac{b-a}{\delta}\sinh\frac{\delta t}{2}\right].
\]
For \(\Delta=0\), it yields \(u_r(t)=e^{-(a+b)t/2}[1+(b-a)t/2]\). For \(\Delta<0\), put \(\omega=\sqrt{-\Delta}\), obtaining
\[
u_r(t)=e^{-(a+b)t/2}\left[\cos\frac{\omega t}{2}+\frac{b-a}{\omega}\sin\frac{\omega t}{2}\right].
\]
All formulas are continuous at the repeated-root case \(\Delta=0\).

**3. Root classification.** If \(c\geq0\), the off-diagonal entries of the harmonic matrix are nonnegative; its exponential has nonnegative entries, and paths without any state change give \(u_r(t)\geq e^{-at}>0\). If \(\Delta<0\), the cosine--sine bracket is a nonzero sinusoid whose initial value is one. Its first zero and all later zeros are explicitly
\[
t_n=\frac{2}{\omega}\left[\frac\pi2+\arctan\!\left(\frac{b-a}{\omega}\right)+n\pi\right],\qquad n=0,1,2,\ldots.
\]
Every zero is positive and simple, with alternating signs.

It remains to consider \(c<0\), \(\Delta\geq0\). In that regime \((a-b)^2\geq-4\alpha\beta c>0\), hence \(a\ne b\) and \(0\leq\sqrt\Delta<|a-b|\). If \(a<b\), the coefficient \((b-a)/\sqrt\Delta\), where defined, is positive; both hyperbolic terms (or the repeated-root linear term) stay strictly positive. If \(a>b\), the coefficient is strictly less than \(-1\), so the hyperbolic bracket crosses zero exactly once, from positive to negative. Its crossing is
\[
t_*=\begin{cases}
\dfrac{2}{\sqrt\Delta}\operatorname{artanh}\!\left(\dfrac{\sqrt\Delta}{a-b}\right),&\Delta>0,\\[4pt]
\dfrac{2}{a-b},&\Delta=0.
\end{cases}
\]
The crossing is simple: its derivative cannot vanish there, since otherwise uniqueness for the homogeneous second-order ODE would contradict \(u_r(0)=1\). This exhausts all signs and all parameter boundaries.

**4. Exact sharp-rate corollary and displacement curvature.** For \(d_r=d_t=0\) and \(c=-1\), the discriminant is \(\Delta=\beta^2(h^2-6h+1)\), whose two positive roots are \(3\pm2\sqrt2\). At the smaller root, \(a<b\) and hence there is no zero; at the larger root, \(a>b\) and there is one zero. This determines the inclusive boundary cases, not merely the generic regimes. For stationary, isotropic propulsion, and independent translational diffusion, the exact Green--Kubo identity is
\[
m_2(t)=4Dt+2\int_0^t(t-s)C(s)\,ds,
\]
whose second derivative for positive lag is \(2C(t)\). For \(ab-\alpha\beta c>0\), the long-time diffusivity is finite and equals
\[
D_{\mathrm{eff}}=D+\frac{v^2\beta b}{2(\alpha+\beta)(ab-\alpha\beta c)}.
\]
The only exception to this finite-diffusivity formula within the permitted parameters is \(c=1\), \(d_r=d_t=0\), when direction persistence causes ballistic growth.

## Verification
The accompanying standalone `verify.py` independently compares the three closed correlation formulas with numerical matrix exponentials over a parameter grid, checks exact repeated-eigenvalue boundaries, independently derives the zero-lag Laplace integral from a matrix inverse, and compares against a four-state physical jump generator for directional changes by \(0\) or \(\pi\). All **2,730** assertions passed with the stated floating-point tolerances. These tests corroborate the finite evaluations; the all-parameter zero-count conclusion follows from the analytic proof, not numerical enumeration. Reproduce with `python verify.py` in an environment with NumPy and SciPy.

## Relationship to prior work
Datta, Beta and Großmann (2024), especially their Secs. II--V and Eqs. (15)--(16), give the general run--turn renewal velocity-correlation transform and explain dependence on the first angular Fourier moment. This result does **not** claim that transform or the underlying model as new. Instead, specializing to finite exponential run and pause durations produces a sharp global *sign and zero-count* classification, including a distinct always-positive antipersistent sector, an infinite-oscillation sector, a single-crossing sector, and exact algebraic boundaries. The source paper did not state this classification.

Peruani and Chaudhuri's stop--go models (arXiv:2306.05647) contain exact velocity autocorrelations for several state-specific orientation rules; their displayed formulas and fixed-orientation reset models do not supply the negative first-Fourier jump sector with the above full trichotomy. Großmann, Peruani and Bär (arXiv:1511.04542) already exhibit oscillatory correlations for constant-speed directional reversals with an internal multistep clock; oscillations themselves are therefore **not** asserted to be novel. Seyrich and coauthors (arXiv:1805.08860) model finite tumble events with stochastic speed recovery and angular diffusion but not the stated zero-count diagram. This theorem is a closed-form specialization of a stronger general transform, not an independent general-renewal transport theory.

## Limitations
This is an exact result only for independent exponential run and turn durations, symmetric iid turning-angle jumps, independent angular diffusion, spatially homogeneous trajectories, and stationary motility-state initialization. It does not classify general renewal waiting times, nonlinear confined dynamics, collective interactions, asymmetric turns, or time-varying parameters. The sign of the regular active-velocity correlation does not imply the sign of the full distribution's excess kurtosis or any mean-current reversal. Published general renewal formulas provide broad coverage of the underlying observable; priority for the particular complete algebraic sign classification has not been independently certified.

## References
1. A. Datta, C. Beta and R. Großmann, *The random walk of intermittently self-propelled particles*, arXiv:2406.15277v1 (first posted 21 June 2024). https://arxiv.org/html/2406.15277v1
2. F. Peruani and D. Chaudhuri, *Active stop and go motion: a strategy to improve spatial exploration?*, arXiv:2306.05647v1 (first posted 9 June 2023); later published as *Active stop and go motion: A strategy to improve spatial exploration and survival*. https://arxiv.org/pdf/2306.05647
3. R. Großmann, F. Peruani and M. Bär, *Diffusion properties of active particles with directional reversal*, arXiv:1511.04542v3 (2016). https://arxiv.org/pdf/1511.04542
4. M. Seyrich, Z. Alirezaeizanjani, C. Beta and H. Stark, *Statistical parameter inference of bacterial swimming strategies*, arXiv:1805.08860v1 (2018). https://arxiv.org/pdf/1805.08860
