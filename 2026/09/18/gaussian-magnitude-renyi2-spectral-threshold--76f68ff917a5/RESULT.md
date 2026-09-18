# Exact Rényi-2 total correlation of Gaussian magnitudes and a spectral phase transition

## Statement

Let \(R\) be an \(n\times n\) positive-definite correlation matrix and
\[
X\sim N(0,R).
\]
Let \(P_R\) denote the law of the coordinatewise magnitudes
\[
(|X_1|,\ldots,|X_n|)
\]
on \((0,\infty)^n\), and let \(Q\) be the product of its marginals. Since each marginal is standard half-normal, \(Q\) is the law of \((|Z_1|,\ldots,|Z_n|)\) for \(Z\sim N(0,I_n)\).

For \(s=(s_1,\ldots,s_n)\in\{\pm1\}^n\), write
\[
D_s=\operatorname{diag}(s_1,\ldots,s_n),\qquad
A_s=R^{-1}+D_sR^{-1}D_s-I_n.
\]

Then the order-2 Rényi total correlation has the following exact form.

**Theorem.**
\[
\boxed{
D_2(P_R\|Q)<\infty
\quad\Longleftrightarrow\quad
\lambda_{\max}(R)<2.
}
\]
In the finite regime,
\[
\boxed{
\exp D_2(P_R\|Q)
=
\frac{1}{2^n\det R}
\sum_{s\in\{\pm1\}^n}
\frac{1}{\sqrt{\det A_s}}.
}
\tag{1}
\]
If \(\lambda_{\max}(R)\ge2\), then \(D_2(P_R\|Q)=+\infty\).

Thus a recent moment-based lower certificate for this Rényi total correlation can be complemented by a closed determinant/sign-sum formula and an exact spectral finiteness criterion.

## Proof

Let \(\varphi_C\) denote the centered Gaussian density with covariance \(C\), and let \(\varphi=\varphi_{I_n}\). The standard multivariate folded-normal density identity gives, for \(x\in(0,\infty)^n\),
\[
p_R(x)=\sum_{s\in\{\pm1\}^n}\varphi_{D_sRD_s}(x),
\qquad
q(x)=2^n\varphi(x).
\]
Hence
\[
\frac{p_R(x)}{q(x)}
=
2^{-n}\sum_s L_s(x),
\qquad
L_s(x)=\frac{\varphi_{D_sRD_s}(x)}{\varphi(x)}.
\tag{2}
\]

If \(Z\sim N(0,I_n)\), the sign vector of \(Z\) is uniform and independent of \(|Z|\). The sign average in (2) is coordinatewise even, so
\[
\exp D_2(P_R\|Q)
=
\mathbb E\left[
\left(2^{-n}\sum_s L_s(Z)\right)^2
\right].
\tag{3}
\]
Expanding the square, and using invariance of standard Gaussian measure under every \(D_s\), the cross term for a pair \((s,t)\) depends only on the coordinatewise product \(u=s\odot t\). Every \(u\in\{\pm1\}^n\) occurs for exactly \(2^n\) ordered pairs. Therefore
\[
\exp D_2(P_R\|Q)
=
2^{-n}\sum_u J_u,
\qquad
J_u=\mathbb E[L_{\mathbf 1}(Z)L_u(Z)].
\tag{4}
\]

For positive-definite covariance matrices \(C_1,C_2\),
\[
\mathbb E_{\varphi}
\left[
\frac{\varphi_{C_1}(Z)}{\varphi(Z)}
\frac{\varphi_{C_2}(Z)}{\varphi(Z)}
\right]
=
\frac{1}
{\sqrt{\det C_1\,\det C_2}\,
 \sqrt{\det(C_1^{-1}+C_2^{-1}-I_n)}}
\tag{5}
\]
whenever
\[
C_1^{-1}+C_2^{-1}-I_n\succ0.
\]
If this matrix is singular or has a negative direction, the integral is infinite. Applying (5) with
\[
C_1=R,\qquad C_2=D_uRD_u
\]
gives
\[
J_u
=
\frac{1}{\det R\,\sqrt{\det A_u}}
\tag{6}
\]
whenever \(A_u\succ0\).

It remains to determine when all terms in (4) are finite. For \(u=\mathbf1\),
\[
A_{\mathbf1}=2R^{-1}-I_n.
\]
Hence \(J_{\mathbf1}<\infty\) exactly when
\[
2R^{-1}-I_n\succ0
\quad\Longleftrightarrow\quad
\lambda_{\max}(R)<2.
\tag{7}
\]
If (7) fails, the positive term \(J_{\mathbf1}\) in (4) is already infinite.

Conversely, if \(\lambda_{\max}(R)<2\), then
\[
R^{-1}\succ\tfrac12 I_n
\]
and also
\[
D_uR^{-1}D_u\succ\tfrac12 I_n
\]
for every sign vector \(u\). Thus
\[
A_u=R^{-1}+D_uR^{-1}D_u-I_n\succ0
\]
for every \(u\). Substitution of (6) into (4) proves (1) and the finiteness criterion.

## Consequences

### 1. Exact bivariate formula

For
\[
R_\rho=
\begin{pmatrix}
1&\rho\\
\rho&1
\end{pmatrix},
\qquad |\rho|<1,
\]
the two sign classes give
\[
J_+=\frac1{1-\rho^2},
\qquad
J_-=\frac1{1+\rho^2}.
\]
Therefore
\[
\boxed{
\exp D_2(P_\rho\|Q)
=
\frac12\left(\frac1{1-\rho^2}+\frac1{1+\rho^2}\right)
=
\frac1{1-\rho^4},
}
\]
or equivalently
\[
\boxed{
D_2(P_\rho\|Q)=-\log(1-\rho^4).
}
\tag{8}
\]
Since \(x\mapsto x^2\) is a bijection on \((0,\infty)\), the same formula applies to the pair \((X_1^2,X_2^2)\). This bivariate identity is consistent with the classical Lancaster/Kibble gamma expansion and is not claimed here as a standalone new fact.

Equation (8) shows the information loss caused by discarding Gaussian signs: near independence,
\[
D_2(P_\rho\|Q)=\rho^4+O(\rho^8),
\]
whereas for the signed Gaussian pair
\[
D_2(N(0,R_\rho)\|N(0,I_2))
=
-\log(1-\rho^2)
=
\rho^2+O(\rho^4).
\]

### 2. A high-dimensional \(L^2\) phase transition

For the equicorrelation matrix
\[
R_n(\rho)=(1-\rho)I_n+\rho\mathbf1\mathbf1^\top,
\qquad
-\frac1{n-1}<\rho<1,
\]
the largest eigenvalue equals \(1+(n-1)\rho\) when \(\rho\ge0\), and \(1-\rho\) when \(\rho<0\). Hence
\[
\boxed{
D_2(P_{R_n(\rho)}\|Q)<\infty
\quad\Longleftrightarrow\quad
-\frac1{n-1}<\rho<\frac1{n-1}.
}
\tag{9}
\]
For every \(n\ge3\), this creates an interior phase transition: positive equicorrelation remains a perfectly valid nonsingular Gaussian law for
\[
\frac1{n-1}\le\rho<1,
\]
but the Rényi-2 total correlation of its magnitudes is already infinite.

This is genuinely multivariate. Every bivariate marginal has finite Rényi-2 dependence whenever \(|\rho|<1\), while the joint Rényi-2 total correlation in (9) can be infinite.

For \(n=3\), the finite side also simplifies explicitly:
\[
\exp D_2(P_{R_3(\rho)}\|Q)
=
\frac{1}{4(1-\rho^2)\sqrt{1-4\rho^2}}
+
\frac{3}{4\sqrt{(1-\rho^2)(1+3\rho^2+4\rho^4)}},
\qquad
-\tfrac12<\rho<\tfrac12.
\tag{10}
\]

### 3. Sharp pairwise certificates

Rényi divergence obeys data processing. Projecting onto coordinates \(i,j\) and applying (8) gives
\[
\boxed{
D_2(P_R\|Q)
\ge
\max_{i<j}
\bigl[-\log(1-\rho_{ij}^4)\bigr].
}
\tag{11}
\]
This certificate is exact in dimension two. It also shows why pairwise information cannot detect the joint divergence in the equicorrelated phase (9): every right-hand side in (11) stays finite while the left-hand side can be \(+\infty\).

### 4. Comparison with the signed Gaussian

Let \(G_R=N(0,R)\) and \(G_0=N(0,I_n)\). In the same finite regime,
\[
D_2(G_R\|G_0)
=
-\frac12\log\!\left[\det R\,\det(2I_n-R)\right].
\tag{12}
\]
The folded likelihood ratio is the conditional expectation of the signed likelihood ratio given the magnitudes under \(G_0\). Conditional Jensen therefore gives
\[
D_2(P_R\|Q)\le D_2(G_R\|G_0).
\tag{13}
\]
If \(R\ne I_n\), the inequality is strict: equality in conditional Jensen would force the Gaussian likelihood ratio to be invariant under every coordinate sign flip, which forces all off-diagonal entries of \(R^{-1}\) to vanish, hence \(R=I_n\).

Notably, folding strictly reduces every finite nonzero Rényi-2 dependence value but does not enlarge its finiteness domain: both (1) and (12) are finite exactly when \(\lambda_{\max}(R)<2\).

## Relation to prior work

Ouimet and Greaves prove the strong Gaussian product inequality and derive an order-2 Rényi total-correlation lower certificate for Gaussian magnitudes. Their Corollary 4.11 uses a product moment as a test function and explicitly avoids direct evaluation of the joint density ratio. Formula (1) instead evaluates that ratio exactly and resolves when its square is integrable.

The sign-sum density representation used above is standard multivariate folded-normal theory; it appears in Chakraborty and Chatterjee (2013) and in later corrected/developed treatments, including Liu et al. (2023) and Benko, Hübnerová and Witkovský (2025). General properties of Rényi divergence, including data processing, are standard. Classical Lancaster theory and the canonical-correlation theory of bivariate gamma laws also cover the orthogonal-series mechanism behind the bivariate special case (8).

Targeted searches by the exact object, by folded/absolute-normal terminology, by Rényi and Pearson/chi-square divergence terminology, by total-correlation terminology, by the determinant form, and by the equicorrelation threshold did not locate a prior statement of the multivariate formula (1), the spectral criterion \(\lambda_{\max}(R)<2\), or the resulting joint-versus-pairwise phase transition. Originality is therefore claimed only to the best of our knowledge, and only for these multivariate statements rather than for the underlying folded density, Gaussian integral, data-processing principle, or bivariate Lancaster mechanism.

## Limitations

The result is restricted to centered Gaussian vectors with standardized marginal variances and order-2 Rényi divergence. Formula (1) contains \(2^n\) sign terms and is therefore not by itself a scalable high-dimensional numerical algorithm. No corresponding closed form is established here for general Rényi order, nonzero Gaussian means, non-Gaussian elliptical laws, or singular correlation matrices. The literature search cannot exclude an equivalent formulation in older multivariate Lancaster, Gaussian-sign-mixture, or folded-normal work.

## References

1. F. Ouimet and D. Greaves, *A proof of the strong Gaussian product inequality conjecture*, arXiv:2609.20234 (2026).
2. A. K. Chakraborty and M. Chatterjee, *On multivariate folded normal distribution*, Sankhya B 75 (2013), 1–15. DOI: 10.1007/s13571-013-0064-5.
3. X. Liu, Y. Jin, Y. Yang and X. Pan, *Properties and Estimations of a Multivariate Folded Normal Distribution*, Mathematics 11 (2023), 4860. DOI: 10.3390/math11234860.
4. M. Benko, Z. Hübnerová and V. Witkovský, *Characteristic function and moment generating function of multivariate folded normal distribution*, Statistical Papers (2025). DOI: 10.1007/s00362-025-01711-z.
5. T. van Erven and P. Harremoës, *Rényi Divergence and Kullback–Leibler Divergence*, IEEE Trans. Inform. Theory 60 (2014), 3797–3820. DOI: 10.1109/TIT.2014.2320500.
6. H. O. Lancaster, *The Structure of Bivariate Distributions*, Ann. Math. Statist. 29 (1958), 719–736. DOI: 10.1214/aoms/1177706532.
7. R. C. Griffiths, *The Canonical Correlation Coefficients of Bivariate Gamma Distributions*, Ann. Math. Statist. 40 (1969), 1401–1408. DOI: 10.1214/aoms/1177697511.
