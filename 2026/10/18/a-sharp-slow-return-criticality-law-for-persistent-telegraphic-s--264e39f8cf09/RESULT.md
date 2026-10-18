# A sharp slow-return criticality law for persistent telegraphic search

## Finding

Consider a one-dimensional run-and-tumble particle traveling with speed \(c>0\), reversing its velocity at Poisson rate \(\gamma>0\), and starting at the origin with each initial velocity sign equally likely. A target at \(b>0\) absorbs it at its first visit. Independently, rate-\(r>0\) alarms interrupt the free search; after an alarm the particle returns to the origin deterministically at speed \(v>0\), then starts an independent free search with a newly randomized velocity sign. Return travel consumes physical time but causes neither reversals, new alarms, nor target capture.

Introduce the dimensionless parameters
\[
 z=\frac{rb}{c},\qquad \varepsilon=\frac{\gamma b}{c},\qquad h=\frac cv,\qquad w=\sqrt{z(z+2\varepsilon)}.
\]
The exact mean first-passage time, previously obtained in another form by Radice, is \(\mathbb E T=(b/c)F_{\varepsilon,h}(z)\), where
\[
 F_{\varepsilon,h}(z)=A_\varepsilon(z)+hB_\varepsilon(z),\quad
 A_\varepsilon(z)=\frac{(1+z/w)e^w-1}{z},\quad
 B_\varepsilon(z)=\frac{2\sinh w}{w}-1+\frac{2\cosh w-1}{z+2\varepsilon}.
\]

**Slow-return optimization theorem.** Let \(\varepsilon_c=0.439692620785908384\ldots\) be the unique positive solution of
\[
 8\varepsilon_c^3+12\varepsilon_c^2-3=0.
\]
For each fixed \(\varepsilon>0\), the function \(F_{\varepsilon,h}\) has a unique global minimizer \(z_h>0\) for every sufficiently large \(h\). As \(h\to\infty\), its behavior is exactly the following three-way classification:

* **Persistent regime:** If \(0<\varepsilon<\varepsilon_c\), there is a unique \(\zeta_\varepsilon>0\) with \(B_\varepsilon'(\zeta_\varepsilon)=0\), and
  \[
  z_h=\zeta_\varepsilon-\frac{A_\varepsilon'(\zeta_\varepsilon)}{hB_\varepsilon''(\zeta_\varepsilon)}+O_\varepsilon(h^{-2}).
  \]
  In particular, optimal alarm resetting persists at a strictly positive limiting rate even when returns are arbitrarily slow.
* **Critical regime:** If \(\varepsilon=\varepsilon_c\), write
  \[
  a_\varepsilon=\frac{2\varepsilon+1}{\sqrt{2\varepsilon}},\qquad
  g_{2,\varepsilon}=\frac{\varepsilon^2}{15}+\frac\varepsilon6+\frac13+\frac{1}{8\varepsilon^3}.
  \]
  Then
  \[
  z_h\sim\left(\frac{a_{\varepsilon_c}}{4g_{2,\varepsilon_c}\,h}\right)^{2/5}.
  \]
* **Frequent-reversal regime:** If \(\varepsilon>\varepsilon_c\), write
  \[
  g_{1,\varepsilon}=1+\frac{2\varepsilon}{3}-\frac{1}{4\varepsilon^2}>0.
  \]
  Then
  \[
  z_h\sim\left(\frac{a_\varepsilon}{2g_{1,\varepsilon}\,h}\right)^{2/3}.
  \]

Thus, since \(r_*=(c/b)z_h\) and \(h=c/v\), the slow-return optimum exhibits a sharp transition between a nonzero limiting alarm rate, a \(v^{2/5}\) critical law, and a \(v^{2/3}\) law. All asymptotics keep \(b,c,\gamma\) fixed and let \(v\downarrow0\); the zero-speed endpoint itself is excluded.

## Assumptions and scope

The moving particle occupies the entire half-line \(( -\infty,b)\) before capture. Velocity flips and alarm times are independent exponential clocks; after each completed return all clocks and the velocity sign are reinitialized independently. The target is detected during free motion, and returns are deterministic inactive phases. The theorem concerns the full mean physical first-passage time (including returns), not just mean exploratory time. The target distance, flight speed, and reversal rate \(b,c,\gamma\) are strictly positive; both resetting and return speeds are positive before limits are taken.

## Proof

**1. Renewal reduction and an exact representation.** The finite-speed telegraph first-passage survival resolvent for a free, symmetrically oriented particle launched at zero and killed at \(b\) is, for \(x<b\),
\[
 \widehat q(x,r)=\frac{\lambda}{2r}\left[e^{-\lambda|x|}-\frac{r+\gamma-c\lambda}{\gamma}e^{-\lambda(2b-x)}\right],\qquad
 \lambda=\frac{\sqrt{r(r+2\gamma)}}c.
\]
This follows from the two-velocity transport equations with zero incoming density at \(b\), and is the resolvent derived in Radice, Appendix D. Its integral gives the first-passage Laplace transform, hence the probability of hitting the target before an independent rate-\(r\) alarm is
\[
 p=\mathbb E[e^{-rT_0}]=\frac{e^{-\lambda b}}{1+\sqrt{r/(r+2\gamma)}}.
\]
In one search cycle the expected active duration before capture or alarm is \((1-p)/r\). The unconditional mean return time accumulated on failed cycles is
\[
 \frac rv\int_{-\infty}^{b}|x|\widehat q(x,r)\,dx.
\]
The renewal equation therefore yields
\[
 \mathbb E T=\frac{(1-p)/r+(r/v)\int_{-\infty}^b|x|\widehat q(x,r)\,dx}{p}.
\]
Inserting the two exponential pieces, integrating separately on \(( -\infty,0)\) and \((0,b)\), and using \(z/w=\sqrt{r/(r+2\gamma)}\) gives the displayed \(A_\varepsilon+hB_\varepsilon\). Equivalently, it is an algebraic rewriting of Radice's published constant-speed-return mean-time formula, Eq. (129). This entire mean-time identity is used as established prior work, not claimed as new.

**2. Strict convexity of the return-cost factor.** For every \(\varepsilon>0\) and \(z\ge0\), analytic continuation at \(z=0\) and the hyperbolic power series give the absolutely convergent identity
\[
 B_\varepsilon(z)=1+\frac1{z+2\varepsilon}
 +\sum_{n=1}^\infty\left[
 \frac{2z^n(z+2\varepsilon)^n}{(2n+1)!}
 +\frac{2z^n(z+2\varepsilon)^{n-1}}{(2n)!}
 \right].
\]
Each summand is a polynomial in \(z\) with nonnegative coefficients, so its second derivative is nonnegative on \([0,\infty)\). The rational term has strictly positive second derivative. Termwise differentiation is justified by locally uniform convergence. Consequently \(B_\varepsilon''(z)>0\) for all \(z\ge0\). Direct coefficient extraction gives
\[
 B_\varepsilon(z)=1+\frac1{2\varepsilon}+g_{1,\varepsilon}z+g_{2,\varepsilon}z^2+O_\varepsilon(z^3),
\]
with exactly the coefficients displayed above. The sign of \(g_{1,\varepsilon}\) is the sign of the strictly increasing cubic \(8\varepsilon^3+12\varepsilon^2-3\). Since \(B_\varepsilon(z)\to\infty\) as \(z\to\infty\), strict convexity yields a unique interior minimum \(\zeta_\varepsilon\) precisely when \(\varepsilon<\varepsilon_c\); otherwise \(B_\varepsilon\) is strictly increasing for positive \(z\), with infimum at the unattained endpoint zero.

**3. Uniform localization of large-return-cost minimizers.** For fixed \(\varepsilon>0\), \(A_\varepsilon(z)>0\), and as \(z\downarrow0\),
\[
 A_\varepsilon(z)=a_\varepsilon z^{-1/2}+O_\varepsilon(1),\quad
 A_\varepsilon'(z)=-\frac{a_\varepsilon}{2}z^{-3/2}+O_\varepsilon(z^{-1/2}),\quad
 A_\varepsilon''(z)=\frac{3a_\varepsilon}{4}z^{-5/2}+O_\varepsilon(z^{-3/2}).
\]
At infinity \(A_\varepsilon(z)\to\infty\). Thus \(F_{\varepsilon,h}\) has at least one positive global minimum. Dividing \(F\) by \(h\), comparison against a fixed point near the unique interior minimizer of \(B\), or against trial values \(z\downarrow0\) with \(A(z)/h\to0\), shows that every global minimizer converges respectively to \(\zeta_\varepsilon\) when \(\varepsilon<\varepsilon_c\), or to zero when \(\varepsilon\ge\varepsilon_c\). Strict positivity of \(B''\), combined with bounded \(A''\) near \(\zeta_\varepsilon\) or positive \(A''\) near zero, makes \(F''>0\) throughout the region containing all large-\(h\) minimizers. The global minimizer is therefore unique for sufficiently large \(h\).

**4. Sharp asymptotics.** In the persistent regime, the stationarity equation \(A'(z_h)+hB'(z_h)=0\), Taylor expansion at \(\zeta_\varepsilon\), and the implicit-function theorem give the stated expansion with \(O_\varepsilon(h^{-2})\) error. Above the threshold, the same equation at \(z_h\to0\) becomes
\[
 -\frac{a_\varepsilon}{2}z_h^{-3/2}(1+o(1))
 +h\left(g_{1,\varepsilon}+O_\varepsilon(z_h)\right)=0,
\]
which forces the \(h^{-2/3}\) law. At the threshold the linear term vanishes and the second term is instead \(h(2g_{2,\varepsilon_c}z_h+O(z_h^2))\), forcing the \(h^{-2/5}\) law with the explicit coefficient. These are asymptotic equalities, not numerical fits.

## Verification

The standalone program `verify.py` uses high-precision arithmetic to reproduce the hyperbolic simplification and local coefficients, compares the optimized finite-\(h\) values against all three scaling laws, independently integrates the killed telegraph resolvent, and simulates the original alternating flight/return renewal process with event-driven trajectories. Running `python3 verify.py` passed 70 checks. Three Monte Carlo batches of 42,000 trajectories each differed from the exact mean by relative errors approximately 0.001945, 0.005473, and 0.001504. Numerical comparisons support the analytic steps but do not prove the infinite-parameter theorem.

## Relationship to prior work

Radice (arXiv:2106.00670, originally public 1 June 2021), Section V.1, Eq. (129), derives the exact constant-speed-return mean first-passage time and numerically explores optimal resetting as velocity-flip and return rates vary; its Appendix D and E derive the killed resolvent and unsuccessful-cycle transform. The present finding does **not** claim that formula, the renewal method, or ballistic-rate optimization as original. Its mathematical contribution is the strict convexity of the speed-weighted return factor and the complete slow-return optimization threshold with two distinct critical exponents and sharp prefactors.

Tucci, Gambassi, Majumdar, and Schehr (arXiv:2203.16066) study a different experimental-inspired protocol based on instantaneous redistribution from a harmonic-trap position law, rather than deterministic constant-speed returns from the actual alarm location. The general theory of optimal resetting phases supplies conceptual context but does not by itself establish the present model-specific cubic threshold or exponents. These comparisons do not constitute an independent determination of priority.

## Limitations

The classification fixes positive reversal strength before making returns arbitrarily slow; the ballistic boundary \(\gamma=0\) has different first-passage behavior and is excluded. The result describes large \(c/v\), not global optimizer uniqueness at all finite return speeds. It assumes independent Poisson alarms, symmetric reinitialization, deterministic constant-speed return travel, and no absorption during returns. A general return-time law, finite observation windows, directional resetting biases, and resetting position distributions are not covered. The published exact mean-time formula and its underlying killed resolvent are prior work; any overlooked independent analysis of their slow-return extrema could affect originality.

## References

1. M. Radice, *The one-dimensional telegraphic process with noninstantaneous stochastic resetting*, arXiv:2106.00670v1 (1 June 2021), revised version v3 (2021), Phys. Rev. E **104**, 044126 (2021), DOI:10.1103/PhysRevE.104.044126. Sections III and V.1, Appendices D and E.
2. G. Tucci, A. Gambassi, S. N. Majumdar, and G. Schehr, *First-passage time of run-and-tumble particles with non-instantaneous resetting*, arXiv:2203.16066v1 (30 March 2022), Phys. Rev. E **106**, 044127 (2022). Section IV.
3. A. Pal, Ł. Kuśmierz, and S. Reuveni, *Diffusion with stochastic resetting is invariant to return speed*, arXiv:1907.12208 (2019), on diffusive stationary position laws, distinct from telegraphic mean target-hitting times.
