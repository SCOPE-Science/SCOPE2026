# Planar power-diffusion universality under radial threshold resetting

## Finding
For an integer dimension \(d\ge1\), exponent \(\alpha\ge0\), and threshold \(L>0\), consider radial Itô diffusion with generator
\[\mathcal L_{d,\alpha}f(r)=r^{-\alpha}\bigl(f''(r)+(d-1)f'(r)/r\bigr),\quad 0<r<L,\]
started at \(r=0\), killed when it reaches \(L\), and immediately restarted from \(0\). The boundary at \(0\) means the canonical instantaneous reflecting/entrance extension specified below, without holding or additional stickiness. Set
\[\gamma=\alpha+2,\quad \kappa=L^\gamma/\gamma^2,\quad b=(d+\alpha)/\gamma,\quad U_s=(R_{\kappa s}/L)^\gamma.\]
Then the complete reset process \(U\), including all hitting times and finite-dimensional distributions, is the unit-threshold reset squared-Bessel process with generator \(u\partial_{uu}+b\partial_u\). **In dimension \(d=2\), \(b=1\) for every \(\alpha\ge0\): the complete transformed-and-rescaled reset law is independent of the slowing exponent and threshold.** For fixed \(d\ne2\), the parameter \(b\) genuinely depends on \(\alpha\); this uniqueness statement concerns the displayed normalization.

The unique invariant distribution of \(U\) has density, for \(0<u<1\),
\[p_b(u)=\begin{cases}\dfrac{b}{b-1}(1-u^{b-1}),&b\ne1,\\-\log u,&b=1.\end{cases}\]
In particular, in the planar case \(U_\infty\) is distributed as a product of two independent uniform variables on \((0,1)\), \(\mathbb E[U_\infty^k]=(k+1)^{-2}\) for integers \(k\ge0\), and \(-\log(R_\infty/L)\) is Gamma with shape \(2\) and rate \(\alpha+2\).

The entire stationary radial classification is explicit. With \(Z=R_\infty/L\),
\[f_{d,\alpha}(z)=\begin{cases}(\alpha+1)(\alpha+2)z^\alpha(1-z),&d=1,\\(\alpha+2)^2z^{\alpha+1}\log(1/z),&d=2,\\\dfrac{(\alpha+2)(d+\alpha)}{d-2}z^{\alpha+1}(1-z^{d-2}),&d\ge3,\end{cases}\quad 0<z<1.\]
Thus for \(d=1\), \(Z\) is Beta\((\alpha+1,2)\); for \(d\ge3\), \(Z^{d-2}\) is Beta\(((\alpha+2)/(d-2),2)\). The planar case is the logarithmic transition between the two power laws.

In \(d=2\), the rescaled inter-reset duration \(\tau\) satisfies
\[\mathbb E e^{-s\tau}=[{}_0F_1(;1;s)]^{-1}=[I_0(2\sqrt s)]^{-1},\quad \mathbb E\tau=1,\quad\operatorname{Var}(\tau)=\tfrac12.\]
For the reset count \(N_t\) measured in this rescaled clock, the functional renewal central limit theorem gives
\[\bigl((N_{Tt}-Tt)/\sqrt T\bigr)_{t\ge0}\Rightarrow\bigl(B_t/\sqrt2\bigr)_{t\ge0}\]
in the Skorokhod topology as \(T\to\infty\), with standard Brownian motion \(B\), and \(\lim_{T\to\infty}\operatorname{Var}(N_T)/\mathbb E N_T=1/2\).

## Assumptions and scope
The radial process is fixed by constructing \(U\) from the non-sticky squared-Bessel diffusion of dimension \(2b>0\): \(dU_s=b\,ds+\sqrt{2U_s}\,dW_s\) on \([0,1]\), starting at \(0\), instantaneously reset to \(0\) on hitting \(1\). The original process is recovered as \(R_t=L(U_{t/\kappa})^{1/\gamma}\), with reset times scaled by \(\kappa\). When \(b<1\), this selects instantaneous reflection at zero rather than absorption, killing or stickiness. The generator is the Itô convention; changing the stochastic interpretation of heterogeneous diffusion can change the radial drift and all coefficients.

## Proof
**Generator conjugacy.** For \(u=(r/L)^\gamma\), direct differentiation gives
\[\mathcal L_{d,\alpha}u=\gamma(d+\alpha)/L^\gamma,\qquad r^{-\alpha}(\partial_ru)^2=\gamma^2u/L^\gamma.\]
Consequently \(\mathcal L_{d,\alpha}(g\circ u)=\kappa^{-1}(u g''+b g')\); deterministic rescaling by \(\kappa\) gives the claimed squared-Bessel process, including its canonical zero boundary via the construction. Because cycles restart from zero, the equivalence is pathwise at all reset epochs, not just at stationarity. Moreover \(\partial_\alpha b=(2-d)/(\alpha+2)^2\), proving the distinguished planar value.

**Invariant occupation density.** The killed unit-interval process with generator \(\mathcal B_b=u\partial_{uu}+b\partial_u\) has mean first-hitting time \(m(u)=(1-u)/b\), since \(\mathcal B_bm=-1\), \(m(1)=0\), and the regular zero boundary selects this unique non-explosive solution. Thus \(\mathbb E_0\tau=1/b<\infty\). Renewal-reward theory makes the stationary density the zero-start Green occupation divided by this mean. Explicitly, the claimed \(p_b\) is normalized, vanishes at \(u=1\), solves the adjoint stationary equation \((up_b)''-(bp_b)'=0\) in \((0,1)\), and has constant outward probability flux \(bp_b-(up_b)'=b\), exactly balancing resets to zero at rate \(1/\mathbb E_0\tau=b\). Its zero-boundary behavior agrees with the canonical diffusion. This gives the regenerative invariant density; regeneration with finite mean gives uniqueness and weak convergence of time marginals.

**Stationary radial formulas.** Transform \(p_b\) by \(u=z^\gamma\), so \(f_Z(z)=\gamma z^{\gamma-1}p_b(z^\gamma)\). For \(d\ne2\) use \(\gamma(b-1)=d-2\); the displayed formulas follow. The Beta statements follow by the change of variable \(z^{d-2}\), and for \(d=2\), \(p_1(u)=-\log u\) is the standard product-of-uniforms density. Hence \(-\log U_\infty\) is Gamma\((2,1)\), which gives the radial log law.

**Planar inter-reset law.** For \(b=1\), \(\phi_s(u)=\mathbb E_u e^{-s\tau}\) is the bounded-at-zero solution of \(u\phi_s''+\phi_s'=s\phi_s\), \(\phi_s(1)=1\). Its regular power-series solution is \({}_0F_1(;1;su)/{}_0F_1(;1;s)\). At zero this gives the claimed Laplace transform. Expanding the reciprocal at zero yields \(1-s+3s^2/4+O(s^3)\), so the second moment is \(3/2\) and the variance is \(1/2\). Repeated reset cycles are independent, identically distributed, continuous and positive, with finite second moment; standard renewal-count functional central limit and variance asymptotics give the final statements. Ordinary large-time counts in physical units correspond to \(N_{t/\kappa}\).

## Verification
Run the attached `verify.py` using Python 3 with SymPy and mpmath. The recorded `verify.out` confirms the symbolic generator conjugacy, stationary adjoint equation, density normalization and planar limit, second-moment boundary-value equations, first 20 planar stationary moments, 30 normalized radial density cases and exact hypergeometric series through cubic order. These finite checks corroborate algebra; the statements for every exponent, dimension and time follow from the analytical argument, not sample enumeration.

## Relationship to prior work
Frimpong, Bresque and Roldán (arXiv:2610.21962, first public 2026-10-15) study one-dimensional sluggish random walks with Poissonian and threshold resetting, motivating the higher-dimensional threshold problem. Sandev, Fumeron, Henkel and Lenzi (arXiv:2609.24427, first public 2026-09-21) treat radially heterogeneous **planar Poissonian** resetting; an independent exponential clock is different from the first-exit threshold clock here. Das, Majumdar and Pal (arXiv:2609.24438) analyze threshold resetting for drift-diffusion and supply general renewal/Green formalism; the specific singular heterogeneous radial generator, planar pathwise parameter cancellation, full dimension-indexed invariant classification and renewal-count noise formula are not supplied by the accessible materials. Bessel hitting-time transforms and regenerative stationary occupation are classical ingredients, not claimed as discoveries. A generic theorem applicable by nontrivial specialization could reduce the originality of the presentation; that historical priority risk is explicitly retained.

## Limitations
The theorem concerns a canonically defined radial Itô model, not arbitrary heterogeneous diffusion prescriptions, angular observables, stochastic resetting clocks or resets to locations other than the origin. It assumes \(\alpha\ge0\), a fixed integer dimension and no holding at zero. The stationary law is radial only. The independent audit has not been performed. Historical coverage through a general first-exit/reset diffusion theorem under different notation is not completely excluded.

## References
- T. D. Frimpong, L. Bresque, E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962 (2026; first submitted October 15).
- T. Sandev, S. Fumeron, M. Henkel, E. K. Lenzi, *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting*, arXiv:2609.24427 (2026; first submitted September 21).
- Das, Majumdar and Pal, *Non-equilibrium dynamics of drift-diffusion process under threshold resetting*, arXiv:2609.24438 (2026).
- Y. Hamana and H. Matsumoto, *The probability distributions of the first hitting times of Bessel processes*, arXiv:1106.6132 (classical Bessel hitting-time background).
