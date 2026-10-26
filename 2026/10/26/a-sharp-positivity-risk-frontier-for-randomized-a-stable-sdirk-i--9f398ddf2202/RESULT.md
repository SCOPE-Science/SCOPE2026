# A sharp positivity-risk frontier for randomized A-stable SDIRK integration

## Finding

The two-stage singly diagonally implicit Runge–Kutta family with random parameter \(\xi\in[1/2,1]\) has a complete scalar sign-loss phase diagram and a sharp extremal law when the randomization is constrained to retain the formal third-order Runge–Kutta conditions in expectation.

Define its tableau, with independently sampled parameters at successive steps, by
\[
\begin{array}{c|cc}
\xi&\xi&0\\
1-\xi&1-2\xi&\xi\\\hline
&1/2&1/2
\end{array}.
\]
For the positive decaying scalar solution \(y'=-\lambda y\), \(y(0)>0\), let \(s=h\lambda>0\) and denote the one-step multiplier by \(R_s(\xi)\). Write \(\mathcal P\) for a probability law supported on \([1/2,1]\) satisfying
\[
\mathbb E_{\mathcal P}(\xi-1/2)^2=1/12.
\]
This condition is equivalent to **both** formal third-order RK order identities holding in expectation; it does not by itself guarantee the low-regularity convergence result proved for uniform sampling in the motivating paper.

Set \(s_*=2.2458294939508742326\ldots\), the unique positive root of
\[
2+\frac{2s}{\sqrt3}-\left(\frac13+\frac1{\sqrt3}\right)s^2=0,
\]
and for \(2<s\le 1+\sqrt3\) put
\[
r_s=1-\frac1s+\sqrt{\frac{s-2}{2s}},\qquad a_s=(r_s-1/2)^2.
\]
Then the **sharp achievable negative-step probability**, with the infimum over all laws satisfying the moment constraint, is
\[
\boxed{
\inf_{\mathcal P}\Pr_{\mathcal P}\{R_s(\xi)<0\}=
\begin{cases}
0,&0<s\le s_*,\\
1-\dfrac1{12a_s},&s_*<s\le1+\sqrt3,\\
1,&s>1+\sqrt3.
\end{cases}}
\]
For \(s_*<s\le1+\sqrt3\), equality is attained by a two-point sampling law supported at \(1/2\) and \(r_s\), with probabilities \(1-1/(12a_s)\) and \(1/(12a_s)\), respectively. At the upper endpoint the second atom has zero, rather than positive, amplification. A moment-admissible law with strictly positive one-step amplification almost surely exists if and only if \(s<s_*\); genuinely nondegenerate two-point laws exist throughout this open range. At \(s=s_*\), the only law with no negative amplification is the point mass at \(\xi=1/2+1/\sqrt{12}\), which has zero amplification.

For the original independent uniform draws \(\xi_k\sim\mathcal U(1/2,1)\), the exact probability of a negative multiplier is
\[
\boxed{p(s)=\begin{cases}
0,&0<s\le2,\\
1-\dfrac2s+\sqrt{\dfrac{2(s-2)}s},&2<s<1+\sqrt3,\\
1,&s\ge1+\sqrt3.
\end{cases}}
\]
In the mixed regime \(2<s<1+\sqrt3\), the first negative iterate index \(T=\min\{n\ge1:y_n<0\}\) is geometric with parameter \(p(s)\), and
\[
\Pr(y_n<0)=\frac{1-(1-2p(s))^n}{2},\qquad
\Pr(T>n)=(1-p(s))^n.
\]
Although \(y_n\to0\) at a deterministic geometric envelope for every fixed \(s>0\), its sign changes infinitely often almost surely throughout the mixed regime. As \(s=2+\delta\downarrow2\),
\[
p(2+\delta)=\sqrt\delta+\frac\delta2+O(\delta^{3/2}),\qquad
\sqrt\delta\,T\ \Rightarrow\ \operatorname{Exp}(1).
\]
The square-root onset comes from tangency of the multiplier zero at the endpoint \(\xi=1/2\). More generally, for iid draws with \(\Pr\{\xi-1/2<u\}\sim c u^q\) as \(u\downarrow0\), with \(c,q>0\) and no atom at the endpoint, the negative-step probability satisfies \(p(2+\delta)\sim c2^{-q}\delta^{q/2}\), and \(\delta^{q/2}T\Rightarrow\operatorname{Exp}(c2^{-q})\).

## Assumptions and scope

The ODE is scalar, autonomous, linear, with \(\lambda>0\), fixed step \(h>0\), strictly positive initial state, and independent draws between steps. Every draw lies in \([1/2,1]\). The extremal sampling result concerns all probability measures with the displayed single moment constraint (atoms are permitted); the explicit geometric laws concern the published uniform sampler. Probabilities are for exact arithmetic. Strict positivity, nonnegativity and negative amplification are distinguished at isolated zero-amplification endpoints.

The moment condition is necessary and sufficient for **expectations of the two formal third-order RK conditions**; no higher-order convergence for arbitrary moment-admissible distributions is asserted. For other samplers, the edge-tail asymptotic additionally assumes the indicated CDF behavior and independence across steps.

## Proof

**1. Exact multiplier and monotonicity.** The stage equations on \(y'=-\lambda y\) solve triangularly. With \(s=h\lambda\) and deterministic parameter \(x\), the exact amplification is
\[
R_s(x)=\frac{2+(4x-2)s+(2x^2-4x+1)s^2}{2(1+sx)^2},
\qquad
\frac{\partial R_s(x)}{\partial x}=\frac{s^3(2x-1)}{(1+sx)^3}.
\]
Thus \(R_s\) increases strictly on \((1/2,1]\). Its endpoint values are
\[
R_s(1/2)=\frac{2-s}{2+s},\qquad
R_s(1)=\frac{2+2s-s^2}{2(1+s)^2}.
\]
Therefore it is nonnegative for every parameter when \(0<s\le2\), has both signs when \(2<s<1+\sqrt3\), and is strictly negative for all parameters when \(s>1+\sqrt3\). At the upper endpoint only \(x=1\) has zero amplification. Solving the quadratic numerator gives the unique zero in \((1/2,1)\) as \(r_s\) in the stated mixed interval; a draw is negative exactly for \(x<r_s\). At \(s=2\) the only zero lies at \(x=1/2\).

**2. Exact order-moment equivalence.** For this tableau, the two third-order Runge–Kutta expressions are
\[
b^{\mathsf T}c^{\circ2}=(x-1/2)^2+1/4,
\qquad b^{\mathsf T}Ac=1/4-(x-1/2)^2.
\]
Their third-order targets are \(1/3\) and \(1/6\), respectively. Taking expectations, each identity is equivalent to \(\mathbb E(\xi-1/2)^2=1/12\).

**3. Sharp extremal sampling law.** Put \(U=(\xi-1/2)^2\in[0,1/4]\), so \(\mathbb E U=m=1/12\). In the mixed regime a negative multiplier is equivalent to \(U<a_s\). If \(p=\Pr(U<a_s)\), then
\[
m=\mathbb E U\ge a_s\Pr(U\ge a_s)=a_s(1-p),
\]
so \(p\ge\max\{0,1-m/a_s\}\). If \(a_s\le m\), the point law at \(U=m\) attains zero negative probability. If \(a_s>m\), the two-point law \(\Pr(U=0)=1-m/a_s\), \(\Pr(U=a_s)=m/a_s\) attains equality. These are exactly the sampling laws stated in the finding. Since \(r_s\) increases strictly, \(a_s=m\) has one solution, obtained by substituting \(x=1/2+1/\sqrt{12}\) into the numerator of \(R_s(x)\); this is \(s_*\). At \(s=1+\sqrt3\), the same proof applies with \(a_s=1/4\), yielding the sharp value \(2/3\). For greater \(s\), all multipliers are negative, yielding value one. For \(s<s_*\), two distinct parameters arbitrarily close to, and on opposite sides of, \(1/2+1/\sqrt{12}\) can be mixed with positive probabilities to meet \(\mathbb E U=m\), while remaining above \(r_s\); hence genuine randomization with strictly positive amplification is possible. At \(s=s_*\), any law avoiding negativity must have \(U\ge m\) almost surely and \(\mathbb E U=m\), hence \(U=m\) almost surely; its multiplier is zero.

**4. Uniform first-passage and critical scaling.** The uniform density on \([1/2,1]\) is two. Consequently \(p(s)=2(r_s-1/2)\) on the mixed interval. In the lower and upper regimes it is respectively zero and one, up to null endpoints. At every step, the sign changes exactly on a negative multiplier, independently of all preceding signs, and the negative-multiplier events are iid Bernoulli with parameter \(p(s)\). The geometric first-hitting formula follows, and the parity-generating identity \(\mathbb E[(-1)^{N_n}]=(1-2p)^n\) yields the displayed negative-sign probability. In the mixed regime, both event types have positive probability and occur infinitely often almost surely. The endpoint expansion
\[
r_{2+\delta}-1/2=\tfrac12\sqrt\delta+\tfrac14\delta+O(\delta^{3/2})
\]
proves the uniform square-root onset and exponential limit for the rescaled geometric waiting time. Replacing the uniform endpoint CDF by the displayed power law proves the general exponent and rate.

Finally, all fixed-parameter Runge–Kutta realizations are A-stable on this tableau interval (as proved in the cited source); for real \(s>0\), the displayed endpoint formulas and monotonicity also give directly
\[
|R_s(x)|\le q_s:=\max\left\{\left|\frac{2-s}{2+s}\right|,
\left|\frac{2+2s-s^2}{2(1+s)^2}\right|\right\}<1.
\]
Thus \(|y_n|\le q_s^n y_0\) on every sample path: persistent sign changes coexist with deterministic-magnitude decay.

## Verification

The standalone program `verify.py` uses only the Python standard library. Re-running `python3 verify.py` verifies 4,270 exact rational stage-versus-amplification identities and strict contractions, 1,056 derivative-sign evaluations, 20,100 rational sign-region cases, 126 moment-constrained two-atom extremal checks, 30 exact finite-length sign-parity laws, and 12 high-precision root/critical-edge checks. These finite checks are complementary to, not substitutes for, the universal arguments above. The proof requires no numerical search, machine-precision threshold, or unverified external certificate.

## Relationship to prior work

Eisenmann, Jans, Kruse and Podhaisky (2026, arXiv:2607.18928v1) introduced the exact randomized tableau, gave its rational stability function and proved algebraic/A-stability and convergence bounds for uniform sampling. The present result instead classifies exact **sign risk**, its first-passage scaling, and the sharp distributional optimization under expected third-order moment identities. Algebraic/A-stability alone controls magnitudes, not signs; those probability and extremal-measure claims are not stated in their Section 3, 5 or 8.

Bochacik and Przybyłowicz (arXiv:2404.19059, 2024) study different two-stage implicit randomized updates whose scalar multipliers are \(1+z/(1-z\tau)\); their stability-region analysis does not subsume the present tableau-specific law. The classical absolute-monotonicity and SSP literature gives monotonicity/step-size guarantees for deterministic methods and provides context, but no inspected source supplied the sharp moment-constrained probability envelope or the uniform first-sign critical law. The published rational multiplier makes parts of this result algebraically accessible, and independent priority confirmation remains warranted.

## Limitations

The result concerns scalar positive decay and the exact printed tableau, not componentwise positivity of arbitrary coupled semidiscretizations or nonlinear positive systems. A third-order **order-condition expectation** under arbitrary sampling laws is not a convergence-order theorem; changing the uniform law may forfeit the published low-regularity advantage. Extremizing negative probability permits zero multipliers at support atoms; thus minimal negative probability does not mean strict positive outputs. The support, independence and near-endpoint regular variation assumptions are essential to the stated probability and universality claims. No independent mathematical audit has been performed.

## References

1. M. Eisenmann, M. Jans, R. Kruse and H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge–Kutta Method*, arXiv:2607.18928v1, first submitted 2026-07-21. https://arxiv.org/html/2607.18928v1.
2. T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059 (initially submitted 2024-04-29). https://arxiv.org/pdf/2404.19059.
3. M. N. Spijker, *Stepsize Conditions for General Monotonicity in Numerical Initial Value Problems*, SIAM J. Numer. Anal. 45 (2007), 1226–1245, doi:10.1137/060661739.
4. J. F. B. M. Kraaijevanger, *Contractivity of Runge–Kutta methods*, BIT 31 (1991), 482–528.
