# Exact Hermitian norms of weighted one-body marginal projections

## Finding

Let \(n\geq1\), let \(d_1,\ldots,d_n\geq2\) be integers, and let \(t_1,\ldots,t_n\in\mathbb R\). On the real normed space of Hermitian operators on \(\mathcal H=\bigotimes_{j=1}^n\mathbb C^{d_j}\), equipped with the spectral norm, define the centered one-body extraction map
\[
\mathcal P_t(H)=\sum_{j=1}^nt_j\bigl(E_j(H)-E_0(H)\bigr),\qquad
E_j(H)=\frac{\operatorname{Tr}_{j^c}H}{\prod_{k\ne j}d_k}\otimes I_{j^c},\qquad
E_0(H)=\frac{\operatorname{Tr}H}{\prod_kd_k}I.
\]
Here tensor placement is canonical and \(\operatorname{Tr}\) and \(\operatorname{Tr}_{j^c}\) are *unnormalized* full and partial traces. Let \(B_j\) be independent Bernoulli variables with \(\Pr(B_j=1)=1/d_j\). The exact induced Hermitian spectral norm is
\[
\boxed{\ \|\mathcal P_t\|_{\infty\to\infty,\mathrm{Herm}}=
\mathbb E\left|\sum_{j=1}^nt_j(d_jB_j-1)\right|.\ }
\]
The same number is its Hermitian trace-norm operator norm \(\|\mathcal P_t\|_{1\to1,\mathrm{Herm}}\). Moreover, the extremal dual state may always be chosen as a **pure product state**, so entanglement cannot increase the amplification in either Hermitian endpoint norm.

For equal dimensions \(d_j=d\geq2\) and equal unit weights, the exact closed formula is
\[
\boxed{\ \|\mathcal P_{\mathbf1}\|_{\infty\to\infty,\mathrm{Herm}}
=\frac{2n}{d^n}\binom{n-1}{\lfloor n/d\rfloor}
(d-1)^{n-\lfloor n/d\rfloor}.\ }
\]
For each fixed \(d\), this equals \(\sqrt{2n(d-1)/\pi}\,(1+o(1))\) as \(n\to\infty\). If \(n,d\to\infty\) with \(n/d\to\lambda\in(0,\infty)\), its ratio to \(n\) converges to
\[
F(\lambda)=2e^{-\lambda}\frac{\lambda^{\lfloor\lambda\rfloor}}{\lfloor\lambda\rfloor!}.
\]
This continuous profile has a genuine derivative jump at every positive integer \(k\): \(F'_+(k)-F'_-(k)=F(k)/k>0\). The endpoint limits are \(F(0+)=2\) and \(F(\lambda)\sim\sqrt{2/(\pi\lambda)}\) as \(\lambda\to\infty\).

## Assumptions and scope

All spaces are finite-dimensional complex Hilbert spaces; the *domain and codomain* of the asserted operator norms consist only of Hermitian matrices viewed as a **real** Banach space. No assertion is made for the complex-linear spectral norm on all, possibly non-Hermitian, matrices or for completely bounded norms. The weights are arbitrary real numbers, including negative and zero weights; the dimensions can differ and may grow with \(n\). The map has \(\mathcal P_t(I)=0\), is trace preserving only in the zero-trace sense \(\operatorname{Tr}\mathcal P_t(H)=0\), and for all-one weights extracts exactly the one-site, traceless tensor terms.

A pure product state is a rank-one projection \(\rho=\bigotimes_j|u_j\rangle\langle u_j|\). It is used as a dual witness; the norm-attaining Hermitian *input* can be taken as \(\operatorname{sgn}(\mathcal P_t(\rho))\), assigning arbitrary signs to zero eigenvalues. The trace norm uses the ordinary unnormalized trace. The formulas remain valid for \(n=1\) and every \(d_j\ge2\).

## Proof

**1. Endpoint duality.** Each \(E_j\) and \(E_0\) is self-adjoint for the unnormalized Hilbert–Schmidt trace pairing, hence so is \(\mathcal P_t\) because \(t_j\) is real. For Hermitian \(H\), \(\|H\|_\infty=\sup_{\rho\text{ pure}}|\operatorname{Tr}(H\rho)|\). Interchanging the two finite-dimensional suprema and using trace/spectral duality on Hermitian matrices gives
\[
\|\mathcal P_t\|_{\infty\to\infty,\mathrm{Herm}}
=\sup_{\rho\text{ pure}}\|\mathcal P_t(\rho)\|_1.
\]
The same supremum is \(\|\mathcal P_t\|_{1\to1,\mathrm{Herm}}\), because rank-one positive and negative projections are the extreme points of the Hermitian trace-norm unit ball. These steps use no normalization of the trace pairing.

**2. Marginal spectral reduction.** For any density operator \(\rho\), write \(\rho_j=\operatorname{Tr}_{j^c}\rho\) and let \(\lambda_{j,1},\ldots,\lambda_{j,d_j}\) be its eigenvalues, nonnegative and summing to one. With \(D=\prod_jd_j\), direct substitution gives
\[
\mathcal P_t(\rho)=D^{-1}\sum_jt_j(d_j\rho_j-I_j)^{(j)}.
\]
The terms act on distinct tensor factors and commute. Taking the trace norm by simultaneous diagonalization yields
\[
\|\mathcal P_t(\rho)\|_1
=\mathbb E_{I_1,\ldots,I_n}
\left|\sum_jt_j(d_j\lambda_{j,I_j}-1)\right|,
\]
where the independent indices \(I_j\) are uniform on \(\{1,\ldots,d_j\}\). This identity does not assume that \(\rho\) is separable.

**3. Sharp convex-order comparison.** Independently sample indices \(K_j\) with \(\Pr(K_j=r)=\lambda_{j,r}\). Conditional on the independent uniform indices \((I_j)\),
\[
 d_j\lambda_{j,I_j}-1
 =\mathbb E\left[d_j\mathbf1_{\{I_j=K_j\}}-1\mid I_j\right].
\]
Because absolute value is convex, conditional Jensen's inequality gives
\[
\|\mathcal P_t(\rho)\|_1\leq
\mathbb E_{I,K}\left|\sum_jt_j(d_j\mathbf1_{\{I_j=K_j\}}-1)\right|.
\]
Each event \(\{I_j=K_j\}\) has probability \(1/d_j\); the events are independent across sites. The right side is therefore precisely the stated Bernoulli absolute moment, independently of \(\rho\). For a pure product state, every \(\rho_j\) has eigenvalue list \((1,0,\ldots,0)\) and the Jensen comparison is an equality. By Step 1 this proves both exact endpoint norms and attainment. It also proves the stronger statement that the trace-norm image of **every** state is bounded by the value at a product-pure state.

**4. Equal local dimensions.** Suppose \(d_j=d\) and \(t_j=1\). Then \(K=\sum_j B_j\) has the binomial law \(\mathrm{Bin}(n,p)\) with \(p=1/d\), and the exact norm is \(d\,\mathbb E|K-np|\). Put \(m=\lfloor np\rfloor\). Since \(\mathbb E(K-np)=0\), separate the positive and negative parts and use \(k\binom nk=np\binom{n-1}{k-1}/p\) to obtain
\[
\mathbb E|K-np|=2np(1-p)\Pr(\mathrm{Bin}(n-1,p)=m).
\]
Inserting the binomial point mass gives the displayed closed form. The equality also holds when \(np\) is an integer: including or omitting the zero contribution changes nothing.

**5. Limits and cusps.** For fixed \(d\), the local central limit theorem applied at \(m=\lfloor n/d\rfloor\) gives
\(\Pr(\mathrm{Bin}(n-1,1/d)=m)\sim[2\pi n(1/d)(1-1/d)]^{-1/2}\), proving the fixed-dimension asymptotic. If \(n/d\to\lambda>0\) with \(n,d\to\infty\), the binomial point mass converges to the corresponding Poisson point mass. When \(\lambda\) is an integer, either adjacent integer cut-off has the same Poisson mass, so the limit is unambiguous and equals \(F(\lambda)\). The same expression yields \(F(0+)=2\) and its large-\(\lambda\) limit by Stirling's formula. On \(k<\lambda<k+1\), logarithmic differentiation gives \(F'(\lambda)=F(\lambda)(k/\lambda-1)\). Its one-sided limits at \(k\) are \(-F(k)/k\) and \(0\), proving the cusp formula.

## Verification

The standalone `checker.py` (Python 3 with NumPy) tests the rational Bernoulli moment against the exact central-binomial expression, compares product-pure witnesses with full tensor-matrix partial traces, checks the Hermitian norm dual sign witness, and tests the upper bound on randomly sampled entangled pure states and Hermitian matrices in several heterogeneous weighted dimensions. It additionally checks the Gaussian and Poisson approximations numerically. Invoke `OPENBLAS_NUM_THREADS=1 python checker.py`. A successful replay prints `PASS: 275 finite checks; all source normalizations and random inequalities consistent`. These finite tests validate implementations and special instances; the five analytical steps above, not the tests, prove the all-dimensions statement.

## Relationship to prior work

Volberg and Zhang, *Noncommutative Bohnenblust--Hille inequalities*, arXiv:2210.14468 (first public 2022-10-26), introduce the Pauli-string weight hierarchy and upper coefficient inequalities for quantum Boolean cubes. Their inequalities do not give this weighted, endpoint-norm equality on Hermitian matrices, nor its qudit and Poisson crossover. Rouzé, Wirth and Zhang, *Quantum Talagrand, KKL and Friedgut's theorems and the learnability of quantum Boolean functions*, arXiv:2209.07279 (first public 2022-09-15), study influences and noncommutative functional inequalities with the same conditional-expectation framework, but not the exact one-body extraction norm. Defant, Galicer, Mansilla, Mastyło and Muro, arXiv:2302.00233 (first public 2023-02-01), obtain sharp classical Boolean Fourier projection constants, including a special case of the Rademacher first-level moment. That **commutative** lower-bound example does not by itself establish the quantum upper bound over arbitrary entangled states, nor unequal qudit dimensions. The novelty claim is restricted to the explicit weighted Hermitian quantum identity, its product-state extremality, and its dimension-dependent asymptotic phase profile; classical first-level moments are not claimed as new.

## Limitations

The map is not asserted to have the same norm on nonselfadjoint inputs; neither completely bounded norms nor higher-body conditional-expectation projections are determined. A possible equivalent result in broader noncommutative martingale or conditional-expectation literature remains an originality risk. The Poisson scaling assumes \(n,d\to\infty\) with \(n/d\to\lambda>0\), whereas the fixed-local-dimension central-limit regime is treated separately. No claim is made about quantum learning sample complexity.

## References

1. A. Volberg and H. Zhang, *Noncommutative Bohnenblust--Hille inequalities*, arXiv:2210.14468v1 (2022-10-26), https://arxiv.org/abs/2210.14468 .
2. C. Rouzé, M. Wirth and H. Zhang, *Quantum Talagrand, KKL and Friedgut's theorems and the learnability of quantum Boolean functions*, arXiv:2209.07279v1 (2022-09-15), https://arxiv.org/abs/2209.07279 .
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon-Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1 (2023-02-01), https://arxiv.org/abs/2302.00233 .
