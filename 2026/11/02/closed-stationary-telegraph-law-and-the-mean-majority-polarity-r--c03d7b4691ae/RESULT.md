# Closed stationary telegraph law and the mean-majority polarity reversal

## Finding

For a two-speed telegraph particle with Bernoulli resets, the entire stationary position law has an elementary two-sided-exponential form; this evaluates the stationary local-time integral of Di Crescenzo, Iuliano and Verasani (2026). Its mean and its majority sign have distinct sharp parameter thresholds, so a particle that restarts to the right may spend a majority of stationary observations on the right but have a negative stationary mean.

Fix \(\lambda,c,v>0\) and \(0<\theta\le1\). Define

\[
D=\sqrt{(v-c)^2+4cv\theta(2-\theta)},\qquad
r=\lambda\theta,\qquad
d_\pm=\frac{\lambda(D\pm(v-c))}{2cv}.
\]

The notation means \(d_+=\lambda(D+v-c)/(2cv)\) and \(d_-=\lambda(D-v+c)/(2cv)\). Set

\[
A=\frac{d_+(d_-+r/c)}{d_++d_-},\qquad
B=\frac{d_-(d_+-r/c)}{d_++d_-}.
\]

Then the unique stationary position distribution has **no atom** and density, for Lebesgue-almost every real \(x\),

\[
f(x)=A e^{-d_+x}\mathbf1_{\{x>0\}}+B e^{d_-x}\mathbf1_{\{x<0\}}.
\]

For \(0<\theta<1\), both coefficients are strictly positive. At \(\theta=1\), the second coefficient vanishes and the law is a one-sided exponential. The stationary density has the exact one-sided jump \(f(0+)-f(0-)=r/c\). In addition,

\[
\begin{aligned}
\Pr_\pi(X<0)&=\frac12+\frac{v(1-2\theta)-c}{2D},\\
\mathbb E_\pi X&=\frac{c-v(1-\theta)}{\lambda\theta(2-\theta)}.
\end{aligned}
\]

Consequently, stationary **negative-location majority** occurs if and only if \(v(1-2\theta)>c\), and stationary **negative mean** occurs if and only if \(v(1-\theta)>c\). They are not equivalent. In particular, a negative mean together with a strict positive-location majority occurs exactly on the nonempty region

\[
v(1-\theta)>c\quad\text{and}\quad v(1-2\theta)<c.
\]

For every \(0<\theta<1\), such parameters exist: if \(\theta<1/2\), choose \(c/(1-\theta)<v<c/(1-2\theta)\); if \(\theta\ge1/2\), any \(v>c/(1-\theta)\) works. Negative-location majority always implies negative mean, but the converse fails. Neither sign threshold depends on \(\lambda\).

## Assumptions and scope

The particle begins at \((0,c)\). Its motion has velocity \(+c\) or \(-v\). Every run lasts an independent exponential time with rate \(\lambda\), independent of every Bernoulli decision. At the end of each run the particle either instantly resets to position zero and the *original positive velocity* \(+c\), with probability \(\theta\), or switches velocity sign (and its speed accordingly), with probability \(1-\theta\). All future randomness is fresh after a reset. The result concerns fixed finite parameters \(\lambda,c,v>0\) and \(0<\theta\le1\). The restriction \(\theta>0\) is essential for positive recurrence by resets; no assertion is made at \(\theta=0\).

The reset and velocity-flip instants are independently thinned Poisson point processes with respective intensities \(r=\lambda\theta\) and \(a=\lambda(1-\theta)\). This representation is valid because holding times are exponential. It need not hold for general renewal or Erlang-2 holding times.

## Proof

**1. Unique stationary law.** Independently mark the times of a rate-\(\lambda\) Poisson clock as reset with probability \(\theta\) and flip otherwise. Poisson splitting gives independent reset and flip clocks of rates \(r\) and \(a\). Construct the process on the whole real line with two-sided stationary clocks. At each reset it is placed at \((0,c)\) and then evolves by the flip clock until the next reset. This constructs an invariant probability law. Couple two copies using common clocks: they coincide after their first common reset, so their total-variation distance at time \(t\) is at most \(e^{-rt}\). Thus the invariant law is unique and attracts every initial state (for the joint position/velocity process).

**2. Geometric-excursion transform.** At a stationary observation time, the age \(E\) since the most recent reset has exponential law of rate \(r\). Its position has the same law as the no-reset telegraph displacement run from velocity \(+c\) for an independent duration \(E\). Until this independent killing time, flips occur at rate \(a\). The number \(N\) of flips is geometric with \(\Pr(N=n)=\theta(1-\theta)^n\), for \(n=0,1,\ldots\); conditional on the marked event types, each of the \(N+1\) holding times is an independent exponential of rate \(r+a=\lambda\). With

\[
h_+(k)=\frac{\lambda}{\lambda-ikc},\qquad
h_-(k)=\frac{\lambda}{\lambda+ikv},\qquad q=1-\theta,
\]

the stationary characteristic function, obtained by summing even and odd values of \(N\), is

\[
\begin{aligned}
\phi(k)&=\frac{\theta h_+(k)[1+qh_-(k)]}{1-q^2h_+(k)h_-(k)}\\
&=\frac{r\,[r+2a+ikv]}{cvk^2+ik(r+a)(v-c)+r(r+2a)}.
\end{aligned}
\]

This is an identity for every real \(k\). The geometric series is absolutely convergent, even for \(k=0\), because \(q<1\). Its denominator factors as

\[
cv(d_+-ik)(d_-+ik),
\]

since \(d_+d_-=r(r+2a)/(cv)\) and \(d_+-d_-=(r+a)(v-c)/(cv)\). Elementary partial fractions therefore give

\[
\phi(k)=\frac{A}{d_+-ik}+\frac{B}{d_-+ik},
\]

with the coefficients in the Finding. Each term is the Fourier transform of its asserted half-line exponential. Uniqueness of characteristic functions proves the probability density formula (including its absence of an atom at zero).

**3. Positivity and boundaries.** Both decay rates are positive because \(D>|v-c|\). Direct algebra gives

\[
D^2-[c-v(1-2\theta)]^2=4\theta(1-\theta)v(c+v).
\]

Thus \(d_+-r/c>0\) for \(0<\theta<1\), and \(d_+-r/c=0\) at \(\theta=1\). Hence \(B\) is strictly positive precisely below that endpoint, and \(A>0\) always. By the partial-fraction identities, \(A-B=r/c\) and \(A/d_++B/d_-=1\). These verify the density normalization and the stated jump. The values at \(x=0\) themselves are immaterial.

**4. Sign phase diagram.** Integration of the negative half-line gives

\[
\Pr_\pi(X<0)=\frac{B}{d_-}=
\frac{d_+-r/c}{d_++d_-}
=\frac12+\frac{v(1-2\theta)-c}{2D}.
\]

Similarly the mean is \(A/d_+^2-B/d_-^2\). Simplifying yields

\[
\mathbb E_\pi X=\frac{c-v(1-\theta)}{\lambda\theta(2-\theta)},
\]

which agrees with the first-moment limit in the motivating paper. All denominators involved in these sign comparisons are positive. The two sign inequalities and the stated disagreement region now follow without approximation. At a majority boundary the probability is exactly \(1/2\); at a mean boundary the mean is exactly zero. Because the stationary law has no atom at zero, \(\Pr(X>0)=1-\Pr(X<0)\).

**5. An explicit local-time integral.** Let \(L_0^\infty(x\mid c)\) denote the integral of the continuous no-reset density in equations (41)–(42) of Di Crescenzo, Iuliano and Verasani (2026). Their Proposition 7 asserts, almost everywhere,

\[
f(x)=rL_0^\infty(x\mid c)+\frac{r}{c}e^{-\lambda x/c}\mathbf1_{\{x>0\}}.
\]

Solving for its previously integral-defined term gives an elementary expression:

\[
L_0^\infty(x\mid c)=
\begin{cases}
\frac{A}{r}e^{-d_+x}-\frac1c e^{-\lambda x/c},&x>0,\\
\frac{B}{r}e^{d_-x},&x<0.
\end{cases}
\]

The two one-sided values agree at zero (both equal \(B/r\)); the integral itself is a continuous function there. This is a consequence of the full stationary law rather than a separate claim of an independently new general local-time formula.

## Verification

A standalone Python 3 standard-library checker is included as `verify_stationary.py`. It evaluates the stationary density, both characteristic-function derivations (two-state resolvent and geometric-excursion sums), directly truncated renewal series, normalization, jump, mean, polarity thresholds, all accessible endpoint cases, and an exactly rational sign-order implication. Running it produces the accompanying `verification_output.txt`. Its finite checks supplement the proof; the infinite statements follow from Poisson splitting, the absolutely convergent geometric series, uniqueness of Fourier transforms and exact algebra.

One illustrative parameter set is \(\lambda=c=1\), \(v=2\), and \(\theta=0.4\). It gives \(\Pr_\pi(X<0)\approx0.378732187482\) but \(\mathbb E_\pi X=-0.3125\), demonstrating strict disagreement of the majority and mean signs.

## Relationship to prior work

Di Crescenzo, Iuliano and Verasani (2026), Sections 2 and 4.2, define this precise Bernoulli-reset telegraph process, prove existence of the stationary position density and present it using the uncomputed integral of the continuous no-reset local-time density, in their equations (41)–(42). They separately compute the first stationary moment. Those conclusions are prior results and are not presented here as new. The present statement supplies the elementary closed half-line density, an explicit evaluation of the stationary integral, and a complete polarity/mean-sign classification for their exponential intertime case.

Evans and Majumdar (2018) study symmetric-speed run-and-tumble resetting with independent Poisson resets and symmetric initial-velocity conditions and obtain a symmetric Laplace stationary density. The model here has arbitrary unequal speeds and deterministic positive post-reset velocity; its two half-line exponents and masses are generally unequal. The independent-Poisson clock representation is a standard thinning fact, not a novelty claim. Di Crescenzo and collaborators (2023) instead study geometrically counted nonexponential displacement times with external Poisson resets. General matrix-fluid resolvent theory may contain equivalent formulas in broader language; an exhaustive historical-priority certification is not claimed.

## Limitations

This result does not extend the explicit elementary formula to the source paper's Erlang-2 displacement-time case or any nonmemoryless run durations. The limit \(\theta\downarrow0\) is singular: no stationary reset regime is asserted for \(\theta=0\). It does not claim explicit finite-time transition laws, pathwise Kac limits or sharpness of the standard coupling rate. The originality assessment is source-specific, not a proof of global novelty; the historical risk of a broader equivalent two-state Markov-modulated-fluid formula remains. No independent mathematical audit has been performed.

## References

1. A. Di Crescenzo, A. Iuliano and G. Verasani, *A Generalized Telegraph Process with Resetting to the Origin Driven by Bernoulli Trials*, Journal of Statistical Physics **193** (2026), article 97, published July 18, 2026. DOI: https://doi.org/10.1007/s10955-026-03670-7 (especially Sections 2, 4.1–4.2, Proposition 7 and Remark 15).
2. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450v2 (2018), https://arxiv.org/html/1808.06450v2 (especially Sections 3 and 6).
3. A. Di Crescenzo, A. Iuliano, V. Mustaro and G. Verasani, *On the Telegraph Process Driven by Geometric Counting Process with Poisson-Based Resetting*, Journal of Statistical Physics **190** (2023), article 191, https://doi.org/10.1007/s10955-023-03189-1.
4. N. Ratanov and M. Turov, *On Local Time for Telegraph Processes*, Mathematics **11** (2023), 934, https://doi.org/10.3390/math11040934.
