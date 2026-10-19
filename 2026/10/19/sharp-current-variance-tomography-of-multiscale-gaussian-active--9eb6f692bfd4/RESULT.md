# Sharp current-variance tomography of multiscale Gaussian active gases

## Finding

**Theorem (sharp finite-time recovery of multiscale active noise).** Fix a known particle density \(\rho>0\), a sampling interval \(h>0\), and an integer \(N\geq1\). Independently for every particle in a homogeneous Poisson gas on the real line, let
\[
 X(t)=X(0)+\sqrt{2D}\,W(t)+\int_0^t V(s)\,ds,\qquad
 \mathbb E[V(t)V(s)]=\sum_{j=1}^{N}a_j e^{-\lambda_j|t-s|},
\]
where \(D>0\), every \(a_j>0\), and the distinct rates \(\lambda_j>0\) are unknown. Each \(V\) is stationary, centered Gaussian, independent of its Brownian noise; different particles are independent. Define the signed net current \(Q(t)\) across the origin by subtracting particles that started to the right and end to the left from those that started left and end right. Write \(R(t)=\operatorname{Var}Q(t)\).

Exactly \(2N+1\) scalar measurements
\[
 R(h),R(2h),\ldots,R((2N+1)h)
\]
recover the unordered complete collection \(\{(a_j,\lambda_j):1\leq j\leq N\}\) and \(D\) uniquely. A concrete reconstruction, with a test for physical admissibility of exact observations, is provided below. The count is **sharp among predetermined scalar sampling times**: no choice of fewer than \(2N+1\) positive times gives an injective measurement map on the class with exactly \(N\) positive distinct modes and unknown \(D\).

The same transport observable provides a nonparametric identification boundary: for an arbitrary continuous stationary centered Gaussian propulsion covariance \(K\) of finite variance, knowing \(R(t)\) for every \(t>0\) identifies \(D\) and all of \(K\), whereas any fixed finite set of sampling times fails to identify an unrestricted covariance, even when \(D\) and \(K(0)\) are known. Without restrictions on high-frequency spectral content, this infinite-time inverse is not uniformly stable to additive errors in \(R\).

## Assumptions and scope

The Poisson gas has independently marked starting points with intensity \(\rho\) on \(\mathbb R\). Its infinitely many particles have independent displacement processes, and the current counts *net start-to-end crossings* at each time, not the number of successive recrossings. The two directional crossing counts are finite almost surely for every finite time. For finite-mode reconstruction we assume independent stationary OU components with covariance amplitudes \(a_j>0\) and distinct rates \(\lambda_j>0\); their sum is a centered stationary Gaussian process. The physical diffusion coefficient \(D>0\) and all OU parameters are unknown; \(\rho\), \(h\), and the mode count \(N\) are known. Measurements are ideal ensemble variances, free from noise. All reconstruction formulas use natural time units and no hidden normalization of the OU variance.

The broader inverse statement assumes an even, continuous, positive-definite covariance \(K(t)\) with \(K(0)<\infty\), a stationary centered Gaussian propulsion with this covariance, \(D>0\), and density \(\rho\) known. Neither propulsion coupling between different particles nor nonstationary initial velocities are included.

## Proof

**1. Crossing law and the correct observable.** Denote a displacement over time \(t\) by \(Z(t)=X(t)-X(0)\) and its variance by \(S(t)\). It is centered Gaussian. Thinning a homogeneous Poisson process by the independent crossing probabilities gives two independent Poisson crossing counts, each of mean
\[
 \rho\int_0^\infty \mathbb P\{Z(t)>y\}\,dy
 =\rho\mathbb E[Z(t)_+]
 =\frac{\rho\sqrt{S(t)}}{\sqrt{2\pi}}.
\]
Thus \(Q(t)\) is a symmetric Skellam variable with cumulant generating function \(2m_t(\cosh z-1)\), where \(m_t=\rho\sqrt{S(t)/(2\pi)}\). In particular,
\[
 \boxed{R(t)=\rho\sqrt{\frac{2}{\pi}}\sqrt{S(t)},\qquad
 S(t)=\frac{\pi}{2\rho^2}R(t)^2.}\tag{1}
\]
This remains true with any centered Gaussian stationary propulsion of finite second moment.

**2. Multiscale OU variogram.** Stationarity and independence give the Green–Kubo formula
\[
 S(t)=2Dt+2\int_0^t(t-u)K(u)\,du
 =2Dt+2\sum_{j=1}^N a_j\left[\frac{t}{\lambda_j}-\frac{1-e^{-\lambda_jt}}{\lambda_j^2}\right].\tag{2}
\]
In particular \(S(0)=0\). Put \(s_k=\pi R(kh)^2/(2\rho^2)\) for \(0\leq k\leq2N+1\), where \(s_0=0\) does not require a measurement. Form \(2N\) second differences
\[
 d_k=s_{k+2}-2s_{k+1}+s_k=\sum_{j=1}^N w_jq_j^k,
 \quad 0\leq k\leq2N-1,\tag{3}
\]
with strictly positive weights and distinct nodes in \((0,1)\):
\[
 q_j=e^{-\lambda_jh},\qquad
 w_j=\frac{2a_j}{\lambda_j^2}(1-q_j)^2.\tag{4}
\]

**3. Positive Hankel inversion, admissibility, and parameter recovery.** Form the \(N\)-square matrix \(H_{ik}=d_{i+k}\) for \(0\leq i,k<N\). With Vandermonde \(A_{ij}=q_j^i\),
\[
 H=A\operatorname{diag}(w_1,\ldots,w_N)A^{\mathsf T}\succ0.
\]
Hence the unique vector \(c_0,\ldots,c_{N-1}\) solving
\[
 H(c_0,\ldots,c_{N-1})^{\mathsf T}
 =-(d_N,\ldots,d_{2N-1})^{\mathsf T}
\]
defines a monic polynomial \(p(z)=z^N+\sum_{i=0}^{N-1}c_i z^i\). Equation (3), invertibility of the Vandermonde, and the defining linear system force \(p(q_j)=0\). Thus its \(N\) simple roots in \((0,1)\) recover all nodes. Solve \(\sum_j w_jq_j^i=d_i\) for \(0\leq i<N\); the unique solution gives all positive weights. Recover
\[
 \boxed{\lambda_j=-\frac{\log q_j}{h},\qquad
 a_j=\frac{w_j\lambda_j^2}{2(1-q_j)^2}.}\tag{5}
\]
Finally, because the OU contribution to \(S(h)\) is now known,
\[
 \boxed{D=\frac{s_1}{2h}-\frac1h\sum_{j=1}^N a_j\left[\frac{h}{\lambda_j}-\frac{1-q_j}{\lambda_j^2}\right].}\tag{6}
\]
Exact data are compatible with the stipulated **exactly \(N\)-mode** model if and only if the above procedure yields \(H\succ0\), distinct real roots in \((0,1)\), positive \(w_j\), positive \(D\), and reconstitutes the input data under (1)–(2). Necessity was proved above. Conversely, positive reconstructed parameters define independent stationary OU processes and a Brownian motion giving those data, which proves sufficiency. This is a falsifiable physical feasibility test, not merely an interpolation procedure. When fewer than \(N\) modes are allowed, the Hankel rank detects the actual number, provided exact data.

**4. Sharp number of samples.** With ordered rates \(0<\lambda_1<\cdots<\lambda_N\), the full parameter domain \((D,a_1,\ldots,a_N,\lambda_1,\ldots,\lambda_N)\) is a nonempty open subset of \(\mathbb R^{2N+1}\). The forward map to variances at any \(m\) predetermined times is continuous. For \(m<2N+1\), such a map cannot be injective: composing an assumed injection with the standard embedding of \(\mathbb R^m\) into \(\mathbb R^{2N+1}\) contradicts invariance of domain, since its image is contained in a lower-dimensional hyperplane. This is a nonadaptive, exact-data lower bound. Step 3 attains it.

**5. Nonparametric boundary and instability.** For a continuous even stationary Gaussian covariance \(K\), equation (2) without its last finite sum gives
\[
 S'(0+)=2D,\qquad S''(t)=2K(t)\ \ (t>0).
\]
Hence the entire curve \(R(t)\) identifies \(D\) and \(K(t)\), with continuity giving \(K(0)\). Every continuous positive-definite even \(K\) admits a finite nonnegative symmetric spectral measure, and conversely, so the admissibility condition is genuine physical realizability rather than pointwise positivity alone.

For an arbitrary finite collection of \(m\) positive observation times, select \(m+2\) distinct nonnegative frequencies. Their cosine covariance functions are linearly independent, but the \(m\) observed integrals \(\int_0^t(t-u)\cos(\omega u)du\), together with the constraint on total spectral mass \(K(0)\), impose only \(m+1\) homogeneous linear equations on \(m+2\) spectral weights. A nonzero null vector exists; perturbing a strictly positive baseline mass vector by a sufficiently small multiple of it gives two distinct positive spectral measures with the same \(D\), the same \(K(0)\), and identical sampled \(R\)-values. The covariance functions differ because cosines of distinct nonnegative frequencies are linearly independent.

For lack of uniform stability, compare a base covariance \(K_0\) with \(K_\omega(t)=K_0(t)+\varepsilon\cos(\omega t)\), for fixed \(\varepsilon>0\). Both are stationary Gaussian covariances, yet their zero-lag values differ by \(\varepsilon\). The difference of their displacement variances is \(2\varepsilon[1-\cos(\omega t)]/\omega^2\); by (1) and \(|\sqrt u-\sqrt v|\leq\sqrt{|u-v|}\),
\[
 \sup_{t\geq0}|R_\omega(t)-R_0(t)|
 \leq\rho\sqrt{\frac{8\varepsilon}{\pi}}\,\frac1\omega\longrightarrow0.
\]
Thus even an arbitrarily accurate uniform current-variance curve cannot bound the error in instantaneous propulsion variance without restrictions on high-frequency spectral content.

## Verification

Execute `python verify.py` with Python 3 and `mpmath`. The standalone test reconstructs \(N=1,2,3,4\) independent multi-OU spectra at 70-digit precision, checks the second-difference identity, compares the OU formula with independent Green–Kubo quadrature, evaluates the Poisson crossing-rate integral independently, exhibits distinct positive spectral measures indistinguishable at finitely many times (including their total masses), and checks the high-frequency instability estimate. It reported **60 passed comparisons**. These finite computations support arithmetic and implementation but are not substitutes for the infinite-dimensional arguments or the topological lower-bound proof.

## Relationship to prior work

Jangid, Kumbhakar, Klamser, and Sadhu (2026), arXiv:2608.25916v1, derive full current fluctuations for one stationary active OU propulsion; their single-mode mean-square displacement is the \(N=1\) case of (2). The Poisson crossing and Gaussian displacement ingredients are thus prior work. The present exact inference theorem addresses an arbitrary fixed number of unknown OU relaxation scales and unknown Brownian diffusivity, supplies their sharp predetermined-sample count and a physical feasibility test, and separates all-time identifiability from finite-time and noisy non-identifiability.

The Hankel/Prony exponential-moment inversion is an established technique, not a new algorithm claimed here. Kunis, Peter, Römer, and von der Ohe (2015), arXiv:1506.00450, and Sauer (2016), arXiv:1610.02780, provide Prony-method context. Deng, Yang, and Qian (2026), arXiv:2606.21815, use Hankel rank to identify point heat sources from boundary flux in a different inverse PDE problem. The new relationship is the physical conversion of **macroscopic current noise** to a finite exponential moment sequence with a sharp measurement threshold for **microscopic stationary active-noise relaxation rates**. It is possible that broader variogram-inversion or exponential-signal identification results imply components of this specific combination; no general priority over Prony or Green–Kubo theory is asserted.

## Limitations

The model is noninteracting and spatially homogeneous, with known initial density and stationary independent centered Gaussian propulsion. No result is asserted for interacting active particles, shared environmental noise, nonstationary velocity initializations, unknown particle density, current measurements other than ideal ensemble statistics, or nonlinear propulsion. The \(2N+1\) minimality concerns predetermined scalar measurement times and the exactly \(N\)-mode positive model with unknown \(D\), not adaptive schemes with arbitrary observables. Uniqueness is exact-data uniqueness and does not entail well-conditioned recovery when rates nearly coincide or amplitudes nearly vanish. The generalized inverse is provably ill-posed without spectral regularization.

## References

1. S. Jangid, A. Kumbhakar, J. U. Klamser, T. Sadhu, *Current fluctuations in a gas of active Ornstein–Uhlenbeck particles*, arXiv:2608.25916v1 (first public 2026-08-26), https://arxiv.org/abs/2608.25916.
2. S. Kunis, T. Peter, T. Römer, U. von der Ohe, *A multivariate generalization of Prony's method*, arXiv:1506.00450 (2015), https://arxiv.org/abs/1506.00450.
3. T. Sauer, *Reconstructing sparse exponential polynomials from samples*, arXiv:1610.02780 (2016), https://arxiv.org/abs/1610.02780.
4. Z. Deng, X. Yang, A. Qian, *A Moment–Hankel Rank Method for Identifying the Number of Point Sources in the Heat Equation*, arXiv:2606.21815 (2026), https://arxiv.org/abs/2606.21815.
