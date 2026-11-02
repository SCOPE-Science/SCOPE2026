# A sharp sample-size crossover for Fourier-truncated periodic Matérn covariance matrices

## Finding

Let \(d\ge1\) be an integer, let \(\nu>0\), and sample \(X_1,\ldots,X_N\) independently and uniformly on the torus \(\mathbb T^d=\mathbb R^d/\mathbb Z^d\), where \(N\ge1\). Consider the normalized periodic Matérn-type covariance kernel
\[
 k(x)=Z^{-1}\sum_{j\in\mathbb Z^d}(1+\|j\|_2^2)^{-\nu-d/2}e^{2\pi i j\cdot x},\qquad
 Z=\sum_{j\in\mathbb Z^d}(1+\|j\|_2^2)^{-\nu-d/2},
\]
with its Fourier truncation \(k_m\) obtained by retaining precisely \(\|j\|_\infty\le m\), for integers \(m\ge1\). Let \(K=(k(X_i-X_j))_{i,j=1}^N\), \(K_m=(k_m(X_i-X_j))_{i,j=1}^N\), and \(F_{m,N}=\|K-K_m\|_F^2\). Write
\[
 T_m=\sum_{\|j\|_\infty>m}(1+\|j\|_2^2)^{-\nu-d/2},\quad
 S_m=\sum_{\|j\|_\infty>m}(1+\|j\|_2^2)^{-2\nu-d},\quad
 D_m=T_m/Z,\quad V_m=S_m/Z^2.
\]
**Exact finite-sample law:**
\[
 \boxed{\mathbb E F_{m,N}=N D_m^2+N(N-1)V_m.}
\]
For all \(N\ge2\) and every \(\varepsilon>0\), define \(q_{m,N}=(N-1)V_m/D_m^2\). Then the dimension-free bound
\[
 \boxed{\mathbb P\left(\left|\frac{F_{m,N}}{\mathbb E F_{m,N}}-1\right|>\varepsilon\right)
 \le \frac{2q_{m,N}}{N\varepsilon^2(1+q_{m,N})^2}\le\frac1{2N\varepsilon^2}}
\]
holds, and the probability on the left tends to zero as \(m\to\infty\) **for every deterministic choice of integer sample sizes \(N=N(m)\ge1\)**, including bounded and oscillating sequences.

Define finite positive constants
\[
 t_{d,\nu}=\int_{\mathbb R^d\setminus[-1,1]^d}\|u\|_2^{-2\nu-d}\,du,\qquad
 s_{d,\nu}=\int_{\mathbb R^d\setminus[-1,1]^d}\|u\|_2^{-4\nu-2d}\,du.
\]
Then \(T_m\sim t_{d,\nu}m^{-2\nu}\), \(S_m\sim s_{d,\nu}m^{-(4\nu+d)}\), and there is a **sharp sample-size crossover at \(N\asymp m^d\)**:

- If \(N/m^d\to0\), then \(F_{m,N}/(ND_m^2)\to1\) in probability; the diagonal error determines the leading norm.
- If \(N/m^d\to\tau\in(0,\infty)\), then
  \[
  \boxed{\frac{F_{m,N}}{N Z^{-2}t_{d,\nu}^{\,2}m^{-4\nu}}
  \xrightarrow{\mathbb P}1+\tau\frac{s_{d,\nu}}{t_{d,\nu}^{\,2}}.}
  \]
- If \(N/m^d\to\infty\), then \(F_{m,N}/(N(N-1)V_m)\to1\) in probability; the off-diagonal error determines the leading norm.

In particular, the Frobenius norm improves from order \(\sqrt N\,m^{-2\nu}\) to order \(Nm^{-(2\nu+d/2)}\) only when there are enough sampled points to enter the off-diagonal regime. For \(d=1\), \(\nu=1/2\), the exact critical constant is \(s_{1,1/2}/t_{1,1/2}^2=1/6\): the normalized squared error in the window \(N/m\to\tau\) tends to \(1+\tau/6\).

## Assumptions and scope

The points are iid Haar-uniform on the full torus. The Fourier coefficients are the positive, isotropic, periodic Matérn-type spectrum specified above; its normalization ensures \(k(0)=1\). The truncation is by an axis-parallel cube in Fourier frequency. The matrix error is measured by the unnormalized squared Frobenius norm, and statements of convergence hold as \(m\to\infty\) with dimension and smoothness fixed. The true and truncated kernels are positive definite/positive semidefinite because their Fourier weights are nonnegative.

No randomness is assigned to the Fourier coefficients or to the Gaussian field itself; only the sample locations are random. The periodic model avoids both boundary aliasing and the frequency-mesh error of a nonperiodic Fourier-grid approximation.

## Proof

**1. Exact diagonal/off-diagonal decomposition.** Let \(e_m=k-k_m\). Absolute summability of its nonnegative Fourier coefficients ensures that \(e_m\) is real and continuous and \(|e_m(x)|\le e_m(0)=D_m\). For distinct independent Haar points, their difference is Haar-uniform. By character orthogonality (Parseval),
\[
 \int_{\mathbb T^d}e_m(x)^2\,dx
 =Z^{-2}\sum_{\|j\|_\infty>m}(1+\|j\|_2^2)^{-2\nu-d}=V_m.
\]
The \(N\) diagonal matrix entries equal \(D_m\), while the \(N(N-1)\) off-diagonal entries have mean squared error \(V_m\), proving the finite-sample identity. This retains the diagonal term for every finite \(N\).

**2. Variance and uniform concentration.** Set \(g_m(x)=e_m(x)^2\). For \(i<j\), let \(G_{ij}=g_m(X_i-X_j)\). Distinct unordered pairs with no shared point are independent. Pairs sharing exactly one point are uncorrelated: conditioning on the shared Haar point makes the two other points independent and leaves each conditional mean equal to the constant \(V_m\). Hence, with \(B=\sum_{i\ne j}G_{ij}=2\sum_{i<j}G_{ij}\),
\[
 \operatorname{Var}(F_{m,N})=\operatorname{Var}(B)
 =2N(N-1)\left(\int_{\mathbb T^d}e_m(x)^4\,dx-V_m^2\right).
\]
Since \(0\le g_m\le D_m^2\), the parenthesis is nonnegative and at most \(D_m^2V_m\). Dividing by the square of the exact expectation gives
\[
 \frac{\operatorname{Var}(F_{m,N})}{(\mathbb EF_{m,N})^2}
 \le \frac{2q_{m,N}}{N(1+q_{m,N})^2}\le\frac1{2N},
\]
and Chebyshev proves the stated bound. For \(N=1\), the error is deterministic. To obtain concentration along an arbitrary sequence \(N(m)\), split into \(N\) above a fixed large integer (use \(1/(2N)\)) and bounded \(N\) (use \(q_{m,N}=O(Nm^{-d})\to0\)). This yields convergence in probability without a restriction on the relative growth of \(N\) and \(m\).

**3. Sharp spectral-tail constants.** For \(\alpha>d\), a Riemann-sum comparison on the complement of the frequency cube gives
\[
 m^{\alpha-d}\sum_{\|j\|_\infty>m}(1+\|j\|_2^2)^{-\alpha/2}
 \longrightarrow \int_{\mathbb R^d\setminus[-1,1]^d}\|u\|_2^{-\alpha}\,du.
\]
To justify the unbounded region, first truncate it at radius \(R\), where uniform continuity and the measure-zero cube boundary give ordinary Riemann convergence. The omitted tails are bounded uniformly by a constant times \(R^{d-\alpha}\), by comparison with integer annuli. Let \(R\to\infty\). Applying this with \(\alpha=2\nu+d\) and \(\alpha=4\nu+2d\) yields the stated asymptotics for \(T_m\) and \(S_m\).

**4. The three regimes.** The exact ratio of off-diagonal to diagonal expectation is
\[
 q_{m,N}=\frac{(N-1)S_m}{T_m^2}
 \sim\frac{s_{d,\nu}}{t_{d,\nu}^2}\frac{N-1}{m^d}.
\]
Combine this with the concentration result and the tail limits. A vanishing, finite positive, or diverging ratio produces exactly the three claims. Strict positivity of the constants makes the crossover necessary and sharp. In one dimension with \(\nu=1/2\), direct integration gives \(t_{1,1/2}=2\), \(s_{1,1/2}=2/3\), whence \(s/t^2=1/6\).

## Verification

Run `python verify.py` with Python 3, NumPy and mpmath. The standalone file uses exact rational finite Fourier weights in dimensions one and two to reconstruct the spectral tail, its square and its fourth-moment convolution. It checks the expectation, covariance-count and variance-bound identities for multiple sample sizes. It also computes periodic-grid quadratures with enough nodes to integrate the fourth-order trigonometric polynomial exactly, and checks the one-dimensional infinite spectral series against the asymptotic constants. In the supplied execution, **115 check groups passed**.

These finite checks corroborate the stated identities and constants. The arbitrary-dimension and arbitrary-sample-size results rest on the analytic proof above, not on enumerating finite cases or on simulation.

## Relationship to prior work

Barnett, Greengard and Rachh (2023, arXiv:2305.11065, Section 4 and Conjecture 9) motivate the squared-Frobenius question for Matérn Fourier-grid approximations at iid random sites and predict an extra \(d/2\) spectral-error exponent in a large-sample regime. Their setting is a nonperiodic kernel approximated by a finite frequency grid, and their stated heuristic does not supply the finite-\(N\) diagonal/off-diagonal crossover, the exact two-term law, the uniform concentration bound, or the critical constant for the **periodic spectral truncation** considered here. No nonperiodic version of that conjecture is claimed.

Bachmayr, Graham, Nguyen and Scheichl (2019 preprint; 2020 journal version, arXiv:1905.13522) analyze torus periodization and eigenvalue decay for Matérn covariance sampling on uniform grids. Those eigenvalue and positive-definiteness results neither make the sites iid Haar-uniform nor compute the same random Gram-matrix Frobenius error across joint sample-size/bandwidth regimes. Puchkin, Noskov and Spokoiny (2023, arXiv:2308.14739) investigate Frobenius fluctuations of a **sample covariance estimator**, a different random matrix and comparison target.

Standard Parseval identities, lattice tail integrals and degenerate \(U\)-statistic variance calculations are ingredients, not claimed as original. The contribution is their exact combination into a sharp, all-growth-regime, finite-sample covariance-kernel approximation theorem with explicit constants and a dimension-dependent transition.

## Limitations

The result concerns a periodic Matérn-type Fourier spectrum and iid Haar sampling. It does not directly prove the 2023 nonperiodic Matérn Fourier-grid conjecture, deal with nonuniform site density, other spectral windows, approximation of posterior means, or operator-norm error. A universal finite probability bound is given by Chebyshev, not an exponential tail inequality. The theorem is mathematically proved and has undergone only self-review; independent validation and publication-priority review have not occurred.

## References

1. A. Barnett, P. Greengard and M. Rachh, *Uniform approximation of common Gaussian process kernels using equispaced Fourier grids*, arXiv:2305.11065 (first posted May 18, 2023), especially Section 4 and Conjecture 9. https://arxiv.org/html/2305.11065
2. M. Bachmayr, I. G. Graham, V. K. Nguyen and R. Scheichl, *Unified Analysis of Periodization-Based Sampling Methods for Matérn Covariances*, arXiv:1905.13522 (first posted May 31, 2019), SIAM Journal on Numerical Analysis 58 (2020). https://arxiv.org/abs/1905.13522
3. N. Puchkin, F. Noskov and V. Spokoiny, *Sharper dimension-free bounds on the Frobenius distance between sample covariance and its expectation*, arXiv:2308.14739 (first posted August 28, 2023). https://arxiv.org/abs/2308.14739
