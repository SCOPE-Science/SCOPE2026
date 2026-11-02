# A positive cross-frequency fourth-cumulant kernel and a unique kurtosis reversal for Gaussian-spectrum active propulsion

## Finding

For a free planar active Brownian particle whose signed propulsion amplitude is a constant plus an independent stationary Gaussian process with *any gapped positive mixture of exponential covariance kernels*, the long-time fourth displacement cumulant is exactly a quadratic polynomial in the colored-speed intensity. Its quadratic coefficient is a **strictly positive cross-frequency kernel**, so a particle with nonzero mean propulsion has precisely one transition from negative to positive long-time fourth-cumulant growth as its speed variance increases. At the transition, normalized displacement excess kurtosis decays at least quadratically in observation time, instead of with the generic inverse-time law.

Define, for \(q,r>0\),
\[
a(q)=\frac{3(3q^3+21q^2+60q+64)}{2q(q+1)^2(q+4)},\qquad
b(q,r)=\frac{3\bigl[3(q+r)^3+21(q+r)^2+60(q+r)+64+qr(q+r)(q+r+4)\bigr]}{4(q+1)^2(r+1)^2(q+r)(q+r+4)}.
\]
Both kernels are strictly positive. Given the spectral measure \(\nu\) defined below, put
\[
A_\nu=\int a(q)\,\nu(dq)>0,\qquad
B_\nu=\iint b(q,r)\,\nu(dq)\nu(dr)>0.
\]
Then, for every \(\lambda\ge0\), the longitudinal cumulant rates exist and obey
\[
\boxed{\lim_{t\to\infty}\frac{\operatorname{cum}_4(X_t)}t
=\frac{-21\mu^4/4+\lambda\mu^2 A_\nu+\lambda^2 B_\nu}{D_r^3}.}
\]
For \(\mu\ne0\) this rate changes sign exactly once, at
\[
\boxed{\lambda_*=\frac{\mu^2\bigl(\sqrt{A_\nu^2+21B_\nu}-A_\nu\bigr)}{2B_\nu}>0.}
\]
It is negative below \(\lambda_*\), zero at \(\lambda_*\), and positive above. For \(\mu=0\) and \(\lambda>0\), it is strictly positive. These are asymptotic temporal-cumulant signs, not assertions about finite-time kurtosis.

## Assumptions and scope

Fix \(D_r>0\), \(D_T\ge0\), \(\mu\in\mathbb R\), and \(\lambda\ge0\). The angle process \(\Theta_t\) is a stationary circular Brownian motion, with uniform initial angle and angular diffusion generator \(D_r\partial_\theta^2\). Independently, \(Z_t\) is a centered stationary real Gaussian process whose covariance has a spectral gap:
\[
\mathbb E[Z_sZ_{s+\tau}]=\int_{[\varepsilon,\infty)}e^{-D_r q|\tau|}\nu(dq),
\quad \varepsilon>0,
\]
where \(\nu\) is any nonzero finite positive Borel measure. For an independent standard real Brownian motion \(B_t\), define
\[
X_t=\int_0^t(\mu+\sqrt\lambda Z_s)\cos\Theta_s\,ds+\sqrt{2D_T}\,B_t.
\]
Here \(\mu+\sqrt\lambda Z_s\) is a signed propulsion amplitude, not a constrained nonnegative speed; an OU mixture is a physical approximation permitting direction reversals. The covariance measure may have arbitrarily many atoms or a continuous part. The initial angle and Gaussian drive have their stationary laws. All time limits are at fixed parameters and measure.

The asymptotic variance rate is
\[
K_2=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}t
=2D_T+\frac{\mu^2+\lambda\int(q+1)^{-1}\nu(dq)}{D_r}>0
\]
except for the degenerate case \(\mu=\lambda=D_T=0\), which is excluded when normalizing by variance. Define \(K_4\) by the displayed fourth-cumulant formula. The spectral gap and finite mass ensure all integrals defining \(A_\nu\) and \(B_\nu\) converge.

## Proof

Write \(U_t=(\mu+\sqrt\lambda Z_t)\cos\Theta_t\) and \(V_t=\mu+\sqrt\lambda Z_t\). Stationarity and reflection symmetry make \(\mathbb E U_t=0\). Angle Fourier modes give \(\mathbb E[\cos\Theta_0\cos\Theta_\tau]=\frac12e^{-D_r|\tau|}\), and for ordered times \((0,u,u+v,u+v+w)\), with \(u,v,w\ge0\),
\[
\mathbb E\prod_{j=1}^4\cos\Theta_{t_j}
=\tfrac14e^{-D_r(u+w)}+\tfrac18e^{-D_r(u+4v+w)}.
\]
To reconstruct the latter identity, write each cosine as the sum of Fourier charges \(\pm1\) divided by two. Uniform averaging retains only zero total charge; the two surviving intermediate charge magnitudes are zero and two, with relaxation rates zero and \(4D_r\), respectively.

Write \(C_{ij}=\mathbb E[Z_{t_i}Z_{t_j}]\). Wick's Gaussian identity yields
\[
\mathbb E\prod_{j=1}^4 V_{t_j}=
\mu^4+\mu^2\lambda\sum_{i<j}C_{ij}
+\lambda^2(C_{12}C_{34}+C_{13}C_{24}+C_{14}C_{23}).
\]
The ordered connected velocity correlation is the product of the angular and speed four-point factors **minus** the three products of corresponding velocity two-point functions. The terms that appear constant in the middle spacing \(v\) cancel at this stage. Integrability follows by expanding each \(C_{ij}\) as an exponential mixture and using the strictly positive relaxation rates \(D_r\) and \(D_r\varepsilon\); finite spectral mass gives dominated integrability. The stationary cumulant identity then gives
\[
K_4=24\int_0^\infty\!\int_0^\infty\!\int_0^\infty
\operatorname{cum}(U_0,U_u,U_{u+v},U_{u+v+w})\,du\,dv\,dw.
\]
Every surviving term is an elementary triple Laplace integral, \(\int_{\mathbb R_+^3}e^{-\alpha u-\beta v-\gamma w}dudvdw=(\alpha\beta\gamma)^{-1}\), with positive \(\alpha,\beta,\gamma\). First set \(D_r=1\) by changing the three gap variables; restoring units multiplies the result by \(D_r^{-3}\). Direct collection of the constant-mean, one-covariance, and two-covariance terms produces, respectively,
\[
-\frac{21}{4}\mu^4,\quad
\mu^2\lambda\int\frac{3(3q^3+21q^2+60q+64)}{2q(q+1)^2(q+4)}\nu(dq),\quad
\lambda^2\iint b(q,r)\nu(dq)\nu(dr).
\]
In particular, the mixed coefficient for two distinct OU rates \(q,r\) is **\(2b(q,r)\)**; the factor two accounts for exchanging the two spectral integrations. An independent rational polynomial-generator calculation checks this cross term, not merely the diagonal \(q=r\). Both numerators of \(a\) and \(b\) are strictly positive for positive rates, proving \(A_\nu,B_\nu>0\). The fourth rate is therefore a strictly increasing quadratic in \(\lambda\ge0\) when \(\mu\ne0\), beginning at \(-21\mu^4/(4D_r^3)\); the quadratic formula proves existence and uniqueness of \(\lambda_*\). For zero mean, it is simply \(\lambda^2 B_\nu/D_r^3>0\).

The two-point correlation is \(\frac12e^{-D_r|\tau|}[\mu^2+\lambda C_Z(\tau)]\). Twice its integral over \(\tau\ge0\), plus the independent Brownian variance \(2D_T\), gives \(K_2\) above. The spectral gap bounds both the covariance tail and the connected four-point correlation by exponentially integrable functions with finite first temporal moments. Consequently \(\operatorname{Var}(X_t)=K_2t+O(1)\) and \(\operatorname{cum}_4(X_t)=K_4t+O(1)\). Thus, whenever \(K_2>0\),
\[
\frac{\operatorname{cum}_4(X_t)}{3\operatorname{Var}(X_t)^2}
=\frac{K_4}{3K_2^2t}+O(t^{-2}),
\]
and at \(\lambda=\lambda_*\) the leading term vanishes, leaving \(O(t^{-2})\). Independent thermal Brownian increments have zero fourth cumulant and add no mixed connected contributions.

## Verification

The attached standalone \(\texttt{verify_spectral.py}\) computes \(K_2\) and \(K_4\) in two independent ways for several finite Gaussian OU spectra. One method evaluates the positive spectral-kernel formulas; the other constructs an exact rational perturbation expansion of the tilted Fourier–Hermite generator. It verifies equality, *including cross-frequency terms*, for four rational parameter cases (one-, two-, and three-rate mixtures, both signs of \(K_4\), and zero mean). The proof above, rather than these finite computations, supplies the arbitrary positive-measure extension. Run with \(\texttt{python verify_spectral.py}\), using only the Python standard library.

## Relationship to prior work

Shee and Chaudhuri, arXiv:2108.12228 (first public 27 August 2021), evaluate moments and dynamical crossovers of active Brownian motion with an OU speed fluctuation at a single relaxation rate, including transient kurtosis behavior. That result provides the parent physical model but does not supply the positive arbitrary-two-frequency kernel \(b(q,r)\), the integral for arbitrary positive rate spectra, or the global one-threshold long-time fourth-cumulant sign classification stated here. Peruani and Morelli, arXiv:0705.4646, obtain transport information from speed and direction fluctuations, including covariance-based second moments, not the evaluated fourth-order cross-frequency kernel. Shee and Chaudhuri, arXiv:2112.13415, study speed and orientation fluctuations and transient displacement moments; the available material does not resolve every possible full-text implication, which remains an originality risk. Stationary Gaussian Wick and Fourier methods are standard and are not claimed as new.

## Limitations

The Gaussian signed speed is unbounded and can be negative. The spectral measure must be positive, finite, and have a strictly positive lower relaxation-rate bound. The result does not treat arbitrary signed covariance kernels, non-Gaussian speed amplitudes, speed-angle correlations, or weakly mixing zero-gap spectra. The positive quadratic and unique threshold apply to the fourth **long-time growth rate**, not uniformly to kurtosis at each finite time. This is a mathematical self-review, not an independent publication-priority determination or experimental validation.

## References

1. A. Shee and D. Chaudhuri, *Active Brownian motion with speed fluctuations in arbitrary dimensions: exact calculation of moments and dynamical crossovers*, arXiv:2108.12228 (first public 2021-08-27), https://arxiv.org/abs/2108.12228.
2. F. Peruani and L. G. Morelli, *Self-propelled particles with fluctuating speed and direction of motion*, arXiv:0705.4646, https://arxiv.org/abs/0705.4646.
3. A. Shee and D. Chaudhuri, *Self-propulsion with speed and orientation fluctuation: exact computation of moments and dynamical bistabilities in displacement*, arXiv:2112.13415, https://arxiv.org/abs/2112.13415.
