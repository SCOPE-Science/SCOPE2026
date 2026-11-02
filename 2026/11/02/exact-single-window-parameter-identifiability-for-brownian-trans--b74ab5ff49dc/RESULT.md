# Exact single-window parameter identifiability for Brownian transport with diffusivity-only resetting

## Finding

A particle can have a strictly linear mean-square displacement while the law of each finite-time displacement is non-Gaussian and its successive squared increments remain correlated. In the model below, an exact **one-observation-window inverse theorem** identifies an unobserved Poisson reset rate and a diffusivity scale from only a coordinate variance and its normalized fourth cumulant. These two observable moments determine the parameters uniquely at **every** observation duration; neither the reset times nor the fluctuating diffusivity need to be observed.

For every dimension \(d\ge1\) and every \(t>0\), write \(z=\alpha t\). Then
\[
V(t)=\mathbb E[(X_t^j)^2]=\frac{4\Lambda^2t}{\alpha},\qquad
K(t)=\frac{\mathbb E[(X_t^j)^4]-3V(t)^2}{3V(t)^2}
=10\frac{z-1+e^{-z}}{z^2}.
\]
The map \(z\mapsto K\) is a strictly decreasing bijection from \((0,\infty)\) onto \((0,5)\). Thus, if the ideal population quantities \(V(t)>0\) and \(0<K(t)<5\) are observed at known \(t>0\), the parameters are **identified without ambiguity** by
\[
\alpha=\frac{K_*^{-1}(K(t))}{t},\qquad
\Lambda=\sqrt{\frac{\alpha V(t)}{4t}},\qquad
K_*(z)=10\frac{z-1+e^{-z}}{z^2}.
\]
This is not a statement about stable estimation with finite noisy samples.

The same invariant is obtained from the radial observable in every integer dimension:
\[
\frac{d}{d+2}\frac{\mathbb E|X_t|^4}{(\mathbb E|X_t|^2)^2}-1=K(t).
\]
It is strictly positive at every finite time, approaches \(5\) as \(t\downarrow0\), and is asymptotic to \(10/(\alpha t)\) at large times. Meanwhile
\[
\operatorname{Cov}\!\left((X_h^i-X_0^i)^2,(X_{\tau+h}^j-X_\tau^j)^2\right)
=\frac{80\Lambda^4}{\alpha^4}e^{-\alpha(\tau-h)}(1-e^{-\alpha h})^2>0
\]
for every \(h>0\), \(\tau\ge h\), and \(i,j\in\{1,\ldots,d\}\). Here raw nonoverlapping displacement increments are uncorrelated, and for distinct components they are conditionally independent given the diffusivity path. Positive squared-increment correlations reveal the otherwise hidden reset rate, independently of the moment inversion.

For reference, the explicit Fourier–Laplace transform is computed below. Its general renewal quotient is **not new**: the partial-reset propagator identity was established by Olsen and Löwen (2024). The contribution assessed here is the **model-specific all-duration strict inverse theorem**, the evaluated universal kurtosis curve and its associated squared-increment clustering law.

## Assumptions and scope

Fix an integer \(d\ge1\) and constants \(\alpha,\Lambda>0\). Let \(B=(B^1,\ldots,B^d)\) and \(W\) be mutually independent standard Brownian motions, and let \(N\) be an independent homogeneous Poisson process of rate \(\alpha\). The scalar mobility \(\omega\) follows \(d\omega_t=\sqrt2\Lambda\,dW_t\) between Poisson events and is set to zero on each event. The observed position never resets, with \(X_0=0\) and Itô dynamics
\[
dX_t^j=\sqrt2\,\omega_t\,dB_t^j,\qquad j=1,\ldots,d.
\]
The physical diffusivity is the nonnegative process \(D_t=\omega_t^2\), the same one for every observed coordinate. The mobility is initialized in its unique invariant law, which is symmetric Laplace with density
\[
p_{\mathrm{eq}}(w)=\frac{\sqrt\alpha}{2\Lambda}e^{-\sqrt\alpha|w|/\Lambda},\quad w\in\mathbb R.
\]
This stationary initialization is essential: with a fresh mobility \(\omega_0=0\), the finite-time moment formulas differ. The observed process \(X\) has stationary increments but no stationary position distribution. All expectations and covariances refer to ideal ensembles; \(X\) is unbounded in time.

## Proof

**1. Invariant diffusivity moments and covariance.** At a stationary observation epoch the time \(A\) since the last mobility reset is exponential with parameter \(\alpha\). Conditional on \(A=a\), the mobility is centered normal of variance \(2\Lambda^2a\). Mixing these normals over the exponential age gives the stated Laplace law. Hence
\[
\mathbb E\omega_0^2=\frac{2\Lambda^2}{\alpha},\qquad
\mathbb E\omega_0^4=\frac{24\Lambda^4}{\alpha^2},\qquad
\operatorname{Var}(\omega_0^2)=\frac{20\Lambda^4}{\alpha^2}.
\]
For \(u\ge0\), conditional on the absence of a reset between zero and \(u\), \(\omega_u=\omega_0+\sqrt2\Lambda(W_u-W_0)\); after at least one reset, \(\omega_u\) is independent of \(\omega_0\). The conditional expectation contains the \(\omega_0^2\) term only on the no-reset event, giving exactly
\[
\operatorname{Cov}(D_0,D_u)=\frac{20\Lambda^4}{\alpha^2}e^{-\alpha u}.
\]
The mean and covariance are continuous at zero and absolutely integrable in lag.

**2. Conditional Gaussian mixing and fourth-order law.** Set \(H_t=\int_0^tD_u\,du\). Conditional on the entire mobility path, \(X_t\) is isotropic Gaussian with covariance \(2H_tI_d\). Thus
\[
\mathbb E[(X_t^j)^2]=2\mathbb EH_t=\frac{4\Lambda^2t}{\alpha},\qquad
\operatorname{cum}_4(X_t^j)=12\operatorname{Var}(H_t).
\]
Stationarity yields
\[
\operatorname{Var}(H_t)=2\int_0^t(t-u)\operatorname{Cov}(D_0,D_u)\,du
=\frac{40\Lambda^4}{\alpha^4}(z-1+e^{-z}),\quad z=\alpha t.
\]
Consequently \(\operatorname{cum}_4(X_t^j)=480\Lambda^4(z-1+e^{-z})/\alpha^4\), and dividing by three times the squared variance yields \(K(t)=10(z-1+e^{-z})/z^2\). For conditional isotropic Gaussians, \(\mathbb E(|X_t|^4\mid H_t)=4d(d+2)H_t^2\) and \(\mathbb E|X_t|^2=2d\mathbb EH_t\), proving the stated dimension-independence exactly for all \(d\ge1\).

**3. Strict inverse theorem at every observation time.** For \(z>0\), the numerator \(z-1+e^{-z}\) is positive, since it equals \(\int_0^z(1-e^{-v})\,dv\). Direct differentiation gives
\[
\frac{z^3}{10}K_*'(z)=2-z-(z+2)e^{-z}=:G(z).
\]
The boundary value is \(G(0)=0\) and \(G'(z)=-1+(1+z)e^{-z}<0\), since \(e^z>1+z\) for \(z>0\). Therefore \(K_*'(z)<0\). Taylor expansion and elementary asymptotics give \(\lim_{z\downarrow0}K_*(z)=5\) and \(\lim_{z\to\infty}K_*(z)=0\). Hence \(K_*\) maps \((0,\infty)\) bijectively onto \((0,5)\), and the inverse formulas above are unique for every \(t>0\). No finite-time threshold or multiple-solution regime exists for this ideal inference problem.

**4. Volatility clustering, independently visible from position increments.** Let \(I_1=[0,h]\), \(I_2=[\tau,\tau+h]\) with \(h>0\) and \(\tau\ge h\). Conditional on the mobility path, Brownian increments on these disjoint time intervals are independent, with coordinate conditional variances \(2\int_{I_1}D_u\,du\) and \(2\int_{I_2}D_u\,du\). Their squared increments thus have covariance
\[
4\int_0^h\int_\tau^{\tau+h}\operatorname{Cov}(D_u,D_v)\,dv\,du
=\frac{80\Lambda^4}{\alpha^4}e^{-\alpha(\tau-h)}(1-e^{-\alpha h})^2.
\]
All factors are strictly positive. The result holds whether the two coordinate indices coincide or differ. At fixed \(h\), the ratio between this covariance at two nonoverlapping lags \(\tau_1,\tau_2\) equals \(e^{-\alpha(\tau_2-\tau_1)}\). This supplies an independent ideal ensemble measurement of the same reset rate.

**5. Complete propagator for reproducibility, with prior-renewal provenance.** Let \(k=|\xi|\) and \(s>0\). By conditional Gaussianity,
\[
\mathbb E[e^{i\xi\cdot X_t}]=\mathbb E\exp\!\left[-k^2\int_0^t\omega_u^2\,du\right].
\]
For a reset-free mobility started at \(\omega_0=w\), harmonic-oscillator Feynman–Kac solves \(\partial_tF=\Lambda^2\partial_{ww}F-k^2w^2F\), \(F(0,w)=1\), giving
\[
F_k(t,w)=\frac{\exp[-\frac{k}{2\Lambda}\tanh(2\Lambda kt)w^2]}{\sqrt{\cosh(2\Lambda kt)}}.
\]
Define the reset-fresh kernel \(f_k(t)=F_k(t,0)\), and the equilibrium-initialized no-reset kernel
\[
g_k(t)=\frac{\sqrt\alpha}{\Lambda}f_k(t)\int_0^\infty\exp\!\left[-\frac{\sqrt\alpha}{\Lambda}y-\frac{k}{2\Lambda}\tanh(2\Lambda kt)y^2\right]dy.
\]
The nonnegative kernels are continuous with value one at \(k=0\). Write \(\widehat f_k(q)=\int_0^\infty e^{-qt}f_k(t)dt\) and similarly \(\widehat g_k(q)\). On the first future reset, the remaining displacement has the reset-fresh law; the same first-reset argument with initial mobility zero gives a renewal equation for that fresh law. Taking temporal Laplace transforms yields
\[
\int_0^\infty e^{-st}\mathbb E[e^{i\xi\cdot X_t}]dt
=\frac{\widehat g_k(s+\alpha)}{1-\alpha\widehat f_k(s+\alpha)}.
\]
The denominator is strictly positive for every \(s>0\), because \(\alpha\widehat f_k(s+\alpha)\le\alpha/(s+\alpha)<1\); at \(k=0\) the ratio reduces to \(1/s\). This is a **specific evaluation** of the generic partial-reset Fourier–Laplace renewal quotient already derived by Olsen and Löwen (2024, their Eq. (5)), not an independent discovery of that generic quotient. The reset-free \(f_k\) is explicitly given by Santra, Basu, and Sabhapandit (2022, Eq. (14)).

**6. Gaussian long-time limit.** The stationary Poisson-reset mobility is exponentially mixing with finite moments, so its time-averaged diffusivity satisfies \(H_t/t\to2\Lambda^2/\alpha\) almost surely. The conditional characteristic function at the diffusive scale is \(\mathbb E\exp[-|\xi|^2H_t/t]\); bounded convergence gives its limit \(\exp[-2\Lambda^2|\xi|^2/\alpha]\). Thus
\[
X_t/\sqrt t\ \Rightarrow\ N_d(0,(4\Lambda^2/\alpha)I_d).
\]
This is weak convergence, not a quantitative distributional rate.

## Verification

Run the included standalone program with \(\texttt{python3 verify.py}\), using NumPy, SciPy, and SymPy. It separately verifies the harmonic-oscillator Feynman–Kac PDE; fourth-moment generator identities; three Fourier–Laplace renewal comparisons against a time-domain quadrature; an independently simulated mobility-path conditional characteristic function; 45 strict-kurtosis derivative and boundary checks; and three analytic covariance integrals against direct numerical integration. A representative independent comparison at \(t=2\), \(\alpha=1.3\), \(\Lambda=0.7\), \(k=0.6\) gives time-domain renewal \(0.67599544\) versus conditional Monte Carlo \(0.67686311\). The stochastic tolerance covers finite simulation error and discretization. These tests support but do not replace the proofs above.

## Relationship to prior work

Santra, Basu, and Sabhapandit (arXiv:2205.00549v1, 1 May 2022) study the same unreset squared-Brownian mobility and then **joint resetting of position and mobility**. Their Section 7 explicitly names *resetting only the diffusion coefficient* as an open alternative. Their no-reset harmonic-oscillator kernel is an essential known ingredient and not newly claimed.

Olsen and Löwen (arXiv:2401.12685v1, 23 January 2024, Section 2, Eq. (5)) prove a **general** Fourier–Laplace renewal quotient for spatially homogeneous coupled systems under resetting of a hidden coordinate while leaving the position untouched. Their general theorem **does cover the renewal architecture** used here. The quotient by itself is neither a novelty assertion nor the focus of this finding. They discuss inertial velocity-reset transport rather than the explicit squared-Brownian volatility observation law, its strictly invertible one-time fourth-cumulant curve, and the evaluated disjoint squared-increment clustering expression.

Miyaguchi, Akimoto, and Yamamoto (arXiv:1605.00106v1, 30 April 2016, Appendix E) derive a general non-Gaussianity functional in terms of an arbitrary fluctuating-diffusivity covariance. That generic relation is **covered prior work**. They analyze a two-state diffusivity law, not the exact Poisson-reset squared-Brownian diffusivity. The finite-time evaluated curve and strict parameter uniqueness require the particular stationary fourth moment and monotonicity computation presented here. Santra and Olsen (arXiv:2506.08876v1, 10 June 2025) study energy renewals of underdamped Langevin dynamics; their reset is of kinetic energy and does not supply this particular stochastic-volatility observable law.

The **originality claim is restricted** to the integrated model-specific *exact two-parameter identifiability at any observation duration* and the evaluated dimension-universal fourth-order and disjoint-increment observables. The generic Feynman–Kac, mixture, and renewal methods are acknowledged as prior theory. Relevant full primary sources and accessible research records were compared by mathematical implication rather than title alone; absence of an identified exact inverse theorem is not proof of exhaustive publication priority.

## Limitations

The mobility starts in its invariant law; starting it at zero changes the shape curve. Position is *never* reset and cannot itself have a stationary distribution. The common mobility drives every coordinate; independent component mobilities have different cross-component moments. The inference is algebraic at the population-moment level and does not prove finite-sample convergence, identifiability from only the mean-square displacement, robustness to measurement noise, or extensions to general mobility/renewal laws. Generic renewal and fluctuating-diffusivity identities predate this application. A stronger, not yet identified model-specific published theorem might subsume the evaluation or identifiability conclusion. Independent audit has not been performed.

## References

1. I. Santra, U. Basu, and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (2022), https://arxiv.org/html/2205.00549v1 (especially Eq. (14) and Section 7).
2. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (2024), https://arxiv.org/html/2401.12685v1 (especially Section 2, Eq. (5)).
3. T. Miyaguchi, T. Akimoto, and E. Yamamoto, *Langevin equation with fluctuating diffusivity: a two-state model*, arXiv:1605.00106v1 (2016), https://arxiv.org/html/1605.00106v1 (especially Appendix E).
4. I. Santra and K. S. Olsen, *Brownian motion with stochastic energy renewals*, arXiv:2506.08876v1 (2025), https://arxiv.org/abs/2506.08876 (different renewal observable).
