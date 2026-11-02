# Universal temporal memory of a resetting Thomas–Fermi condensate edge

## Finding

Consider a one-dimensional Thomas–Fermi condensate in the hydrodynamic free-expansion approximation, periodically restored *instantaneously* to its original state by a stationary rate-\(r\) Poisson resetting process. Let its macroscopic right support edge be \(E_t=x_0 b(A_t)\), where \(A_t\) is the time since the most recent reset. For every \(r,\omega,x_0>0\), set
\[
 b''(s)=\frac{\omega^2}{b(s)^2},\qquad b(0)=1,\quad b'(0)=0,
 \quad Z\sim\operatorname{Exp}(1),\quad
 V_r=\operatorname{Var}\bigl(b(Z/r)\bigr)>0.
\]
Then for every \(\tau\ge0\), the exact stationary covariance is
\[
 \boxed{C_r(\tau):=\operatorname{Cov}(E_0,E_\tau)
 =x_0^2e^{-r\tau}\operatorname{Cov}\bigl(b(Z/r),b(Z/r+\tau)\bigr).}
\]
The normalized edge covariance has a **strictly enhanced exponential envelope**, for every \(\tau>0\):
\[
 C_r(\tau)>C_r(0)e^{-r\tau}>0.
\]
Its integrated correlation time \(T_r=\int_0^\infty C_r(\tau)\,d\tau/C_r(0)\) is finite and satisfies \(rT_r>1\). At fixed \(r\), the large-lag prefactor obeys the sharper exact identity
\[
 \lim_{\tau\to\infty}e^{r\tau}C_r(\tau)
 =x_0^2\sqrt2\,\omega\,\operatorname{Cov}\bigl(b(Z/r),Z/r\bigr)
 > C_r(0).
\]
The *fast-reset* profile and first finite-rate correction are
\[
 \boxed{\lim_{r/\omega\to\infty}\frac{C_r(u/r)}{C_r(0)}
 =e^{-u}\left(1+\frac{2u}{5}\right),\quad u\ge0,}
\]
\[
 \boxed{rT_r=\frac75-\frac{88}{25}\left(\frac\omega r\right)^2
 +O\left(\left(\frac\omega r\right)^4\right).}
\]
The fixed-\(u\) convergence is uniform on compact subsets of \([0,\infty)\). In the *slow-reset* limit, \(\lim_{r/\omega\downarrow0}rT_r=1\). Thus the same macroscopic edge has two distinct dimensionless memory limits, \(1\) and \(7/5\), although its underlying resetting clock is memoryless.

## Assumptions and scope

The model is the deterministic, normalized hydrodynamic Thomas–Fermi scaling solution of the repulsive one-dimensional Gross–Pitaevskii condensate at large particle number and within the approximations stated in the motivating paper [1]. Every reset restores the **entire** hydrodynamic profile with zero initial expansion velocity; successive reset waiting times are i.i.d. exponential with rate \(r>0\). There is no finite reset duration or state-dependent rate. The spatial support length \(x_0>0\) and trap frequency \(\omega>0\) are fixed. The system is in the stationary, two-sided-Poisson regime. Observables are macroscopic support edges, not finite-particle random maxima or quantum microscopic fluctuations.

The differential equation has a unique global positive smooth solution. Multiplying by \(b'\) gives the first integral
\[
 b'(s)^2=2\omega^2\left(1-\frac1{b(s)}\right),
\]
where \(b(s)\ge1\), \(b'(s)>0\) for \(s>0\), and \(0<b'(s)<c:=\sqrt2\,\omega\). Also \(b''(s)>0\) and \(b'(s)\uparrow c\). In particular, \(b\) is strictly increasing and strictly convex, has at most linear growth, and \(b(s)/s\to c\) as \(s\to\infty\). These properties make every covariance and time integral below well-defined.

## Proof

**1. Exact two-time law.** In a stationary rate-\(r\) Poisson process, \(A_0\sim\operatorname{Exp}(r)\), independent of all reset events after time zero. Let \(B\) denote the event that the interval \((0,\tau]\) contains no reset, so \(\mathbb P(B)=e^{-r\tau}\). On \(B\), \(A_\tau=A_0+\tau\). On its complement, \(A_\tau\) depends only on post-zero resets and is independent of \(A_0\). Since \(\mathbb E[b(A_0)-\mathbb Eb(A_0)]=0\) even after conditioning on whether \(B\) occurred, the contribution from \(B^c\) to the centered covariance vanishes. Conditioning on \(B\) yields the displayed exact formula. At \(\tau=0\), \(C_r(0)=x_0^2V_r>0\).

**2. Strict memory enhancement.** Put \(f(s)=b(s)\) and \(h_\tau(s)=b(s+\tau)-b(s)\). For each \(\tau>0\), strict convexity of \(b\) makes \(h_\tau\) strictly increasing, as is \(f\). If \(A,A'\) are independent, nondegenerate exponential ages, then
\[
 2\operatorname{Cov}(f(A),h_\tau(A))
 =\mathbb E[(f(A)-f(A'))(h_\tau(A)-h_\tau(A'))]>0.
\]
Therefore \(\operatorname{Cov}(b(A),b(A+\tau))>\operatorname{Var}(b(A))\), proving the sharp strict inequality. The global bound \(|b(s)-b(t)|\le c|s-t|\) and the same independent-copy covariance identity imply \(0<C_r(\tau)\le x_0^2c^2r^{-2}e^{-r\tau}\). Thus \(T_r\) is finite, and integration of the strict inequality gives \(rT_r>1\).

**3. Large-lag prefactor.** For each fixed \(a\ge0\),
\[
 b(a+\tau)-b(\tau)=\int_0^a b'(\tau+s)\,ds\longrightarrow ca.
\]
The difference is dominated by \(ca\), which is square-integrable under the exponential age law. Hence in \(L^2\), \(b(A+\tau)-b(\tau)\to cA\), and the covariance formula yields the stated limit. Moreover, \(s\mapsto cs-b(s)\) has strictly positive derivative \(c-b'(s)\) on every finite \(s\). The same monotone-covariance identity shows \(c\operatorname{Cov}(b(A),A)>\operatorname{Var}(b(A))\).

**4. Fast resetting.** With \(\varepsilon=\omega/r\), analytic expansion of the governing ODE at the reset state yields
\[
 b(z/r)=1+\tfrac12\varepsilon^2 z^2-\tfrac1{12}\varepsilon^4 z^4
 +O(\varepsilon^6z^6)
\]
for bounded \(\varepsilon z\). Let \(Z,U\) be independent unit-mean exponential variables. The factorial identities \(\mathbb EZ^k=k!\) give
\[
 \operatorname{Var}(Z^2)=20,\qquad
 \operatorname{Cov}(Z^2,(Z+u)^2)=20+8u,\qquad
 \operatorname{Cov}(Z^2,Z^4)=672.
\]
Consequently, for each fixed \(u\ge0\),
\[
 \frac{\operatorname{Cov}(b(Z/r),b((Z+u)/r))}
      {\operatorname{Var}(b(Z/r))}=1+\frac{2u}{5}+O(\varepsilon^2).
\]
The remainder is uniform on compact \(u\)-intervals. In the dimensionless integrated covariance,
\[
 rT_r=\frac{\displaystyle\int_0^\infty e^{-u}
 \operatorname{Cov}(b(Z/r),b((Z+u)/r))\,du}
 {\operatorname{Var}(b(Z/r))},
\]
the exact exponential moment computations additionally give
\[
 \operatorname{Var}(b(Z/r))=5\varepsilon^4-56\varepsilon^6+O(\varepsilon^8),
\]
\[
 \int_0^\infty e^{-u}\operatorname{Cov}(b(Z/r),b((Z+u)/r))\,du
 =7\varepsilon^4-96\varepsilon^6+O(\varepsilon^8).
\]
The second integral uses
\[
 \int_0^\infty e^{-u}\operatorname{Cov}(Z^2,(Z+u)^2)\,du=28,
\]
\[
 \int_0^\infty e^{-u}\bigl[\operatorname{Cov}(Z^2,(Z+u)^4)
 +\operatorname{Cov}(Z^4,(Z+u)^2)\bigr]du=2304.
\]
Dividing these expansions gives \(7/5-(88/25)\varepsilon^2+O(\varepsilon^4)\). To justify integrated remainder bounds, split the exponential integrals into \(Z+U\le\varepsilon^{-1/2}\) and its complement. On the first region the analytic Taylor series has bounded polynomial remainder; on the complement the linear-growth bound for \(b\) together with the exponential tails gives an error smaller than every fixed power of \(\varepsilon\). The same argument applies without integration over \(U\).

**5. Slow resetting.** Since \(b(s)/s\to c\) and \(0\le b(s)-1\le cs\),
\[
 \frac r c\,b(Z/r)\longrightarrow Z
 \quad\text{in }L^2,
\]
and, for every fixed \(u\ge0\), the centered pair \(\frac r c\bigl(b(Z/r),b((Z+u)/r)\bigr)\) converges in \(L^2\) to \((Z,Z+u)\). Thus their covariance-to-variance ratio tends to \(1\). Both functions of \(Z\) are \(c/r\)-Lipschitz, so their covariance is at most \(c^2/r^2\), while the variance is asymptotic to \(c^2/r^2\). This provides an eventual uniform bound in \(u\); dominated convergence under \(e^{-u}du\) then proves \(rT_r\to1\).

## Verification

Run `python verify_edge.py` with Python 3.10 or newer. The dependency-free exact-rational part independently reconstructs every factorial moment, both integrated polynomial covariance sums, and the coefficients \(7/5\) and \(-88/25\). If NumPy and SciPy are installed, the same standalone script solves the expansion ODE and evaluates independent Gauss–Laguerre quadratures for reset ratios \(r/\omega=20\) and \(40\); these verify the strict memory enhancement and the predicted asymptotic correction. This finite verification supplements, rather than substitutes for, the analytical argument.

## Relationship to prior work

Mesquita, Kulkarni, Majumdar and Sabhapandit [1] introduce the Thomas–Fermi resetting protocol, derive the scaling equation (37) and stationary **one-time** edge law (their §4.2, equations (61)–(62)). These are taken as inputs, not claimed as new. The present claim is confined to the *stationary two-time macroscopic edge covariance*, the strict all-rate enhancement, and the dimensionless memory crossover and correction. Stojkoski, Sandev, Kocarev and Pal [2] already derive autocorrelation functions from renewal/last-reset-time arguments for diffusion and drift-diffusion. Hence the general no-reset conditioning method itself is not new; [2] does not examine this nonlinear condensate expansion equation, its strict convex-edge comparison or the displayed constants. A more general unlocated result for deterministic convex observables of Poisson age could subsume the first inequality or the covariance decomposition; the physically specialized two-limit expansion and first correction are the substantive additional statements.

## Limitations

The result describes the macroscopic Thomas–Fermi support edge in the hydrodynamic large-particle-number approximation, not the exact finite-\(N\) quantum maximum, condensate edge noise, or experimentally verified time series. The reset is idealized as instantaneous and complete. The theorem gives no assertion that \(rT_r\) is globally monotone or always below \(7/5\); only strict \(rT_r>1\) and the two limiting expansions are proved. The universal leading profile does not imply universality for non-Poisson clocks or for arbitrary free-expansion laws. Broader generic resetting-correlation theorems remain a possible subsumption/priority risk; originality is assessed against the cited, inspected literature, not independently certified.

## References

[1] N. Mesquita, M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Weakly interacting Bose-Einstein condensate with stochastic resetting*, arXiv:2609.37110v1, first public September 29, 2026. https://arxiv.org/abs/2609.37110 ; https://pdfs.assets.alphaxiv.org/2609.37110v1.pdf . Equation (37), §3, §4.2 and equations (61)–(62) read in the accessible preprint.

[2] V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686, first public July 24, 2021. https://arxiv.org/abs/2107.11686 . In particular §2.2, §3, and equation (11) provide the relevant renewal-correlation comparator.

[3] M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106 (2011), 160601, arXiv:1102.2704. https://arxiv.org/abs/1102.2704 . Background on Poisson resetting; not a claim of priority over general renewal arguments.
