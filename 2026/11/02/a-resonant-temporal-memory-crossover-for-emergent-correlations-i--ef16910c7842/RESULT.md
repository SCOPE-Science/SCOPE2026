# A resonant temporal-memory crossover for emergent correlations in switching harmonic traps

## Finding

Consider at least two independently diffusing overdamped particles in one spatial dimension subject to the **same** randomly switching harmonic confinement. The exact stationary equal-time cross-particle squared-position covariance was given by Biroli, Kulkarni, Majumdar and Schehr [1]. Here we classify its **time-lagged** counterpart and prove a sharp change of the slow relaxation mechanism.

Write the two positive trap relaxation rates as \(\mu_{+}=\kappa+\delta\) and \(\mu_{-}=\kappa-\delta\), with \(\kappa>\delta>0\). The stiffness state \(\sigma_t\in\{-1,+1\}\) switches in either direction with the same rate \(r>0\). Each particle has diffusion coefficient \(D>0\). For distinct particles \(i\ne j\), define
\[
C(h)=\operatorname{Cov}\bigl(X_i(0)^2,X_j(h)^2\bigr),\qquad h\geq0,
\]
in the unique stationary regime. Put
\[
B=\kappa(\kappa+r)-\delta^2,\quad H=2(\kappa^2-\delta^2)+\kappa r,
\quad F=\frac{4D^2\delta^2}{B},
\]
\[
V=\frac{D^2\delta^2[2(\kappa^2-\delta^2)+3\kappa r+r^2]}{H B^2},\qquad
 a_{\pm}=2\kappa+r\pm\sqrt{r^2+4\delta^2}.
\]
All these denominators, \(a_{-}\), and \(a_{+}\) are strictly positive. The covariance is the unique solution of
\[
C''+(4\kappa+2r)C'+4BC=F e^{-2rh},\qquad C(0)=V,\quad C'(0)=0.
\]
It is strictly positive and **strictly decreasing for every \(h>0\)**. Its complete Laplace transform, for \(s>0\), is
\[
\widehat C(s)=\frac{(s+4\kappa+2r)V+F/(s+2r)}{(s+a_-)(s+a_+)}.
\]

The **unique slow-mode crossover** occurs at the harmonic mean of the two positive trap relaxation rates,
\[
\boxed{r_c=\frac{\kappa^2-\delta^2}{\kappa}
=\frac{2\mu_{+}\mu_{-}}{\mu_{+}+\mu_{-}}.}
\]
For \(0<r<r_c\), \(2r<a_-<a_+\) and
\[
C(h)\sim \frac{F}{(a_--2r)(a_+-2r)}e^{-2rh}.
\]
For \(r>r_c\), \(a_-<2r<a_+\) and
\[
C(h)\sim \frac{a_+V+F/(2r-a_-)}{a_+-a_-}e^{-a_-h}.
\]
At the exceptional value \(r=r_c\), the two slow eigenvalues coalesce and the leading term instead is
\[
\boxed{C(h)\sim\frac{F}{a_+-2r}\,h e^{-2rh}.}
\]
Every displayed leading amplitude is **strictly positive**. In particular the asymptotic decay rate is \(\min\{2r,a_-\}\), with a genuine linear-time resonance prefactor at its unique crossing. The approach to zero remains strict and monotone even at resonance. This is a relaxation-spectral crossover, **not** an equilibrium phase transition.

## Assumptions and scope

Let \(N\ge2\) be any finite integer and let \(W_i\) be independent standard Brownian motions, independent of a stationary symmetric two-state continuous-time Markov chain \(\sigma\) with switching rate \(r\). The physical equations, for every \(i=1,\ldots,N\), are
\[
 dX_i(t)=-(\kappa+\delta\sigma_t)X_i(t)\,dt+\sqrt{2D}\,dW_i(t),
\qquad \kappa>\delta>0,\ r>0,\ D>0.
\]
Construct the two-sided stationary solution using the stable stochastic convolution from the infinite past. It is unique in law because the restoring drift is bounded below by the strictly positive number \(\kappa-\delta\). Conditional on the entire stiffness history, the coordinates are independent centered Gaussian processes. The theorem concerns distinct labels \(i\ne j\), the squared-position observable, and nonnegative lag \(h\). The \(\delta=0\) case has identically zero interparticle covariance and is intentionally excluded; \(\kappa-\delta=0\) is not claimed.

## Proof

**1. The common conditional variance.** Conditional on the complete path of \(\sigma\), all particle positions at time \(t\) have variance
\[
Y_t=2D\int_{-\infty}^t\exp\!\left[-2\int_u^t(\kappa+\delta\sigma_v)\,dv\right]du.
\]
Consequently \(D/(\kappa+\delta)\le Y_t\le D/(\kappa-\delta)\). Its paths are continuous and satisfy between switching times
\[
\dot Y_t=2D-2(\kappa+\delta\sigma_t)Y_t.
\]
Conditional independence of distinct Brownian drivers at **both** observation times gives exactly
\[
\operatorname{Cov}(X_i(0)^2,X_j(h)^2)=\operatorname{Cov}(Y_0,Y_h).
\]
This reduction is not an assertion that two observations of a single particle are independent: the indices must be distinct.

**2. Stationary moments.** Put \(m=\mathbb E[Y]\) and \(z=\mathbb E[\sigma Y]\). The generators for \(Y\), \(\sigma Y\), \(Y^2\), and \(\sigma Y^2\) yield
\[
0=2D-2\kappa m-2\delta z,\qquad
0=-2(\kappa+r)z-2\delta m,
\]
\[
0=4Dm-4\kappa\mathbb E[Y^2]-4\delta\mathbb E[\sigma Y^2],
\]
\[
0=4Dz-(4\kappa+2r)\mathbb E[\sigma Y^2]-4\delta\mathbb E[Y^2].
\]
These linear identities have unique solutions since \(B,H>0\), giving \(m=D(\kappa+r)/B\), \(z=-D\delta/B\), and \(\operatorname{Var}(Y)=V\) as specified above. Since the stationary \(Y\) process is continuous and has bounded piecewise differentiable paths, stationarity of \(Y^2\) gives \(C'(0)=\mathbb E[(Y-m)\dot Y]=0\).

**3. Exact lag equation.** Define \(Q(h)=\mathbb E[(Y_0-m)\sigma_hY_h]\) and \(Z(h)=\mathbb E[(Y_0-m)\sigma_h]\). The telegraph generator yields \(Z(h)=z e^{-2rh}\). The joint Markov generator gives
\[
 C'(h)=-2\kappa C(h)-2\delta Q(h),
\]
\[
 Q'(h)=2DZ(h)-2(\kappa+r)Q(h)-2\delta C(h).
\]
Eliminating \(Q\) and inserting \(z=-D\delta/B\) gives the stated second-order forced equation, including the exact positive forcing amplitude \(F\). Its characteristic polynomial factors as \((s+a_-)(s+a_+)\), proving the Laplace transform identity and uniqueness of the covariance solution.

**4. Strict monotonicity and positivity.** Direct simplification of the stationary moments gives the strictly positive number
\[
A=4BV-F=
\frac{4D^2\delta^2r(2\kappa+r)}{HB}>0.
\]
Set \(g(h)=(e^{-a_-h}-e^{-a_+h})/(a_+-a_-)\), which is positive for every \(h>0\). Differentiating the covariance equation and solving the resulting initial-value problem for \(q=C'\), with \(q(0)=0\) and \(q'(0)=-A\), gives
\[
C'(h)=-A g(h)-2rF\int_0^h g(h-u)e^{-2ru}\,du<0,
\qquad h>0.
\]
All three decay rates \(a_-,a_+,2r\) are positive, so \(C(h)\to0\). Therefore \(C(h)>0\) follows from its strict decrease to zero.

**5. Sharp spectral crossing and critical asymptotics.** The difference between the potentially leading rates changes sign precisely at
\[
a_--2r=2\kappa-r-\sqrt{r^2+4\delta^2}=0
\iff r=r_c.
\]
Since \(a_+>2r\) for all allowed parameters, there are no further crossings. When \(r<r_c\), the simple pole at \(s=-2r\) has residue \(F/[(a_--2r)(a_+-2r)]>0\). When \(r>r_c\), the simple pole at \(s=-a_-\) has residue \([a_+V+F/(2r-a_-)]/(a_+-a_-)>0\). At equality, \(s=-2r=-a_-\) is a genuine double pole, whose highest principal part is \(F/[(a_+-2r)(s+2r)^2]\); it yields the asserted positive \(h e^{-2rh}\) term. All remaining poles decay strictly faster or contribute a lower-degree prefactor. Thus the three asymptotic cases hold without exceptional cancellation.

## Verification

The accompanying executable `verify_covariance.py` checks 162 independent symbolic and numerical identities: exact polynomial relations, agreement of \(V\) with the earlier stationary pair-correlation formula [1, Eq. (14)], a separate four-component Markov-moment propagation, the scalar forced ODE, strict monotonicity at multiple positive lags, and the three spectral-rate regimes. It uses only Python, NumPy, SciPy and SymPy and can be run as `python verify_covariance.py`. The critical-sign and positivity arguments above are analytical; sampled numerical tests are neither substitutes for these proofs nor claims of exhaustive verification.

As one illustrative nondimensional choice, \(\kappa=1\), \(\delta=0.4\), and \(D=1\) give \(r_c=0.84\). The asymptotic rate is \(0.6\) at \(r=0.3\), \(1.68\) with an additional linear-time factor at \(r=0.84\), and approximately \(1.845934077146\) at \(r=2\).

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr [1] establish the common-switching particle model, its full **one-time** stationary Gaussian mixture, and its positive **equal-time** cross-particle squared-position covariance. Their results fix the zero-lag value \(V\) but do not determine temporal persistence of that correlation. Frydel [2] studies the on/off specialization \(\mu_-=0\), rather than the present strictly positive two-stiffness region and its interior harmonic-mean resonance. The experimental work of Biroli and collaborators [3] measures stationary collective correlations and time-delayed **linear-position** hydrodynamic correlations; the latter vanish without direct coupling and are not this squared-energy observable. Behme [4] provides broadly applicable Markov-modulated Ornstein–Uhlenbeck covariance machinery in a financial-stochastic setting. That general operator machinery provides related techniques but does not state the strictly monotone physical two-particle energy memory, the unique harmonic-mean rate threshold, or its double-pole asymptotic. The asserted contribution is this **sharp physical relaxation classification**, not the elementary general principle that finite-dimensional Markov moment systems can be exponentiated.

## Limitations

The result requires two **positive and distinct** stiffnesses, symmetric Markov switching, independent microscopic Brownian motions conditional on the common stiffness, and exact stationarity. In particular it does not cover hydrodynamically interacting particles, non-Poisson switching, unequal switching rates, one-time initialization at the origin, or the on/off boundary \(\mu_-=0\). It does not assert a thermodynamic phase transition or describe same-particle squared-position autocorrelation. The all-lag sign and exact threshold are proved, whereas no claim is made about optimal estimation from finite noisy records. A wider general stochastic-volatility theorem may supply alternative derivations of portions of the covariance formula; independent publication-priority assessment remains outstanding.

## References

[1] M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first public 2023-12-05), https://arxiv.org/abs/2312.02570 .

[2] D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (first public 2024-07-16), https://arxiv.org/abs/2407.12213 .

[3] M. Biroli, S. Ciliberto, M. Kulkarni, S. N. Majumdar, A. Petrosyan and G. Schehr, *Experimental evidence for strong emergent correlations between particles in a switching trap*, arXiv:2508.07199 (first public 2025-08-10), https://arxiv.org/html/2508.07199v2 .

[4] A. Behme, *Volatility modelling in a Markov-switching environment: two Ornstein–Uhlenbeck-related approaches*, arXiv:2407.05866 (first public 2024-07), https://arxiv.org/abs/2407.05866 ; *Finance and Stochastics* **29** (2025), 1109–1138, https://link.springer.com/article/10.1007/s00780-025-00567-3 .
