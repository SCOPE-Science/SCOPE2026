# A strict fourth-cumulant sign law for diffusion with periodic nearest-site resetting

## Finding
Consider one-dimensional Brownian motion of generator \(D\partial_{xx}\), with \(D>0\), on the unbounded line. Fix a regular array of sites \(\ell\mathbb Z\), where \(\ell>0\). At the points of an independent Poisson process of rate \(r>0\), the particle instantaneously relocates to its nearest site; ties at half-integers can be assigned arbitrarily, as they occur with probability zero. Start the particle at site zero, and write \(X_t\) for its **actual continuous-space position** including instantaneous relocations.

Set \(\alpha=\frac{\ell}{2}\sqrt{r/D}\) and \(u=\sinh\alpha\). Let \(\kappa_j(X_t)\) be the \(j\)-th cumulant. The large-time scaled cumulant generating function \(\psi(k)=\lim_{t\to\infty}t^{-1}\log\mathbb E[e^{kX_t}]\) exists for every real \(k\), and is the unique nonnegative solution of
\[
\frac{\psi+r\cosh\bigl(\frac{\ell}{2}\sqrt{(r+\psi)/D}\bigr)}{\psi\cosh\bigl(\ell\sqrt{(r+\psi)/D}\bigr)+r\cosh\bigl(\frac{\ell}{2}\sqrt{(r+\psi)/D}\bigr)}\,\cosh(k\ell)=1.
\]
It is analytic around \(k=0\). In particular, its fourth derivative satisfies the **strict universal sign law**
\[
\boxed{\lim_{t\to\infty}\frac{\kappa_4(X_t)}t=\frac{r\ell^4\cosh\alpha}{4\sinh^5\alpha}\left[2\sinh^3\alpha+6\sinh\alpha-3\alpha(\sinh^2\alpha+2)\right]>0.}
\]
Here the strict inequality holds for every \(D,\ell,r>0\). By contrast, the fourth-cumulant growth of Brownian motion without resetting is zero. For weak resetting,
\[
\lim_{t\to\infty}\frac{\kappa_4(X_t)}t=\frac{r\ell^4}{80}+O(r^2)\qquad(r\downarrow0,\ D,\ell\text{ fixed}).
\]
The nearest-site renewal waiting time \(T\), defined below, obeys the sharp open coefficient-of-variation corridor
\[
\boxed{\frac23<\frac{\operatorname{Var}(T)}{(\mathbb ET)^2}<1,}
\]
whose endpoints are approached respectively as \(r\downarrow0\) and \(r\to\infty\). The strict lower bound, rather than the generic renewal formula alone, drives the fourth-cumulant sign law.

## Assumptions and scope
All parameters \(D,\ell,r\) are fixed and strictly positive. Reset times are homogeneous Poisson, Brownian motion is independent between resets, and relocation chooses the nearest point in the infinite equally spaced lattice. The statement concerns cumulants of displacement from the initial site at late times and **does not** claim that the finite-time fourth cumulant is positive at every time. This is the instantaneous-resetting idealization, not a finite-speed or refractory-period protocol.

Let \(T\) be the first epoch when either the Brownian path reaches \(\pm\ell\) before an intervention, or a reset carries it from the current site zero to \(\pm\ell\). Resets made while the path is in \((-\ell/2,\ell/2)\) return it to zero and do not end \(T\). The next completed lattice-site displacement is \(\pm\ell\) with equal probability, independently of \(T\), by reflection symmetry. Strong Markov and reset-clock memorylessness give independent identically distributed copies of these cycles.

## Proof
**Cycle transform.** For \(z\ge0\), put \(q=\sqrt{(r+z)/D}\), \(c=\cosh(q\ell)\), and \(h=\cosh(q\ell/2)\). Consider a Brownian excursion killed upon leaving \((-\ell,\ell)\) and at its independent rate-\(r\) reset clock. The discounted probability of diffusion exit before reset is \(c^{-1}\). Its killed Green density from zero is
\[
G_z(x)=\frac{\sinh(q(\ell-|x|))}{2Dq\cosh(q\ell)},\qquad |x|<\ell.
\]
Consequently, discounting at rate \(z\), the probability weight of a reset into an adjacent site is \(r(h-1)/((r+z)c)\), and the weight of a failed attempt, resetting to the original site, is \(r(c-h)/((r+z)c)\). Summing the geometric sequence of failed excursions yields
\[
\phi(z):=\mathbb E[e^{-zT}]=\frac{1+\frac r{r+z}(h-1)}{c-\frac r{r+z}(c-h)}=\frac{z+rh}{zc+rh}.
\]
This transform agrees with the prior published first-passage formula; that first-passage transform itself is not claimed as new. The elapsed time \(T\) has exponential moments near zero: from every location before a completed transfer, there is a uniform positive probability of a reset-free Brownian exit within a fixed duration, so a geometric-block argument bounds its survival tail exponentially.

**From cycles to actual displacement.** Let \(S_t\) denote the last completed lattice-site position before time \(t\). A renewal walk formed by the site increments has independent \(\pm\ell\) rewards and independent durations \(T\). Until its next completed site transition, the actual process stays within distance \(\ell\) of \(S_t\). If \(M(k,t)=\mathbb E[e^{k X_t}]\) and \(h_k(t)=\mathbb E[e^{kX_t};T>t]\), then the regenerative renewal equation and its Laplace transform are
\[
M(k,t)=h_k(t)+\cosh(k\ell)\int_{(0,t]}M(k,t-s)\,\mathbb P(T\in ds),
\]
\[
\widehat M(k,z)=\frac{\widehat h_k(z)}{1-\cosh(k\ell)\phi(z)}.
\]
Here \(\widehat h_k\) is analytic in a strip containing \(z=0\), and is positive for real \(z\) in its domain. For any real \(k\), \(\phi\) is continuous, strictly decreasing from one to zero on \([0,\infty)\); thus the denominator has exactly one real nonnegative root \(\psi(k)\). Positive renewal asymptotics show it is the exponential growth rate of \(M(k,t)\). In a complex neighborhood of \((k,z)=(0,0)\) the root is simple, and the nonlattice, exponential-tail cycle law isolates the leading renewal pole. Analytic differentiation then identifies \(\lim_{t\to\infty}\kappa_j(X_t)/t=\psi^{(j)}(0)\) for \(j=2,4\). This step concerns the actual particle, not just the embedded site walk.

**Moments of a completed-site passage.** Put \(u=\sinh\alpha\), \(h_0=\cosh\alpha\). Differentiating \(\phi\) gives
\[
m:=\mathbb ET=\frac{2u^2}{rh_0},\qquad v:=\operatorname{Var}(T)=\frac{4u^2h_0^2-2\alpha u(u^2+2)}{r^2h_0^2}.
\]
Expansion of \(\log\phi(\psi(k))+\log\cosh(k\ell)=0\) at zero, using \(\log\phi(z)=-mz+vz^2/2+O(z^3)\), yields
\[
\psi(k)=\frac{\ell^2}{2m}k^2+\ell^4\left(\frac{v}{8m^3}-\frac1{12m}\right)k^4+O(k^6).
\]
Therefore \(\psi''(0)=\ell^2/m\) and \(\psi^{(4)}(0)=\ell^4(3v-2m^2)/m^3\). The diffusivity \(\ell^2/(2m)=D\alpha^2\operatorname{csch}\alpha\operatorname{coth}\alpha\) recovers the established published formula. Substitution of \(m,v\) gives the claimed expression for \(\psi^{(4)}(0)\).

**Uniform strict sign, without numerical root counting.** Direct simplification gives
\[
3v/m^2-2=\frac{H(\alpha)}{2\sinh^3\alpha},\quad H(a)=2\sinh^3a+6\sinh a-3a(\sinh^2a+2).
\]
Using triple-angle identities,
\[
2H(a)=\sinh(3a)+9\sinh a-3a\cosh(2a)-9a
=\sum_{n=2}^{\infty}\frac{3[9^n+3-(2n+1)4^n]}{(2n+1)!}a^{2n+1}.
\]
Every coefficient is strictly positive: \(9^2>5\cdot4^2\), and \(9(2n+1)>4(2n+3)\) propagates \(9^n>(2n+1)4^n\) by induction for all integers \(n\ge2\). Hence \(H(a)>0\) for all \(a>0\).

For the other coefficient-of-variation bound, \(v/m^2<1\) is equivalent to \(a(\sinh^2a+2)>2\sinh a\). This follows from
\[
2\left[a(\sinh^2a+2)-2\sinh a\right]
=\sum_{n=1}^{\infty}\frac{[2^{2n}(2n+1)-4]}{(2n+1)!}a^{2n+1}>0.
\]
Finally, the displayed formulas give \(v/m^2\to2/3\) as \(a\to0\) and \(v/m^2\to1\) as \(a\to\infty\), both strictly unattained for positive finite parameters. Taylor expansion of \(H(a)=a^5/20+O(a^7)\) yields the weak-reset coefficient \(r\ell^4/80\).

## Verification
Run `python verify.py` with Python 3, SymPy, and mpmath. The standalone program checks the exact hyperbolic identity and series coefficients, verifies the finite coefficient inequalities, differentiates the independent Laplace-transform expression numerically at high precision over a parameter grid, checks both renewal moments against their explicit formulas, and verifies the small-\(k\) implicit scaled-cumulant expansion. It is corroboration, not an infinite proof; the positivity proof is the preceding coefficient induction.

## Relationship to prior work
Alston and Bertrand, arXiv:2401.12772v1 (2024), introduce nearest-site local resetting, derive its first-passage transform (main Eq. 12) and the regular-array effective diffusion coefficient (main Eq. 17). Those forward results are used here as independently reconstructed inputs; neither is new. Their inspected main text and the first-passage appendix do not present the strictly positive fourth cumulant growth law or the sharp waiting-time coefficient-of-variation corridor.

Pacheco-Pozo and Sokolov, arXiv:2012.09656, analyze general continuous-time random-walk large deviations. The general renewal-reward method and, therefore, generic implications for the scaled cumulant-generating function, are prior theory. The model-specific \(2/3\) lower bound and its all-rate consequence are the assessed refinement, not a claim to invent renewal large deviations. An asymmetric ratchet-mediated resetting result, arXiv:2405.10698, treats a different return mechanism and directed currents; its full comparison is a residual literature risk. A prior analysis of an asymmetric ratchet-reset current does not imply the strict sign of the symmetric nearest-site fourth cumulant without an additional parameter and mechanism equivalence that is not established.

## Limitations
This is an idealized infinite regular array with instantaneous, nearest-site Poisson resets and unbounded Brownian diffusion between events. The non-Gaussian coefficient remains of order \(t\) while the variance is of order \(t\), so normalized excess kurtosis decays like \(t^{-1}\); the theorem does not assert a non-Gaussian limiting central-limit distribution. It does not address irregular arrays, biased resetting, reset delays, finite-speed relocations, finite-time signs, noisy parameter inference, or independently certified publication priority. General CTRW formulas were already known; the new mathematical content is the strict, sharp special-model inequality.

## References
- H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1 (first public 2024-01-23), subsequently *Physical Review E* 111, 034114 (2025). https://arxiv.org/abs/2401.12772 ; lawful open PDF https://thibaultbertrand.com/assets/pdf/2024_arxiv_a.pdf .
- A. Pacheco-Pozo and I. M. Sokolov, *Large Deviations in Continuous Time Random Walks*, arXiv:2012.09656; *Physical Review E* 103, 042116 (2021). https://arxiv.org/pdf/2012.09656 .
- C. Roberts, E. Sezik and E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698 (2024). https://arxiv.org/abs/2405.10698 .
