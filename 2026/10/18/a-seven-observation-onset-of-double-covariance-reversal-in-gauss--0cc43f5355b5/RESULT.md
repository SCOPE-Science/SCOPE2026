# Strict positivity in short Gaussian AR(1) crossing windows: sharpness of the seven-observation onset

## Finding

Let \(X_1,\ldots,X_n\) be jointly centered Gaussian, with unit variances and correlations \(\rho^{|i-j|}\), where \(0\leq\rho<1\). Let \(V_n=\sum_j(X_j-\overline X)^2\) and \(Z_n=\sum_{i=1}^{n-1}\mathbf 1\{X_iX_{i+1}<0\}\). For every \(2\leq n\leq 6\) and every \(0\leq\rho<1\),
\[
\operatorname{Cov}(V_n,Z_n)>0.
\]
The earlier centered-energy result [1] proves that for every \(n\geq7\) the covariance is negative at \(\rho=1/2\) and positive at zero and sufficiently near one. The short-window exclusion proved here makes seven the sharp minimum window size for negative covariance. No claim is made about the exact number of zeros when \(n\geq7\).

## Proof

We first recall the mixed-moment identity from [1]. Here is a derivation fixing its normalization. If \(W=(U,V)^{\mathsf T}\) consists of two standard Gaussian variables with correlation \(r\in(-1,1)\), let \(M=\operatorname{Cov}(W)\) and let \(b=(a_1,a_2)^{\mathsf T}=\operatorname{Cov}(W,Y)\) for a jointly centered Gaussian \(Y\). Gaussian regression replaces \(Y^2-\mathbb E Y^2\), conditional on \(W\), by \((b^{\mathsf T}M^{-1}W)^2-b^{\mathsf T}M^{-1}b\). Multiplying this expression by the density of \(W\) gives twice the covariance-direction derivative of the density along \(M+tbb^{\mathsf T}\) at \(t=0\). The derivative can be integrated against the bounded crossing indicator, since the perturbed matrices stay positive definite near zero and the differentiated densities are bounded by a polynomial times a decaying Gaussian. The crossing probability for variances \(s,u\) and covariance \(c\) is \(\pi^{-1}\arccos(c/\sqrt{su})\), by rotational symmetry of a standard bivariate normal. Twice its directional derivative gives
\[
\operatorname{Cov}(Y^2,\mathbf1\{UV<0\})
=\frac{r(a_1^2+a_2^2)-2a_1a_2}{\pi\sqrt{1-r^2}}.
\]

Write \(H=I-\mathbf1\mathbf1^{\mathsf T}/n\), and let \(a_i=(\rho^{|j-i|})_{j=1}^n\) be the \(i\)-th covariance column, with diagonal entries one. Apply the identity to each coordinate of \(HX\) and each adjacent pair. Summation gives \(\operatorname{Cov}(V_n,Z_n)=F_n(\rho)/(\pi\sqrt{1-\rho^2})\) with
\[
F_n(\rho)=\sum_{i=1}^{n-1}\bigl(\|H(a_i-a_{i+1})\|^2
+(\rho-1)(\|Ha_i\|^2+\|Ha_{i+1}\|^2)\bigr).
\]
In particular the identity concerns energy centered at the sample mean, not energy about the known population mean.

For \(2\leq n\leq6\), direct polynomial multiplication in this sum gives \(F_n(\rho)=k_n(1-\rho)^2(1+\rho)P_n(\rho)\), with the following coefficients in increasing power order:

| \(n\) | \(k_n\) | Coefficients of \(P_n\) | Minimum Bernstein coefficient |
|---:|---:|---|---:|
| 2 | \(1\) | \(1\) | \(1\) |
| 3 | \(4/3\) | \(1,0,1\) | \(1\) |
| 4 | \(1/2\) | \(3,-2,5,1,3\) | \(5/2\) |
| 5 | \(4/5\) | \(2,-3,3,1,4,1,2\) | \(23/20\) |
| 6 | \(1/3\) | \(5,-12,5,-1,14,5,11,3,5\) | \(11/56\) |

To reproduce the multiplication, the coefficient of \(\rho^k\) in the \(j\)-th coordinate of \(nHa_i\) is \(n\mathbf1\{|j-i|=k\}-\#\{\ell:|\ell-i|=k\}\). Form the products in the preceding sum using these integers, then divide by \(n^2\). For a polynomial \(\sum_{j=0}^d p_j\rho^j\), its degree-\(d\) Bernstein coefficient at index \(k\) is \(\sum_{j=0}^k p_j\binom{k}{j}/\binom{d}{j}\); this follows by expanding each power in the Bernstein basis. The last column records the exact minima from this formula. Since the Bernstein basis is nonnegative and sums to one on \([0,1]\), each \(P_n\) is strictly positive there. The other factors and the covariance denominator are strictly positive on \([0,1)\), including \(\rho=0\). At \(\rho=1\) the Gaussian vector is degenerate; that endpoint is not included.

## Reproduction

`python3 verify_gaussian.py` checks the five polynomial identities coefficient by coefficient using integer convolution, and verifies the five Bernstein minima using rational arithmetic. The certificate is exact for these five integer dimensions; it does not sample the correlation interval or assert any result for larger dimensions.

## Relationship to prior work

[1] treats the same centered-energy statistic and gives the mixed-moment formula, the sign pattern for every \(n\geq7\), the fixed-correlation limit, and two large-window transition layers. Its sign argument does not exclude a negative covariance at a smaller window size. The contribution here is precisely the exclusion on the whole correlation interval for \(2\leq n\leq6\); the larger-window signs are used only to infer sharpness. Work on covariances *between crossing indicators* or on marginal crossing-count moments concerns a different statistic.

[1] *Two boundary layers for zero-crossing and centered-energy covariance*, Resultary record [e0f4a1d0a49b](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-two-boundary-layers-for-zero-crossing-and-centered-energy-covari--e0f4a1d0a49b/RESULT.md), especially Finding and Proof §2.
