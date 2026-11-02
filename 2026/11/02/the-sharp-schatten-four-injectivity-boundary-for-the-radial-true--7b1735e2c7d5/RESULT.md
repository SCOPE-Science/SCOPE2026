# The sharp Schatten-four injectivity boundary for the radial true-polyanalytic Fock Berezin transform

## Finding

Let \(\mathcal H_{(2)}\) be the true order-two polyanalytic Fock space with Gaussian measure \(\pi^{-1}e^{-|z|^2}dA(z)\), and let \(\mathfrak R\) be its algebra of bounded rotation-commuting operators. The kernel of the normalized coherent-state Berezin map, restricted to \(\mathfrak R\), is precisely the one-dimensional complex line spanned by a compact self-adjoint operator \(D\). In the standard complex-Hermite basis \((\psi_n)_{n\ge0}\),
\[
D\psi_n=L_n(1)\psi_n,\qquad
L_n(1)=\sum_{j=0}^n(-1)^j\binom nj\frac1{j!}.
\]
Here \(L_n\) is the ordinary Laguerre polynomial. Its ordered singular values satisfy the exact limit
\[
\boxed{\lim_{k\to\infty}k^{1/4}s_k(D)=\left(\frac{3e^2}{8\pi^2}\right)^{1/4}.}
\]
Consequently the radial Berezin transform is injective on the radial Schatten ideal \(\mathfrak R\cap\mathcal S_p\) exactly for \(0<p\le4\), and is noninjective for every \(p>4\). More precisely,
\[
D\in\mathcal S_{4,\infty}\setminus\mathcal S_4,\qquad
\lim_{N\to\infty}\frac1{\log N}\sum_{k=1}^{N}s_k(D)^4
=\frac{3e^2}{8\pi^2}.
\]
The one-dimensional nullspace is included to identify the object completely; the new quantitative claim concerns the sharp operator-ideal boundary and ordered singular-value constant.

## Assumptions and scope

The Hilbert space is the orthogonal complement of the analytic Fock space inside the order-at-most-two polyanalytic Fock space over one complex variable. Thus its functions satisfy \(\partial_{\bar z}^{2}f=0\) in the distributional sense, and the Gaussian squared norm is \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}dA(z)\). Its reproducing kernel is
\[
K(z,w)=e^{z\bar w}\bigl(1-|z-w|^2\bigr),\quad K(w,w)=e^{|w|^2}.
\]
A radial operator means a bounded operator commuting with all rotations \(f(z)\mapsto f(e^{-i\theta}z)\). The normalized Berezin transform is \(\widetilde A(w)=\langle AK_w,K_w\rangle/K(w,w)\). The Schatten quasi-ideals are defined by \(\sum_k s_k(A)^p<\infty\) for \(p>0\), including quasi-Banach exponents. The weak class \(\mathcal S_{4,\infty}\) consists of compact operators with \(\sup_k k^{1/4}s_k(A)<\infty\). All constants use this normalization; no finite-dimensional truncation is used to establish the infinite claims.

## Proof

**1. Diagonal form and exact coherent-state identity.** The complex-Hermite vectors
\[
\psi_0(z)=\bar z,\quad
\psi_n(z)=\frac{z^n\bar z-nz^{n-1}}{\sqrt{n!}}\quad(n\ge1)
\]
form an orthonormal basis of \(\mathcal H_{(2)}\), each with its own rotation character. Distinct characters occur with multiplicity one. Hence every radial bounded operator is uniquely \(A\psi_n=a_n\psi_n\) with \(\sup_n|a_n|<\infty\). Put \(x=|w|^2\) and \(F(x)=\sum_{n=0}^{\infty}a_nx^n/n!\), an entire function. Since \(|\psi_0(w)|^2=x\) and, for \(n\ge1\), \(|\psi_n(w)|^2=x^{n-1}(x-n)^2/n!\), absolute convergence of the coherent-state expansion gives
\[
\widetilde A(w)=e^{-x}\bigl[xF''(x)+(1-2x)F'(x)+xF(x)\bigr]. \tag{1}
\]
The right side extends continuously to \(x=0\), with no excluded evaluation point.

**2. All radial null operators.** If (1) vanishes for \(x\ge0\), analyticity forces the bracket to vanish identically. Writing \(F(x)=e^xH(x)\) reduces the differential equation exactly to
\[
xH''(x)+H'(x)+H(x)=0. \tag{2}
\]
If \(H(x)=\sum_{j\ge0}h_jx^j\), the coefficient recurrence is \((j+1)^2h_{j+1}=-h_j\); thus
\[
H(x)=h_0\sum_{j\ge0}\frac{(-x)^j}{(j!)^2},
\quad F(x)=h_0e^x\sum_{j\ge0}\frac{(-x)^j}{(j!)^2}.
\]
Multiplication of the two power series gives \(a_n=h_0\sum_{j=0}^n(-1)^j\binom nj/j!=h_0L_n(1)\). Conversely, these coefficients make (2), hence (1), zero. The Laguerre Plancherel–Rotach expansion below implies \(L_n(1)\to0\), so the diagonal multiplier is bounded, compact, self-adjoint, and nonzero (its zero-index entry is one). Therefore the entire bounded radial nullspace is \(\mathbb CD\).

**3. Asymptotic distribution of the diagonal.** The classical fixed-positive-argument Laguerre asymptotic, with its normalization explicitly given in DLMF 18.15.14–15, states
\[
L_n(1)=A_*n^{-1/4}\left[\cos\!\left(2\sqrt n-\frac\pi4\right)+O(n^{-1/2})\right],\qquad
A_*=\frac{e^{1/2}}{\sqrt\pi}. \tag{3}
\]
For \(t>0\), define \(N_D(t)=\#\{n\ge0:|L_n(1)|>t\}\) and \(M=(A_*/t)^4\). Formula (3) gives an integrable scaled comparison to the indicator \(\mathbf1\{n/M<|\cos(2\sqrt n-\pi/4)|^4\}\), up to an error whose normalized count tends to zero. Here is the needed joint equidistribution justification: for any fixed \(0<\delta<K<\infty\) and nonzero integer \(h\), Euler summation and the change of variables \(v=\sqrt u\) yield
\[
\frac1M\sum_{\delta M\le n\le KM} e^{2ih\sqrt n} = O_{h,\delta,K}(M^{-1/2}). \tag{4}
\]
The same holds with any continuous test weight of \(n/M\), by step-function approximation. Fourier approximation then gives the product of Lebesgue measure in \(u=n/M\) and uniform measure for the phase modulo \(2\pi\). To handle the indicator, its discontinuity boundary \(u=|\cos\phi|^4\) has two-dimensional measure zero. The region \(u<\delta\) contributes at most \(\delta M+O(1)\); a sufficiently large fixed \(K>1\) excludes \(u>K\) for small \(t\) by the uniform upper bound in (3). Letting \(\delta\downarrow0\) and \(K\uparrow\infty\) gives
\[
\lim_{t\downarrow0}\frac{N_D(t)}{M}
=\frac1{2\pi}\int_0^{2\pi}\!|\cos\phi|^4\,d\phi
=\frac38,
\]
whence
\[
\boxed{N_D(t)\sim \frac{3e^2}{8\pi^2}\,t^{-4}.} \tag{5}
\]
The standard inversion of this monotone singular-value counting function gives the stated ordered singular-value asymptotic.

**4. Sharp ideal boundary.** Let \(C_*=3e^2/(8\pi^2)\). Equation (5) yields \(s_k(D)^p\sim C_*^{p/4}k^{-p/4}\). Thus the series defining \(\mathcal S_p\) converges exactly for \(p>4\); the weak fourth-order bound holds with nonzero sharp coefficient. Since every radial Berezin null operator is a multiple of \(D\), radial injectivity holds precisely when \(p\le4\). Finally \(s_k(D)^4\sim C_*/k\) and comparison with the harmonic sum proves the logarithmic mean formula, without asserting an \(O(1)\) remainder.

## Verification

The standalone Python program `check.py` verifies exact rational Laguerre recurrence identities through degree sixty, finite coherent-state cancellations, and sampled fixed-argument asymptotics. It is intended as a falsification aid; it does not certify the infinite tail, the equidistribution step, or the operator-ideal theorem. The analytical proof of these facts is in the preceding section. Numerical experiments with thresholds \(0.1\), \(0.08\), \(0.06\), \(0.045\) gave counting ratios \(N_D(t)t^4/C_*\) near one, but these are not used as proof.

## Relationship to prior work

Maximenko and Tellería-Romero (2019, arXiv:1905.00978, Theorem 1.2 and Sections 3–5) provide the complex-Hermite basis, kernel and radial diagonalization. Alpay, Colombo, Diki and Sabadini (first posted 2021-12-29, arXiv:2112.14367, Sections 1, 3 and 5) treat polyanalytic Fock reproducing kernels and Berezin-type transforms, primarily in an infinite-order setting. Fulsche and Hagger (first posted 2023-08-22, arXiv:2308.11292, Theorems 3.5, 3.8–3.9) already prove noninjectivity of the true-polyanalytic Berezin transform on all bounded operators, identify its weak-star kernel using Weyl operators on Laguerre-zero circles, and prove injectivity on trace-class and bounded-symbol Toeplitz subclasses. The present one-dimensional radial kernel is compatible with and may be recovered by radializing that qualitative general kernel description; it is not claimed as an independent novelty. A related theorem for a different map (bounded-symbol Toeplitz quantization) has a planar symbol-integrability cutoff at exponent four through a radial Bessel null symbol. This is acknowledged as an adjacent dual phenomenon: it does not itself determine Schatten membership of a Berezin-null operator or its ordered Laguerre singular-value coefficient. The present exact radial Schatten boundary, ordered singular-value coefficient, and logarithmic fourth-power average are not among the inspected primary statements of the cited sources. Formula (3) is classical and separately attributed to NIST DLMF; no novelty is claimed for the Laguerre asymptotic itself.

## Limitations

Only the true second polyanalytic level in one complex dimension and the rotation-commuting operator class are addressed. This does not classify the full, nonradial operator kernel, nor other polyanalytic orders, nor the existence of bounded-symbol Toeplitz representatives. The quantitative theorem uses the known Laguerre asymptotic; potential indirect equivalences in the wider operator-ideal and representation-theoretic literature remain a historical-priority risk. No independent audit has been performed.

## References

1. E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (first posted 2019-05-02), Theorem 1.2, Sections 3–5. https://arxiv.org/pdf/1905.00978
2. D. Alpay, F. Colombo, K. Diki and I. Sabadini, *Reproducing kernel Hilbert spaces of polyanalytic functions of infinite order*, arXiv:2112.14367 (first posted 2021-12-29), Sections 1, 3 and 5. https://arxiv.org/pdf/2112.14367
3. R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (first posted 2023-08-22), Theorems 3.5 and 3.8–3.9. https://arxiv.org/pdf/2308.11292
4. NIST Digital Library of Mathematical Functions, §§18.15(iv), equations 18.15.14–15, fixed-argument Laguerre asymptotics. https://dlmf.nist.gov/18.15
