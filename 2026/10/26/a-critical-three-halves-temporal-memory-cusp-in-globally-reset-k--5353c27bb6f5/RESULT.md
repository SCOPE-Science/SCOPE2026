# A critical three-halves temporal-memory cusp in globally reset Kuramoto coherence

## Finding

In a globally reset infinite-population Kuramoto ensemble with Lorentzian intrinsic-frequency law, the **stationary two-time coherence covariance** has a different long-lag asymptotic precisely at the ordinary synchronization threshold. At critical coupling it equals a strictly positive constant times \(e^{-\lambda t}t^{-3/2}\); away from the threshold, except for one exactly constant trajectory, it is a strictly positive constant times a pure exponential with a strictly larger decay rate. Although Poisson resetting maintains positive stationary mean coherence, it does not erase this sharp dynamical distinction.

Define \(C(t)=\mathbb E[(\mathcal R(0)-m)(\mathcal R(t)-m)]\) for stationary order-parameter amplitude \(\mathcal R\), where \(m=\mathbb E[\mathcal R(0)]\). The exact identity, valid for every \(t\geq0\), is

\[
C(t)=e^{-\lambda t}\operatorname{Cov}(f(A),f(A+t)),\qquad A\sim\operatorname{Exp}(\lambda).
\]

For \(K<2\sigma\), put \(\kappa_-=\sigma-K/2\) and \(b_- = \rho_0(1+K\rho_0^2/(2\kappa_-))^{-1/2}\). Then

\[
C(t)=B_-e^{-(\lambda+\kappa_-)t}\bigl(1+O(e^{-2\kappa_-t})\bigr),\quad
B_-=b_-\operatorname{Cov}(f(A),e^{-\kappa_-A})>0.
\]

For \(K>2\sigma\), define \(q=\sqrt{1-2\sigma/K}\) and \(\kappa_+=K-2\sigma\). If \(\rho_0\neq q\), put \(b_+=q(1-q^2/\rho_0^2)/2\). Then

\[
C(t)=B_+e^{-(\lambda+\kappa_+)t}\bigl(1+O(e^{-\kappa_+t})\bigr),\quad
B_+=b_+\operatorname{Cov}(f(A),e^{-\kappa_+A})>0.
\]

If \(\rho_0=q\), the deterministic flow is constant, hence \(C(t)=0\) for all lags.

At \(K=2\sigma\), let \(h=(2\sigma)^{-1/2}\), \(c=(2\sigma\rho_0^2)^{-1}\), and \(z=\lambda c\). Then

\[
C(t)=B_c e^{-\lambda t}t^{-3/2}\bigl(1+O(t^{-1})\bigr),\qquad
B_c=-\frac{h}{2}\operatorname{Cov}\bigl(h(A+c)^{-1/2},A\bigr)>0,
\]

and the coefficient has the closed form

\[
B_c=\frac{e^z}{4\sigma\sqrt\lambda}
\left[(z+1)\Gamma\!\left(\tfrac12,z\right)
-\Gamma\!\left(\tfrac32,z\right)\right].
\]

Here \(\Gamma(s,z)=\int_z^\infty u^{s-1}e^{-u}\,du\) is the upper incomplete gamma function. The critical power is **three-halves**, rather than the one-half power of an uncentered, unreset critical relaxation.

## Assumptions and scope

Choose physical parameters \(\sigma>0\), \(K\geq0\), \(\lambda>0\), \(0<\rho_0\leq1\). The intrinsic frequencies have a centered Lorentzian distribution of half-width \(\sigma\). The infinite-population Ott--Antonsen reduction with a fixed common reset configuration has amplitude equation, between reset times,

\[
\dot f=(K/2-\sigma)f-(K/2)f^3,\qquad f(0)=\rho_0.
\]

Reset times form an independent homogeneous Poisson process of rate \(\lambda\) shared by the oscillator population; at each reset the amplitude returns to the same value \(\rho_0\), with no independent thermal noise in this reduced amplitude equation. We consider the unique stationary renewal realization of the scalar amplitude, obtained from a two-sided Poisson reset process. Statements concern stationary covariance at physical lag \(t\to\infty\), with all stated parameters fixed, and not finite-size oscillator fluctuations or a joint small-reset-rate limit.

## Proof

**Stationarity and covariance identity.** Let \(A_t\) be the time since the last event of a stationary, two-sided Poisson process of rate \(\lambda\). The unique stationary amplitude is \(\mathcal R(t)=f(A_t)\); its marginal reset age is exponential. Split the covariance at lag \(t\) according to whether there is any reset in the intervening time interval. On the no-reset event (probability \(e^{-\lambda t}\)), the future amplitude is \(f(A_0+t)\). Otherwise, the future state depends on reset events after time zero and is independent of the initial age. Subtracting the product of stationary means yields the exact displayed renewal identity. All covariance expectations are finite because the amplitude stays in the compact interval between its initial value and the deterministic equilibrium.

**Subcritical asymptotic.** With \(\kappa_-=\sigma-K/2>0\), direct separation of variables gives

\[
f(a)=\frac{\rho_0e^{-\kappa_-a}}{\sqrt{1+\frac{K\rho_0^2}{2\kappa_-}(1-e^{-2\kappa_-a})}}.
\]

The denominator expansion is uniform for all \(a\geq0\) when replacing \(a\) by \(a+t\) and letting \(t\to\infty\). Thus \(f(a+t)=b_-e^{-\kappa_-t}e^{-\kappa_-a}+O(e^{-3\kappa_-t}e^{-3\kappa_-a})\). Inserting this into the covariance identity gives the stated leading term and remainder. Since both \(f(a)\) and \(e^{-\kappa_-a}\) are strictly decreasing, their covariance under the nonatomic exponential age law is strictly positive (use two independent ages and the identity \(2\operatorname{Cov}(g(A),h(A))=\mathbb E[(g(A)-g(A'))(h(A)-h(A'))]\)).

**Supercritical asymptotic.** Write \(q=\sqrt{1-2\sigma/K}>0\) and \(\kappa_+=K-2\sigma>0\). The deterministic solution is

\[
f(a)=\frac{q}{\sqrt{1+(q^2/\rho_0^2-1)e^{-\kappa_+a}}}.
\]

If \(\rho_0=q\), this is constant. Otherwise, expanding the square root at large \(a+t\) gives \(f(a+t)=q+b_+e^{-\kappa_+t}e^{-\kappa_+a}+O(e^{-2\kappa_+t}e^{-2\kappa_+a})\). The constant \(q\) drops out of the covariance. When \(\rho_0>q\), both \(f\) and the exponential factor decrease, and \(b_+>0\). When \(\rho_0<q\), \(f\) increases, its covariance with the decreasing exponential factor is negative, and \(b_+<0\). Therefore \(B_+>0\) in both nonconstant cases.

**Critical asymptotic.** At \(K=2\sigma\), the flow becomes

\[
f(a)=(\rho_0^{-2}+2\sigma a)^{-1/2}=h(a+c)^{-1/2}.
\]

For every \(a\geq0\), Taylor expansion with a uniform remainder bound gives

\[
f(a+t)=h t^{-1/2}-\frac h2(a+c)t^{-3/2}+O\bigl((a+c)^2t^{-5/2}\bigr).
\]

The exponential age has all moments and \(f(A)\) is bounded. Consequently this expansion may be integrated against \(f(A)-m\). The leading \(t^{-1/2}\) term cancels **exactly** on centering, and the remaining leading coefficient is \(-h\operatorname{Cov}(f(A),A)/2\). This coefficient is strictly positive because \(f\) is strictly decreasing in age. The remainder is \(O(e^{-\lambda t}t^{-5/2})\). Evaluating \(\mathbb E[f(A)]\) and \(\mathbb E[Af(A)]\) using \(u=\lambda(a+c)\) yields the displayed upper-incomplete-gamma expression. This establishes each claimed quantifier, including the critical prefactor's strict positivity.

## Verification

The accompanying stand-alone `verify_kuramoto.py` uses high-precision quadrature of the exponential stationary-age law and independently evaluates the explicit deterministic solution. It checks the differential equation, boundary conditions, the gamma-function coefficient against an independently integrated covariance, and the approach to all three claimed asymptotic regimes. Its recorded execution completed 37 deterministic assertions. These calculations provide reproducibility checks but not the logical basis of the infinite-lag proof, which is the analytic renewal and asymptotic argument above. Run `python verify_kuramoto.py` with Python and `mpmath` installed.

## Relationship to prior work

Sarkar and Gupta (2022, arXiv:2203.00339, Sections III.2--III.3) supply the globally reset Lorentzian Kuramoto/Ott--Antonsen dynamics and its one-time stationary synchronization distribution. Bressloff (2024, arXiv:2401.03501, Section V.3) develops global-reset order-parameter dynamics and stationary statistics. Acharya, Sarkar, and Gupta (2025, arXiv:2504.08510) investigate related stationary-order-parameter fluctuations; their reported correlation \(\langle|\mathbf R(t)|^2\rangle-|\langle\mathbf R(t)\rangle|^2\) is an **equal-time** variance, not the stationary **two-time** covariance at a lag. The present statement adds the exact two-time renewal reduction and the sharp long-lag asymptotic, including the critical cancellation of the leading algebraic term. General regenerative-process identities are standard; this result specializes them to a mathematically motivated Kuramoto critical regime and resolves its coefficient and exponent. A relevant equivalent result in more general reset-dynamics literature cannot be ruled out solely by these source comparisons.

## Limitations

The dynamics is exactly the continuum Ott--Antonsen scalar amplitude evolution with fixed global Poisson resets. It does not cover general intrinsic-frequency densities, independently resetting oscillators, noisy amplitude dynamics, randomized reset amplitudes, or finite-population corrections. The large-lag estimates fix all rates and may be nonuniform as \(K\to2\sigma\), \(\lambda\to0\), or \(\rho_0\to0\). The critical signature concerns **time correlations**, not a thermodynamic phase transition. The model's static synchronization law and ordinary renewal-covariance formalism are known. The claim is not an assertion of exhaustive literature novelty; independent assessment remains necessary.

## References

- M. Sarkar and S. Gupta, *Synchronization in the Kuramoto model in presence of stochastic resetting*, arXiv:2203.00339, first public March 1, 2022. https://arxiv.org/abs/2203.00339
- P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501, first public January 7, 2024. https://arxiv.org/abs/2401.03501
- A. Acharya, M. Sarkar, and S. Gupta, *Stationary-state dynamics of interacting phase oscillators in presence of noise and stochastic resetting*, arXiv:2504.08510, first public April 11, 2025. https://arxiv.org/abs/2504.08510
