# Gaussian first-exit crossover for randomly switched intermittent maps

## Finding

Fix exponents \(0<\alpha<\beta<\infty\) and a switching probability \(0<p<1\), and set \(q=1-p\), \(s=\beta/\alpha-1>0\). At each iteration choose, independently, the Liverani--Saussol--Vaienti intermittent map with exponent \(\alpha\) with probability \(p\), or the map with exponent \(\beta\) with probability \(q\). Start at \(x_0=\tfrac12 Z^{-1/\alpha}\), where \(Z>1\), and stop at its first exit from the neutral branch, \(\tau_Z=\min\{n\ge0:x_n\ge\tfrac12\}\).

The escape time obeys the following sharp three-regime limit as \(Z\to\infty\) (the randomness is solely the independent sequence of selected maps):

\[
\begin{array}{ll}
0<s<\tfrac12:&\displaystyle
\frac{\tau_Z-Z/(\alpha p)}{Z^{1-s}}\ \xrightarrow{\mathsf P}\ -\frac{q}{\alpha p^2(1-s)},\\[8pt]
s=\tfrac12:&\displaystyle
\frac{\tau_Z-Z/(\alpha p)}{\sqrt Z}\ \xRightarrow{}\
\mathcal N\!\left(-\frac{2q}{\alpha p^2},\frac{q}{\alpha p^2}\right),\\[8pt]
s>\tfrac12:&\displaystyle
\frac{\tau_Z-Z/(\alpha p)}{\sqrt Z}\ \xRightarrow{}\
\mathcal N\!\left(0,\frac{q}{\alpha p^2}\right).
\end{array}
\]

Here the second argument of \(\mathcal N\) is its variance. In every regime, \(\tau_Z/Z\xrightarrow{\mathsf P}1/(\alpha p)\). The critical exponent ratio \(\beta/\alpha=3/2\) is precisely where the accumulated drift due to slow-map choices matches the square-root Bernoulli sampling fluctuations. There are no claims of uniformity as \(p\), \(\alpha\), or \(\beta\) vary with \(Z\).

## Assumptions and scope

For each exponent \(\gamma>0\), the underlying interval map is
\[
T_\gamma(x)=\begin{cases}
x\bigl(1+2^\gamma x^\gamma\bigr),&0\le x<1/2,\\
2x-1,&1/2\le x\le1.
\end{cases}
\]
Only its neutral branch is used prior to \(\tau_Z\). Let \((\xi_n)_{n\ge0}\) be independent Bernoulli variables with \(\Pr(\xi_n=1)=p\); choose \(T_\alpha\) when \(\xi_n=1\), otherwise choose \(T_\beta\). All limits use the law of this common infinite driving sequence. No stationarity assumption, invariant measure, or randomness in \(x_0\) is required.

Write \(z_n=(2x_n)^{-\alpha}\) until first exit. Initially \(z_0=Z\), and \(x_n<1/2\) is equivalent to \(z_n>1\). The exact update for \(z_n>1\) is
\[
z_{n+1}=\begin{cases}
z_n(1+z_n^{-1})^{-\alpha},&\xi_n=1,\\
z_n(1+z_n^{-(1+s)})^{-\alpha},&\xi_n=0.
\end{cases}
\]
The resulting first exit is finite almost surely. Define the count \(K_n=\sum_{i=0}^{n-1}\xi_i\), the centered Bernoulli martingale \(M_n=K_n-pn\), and the accumulated slow-map weight
\[
S_Z=\sum_{i=0}^{\tau_Z-1}(1-\xi_i)z_i^{-s}.
\]

## Proof

**1. One-step expansion and a uniform weighted-occupation bound.** For \(u\ge1\) denote the decrements in the two branches by
\[
d_f(u)=u\left[1-(1+u^{-1})^{-\alpha}\right],\qquad
d_s(u)=u\left[1-(1+u^{-(1+s)})^{-\alpha}\right].
\]
The integral identity
\[
d_f(u)=\alpha\int_0^1(1+t/u)^{-\alpha-1}\,dt
\]
shows that \(c_\alpha:=\alpha 2^{-\alpha-1}\le d_f(u)\le\alpha\). Taylor's formula on \([0,1]\) gives the uniform bounds
\[
|d_f(u)-\alpha|\le C_\alpha u^{-1},\qquad
|d_s(u)-\alpha u^{-s}|\le C_{\alpha,s}u^{-1-2s},\qquad 0<d_s(u)\le\alpha u^{-s}.
\]
These are global inequalities for \(u\ge1\), not merely pointwise expansions at infinity.

For any \(t>0\) introduce the nonnegative potential \(H_t(u)=\int_0^u(1+v)^{-t}dv\). As long as \(z_i>1\), the fast branch decreases \(H_t\) by at least \(c_\alpha(1+z_i)^{-t}\). Conditioning on the past and stopping at \(\tau_Z\) therefore yields
\[
\mathbb E\sum_{i<\tau_Z}z_i^{-t}
\le\frac{2^t}{p c_\alpha}H_t(Z)
=\begin{cases}
O_t(Z^{1-t}),&t<1,\\
O_t(\log Z),&t=1,\\
O_t(1),&t>1.
\end{cases}\tag{1}
\]
Indeed \(z_i\ge1\) before exit, the final potential is nonnegative, and monotone convergence justifies the unbounded stopping time. The same bound applies conditionally after first entering \((1,\delta Z]\) for \(0<\delta<1\), with \(Z\) on the right replaced by \(\delta Z\). This is a genuine stopping-time estimate: the future switches are independent of the past.

Every fast choice decreases \(z_i\) by at least \(c_\alpha\), hence \(\tau_Z\) is bounded by the time needed to accumulate \(\lceil Z/c_\alpha\rceil\) fast choices. Consequently \(\tau_Z=O_{\mathsf P}(Z)\) and it is almost surely finite.

**2. A stopping identity and the fluid clock.** Summing the one-step expansions until exit, and applying (1) at \(t=1\) and \(t=1+2s\), gives
\[
z_{\tau_Z}=Z-\alpha K_{\tau_Z}-\alpha S_Z+E_Z,
\qquad E_Z=O_{\mathsf P}(\log Z).
\]
As \(0<z_{\tau_Z}\le1\), this is equivalent to the exact-order stopping relation
\[
\boxed{\displaystyle
\tau_Z=\frac{Z}{\alpha p}-\frac{S_Z}{p}-\frac{M_{\tau_Z}}p
+O_{\mathsf P}(\log Z).}\tag{2}
\]
The error bound is derived by summing absolute errors; it does not assume any independence between the state and the current stopping time.

By (1), \(S_Z=o_{\mathsf P}(Z)\). By the maximal inequality for centered independent Bernoulli sums, \(\sup_{n\le CZ}|M_n|=O_{\mathsf P}(\sqrt Z)\) for each fixed \(C\). Combining this with \(\tau_Z=O_{\mathsf P}(Z)\) and (2) gives \(\tau_Z/Z\to1/(\alpha p)\) in probability. In fact, uniformly for \(0\le n\le\tau_Z\),
\[
\frac{z_n}{Z}=1-\frac{\alpha K_n}{Z}+o_{\mathsf P}(1),
\]
and hence, on every compact time interval before the limiting exit, \(z_{\lfloor tZ\rfloor}/Z\to1-\alpha pt\) uniformly in probability.

**3. The slow-map occupation limit.** Suppose \(0<s<1\). Stop first when \(z_i\le\delta Z\). Before that time, the preceding fluid approximation makes \((z_i/Z)^{-s}\) uniformly bounded; the martingale difference \((1-\xi_i)-q\) contributes \(o_{\mathsf P}(1)\) to the normalized weighted Riemann sum. Thus
\[
\frac1{Z^{1-s}}\sum_{0\le i<\tau_Z:\,z_i>\delta Z}
(1-\xi_i)z_i^{-s}
\xrightarrow{\mathsf P}
q\int_0^{(1-\delta)/(\alpha p)}(1-\alpha pt)^{-s}\,dt
=\frac{q(1-\delta^{1-s})}{\alpha p(1-s)}.
\]
The expectation of the remaining sum below \(\delta Z\) is at most \(C_s(\delta Z)^{1-s}\) by the conditional version of (1). After normalization it vanishes in probability as \(\delta\downarrow0\). Hence
\[
\boxed{\displaystyle
\frac{S_Z}{Z^{1-s}}\xrightarrow{\mathsf P}
\frac{q}{\alpha p(1-s)}\quad(0<s<1).}\tag{3}
\]
For \(s>1/2\), (1) also directly gives \(S_Z=o_{\mathsf P}(\sqrt Z)\): this covers \(s\in(1/2,1)\), \(s=1\), and \(s>1\) without changing hypotheses.

**4. Random-clock central limit theorem and three regimes.** The functional central limit theorem for the independent centered variables \(\xi_i-p\), together with \(\tau_Z/Z\to1/(\alpha p)\), implies the stopped-time limit
\[
\frac{M_{\tau_Z}}{\sqrt Z}\xRightarrow{}
\mathcal N\left(0,\frac q\alpha\right).
\]
This random-time substitution follows from continuity of Brownian sample paths and does not require \(\tau_Z\) to be independent of the increments. Insert this and (3) into (2). When \(0<s<1/2\), the weight \(Z^{1-s}\) exceeds \(\sqrt Z\), so the Bernoulli martingale disappears on the larger scale and (3) gives the asserted deterministic correction. At \(s=1/2\), the limit \(S_Z/\sqrt Z\to2q/(\alpha p)\) shifts the normal mean by \(-2q/(\alpha p^2)\). For \(s>1/2\), the slow contribution vanishes on the Gaussian scale. The common Gaussian variance is \(q/(\alpha p^2)\). This proves all three claims.

## Verification

The accompanying standalone script `check_escape.py` checks the exact conjugacy of the intermittent left branches, one-step decrement bounds for several admissible exponents and states, finite-path stopping identities, and reproducible Monte Carlo sanity tests in the three regimes. Its successful completion prints `VERIFY_OK`. Computations are supplementary; the probability limits use (1)--(3) and the standard Bernoulli invariance principle.

## Relationship to prior work

Bahsoun, Bose, and Duan introduced the independent random LSV compositions and proved annealed mixing-rate estimates; their Proposition 4.1 bounds the mean location of random return intervals. Bahsoun and Bose subsequently proved a sharp first-order almost-sure asymptotic for these intervals (Theorem 1.1), and a related later paper by Bahsoun, Bose, and Ruziboev established quenched return-interval asymptotics and correlation bounds. These first-order statements determine the dominant fast-map scale, but the inspected results do not give a distributional first-exit correction for a fixed small starting point, the Gaussian variance here, or the critical exponent ratio \(3/2\). The central limit theorems of Nicol, Török, and Vaienti concern Birkhoff sums of observables on sequential/random compositions, rather than the present moving-initial-condition laminar stopping clock.

The result uses only the neutral branches of a named, previously studied family. It neither reasserts prior invariant-density nor prior correlation-decay results as new.

## Limitations

The theorem is an annealed law over independent map selections, with deterministic starting point tending toward the indifferent fixed point. It does not assert a quenched limiting distribution for any fixed driving sequence, a limit law for stationary orbit-return times, or a result for correlated switching. The displayed centering is accurate at the indicated scales; for \(s<1/2\), no additional Gaussian claim is made after subtraction of the leading deterministic correction, because further drift orders can intervene. The relative exponent difference \(s\) and all other parameters are fixed as \(Z\to\infty\). The initial-source date describes the previously published map family, not a date of publication for this result. Historical priority remains subject to independent assessment.

## References

1. W. Bahsoun, C. Bose, Y. Duan, *Decay of correlation for random intermittent maps*, arXiv:1305.6588 (first submitted 2013-05-28), especially Section 2 and Proposition 4.1.
2. W. Bahsoun, C. Bose, *Mixing rates and limit theorems for random intermittent maps*, arXiv:1503.06157 (first submitted 2015-03-20), especially Theorem 1.1 and Section 2.
3. W. Bahsoun, C. Bose, M. Ruziboev, *Quenched decay of correlations for slowly mixing systems*, arXiv:1706.04158 (first submitted 2017-06-13), especially Section 5.
4. M. Nicol, A. Török, S. Vaienti, *Central limit theorems for sequential and random intermittent dynamical systems*, arXiv:1510.03214 (first submitted 2015-10-12), especially Sections 1 and 5.
