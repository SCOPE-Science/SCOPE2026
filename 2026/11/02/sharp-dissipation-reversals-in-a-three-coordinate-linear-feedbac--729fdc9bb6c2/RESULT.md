# Sharp dissipation reversals in a three-coordinate linear feedback system

## Finding

Consider a three-coordinate stationary Ornstein–Uhlenbeck diffusion with a nonreciprocal feedback loop and one tunable damping coordinate. Its entropy-production rate has an **exact, exhaustive phase diagram**: decreasing for feedback strength \(0<h\le 1\), uniquely minimized at positive damping for \(1<h<5/2\), and increasing for \(h\ge5/2\). A second sharp threshold \(h_{\mathrm c}\approx1.41759657582884\) determines whether a sufficiently strong damping coupling can increase total dissipation above its uncoupled value. The statement also applies, with a factor-of-two rescaling, to the noncollective mode of two identically coupled three-coordinate diffusions.

Precisely, for \(h>0\), \(k\ge0\), let \(Z_t\in\mathbb R^3\) solve
\[
 dZ_t=M_h(k)Z_t\,dt+\sqrt{2}\,dW_t,\qquad
 M_h(k)=\begin{pmatrix}-1-k&1&0\\0&-1&-h\\-1&h&-1\end{pmatrix},
\]
where \(W_t\) is standard three-dimensional Brownian motion and the three driving noises are independent. There is a unique invariant Gaussian law \(N(0,S_h(k))\). Its stationary current is \(j(z)=[M_h(k)+S_h(k)^{-1}]z\,p(z)\), and its entropy-production rate is
\[
 \Phi_h(k)=\int_{\mathbb R^3}\frac{\lVert j(z)\rVert^2}{p(z)}\,dz.
\]
Define the positive polynomial
\[
 D_h(k)=2h^2+h+2k^2+8k+8.
\]
Then the exact dissipation law is
\[
 \boxed{\Phi_h(k)=\frac{4h^4+4h^2k^2+16h^2k+20h^2-4hk-8h+4k+9}{D_h(k)}}.
\]
Its derivative factors as
\[
 \boxed{\Phi_h'(k)=\frac{4(h^2-h+k+2)[2(h-1)k+2h-5]}{D_h(k)^2}}.
\]
In particular, for \(1<h<5/2\), the unique global minimizer on \([0,\infty)\) is
\[
 \boxed{k_*(h)=\frac{5-2h}{2(h-1)}}.
\]
For \(h\le1\), the rate is strictly decreasing, and for \(h\ge5/2\), it is strictly increasing on positive damping, with a horizontal tangent at the endpoint when \(h=5/2\). In every case
\[
 \lim_{k\to\infty}\Phi_h(k)=2h^2.
\]

There is a finer dissipation-versus-baseline threshold. Let \(h_{\mathrm c}\) be the unique positive root of
\[
 F(h)=2h^3-4h^2+8h-9=0.
\]
For \(0<h\le h_{\mathrm c}\), every finite \(k>0\) gives \(\Phi_h(k)<\Phi_h(0)\). For \(h_{\mathrm c}<h<5/2\), there is exactly one positive crossing of the uncoupled rate,
\[
 \boxed{k_{\mathrm{eq}}(h)=\frac{2(5-2h)(h^2-h+2)}{F(h)}},
\]
with smaller dissipation below this crossing and larger dissipation above it. For \(h\ge5/2\), every positive \(k\) increases dissipation relative to \(k=0\). At \(h=h_{\mathrm c}\), the limiting value equals the baseline, but every finite positive \(k\) strictly reduces it.

For the exact rational witness \(h=2\),
\[
 \Phi_2(k)=\frac{16k^2+60k+137}{2(k^2+4k+9)},\qquad
 \Phi_2(0)=\frac{137}{18},\quad
 \Phi_2(1/2)=\frac{38}{5},\quad
 \lim_{k\to\infty}\Phi_2(k)=8.
\]
The unique minimum occurs at \(k=1/2\), and the uncoupled value is crossed again at \(k=8/7\).

## Assumptions and scope

The process has exactly three real-valued even-under-time-reversal coordinates, additive isotropic diffusion matrix \(I_3\), unit baseline relaxation rates, feedback frequency \(h>0\), and additional diagonal damping \(k\ge0\) on the first coordinate. Entropy production uses the usual stationary overdamped diffusion current, and thus no velocity-reversal parity convention. Stability holds **for every** \(h>0\) and \(k\ge0\); no small-noise, perturbative, or large-coupling approximation is made.

For a direct two-copy realization, take two independent three-dimensional OU systems with drift \(M_h(0)\), each with \(\sqrt2\)-amplitude noise, and couple only their first coordinates through forces \(-\omega(Z_1^{(1)}-Z_1^{(2)})\) and \(-\omega(Z_1^{(2)}-Z_1^{(1)})\), respectively. Orthogonal center/relative coordinates decompose the six-dimensional dynamics into \(M_h(0)\) and \(M_h(2\omega)\). Total stationary EPR is therefore exactly
\[
 \Phi_h^{\mathrm{pair}}(\omega)=\Phi_h(0)+\Phi_h(2\omega).
\]
The sharp coupling-strength minimum and baseline crossing are \(\omega_*=k_*/2\) and \(\omega_{\mathrm{eq}}=k_{\mathrm{eq}}/2\), whenever their respective parameter regimes apply. These are equal-temperature identical-copy interactions, not heterogeneous-bath effects.

## Proof

**1. Stability and Gaussian stationarity.** The characteristic polynomial of \(M_h(k)\) is
\[
 p(\lambda)=\lambda^3+(k+3)\lambda^2+(h^2+2k+3)\lambda+[(h^2+1)(k+1)-h].
\]
Its constant term is positive because \(h^2-h+1=(h-1/2)^2+3/4>0\). Moreover, the cubic Routh–Hurwitz determinant is
\[
 (k+3)(h^2+2k+3)-[(h^2+1)(k+1)-h]=D_h(k)>0.
\]
All coefficients are positive. Hence every eigenvalue has negative real part. The unique stationary covariance is the positive-definite matrix
\[
 S_h(k)=2\int_0^\infty e^{M_h(k)t}e^{M_h(k)^\mathsf Tt}\,dt,
\]
which solves the Lyapunov equation \(M_h(k)S_h(k)+S_h(k)M_h(k)^\mathsf T=-2I_3\).

**2. Current and exact rate.** Set \(Q_h(k)=M_h(k)S_h(k)+I_3\). The Lyapunov equation makes \(Q_h(k)\) antisymmetric. Direct solution of its six independent linear equations yields the following three upper-triangular entries:
\[
\begin{aligned}
 Q_{12}&=\frac{2(h^2-h+k+2)}{D_h(k)},\\
 Q_{13}&=-\frac{2hk+2h-2k-5}{D_h(k)},\\
 Q_{23}&=-\frac{2h^3+2hk^2+8hk+9h-k-2}{D_h(k)}.
\end{aligned}
\]
Since \(j(z)=Q_h(k)S_h(k)^{-1}z\,p(z)\), Gaussian integration gives
\[
 \Phi_h(k)=\operatorname{tr}\!\left(S_h(k)^{-1}Q_h(k)^\mathsf TQ_h(k)\right).
\]
Substituting the Lyapunov solution and the displayed current entries, clearing their strictly positive denominators, and reducing rational polynomials yields the stated exact expression for \(\Phi_h(k)\). The accompanying symbolic checker independently solves all six covariance equations and checks this equality as a rational function in both independent parameters; it does **not** extrapolate from numerical samples.

**3. Unique minimum and monotonicity.** Differentiation of the exact rational expression yields the factorization in the Finding section. Its first nonconstant factor obeys \(h^2-h+k+2=(h-1/2)^2+k+7/4>0\). Therefore the sign of \(\Phi_h'(k)\) is exactly the sign of \(2(h-1)k+2h-5\). This affine function is negative throughout the half-line when \(h\le1\), has one strictly positive zero when \(1<h<5/2\), and is positive on the positive half-line when \(h\ge5/2\). The sign changes establish global uniqueness, not only local optimality. Leading coefficients of the numerator and denominator give the limiting rate \(2h^2\).

**4. Baseline crossing.** Subtraction of the value at zero damping gives the exact identity
\[
 \Phi_h(k)-\Phi_h(0)=
 \frac{2k\,[F(h)k+2(2h-5)(h^2-h+2)]}{[2h^2+h+8]D_h(k)}.
\]
The derivative \(F'(h)=6h^2-8h+8>0\) for all real \(h\), while \(F(1)=-3\) and \(F(2)=7\). Thus \(F\) has exactly one positive root \(h_{\mathrm c}\in(1,2)\). The sign of the affine bracket, together with the positive denominators, gives precisely the three stated baseline regimes and the unique positive crossing. At \(h=h_{\mathrm c}\), the affine bracket is negative for every finite \(k>0\) but tends to a limiting zero after division by the quadratic denominator.

**5. Identical-copy realization.** The orthogonal transformation from the two copies to their center and difference coordinates diagonalizes the two-vertex coupling Laplacian, with eigenvalues zero and two. Isotropic noise remains independent with diffusion matrix \(I_6\); the two modal stationary Gaussian laws factorize. Since the stationary probability currents and their quadratic EPR functionals also factorize, total EPR is the sum of the two modal contributions, yielding the stated identity and coupling thresholds.

## Verification

`verify.py` is a standalone SymPy script. Run `python verify.py` with SymPy installed; it solves the six independent stationary covariance equations symbolically, verifies the Lyapunov identity and antisymmetry, reconstructs stationary EPR, checks the characteristic polynomial, the Routh determinant, the first derivative, the uncoupled difference and the limiting EPR, and validates the exact \(h=2\) example. The checker prints `PASS` only after all assertions succeed. The **general proof is algebraic**, not a finite parameter sweep. The script uses no data or source from a different package.

## Relationship to prior work

The general OU current and entropy-production framework, including a decomposition into oscillatory and nonnormal terms, is developed by Nagayama, Kolchinsky and Ito (2026), first public June 5, 2026; their explicitly analyzed two-particle example has four total coordinates and a distinct drift architecture. Earlier OU treatments give the Lyapunov/current formalism. Doerries, Loos and Klapp (2020) investigate three-coordinate nonreciprocal linear Langevin memory and correlation functions, but only abstract-level material was accessible for the present comparison; a possible implicit relationship to the exact EPR phase diagram remains unresolved. Kharbanda, Burnet and Sabass (first public October 27, 2026) separately prove monotone EPR suppression in identical two-coordinate coupled systems and describe higher-dimensional residual EPR and nonmonotonic possibilities, with a four-coordinate worked example. Those general qualitative results and the two-coordinate monotonicity are prior work, **not** new claims here. The present precise three-coordinate feedback matrix, its complete feedback/damping phase diagram, its positive-damping optimizer and its exact finite-coupling reversal threshold are not stated in the inspected sources. General OU formulas do make this specific result derivable by nontrivial exact elimination; publication priority is not certified.

## Limitations

The result is restricted to the displayed drift family with independent equal-strength Gaussian noises, and to stationary overdamped entropy production. It does not provide a universal phase diagram for arbitrary three-dimensional drifts, anisotropic noise, nonlinear feedback, or time-integrated dissipation fluctuations. Only the specifically given identical-copy network embedding is covered. Mathematical proof and exact symbolic verification do not establish publication novelty, experimental relevance for any particular molecule, or independent validation.

## References

1. R. Nagayama, A. Kolchinsky and S. Ito, *Oscillatory-nonnormal decomposition of dissipation in Ornstein–Uhlenbeck processes*, arXiv:2606.07263 (first public June 5, 2026), https://arxiv.org/abs/2606.07263 and https://arxiv.org/html/2606.07263.
2. V. Kharbanda, A. F. Burnet and B. Sabass, *Residual dynamics determine dissipation in strongly coupled linear Langevin systems*, arXiv:2610.37030v1 (first public October 27, 2026), https://arxiv.org/html/2610.37030v1. The later paper is included for relevant scientific comparison.
3. T. J. Doerries, S. A. M. Loos and S. H. L. Klapp, *Correlation functions of non-Markovian systems out of equilibrium: analytical expressions beyond single-exponential memory*, arXiv:2010.12806 (2020), https://arxiv.org/abs/2010.12806.
4. C. Godrèche and J. M. Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes*, J. Phys. A 52, 035002 (2019), arXiv:1807.00694, https://arxiv.org/abs/1807.00694.
