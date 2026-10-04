# Lévy jumps invalidate the Gaussian density theorem for the linearized stochastic SVI model

## Finding

Wang, Wang, and Teng study a stochastic susceptible-vaccinated-infected model driven simultaneously by Brownian noise and a compensated Poisson random measure. After the logarithmic change of variables, their linearization around a quasi-endemic state has the form
\[
dY_t
=
A Y_t\,dt
+
\Sigma_B\,dB_t
+
\int_Z h(u)\,\widetilde N(dt,du),
\]
where
\[
h(u)
=
\begin{pmatrix}
\ln(1+\eta_1(u))\\
\ln(1+\eta_2(u))\\
\ln(1+\eta_3(u))
\end{pmatrix}.
\]

Theorem 5.1 displays a Gaussian density for \(Y\), hence a log-normal density for the original positive variables. That formula is not an exact stationary density when any admissible jump amplitude is nonzero.

For a Hurwitz matrix \(A\), the stationary solution of the linearized system can be written as the sum of an independent Gaussian convolution and a Lévy stochastic convolution:
\[
Y_\infty
\overset d=
\int_0^\infty e^{As}\Sigma_B\,dB_s
+
\int_0^\infty\!\!\int_Z e^{As}h(u)\,\widetilde N(ds,du).
\]
For every vector \(v\), the fourth cumulant of the scalar projection is
\[
\kappa_4(v^\top Y_\infty)
=
\int_0^\infty\!\!\int_Z
\bigl(v^\top e^{As}h(u)\bigr)^4\,\nu(du)\,ds.
\]
A Gaussian random variable has zero fourth cumulant. Therefore any direction for which the displayed integral is strictly positive rules out an exact Gaussian stationary law.

The contradiction occurs for a simple parameter set satisfying the source assumptions. Let
\[
f(I)=g(I)=\frac{I}{1+I},
\]
and choose
\[
\Lambda=10,\qquad
\pi=\frac12,\qquad
\mu=1,\qquad
\delta=1,
\]
\[
\beta_b=\beta_v=10,
\qquad
\sigma_1=\sigma_2=\sigma_3=1.
\]
Let the jump space consist of one atom of intensity one, with
\[
\eta_1=\frac1{10},
\qquad
\eta_2=\eta_3=0.
\]
These amplitudes satisfy the paper's square-integrability and positivity assumptions.

The source's logarithmic drift parameters are
\[
\mu_1
=
1+\frac12+\frac1{10}-\ln(1.1)
\approx1.5046898202,
\]
and
\[
\mu_2=\mu_3=\frac32.
\]
Its stochastic reproduction threshold is then
\[
\widetilde{\mathcal R}_0^s
=
\frac{\Lambda}{\mu_3+\delta}
\left(
\frac{(1-\pi)\beta_b}{\mu_1}
+
\frac{\pi\beta_v}{\mu_2}
\right)
\approx26.6251093071>1.
\]
The corresponding quasi-endemic root is
\[
I^*\approx3.3469399491,
\]
with
\[
S^*\approx0.5432290275,
\qquad
V^*\approx0.5435059597.
\]

For this witness, the linearized drift matrix is
\[
A
=
\begin{pmatrix}
-9.2042209577&0&-1.7712531638\\
0&-9.1995311375&-1.7712531638\\
1.2496814630&1.2503185370&-1.9248827844
\end{pmatrix}.
\]
Its eigenvalues are approximately
\[
-2.59512675,\qquad
-9.20188568,\qquad
-8.53162245,
\]
so the linearized process is stable.

Take
\[
v=e_1.
\]
The only nonzero jump coordinate is
\[
h_1=\ln(1.1)>0.
\]
Because
\[
e_1^\top e^{A0}e_1=1,
\]
continuity makes the fourth-cumulant integrand strictly positive on an interval starting at zero. Numerically,
\[
\kappa_4(e_1^\top Y_\infty)
\approx2.22362604\times10^{-6}>0.
\]
Hence the stationary distribution is not Gaussian.

The source's covariance replacement is also not the exact jump covariance. The true second-cumulant rate of the log jump is
\[
\ln(1.1)^2
\approx0.00908403037.
\]
The coefficient used in the paper's local second-order equation is
\[
2(0.1-\ln(1.1))
\approx0.00937964039.
\]
These quantities are unequal.

## Assumptions and scope

The result concerns the linearized logarithmic jump-diffusion printed as equation (5.2) and the density statement in Theorem 5.1 of the source.

The jump measure is finite in the source assumptions. The witness uses a one-atom measure, which is therefore within the admitted compound-Poisson class. The jump amplitude obeys
\[
1+\eta_1>0
\]
and all required integrability conditions automatically hold for a single finite atom.

The conclusion does not deny existence of a stationary law for the stable linearized process. It identifies its non-Gaussianity when genuine jumps remain.

The conclusion also does not exclude a Gaussian approximation in a separate small-jump or high-frequency diffusion limit. Such a statement would require a specified scaling and approximation error. No such limiting regime is part of Theorem 5.1.

## Proof

For a smooth test function \(\varphi\), the generator of the additive-jump linear system is
\[
\mathcal L\varphi(y)
=
(Ay)\cdot\nabla\varphi(y)
+
\frac12
\operatorname{tr}
\!\left(
\Sigma_B\Sigma_B^\top\nabla^2\varphi(y)
\right)
\]
\[
\qquad
+
\int_Z
\left[
\varphi(y+h(u))
-\varphi(y)
-h(u)\cdot\nabla\varphi(y)
\right]\nu(du).
\]
The adjoint stationary equation therefore contains the nonlocal term
\[
\int_Z
\left[
p(y-h(u))
-p(y)
+h(u)\cdot\nabla p(y)
\right]\nu(du).
\]
The local Fokker–Planck equation used in the source proof contains no such shifted-density term, so it is not the forward equation of the printed jump process.

Now suppose \(A\) is Hurwitz. The stationary stochastic convolution exists under the finite second-moment assumptions used here. Its Brownian part is Gaussian, hence contributes no cumulants of order above two.

For the compensated Poisson part, the logarithm of the characteristic function of the projection \(v^\top Y_\infty\) is
\[
\int_0^\infty\!\!\int_Z
\left[
e^{i\theta v^\top e^{As}h(u)}
-1
-i\theta v^\top e^{As}h(u)
\right]\nu(du)\,ds.
\]
Expanding at \(\theta=0\), the coefficient of the fourth cumulant is
\[
\kappa_4(v^\top Y_\infty)
=
\int_0^\infty\!\!\int_Z
\bigl(v^\top e^{As}h(u)\bigr)^4\,\nu(du)\,ds.
\]

For the explicit witness, the jump space has one unit-rate atom,
\[
h=(\ln(1.1),0,0)^\top,
\]
and \(v=e_1\). At \(s=0\),
\[
v^\top e^{As}h=\ln(1.1)>0.
\]
By continuity the integrand remains positive for all sufficiently small positive \(s\). Since it is nonnegative everywhere, the full integral is strictly positive. Therefore \(e_1^\top Y_\infty\) is non-Gaussian, so \(Y_\infty\) cannot have the multivariate Gaussian density displayed in Theorem 5.1.

The same generator calculation gives the exact instantaneous covariance matrix
\[
Q_{\mathrm{true}}
=
\Sigma_B\Sigma_B^\top
+
\int_Z h(u)h(u)^\top\,\nu(du).
\]
Thus the stationary covariance, when finite, solves
\[
A C+C A^\top+Q_{\mathrm{true}}=0.
\]
The source instead inserts the diagonal jump coefficient
\[
2\int_Z
\bigl(\eta_i(u)-\ln(1+\eta_i(u))\bigr)\,\nu(du).
\]
That expression is the compensation term entering the logarithmic drift. It is not equal in general to
\[
\int_Z\ln(1+\eta_i(u))^2\,\nu(du),
\]
and it also omits cross-covariances
\[
\int_Z
\ln(1+\eta_i(u))
\ln(1+\eta_j(u))\,\nu(du)
\]
when several coordinates share the same Poisson random measure.

For the one-coordinate witness, the discrepancy already appears on the diagonal:
\[
\ln(1.1)^2
\ne
2(0.1-\ln(1.1)).
\]

## Verification

The bundled checker reconstructs the witness from the source formulas. It verifies
\[
\widetilde{\mathcal R}_0^s>1,
\]
solves the quasi-endemic scalar equation, builds the linearization matrix, and confirms that all three eigenvalues have negative real part.

It then evaluates
\[
\int_0^\infty
\left[
\ln(1.1)\,
e_1^\top e^{As}e_1
\right]^4 ds
\]
by numerical quadrature and confirms strict positivity. The numerical integral is not needed for the logical contradiction: positivity follows analytically from continuity at \(s=0\).

Finally, the checker compares the exact log-jump second-cumulant rate with the coefficient used in the source and verifies that they differ.

## Relationship to prior work

Wang, Wang, and Teng (2022), DOI 10.3934/math.2023148, define the stochastic SVI model, its Lévy-jump assumptions, the logarithmic linearization, and Theorem 5.1. In the theorem proof they replace the jump contribution by a local second-order Fokker–Planck term and solve the resulting local equation with a Gaussian ansatz.

Jongbloed, van der Meulen, and van der Vaart (2005), DOI 10.3150/bj/1130077593, characterize stationary distributions of Lévy-driven Ornstein–Uhlenbeck processes through self-decomposability and the Lévy measure of the driving process. Their framework is consistent with retaining, rather than discarding, the jump component in the stationary law.

Barndorff-Nielsen and Shephard (2001), DOI 10.1111/1467-9868.00282, develop non-Gaussian Ornstein–Uhlenbeck-type processes driven by background Lévy processes. This provides broad prior context for the fact that Ornstein–Uhlenbeck mean reversion does not turn a genuine Lévy jump input into an exact Gaussian stationary law.

The source cites Zhou, Zhang, and Jiang (2020), DOI 10.1016/j.chaos.2020.109865, for a density-function technique in a stochastic epidemic model. That predecessor concerns a diffusion setting and does not justify replacing the nonlocal jump generator in the later Lévy-driven system.

The general non-Gaussianity of Lévy-driven Ornstein–Uhlenbeck laws is therefore prior knowledge. The source-specific finding here is that Theorem 5.1 applies a diffusion-only local equation to its own nonzero-jump linearization, and that an explicit admissible SVI parameter set gives a stable stationary linear process with a provably positive fourth cumulant.

## Limitations

The result is a correction of the exact Gaussian/log-normal density claim for the linearized logarithmic process. It does not classify the full nonlinear SVI stationary distribution.

If every jump amplitude vanishes, then the linearization reduces to a Brownian Ornstein–Uhlenbeck process and the usual Gaussian Lyapunov-covariance formula applies.

For nonzero jumps, a Gaussian approximation may be useful under an additional diffusion approximation regime. The present result does not quantify such an approximation; it shows that the exact theorem and its covariance equation do not follow from the printed jump model.

## References

1. X. Wang, K. Wang, Z. Teng, “Global dynamics and density function in a class of stochastic SVI epidemic models with Lévy jumps and nonlinear incidence,” AIMS Mathematics 8 (2023), 3239–3265. DOI: 10.3934/math.2023148. Published online 10 November 2022.
2. G. Jongbloed, F. H. van der Meulen, A. W. van der Vaart, “Nonparametric inference for Lévy-driven Ornstein–Uhlenbeck processes,” Bernoulli 11 (2005), 759–791. DOI: 10.3150/bj/1130077593.
3. O. E. Barndorff-Nielsen, N. Shephard, “Non-Gaussian Ornstein–Uhlenbeck-based models and some of their uses in financial economics,” Journal of the Royal Statistical Society: Series B 63 (2001), 167–241. DOI: 10.1111/1467-9868.00282.
4. Y. Zhou, W. Zhang, D. Jiang, “Dynamics and density function analysis of a stochastic SVI epidemic model with half saturated incidence rate,” Chaos, Solitons & Fractals 137 (2020), 109865. DOI: 10.1016/j.chaos.2020.109865.
