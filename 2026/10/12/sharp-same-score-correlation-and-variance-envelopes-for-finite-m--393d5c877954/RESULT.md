# Sharp same-score correlation and variance envelopes for finite-memory copulas

## Finding

A finite-range copula built from one chain of orthonormal functions has **sharp lag-dependent same-score correlation bounds** given by finite weighted-path spectra. The same structure gives sharp, score-uniform **finite-sample variance** and **long-run variance** envelopes. In particular, the upper bound of half the largest coefficient asserted for adjacent correlations in Theorem 4.4(2) of Longla (2026) fails when two adjacent coefficients are nonzero; the correct upper endpoint may approach the *entire* largest coefficient, even though the Markov chain is finite-dependent.

Precisely, under the assumptions below, write \(d=m+1\) and \(w_i^{(k)}=\prod_{j=i}^{i+k-1}\lambda_j\). For \(1\le k\le m\), let the symmetric \(d\)-by-\(d\) matrix \(J^{(k)}\) have only \(J^{(k)}_{i,i+k}=J^{(k)}_{i+k,i}=w_i^{(k)}/2\) as possibly nonzero entries, for \(1\le i\le d-k\). Denote its spectral radius by \(r_k\). For *every* nonconstant real square-integrable score \(f\),

\[
-r_k\le \operatorname{Corr}(f(X_0),f(X_k))\le r_k,
\]

and both endpoints are attained by explicit finite linear combinations of the orthonormal functions. These are exact bounds, including when some coefficients vanish.

For every integer \(N\ge1\), define the real symmetric matrix \(H_N\), indexed from \(1\) to \(d\), by

\[
(H_N)_{ij}=\begin{cases}
1,&i=j,\\
(1-|i-j|/N)\displaystyle\prod_{\ell=\min(i,j)}^{\max(i,j)-1}\lambda_\ell,&0<|i-j|<N,\\
0,&|i-j|\ge N.
\end{cases}
\]

If \(S_N=\sum_{n=0}^{N-1}f(X_n)\), the sharp score-uniform envelope is

\[
\lambda_{\min}(H_N)\le
\frac{\operatorname{Var}(S_N)}{N\operatorname{Var}(f(X_0))}
\le\lambda_{\max}(H_N).
\]

The long-run analogue has \(H_{ii}=1\) and \(H_{ij}=\prod_{\ell=\min(i,j)}^{\max(i,j)-1}\lambda_\ell\) for \(i\ne j\), and satisfies

\[
\lambda_{\min}(H)\le
\lim_{N\to\infty}\frac{\operatorname{Var}(S_N)}{N\operatorname{Var}(f(X_0))}
\le\lambda_{\max}(H).
\]

All four finite-sample/asymptotic endpoints are attained by score functions in \(\operatorname{span}\{\phi_1,\ldots,\phi_d\}\). These are statements about a *single identical score at both times*, unlike maximal correlation over two independently chosen scores.

In the homogeneous case \(\lambda_1=\cdots=\lambda_m=t\), the adjacent-correlation bound has the explicit sharp value

\[
r_1=|t|\cos\!\left(\frac{\pi}{m+2}\right).
\]

For \(m=2\), \(t=1/4\), using the concrete trigonometric basis from Longla (2026), the unit-variance score

\[
f(u)=\tfrac12\phi_1(u)+\tfrac{1}{\sqrt2}\phi_2(u)+\tfrac12\phi_3(u)
\]

has adjacent correlation \(1/(4\sqrt2)=\sqrt2/8>1/8\), contradicting the published bound. The exact asymptotic variance-factor range over all scores for this copula is

\[
\left[\frac{33-\sqrt{129}}{32},\ \frac{33+\sqrt{129}}{32}\right].
\]

## Assumptions and scope

Fix an integer \(m\ge1\). Let \(\phi_1,\dots,\phi_{m+1}\) be **real**, **bounded**, mean-zero orthonormal functions of \(L^2([0,1])\). Let \(\lambda_1,\dots,\lambda_m\) be real numbers such that

\[
c(u,v)=1+\sum_{i=1}^m\lambda_i\phi_i(u)\phi_{i+1}(v)\ge0
\quad\text{for almost all }(u,v)\in[0,1]^2.
\]

The density has uniform margins and defines a bivariate copula. Let \((X_n)_{n\ge0}\) be the stationary Markov chain on \([0,1]\) with transition density \(c\), started from the uniform law. Its centered transition operator is nilpotent of order at most \(m+1\), so observations separated by more than \(m\) time steps are independent. No symmetry or reversibility of the copula is assumed. Any real score \(f\in L^2([0,1])\) with positive variance is eligible. If coefficients vanish, the actual dependence horizon may be smaller.

## Proof

**1. Transition and lag covariances.** Center and normalize \(f\) to have \(\int_0^1 f=0\), \(\int_0^1f^2=1\). Write

\[
f=\sum_{i=1}^{d}a_i\phi_i+h,\qquad h\perp\operatorname{span}\{1,\phi_1,\ldots,\phi_d\},\qquad \sum_i a_i^2+\lVert h\rVert_2^2=1.
\]

For the centered transition operator \(T\), direct integration gives \(T\phi_{i+1}=\lambda_i\phi_i\), \(T\phi_1=0\), and \(Th=0\). Induction therefore yields

\[
\gamma_k:=\operatorname{Cov}(f(X_0),f(X_k))
=\langle f,T^k f\rangle
=\sum_{i=1}^{d-k}w_i^{(k)}a_i a_{i+k},\qquad 1\le k\le m,
\]

while \(\gamma_k=0\) for \(k>m\). Thus \(\gamma_k=a^{\mathsf T}J^{(k)}a\).

**2. Sharp lag envelopes.** Each graph of \(J^{(k)}\) is the disjoint union of paths on the index classes modulo \(k\). Assign alternating signs along each path; the resulting diagonal sign matrix \(D\) satisfies \(DJ^{(k)}D=-J^{(k)}\). Therefore the spectrum is symmetric about zero and has endpoints \(\pm r_k\). Since \(\lVert a\rVert_2\le1\), the Rayleigh inequality gives \(|\gamma_k|\le r_k\). A unit eigenvector \(a\) at either spectral endpoint defines the admissible unit-variance score \(f=\sum_i a_i\phi_i\) attaining equality. This proves both sharpness and the complete same-score range. For constant \(\lambda_i=t\), \(J^{(1)}\) is \(t/2\) times the path adjacency matrix on \(d\) vertices, whose discrete-sine eigenvectors have eigenvalues \(t\cos(j\pi/(d+1))\). Since \(d=m+1\), the displayed cosine formula follows.

**3. Sharp variance envelopes.** By stationarity and finite dependence,

\[
\frac1N\operatorname{Var}(S_N)=1+2\sum_{k=1}^{\min(m,N-1)}(1-k/N)\gamma_k.
\]

Substituting the quadratic forms and the orthogonal decomposition gives exactly

\[
\frac1N\operatorname{Var}(S_N)=\lVert h\rVert_2^2+a^{\mathsf T}H_Na.
\]

The matrix \(H_N\) is symmetric with diagonal entries all one, so its average eigenvalue is one; consequently \(\lambda_{\min}(H_N)\le1\le\lambda_{\max}(H_N)\). The Rayleigh principle proves both bounds for every score, and score vectors built from unit endpoint eigenvectors attain them. Taking \(N\to\infty\) gives \(H_N\to H\) entrywise (indeed in operator norm, since dimension is fixed), and the same proof gives the limiting interval with sharp endpoints. This also independently shows both matrices are positive semidefinite for copula-admissible coefficients, since their quadratic forms are normalized actual sample variances and their limits.

**4. Concrete admissible reversal and exact three-dimensional spectrum.** Choose \(m=2\), \(\lambda_1=\lambda_2=1/4\) and

\[
\phi_1(u)=\sqrt2\sin(2\pi u),\quad
\phi_2(u)=\sqrt2\cos(2\pi u),\quad
\phi_3(u)=\sqrt2\sin(4\pi u).
\]

Orthogonality and mean zero follow from Fourier orthogonality. Since \(|\phi_i\phi_{i+1}|\le2\), one has \(c(u,v)\ge1-2(1/4+1/4)=0\), proving copula validity including boundary points. For \(a=(1/2,1/\sqrt2,1/2)\), \(\lVert a\rVert_2=1\) and \(\gamma_1=\tfrac14(a_1a_2+a_2a_3)=1/(4\sqrt2)\). This exceeds \(\max_i|\lambda_i|/2=1/8\). Here

\[
H=\begin{pmatrix}1&1/4&1/16\\1/4&1&1/4\\1/16&1/4&1\end{pmatrix},
\]

whose eigenvalues, by symmetric/antisymmetric decomposition, are \(15/16\) and \((33\pm\sqrt{129})/32\). This establishes the claimed sharp long-run range, rather than merely bounding the one exhibited score.

## Verification

The accompanying `longla_spectral_checker.py` verifies 718 finite identities and inequalities: nilpotent transition powers, all lag-path symmetrizations, sign symmetry of lag spectra, score quadratic forms, sample-variance matrices at different horizons, homogeneous cosine eigenvalues, exact symbolic three-dimensional eigenvalues and witness, and independent two-dimensional Gauss–Legendre quadrature of the one-step and two-step copula densities. Execute with `python longla_spectral_checker.py` using Python, NumPy and SymPy. The infinite-quantifier claims follow from the preceding algebraic proof, not from numerical tests.

## Relationship to prior work

Longla (2026), equation (11), Theorem 4.4, Theorem 5.1, and its explicit two-dependent trigonometric example supply the copula construction and fixed-score lag covariance identities. They **do not** supply correct sharp same-score envelopes across connected coefficients: Theorem 4.4(2) and its proof claim the value \(\max_i|\lambda_i|/2\), which the displayed admissible copula disproves. The present spectral principle distinguishes maximizing one score from separately maximizing two scores, and gives *all* lag, finite-sample and asymptotic score-uniform extrema. The earlier Longla (2025) work studies idempotence and one-dependent constructions; the one-link case does not exhibit interference between adjacent edges. Classical Kac–Murdock–Szegő matrix theory already covers the homogeneous matrix \(H\) as an abstract Toeplitz covariance matrix, so the fact that this matrix has a spectrum is not claimed as new. The added probabilistic content is its exact identification as the attainable long-run variance operator in this nonreversible, finite-dependent copula class, together with sharp bounds and the concrete contradiction of the published assertion.

## Limitations

The result is for the one-chain orthonormal copula expansion above, not arbitrary nilpotent Hilbert-space transition operators, general finite-state Markov models, or arbitrary copulas. It optimizes over **all** real square-integrable scores and does not assert the same bounds for restricted monotone-score classes. The classic linear-algebra ingredients are not new, and the source's explicit covariance formulas are acknowledged. Full published priority cannot be excluded beyond the inspected literature. No independent mathematical audit is represented by the verification program.

## References

1. Martial Longla, *Copulas, m-dependence, and Markov chains*, TEST **35**, 406–439 (2026), https://doi.org/10.1007/s11749-026-01003-0; public 21 February 2026. Relevant: sections 3–5, especially eq. (11), Theorem 4.4(2), section 4.4, Theorem 5.1.
2. Martial Longla, *Continuous Exchangeable Markov Chains, Idempotent and 1-Dependent Copulas*, Mathematics **13** (2025), 2034, https://doi.org/10.3390/math13122034.
3. George Fikioris, *Spectral properties of Kac–Murdock–Szegő matrices with a complex parameter*, arXiv:1804.08140 (2018), https://arxiv.org/abs/1804.08140; see sections 1–2 for the classical Toeplitz matrix and its spectral study.
