# A sharp empirical-mean fluctuation transition under preferential relocation in a harmonic trap

## Finding

A Brownian particle can have the exact Gibbs--Gaussian position marginal **at every observation time** and nevertheless exhibit anomalously slow concentration of its trajectory average. For the uniform-past relocation dynamics defined below, the variance of the trajectory average has a sharp three-regime law at equality of the relocation rate and trap relaxation rate. The result gives exact finite-time expressions and all leading asymptotic constants.

Let \(\mu,D,r>0\), set \(\ell=\mu+r\), \(\alpha=2r/\ell\in(0,2)\), and let \(M(a;b;z)={}_1F_1(a;b;z)\) denote Kummer's confluent hypergeometric function. For \(T>0\), set \(\overline X_T=T^{-1}\int_0^T X_t\,dt\). If \(r\ne\mu\), then exactly
\[
\boxed{\operatorname{Var}(\overline X_T)=\frac{2D}{\mu\ell(\alpha-1)T}\big[M(1-\alpha;2;-\ell T)-1\big].}
\]
At the critical rate \(r=\mu\), put \(z=2\mu T\), define \(E_1(z)=\int_z^\infty e^{-u}du/u\), and let \(\gamma\) be Euler's constant. Then exactly
\[
\boxed{\operatorname{Var}(\overline X_T)=\frac{D}{\mu^2T}\left[\gamma+\log z+E_1(z)-1+\frac{1-e^{-z}}{z}\right].}
\]
The asymptotic regimes are
\[
\boxed{
\operatorname{Var}(\overline X_T)\sim
\begin{cases}
\displaystyle \frac{2D}{\mu(\mu-r)}T^{-1}, & 0<r<\mu,\\[5pt]
\displaystyle \frac{D}{\mu^2}\frac{\log(2\mu T)}{T}, & r=\mu,\\[6pt]
\displaystyle \frac{2D\ell^{\alpha-1}}{\mu(r-\mu)\Gamma(1+\alpha)}T^{-2\mu/\ell}, & r>\mu.
\end{cases}}
\]
For every finite \(r>0\), \(\overline X_T\to0\) in \(L^2\), but the ordinary \(T^{-1}\) sampling-variance rate fails for \(r\ge\mu\).

## Assumptions and scope

At time zero, draw \(X_0\sim N(0,D/\mu)\). Between relocation events, the one-dimensional position obeys
\[
dX_t=-\mu X_t\,dt+\sqrt{2D}\,dW_t.
\]
Independently of the Brownian noise, Poisson relocation events occur at rate \(r\). At an event at physical time \(t>0\), draw \(U\) uniformly on \([0,t]\), independently of the event clock and other fresh randomness, and replace the current position by the stored historical value \(X_{U-}\) (the distinction at the finite set of jump times has probability zero for a continuous uniform draw). **Keep the complete history after every event:** past positions are never erased. The reset clock is time-homogeneous; the relocation rule depends explicitly on the elapsed time since process initialization. The process is generally not a stationary process in the full pathwise sense. Its one-time marginal is \(N(0,D/\mu)\) for every \(t\ge0\), as the OU generator preserves this law and a uniform mixture of the same marginal laws again has that law.

The statement is restricted to Gaussian equilibrium initialization and the uniform-past kernel. It is a variance result for the integrated *position*, not a central limit theorem for the full distribution of the time average. For \(r>0\) finite, it proves \(L^2\) concentration but not almost-sure convergence.

## Proof

Write \(A_t=\int_0^t X_s\,ds\), \(v=D/\mu\), \(c(t)=\mathbb E[X_tA_t]\), and \(w(t)=\mathbb E[A_t^2]\). All second moments are finite, since Cauchy--Schwarz and invariance of \(\mathbb E[X_t^2]=v\) give \(0\le w(t)\le vt^2\). At a relocation event at time \(t\), the predictable conditional mean of the new position is exactly \(A_t/t\), because the historical draw is uniform. Consequently the product rule with jump compensation gives, for every \(t>0\),
\[
 w'(t)=2c(t),\qquad
 c'(t)=v-(\mu+r)c(t)+\frac{r}{t}w(t).
\]
There is no resetting contribution to \(w'\), since the integral \(A_t\) is continuous even when \(X_t\) jumps. Brownian martingale terms have zero expectation. Both \(w(0)=0\) and \(w'(0)=0\). Eliminating \(c\) yields the exact forced singular equation
\[
 w''(t)+\ell w'(t)-\frac{2r}{t}w(t)=2v.\tag{1}
\]
The bound \(w(t)\le vt^2\) justifies the Laplace transform \(W(s)=\int_0^\infty e^{-st}w(t)dt\) for each \(s>0\), together with differentiation and Fubini. In particular, \(\mathcal L\{w(t)/t\}(s)=\int_s^\infty W(u)du\). Taking the Laplace transform of (1) gives
\[
 s(s+\ell)W(s)-2r\int_s^\infty W(u)du=\frac{2v}{s}.
\]
Differentiate and solve the resulting first-order linear equation with integrating factor \(s^{1+\alpha}(s+\ell)^{1-\alpha}\). The solution satisfying the large-\(s\) condition \(W(s)\sim2v/s^3\) is
\[
 W(s)=\frac{2v}{\ell(\alpha-1)s^2}\left[\left(1+\frac{\ell}{s}\right)^{\alpha-1}-1\right],\quad \alpha\ne1.\tag{2}
\]
For \(\alpha=1\), the continuous parameter limit is
\[
 W(s)=\frac{2v}{\ell s^2}\log(1+\ell/s).\tag{3}
\]
By the Laplace transform identity
\[
 \mathcal L\left\{tM(1-\alpha;2;-\ell t)\right\}(s)
 =s^{-2}(1+\ell/s)^{\alpha-1},
\]
(2) inverts to
\[
 w(t)=\frac{2v}{\ell(\alpha-1)}t\left[M(1-\alpha;2;-\ell t)-1\right].\tag{4}
\]
The critical inversion of (3) is equivalently obtained by taking \(\alpha\to1\) in (4):
\[
 w(t)=\frac{2v}{\ell}t\int_0^1\frac{(1-e^{-\ell tu})(1-u)}u\,du
=\frac{2v}{\ell}t\left[\gamma+\log(\ell t)+E_1(\ell t)-1+\frac{1-e^{-\ell t}}{\ell t}\right].\tag{5}
\]
The integral identity follows from differentiating the Euler beta-integral representation of \(M(a;2;-z)\) at \(a=0\), or by matching its power series. The inverse transforms are unique among continuous functions of at most polynomial growth. Dividing (4) and (5) by \(T^2\) proves the finite-time formulas.

For \(0<\alpha<1\), the large-positive-\(z\) Kummer expansion \(M(1-\alpha;2;-z)\sim z^{\alpha-1}/\Gamma(1+\alpha)\) tends to zero, yielding the first regime. For \(1<\alpha<2\), the same leading asymptotic diverges, giving the final regime with its coefficient. At \(\alpha=1\), \(E_1(z)=o(1)\) and \((1-e^{-z})/z=o(1)\), yielding the logarithmic middle regime. Finally, \(\alpha-2=-2\mu/(\mu+r)<0\), so all three variance asymptotics vanish. This establishes the stated \(L^2\) convergence and the sharp variance-rate threshold \(r=\mu\).

## Verification

The standalone `CHECK.py` evaluates the finite-time Kummer formula independently against numerical integration of the two-moment generator system, verifies the critical formula by direct quadrature, tests asymptotic coefficients in all three regimes, and recovers the familiar nonreset OU limit. With NumPy and SciPy, it reports 233 passing deterministic assertions. A separate discretized process simulation with 40,000 trajectories and observation time six found sample-to-predicted integrated-variance ratios approximately 1.013, 1.013, and 1.038 at relocation rates 0.5, 1, and 2.5 for unit \(\mu,D\); the slight sampling/time-step deviations are not used to prove the result. The proof itself is the moment closure and exact Laplace inversion above. These checks do not establish a central limit theorem or infinite-time almost-sure ergodicity.

## Relationship to prior work

Boyer and Majumdar (2024) introduced and solved precisely this confined uniform-history resetting model at the level of **one-time position densities**, finding Gibbs--Boltzmann marginals and anomalous relaxation exponents. Its harmonic first-mode exponent is \(\mu/(r+\mu)\). That result is retained, not presented as new. The present statement instead concerns the **path-dependent integrated position variance**. A one-time spectral decay theorem alone does not determine its two-time covariance or the exact \(T^{-1}\), \((\log T)/T\), \(T^{-2\mu/(\mu+r)}\) transition.

Boyer, Evans and Majumdar (2016/2017) treated the growth of the position variance in *unconfined* preferential resetting. Boyer, Evans and Majumdar (2024 preprint/2025 article) studied general memory kernels under confinement primarily through one-time distributions and their relaxation. Broader work on ergodicity and temporal sampling in reset or reinforced processes motivates comparison, but unlike the present result it does not provide the same harmonic uniform-history, equilibrium-initialized integrated-position identity in the inspected material. A broader empirical-process or generalized Pólya-urn theorem might subsume the exponent, and a complete literature priority assessment remains open.

## Limitations

The trajectory distribution need not be Gaussian, despite every one-time marginal being Gaussian. No stationary two-time law is asserted. The \(L^2\) convergence of the empirical mean does not by itself give a central limit theorem, almost-sure convergence, or results for nonlinear observables. The exact formulas require the continuous-time uniform lookback protocol and equilibrium initialization; discretizations introduce controllable numerical error. The originality assessment is conditional on the literature compared, not a proof of global novelty or independent validation.

## References

1. D. Boyer and S. N. Majumdar, “Power-law relaxation of a confined diffusing particle subject to resetting with memory,” *J. Stat. Mech.* (2024) 073206; arXiv:2405.10283 (first version May 16, 2024). https://arxiv.org/abs/2405.10283 ; https://doi.org/10.1088/1742-5468/ad5a79
2. D. Boyer, M. R. Evans and S. N. Majumdar, “Long time scaling behaviour for diffusion with resetting and memory,” *J. Stat. Mech.* (2017) 023208; arXiv:1611.06743 (first version November 21, 2016). https://arxiv.org/abs/1611.06743
3. D. Boyer, M. R. Evans and S. N. Majumdar, “Diffusion with preferential relocation in a confining potential,” *J. Stat. Mech.* (2025) 013209; arXiv:2411.00641 (first version November 2024). https://arxiv.org/abs/2411.00641
4. E. Barkai, R. Flaquer-Galmés and V. Méndez, “Ergodic properties of Brownian motion under stochastic resetting,” *Phys. Rev. E* 108, 064102 (2023). https://doi.org/10.1103/PhysRevE.108.064102
