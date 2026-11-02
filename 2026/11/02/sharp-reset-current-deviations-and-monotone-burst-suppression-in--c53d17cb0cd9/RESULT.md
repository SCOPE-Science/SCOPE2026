# Sharp reset-current deviations and monotone burst suppression in sluggish diffusion

## Finding

A threshold-reset sluggish diffusion admits a full, explicit renewal-current large-deviation principle, not only a mean reset rate. Set \(p=\alpha+2\), \(b=(\alpha+1)/(\alpha+2)\in[1/2,1)\), and \(m=L^p/[(\alpha+1)(\alpha+2)]\). Let \(N_t\) count complete excursions from zero to either endpoint \(\pm L\) by time \(t\), each followed by instantaneous return to zero. The normalized empirical current \(J_t=mN_t/t\) obeys an LDP of speed \(t/m\), with strictly convex good rate

\[
I_b(j)=\sup_{\theta\in\mathbb R}\{\theta j-\lambda_b(\theta)\},\qquad j\ge0,
\]

and infinite rate for \(j<0\). Here the globally defined, real-analytic scaled cumulant-generating function \(\lambda_b\) is the unique solution in \((-\zeta_b,\infty)\) of

\[
{}_0F_1(;b;b\lambda_b(\theta))=e^\theta,\qquad
\zeta_b=\frac{j_{b-1,1}^2}{4b},
\]

where \(j_{\nu,1}\) denotes the first positive zero of the ordinary Bessel function \(J_\nu\). It has \(\lambda_b(0)=0\), \(\lambda_b'(0)=1\), and \(\lambda_b''(0)=1/(b+1)\).

**Sharp tails and comparative result.** The boundary and fast-current regimes are

\[
I_b(0)=\zeta_b,\qquad \lim_{j\to\infty}\frac{I_b(j)}{j^2}=b.
\]

For every \(j>1\) and \(0\le\alpha_1<\alpha_2<\infty\), the normalized upward-current cost obeys the *strict* inequality

\[
I_{b(\alpha_1)}(j)<I_{b(\alpha_2)}(j).
\]

In particular, the reset-count Fano factor exists and is strictly decreasing in sluggishness,

\[
\lim_{t\to\infty}\frac{\operatorname{Var}(N_t)}{\mathbb E[N_t]}
=\frac{1}{b+1}=\frac{\alpha+2}{2\alpha+3},
\]

from \(2/3\) at \(\alpha=0\) toward \(1/2\) as \(\alpha\to\infty\). The strict rate inequality controls *all* upper-tail current deviations \(j>1\), not only their Gaussian approximation. For fixed \(j>1\), \(\lim_{t\to\infty}(m/t)\log\Pr\{J_t\ge j\}=-I_b(j)\).

## Assumptions and scope

For every \(\alpha\ge0\) and \(L>0\), consider the continuous natural-scale, nonsticky Itô diffusion on \((-L,L)\), started at \(0\), with interior backward generator \(\mathcal Lf(x)=|x|^{-\alpha}f''(x)\) for \(x\ne0\). A precise construction is Brownian motion \(B_s\) with generator \(\partial_x^2\), time-changed by the inverse of the strictly increasing clock \(A(s)=\int_0^s|B_u|^\alpha\,du\). At each first arrival at \(-L\) or \(+L\), immediately restart independently at zero. The process has no holding time at the origin, no resetting delay and no stochastic Poisson resets. \(N_t\) counts completed boundary-to-boundary-free excursions, not crossings of zero. All asymptotic statements first fix \(\alpha,L\), then let \(t\to\infty\); the limits \(\alpha\to\infty\) and \(j\to\infty\) are separate.

The earliest directly motivating public source was posted on October 15, 2026; the analysis concerns its continuum *symmetric boundary-triggered reset* protocol. The known one-cycle mean and known Bessel first-passage transform are credited below and are not themselves claimed new.

## Proof

**1. Proper cycle law.** Let \(\eta_L=\inf\{s\ge0:|B_s|=L\}\). The time-change construction makes a reset cycle distributed as \(\tau=\int_0^{\eta_L}|B_s|^\alpha ds\). Because Brownian zero occupation has zero Lebesgue measure, the clock is strictly increasing and the origin is nonsticky. Also \(0<\tau\le L^\alpha\eta_L\) almost surely (with \(L^0=1\)); the bounded Brownian exit time has an exponential moment in a neighborhood of zero. Hence \(\tau\) is nonlattice with moments of all orders and a positive exponential-moment radius; the reset cycles are independent and identically distributed.

**2. Exact cycle transform.** By Feynman--Kac, \(u(x)=\mathbb E_x[e^{-s\tau}]\), for \(s\ge0\), solves \(u''(x)=s|x|^\alpha u(x)\), \(u(-L)=u(L)=1\), with continuous derivative at the origin. The unique even analytic-in-\(x^p\) solution with value one at the origin is

\[
C_s(x)={}_0F_1\!\left(;b;\frac{s|x|^p}{p^2}\right).
\]

To check the differential equation, the coefficient of \(x^{pn}\) is \((s/p^2)^n/[n!(b)_n]\); its second derivative equals the preceding coefficient multiplied by \(s x^{p-2}\), because \(p n(pn-1)=p^2 n(n-1+b)\). The boundary value then gives

\[
\mathbb E[e^{-s\tau}]=\frac1{{}_0F_1(;b;sL^p/p^2)}.
\]

Expansion at zero yields \(\mathbb E\tau=m=L^p/[p(p-1)]\). For \(Z=\tau/m\), write \(F_b(z)={}_0F_1(;b;bz)\); then \(\mathbb E e^{-zZ}=1/F_b(z)\), and

\[
F_b(z)=1+z+\frac{b}{2(b+1)}z^2+O(z^3).
\]

Thus \(\operatorname{Var} Z=1/(b+1)\). The positive Laplace transform formula and the Bessel eigenvalue theory are standard; their use here identifies the physical renewal clock.

**3. Spectral boundary and global tilt.** By the classical product formula for the Bessel \(J_{b-1}\) zeros, \(Z\) is a positive sum of independent exponential variables with positive scales \(4b/j_{b-1,k}^2\), and its maximal positive exponential-moment argument is \(\zeta_b=j_{b-1,1}^2/(4b)\). Consequently \(F_b(z)=1/\mathbb E e^{-zZ}\) is strictly increasing from zero to infinity for \(z\in(-\zeta_b,\infty)\), and its derivative is strictly positive there. This gives the unique analytic \(\lambda_b(\theta)\) solving \(F_b(\lambda_b(\theta))=e^\theta\) for every real \(\theta\). (Here \(F_b(\lambda)\) already includes the argument \(b\lambda\).) Its derivative \(\lambda_b'(\theta)=[\mathbb E_{\lambda_b(\theta)}Z]^{-1}\) is strictly increasing from zero to infinity as \(\theta\) ranges from \(-\infty\) to \(+\infty\), since the exponentially tilted mean decreases strictly with the tilt. Thus \(\lambda_b\) is strictly convex, with \(\lambda_b'(0)=1\) and \(\lambda_b''(0)=\operatorname{Var}Z=1/(b+1)\).

**4. Regenerative SCGF and LDP.** Normalize physical time by \(m\). The cycle-count generating function \(G_\theta(u)=\mathbb E[e^{\theta N_{mu}}]\) satisfies the renewal equation

\[
G_\theta(u)=\Pr\{Z>u\}+e^\theta\int_0^uG_\theta(u-v)\,\Pr\{Z\in dv\}.
\]

Multiplying by \(e^{-\lambda_b(\theta)u}\) makes the convolution kernel a probability measure because \(e^\theta\mathbb E[e^{-\lambda_b(\theta)Z}]=1\). It has a finite positive mean, and the forcing term is directly Riemann integrable by the strictly subcritical exponential tilt and exponential exit tail. The key renewal theorem therefore yields \(G_\theta(u)=c_\theta e^{\lambda_b(\theta)u}(1+o(1))\), with \(c_\theta>0\). Hence \(\lim_{t\to\infty}(m/t)\log\mathbb E e^{\theta N_t}=\lambda_b(\theta)\). Since \(\lambda_b\) is finite, differentiable and strictly convex on all of \(\mathbb R\), with slope range \((0,\infty)\), the Gärtner--Ellis theorem yields the LDP for \(J_t=mN_t/t\) with rate \(I_b\); its good level sets follow from the superlinear right edge. The endpoint \(j=0\) is also covered by \(\Pr\{N_t=0\}=\Pr\{\tau>t\}\) and the principal eigenvalue tail, identifying its rate as \(\zeta_b\).

**5. Sharp boundary and large-current edges.** As \(\theta\to-\infty\), \(e^\theta\to0\) and \(\lambda_b(\theta)\downarrow-\zeta_b\), proving \(I_b(0)=\zeta_b\). For \(\theta\to+\infty\), the modified Bessel asymptotic of \(F_b(\lambda)\) gives \(\log F_b(\lambda)=2\sqrt{b\lambda}+O_b(\log\lambda)\) as \(\lambda\to\infty\). Thus \(\lambda_b(\theta)\sim\theta^2/(4b)\). Strict convexity and monotonic inversion then give \(I_b(j)\sim b j^2\) as \(j\to\infty\). These are both sharp leading constants.

**6. The strict upper-tail ordering.** Let \(1/2\le b_1<b_2<1\). For \(z>0\), the positive-coefficient series

\[
F_b(z)=\sum_{n=0}^\infty\frac{z^n}{n!}\prod_{k=0}^{n-1}\frac{b}{b+k}
\]

has constant coefficients at orders zero and one, while every coefficient at order \(n\ge2\) is strictly increasing in \(b\). Therefore \(F_{b_2}(z)>F_{b_1}(z)\) for all \(z>0\). For each \(\theta>0\), inversion gives the strict inequality \(\lambda_{b_2}(\theta)<\lambda_{b_1}(\theta)\). For \(j>1\), the unique Legendre maximizer for \(I_{b_1}(j)\) is at some \(\theta>0\). Substitution of that same positive \(\theta\) into the second Legendre transform yields \(I_{b_2}(j)>I_{b_1}(j)\). Since \(b(\alpha)\) increases strictly with \(\alpha\), this proves the theorem's physical comparison at fixed mean current.

**7. Counting variance.** The classical regenerative count CLT and its second-moment asymptotic give \(\mathbb EN_t\sim t/m\) and \(\operatorname{Var}N_t\sim(t/m)\operatorname{Var}Z\). Substitute the exact \(\operatorname{Var}Z=1/(b+1)\) to obtain the Fano factor. This is consistent with the second derivative of the exact SCGF, but is not inferred from an unverified finite-time numerical approximation.

## Verification

The accompanying `verify.py` uses exact rational arithmetic for 145 strict hypergeometric-coefficient comparisons and independently integrates the backward differential equation for several parameter pairs. It also checks the hyperbolic/Bessel endpoint identities, numerically solves positive and negative tilted root equations, confirms strict upper-tail rate ordering, and tests both rate-edge constants. It reports the number of assertions actually executed and requires Python with `mpmath` and `scipy`. Run with `python verify.py`. These finite computations corroborate normalization and implementation, not the universal LDP or infinite-parameter comparison, which are established by the proof above.

## Relationship to prior work

Frimpong, Bresque and Roldán (2026) introduce the exact sluggish continuum diffusion with threshold-reset protocol, derive its stationary profile, mean reset duration, occupation behavior and mean reset-cost rates; their first-passage Laplace transform in Section 5.1.2 concerns absorption at the origin with threshold resets, not the reset-count large-deviation rate. The symmetric zero-start cycle mean here is already given in their renewal analysis and is not claimed new.

Martin, Behn and Germano (2011), the classical Bessel first-passage literature, and Clark (2026) establish general Bessel exit distributions, the spectral exponential representation, and hypergeometric transforms. Those results directly cover the one-cycle formula and moment identities after the correct power-coordinate reduction; these are supporting known tools, **not** originality claims. Del Vecchio Del Vecchio and Majumdar (2024) analyze time fractions, last passages and maximum times of an unreset sluggish walker, not renewal reset-current deviations. A separate earlier analysis of excursion extrema for the same sluggish process already contains the two-boundary first-exit transform as a special case; the present result does not claim it new.

The specific assessed addition is the sharp, globally defined normalized reset-current LDP with both boundary constants and *strict all-upper-tail rate ordering across sluggishness*, obtained through an explicit tilt and hypergeometric coefficient comparison. Standard regenerative large-deviation theory explains the general mechanism but does not by itself supply this model-dependent parameter ordering or rate-edge constants. Search-based novelty assessment is qualified; an unlocated stronger general Bessel/renewal comparison theorem could cover these statements.

## Limitations

This is a mathematical statement for an ideal nonsticky natural-scale continuum process with immediate identical resets at symmetric thresholds, not a theorem for the original discrete-time walk at finite lattice spacing. The normalized current rates are compared using each model's own mean cycle duration \(m\). The ordering is proved for upward deviations \(j>1\), not for arbitrary lower tails or for stochastic dominance of individual cycle durations. The limits \(t\to\infty\), \(\alpha\to\infty\) and \(j\to\infty\) are not asserted uniform or interchangeable. Numerical checks are finite and provide no independent audit. The potential coverage by general parameter-comparison results for Bessel exit laws remains a residual priority risk.

## References

- T. D. Frimpong, L. Bresque and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first posted 2026-10-15), https://arxiv.org/html/2610.21962v1 . Sections 2, 3, 5.1.2, 6.1.2 and 7.2.
- S. P. Clark, *Moment-optimal Gamma approximation of Bessel Process exit times*, arXiv:2610.19233 (first posted 2026-10-13), https://arxiv.org/abs/2610.19233 . Introduction, formula (4), Proposition 2.3, and the cumulant recursion.
- E. Martin, U. Behn and G. Germano, *First-passage and first-exit times of a Bessel-like stochastic process*, Phys. Rev. E 83, 051115 (2011), arXiv:1007.4588, https://arxiv.org/html/1007.4588v1 . Boundary classification and Section IV.
- G. Del Vecchio Del Vecchio and S. N. Majumdar, *Generalized arcsine laws for a sluggish random walker with subdiffusive growth*, arXiv:2410.22097 (first posted 2024-10-29), https://arxiv.org/abs/2410.22097 . Occupation and extremal-time observables.
- A. Godec and R. Metzler, *First passage time distribution in heterogeneity controlled kinetics: going beyond the mean first passage time*, Sci. Rep. 6, 20349 (2016), https://pmc.ncbi.nlm.nih.gov/articles/PMC4745057/ . Different two-phase heterogeneous diffusion and first-passage geometry.
