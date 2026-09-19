# Rényi integrability spectrum of Gaussian magnitudes

## Result

Let `R` be an `n x n` positive-definite correlation matrix, let

\[
X\sim N(0,R),\qquad Y=(|X_1|,\ldots,|X_n|),
\]

and let `P_R` be the law of `Y`. Let `Q` be the product of the marginals of `P_R`; since the diagonal of `R` is one, `Q` is the product of `n` standard half-normal laws. For `gamma>1`, write

\[
D_\gamma(P_R\|Q)=\frac1{\gamma-1}\log\int
\left(\frac{dP_R}{dQ}\right)^\gamma dQ.
\]

The Rényi total correlation of the Gaussian magnitudes has a sharp spectral integrability threshold:

\[
\boxed{
D_\gamma(P_R\|Q)<\infty
\quad\Longleftrightarrow\quad
\lambda_{\max}(R)<\frac{\gamma}{\gamma-1}.
}
\]

Thus, if `R != I` and

\[
\gamma_c=\frac{\lambda_{\max}(R)}{\lambda_{\max}(R)-1},
\]

then `D_gamma(P_R||Q)` is finite exactly for `1<gamma<gamma_c` and is infinite for `gamma>=gamma_c`. If the largest eigenvalue has multiplicity `r`, then

\[
\boxed{
D_\gamma(P_R\|Q)
=-\frac{r(\lambda_{\max}(R)-1)}2\log(\gamma_c-\gamma)+O(1),
\qquad \gamma\uparrow\gamma_c.
}
\]

In particular, discarding all coordinate signs lowers Rényi divergence but does not improve its integrability range.

For every integer `m>=2` below the threshold, the divergence has an exact finite determinant formula. Let

\[
\mathcal G_n=\{\operatorname{diag}(1,s_2,\ldots,s_n):s_i\in\{-1,1\}\},
\qquad K=|\mathcal G_n|=2^{n-1}.
\]

Then

\[
\boxed{
\begin{aligned}
\exp\{(m-1)D_m(P_R\|Q)\}
={}&K^{1-m}|R|^{-m/2}\\
&\times\sum_{S_2,\ldots,S_m\in\mathcal G_n}
\det\!\left(
R^{-1}+\sum_{j=2}^m S_jR^{-1}S_j-(m-1)I
\right)^{-1/2}.
\end{aligned}
}
\]

The matrix inside every determinant is positive definite precisely in the finite regime. At order two this becomes

\[
\boxed{
 e^{D_2(P_R\|Q)}
 =K^{-1}|R|^{-1}
 \sum_{S\in\mathcal G_n}
 \det(R^{-1}+SR^{-1}S-I)^{-1/2}.
}
\]

There is also an exact Hermite--Wick decomposition at order two. Let `H_k` denote the probabilists' Hermite polynomial and, for a multi-index `k=(k_1,...,k_n)`, let `k! = product_i k_i!`. Whenever `lambda_max(R)<2`,

\[
\boxed{
 e^{D_2(P_R\|Q)}-1
 =\sum_{\substack{\boldsymbol{k}\in(2\mathbb N_0)^n\\
 \boldsymbol{k}\ne0}}
 \frac{\left(\mathbb E\prod_{i=1}^n H_{k_i}(X_i)\right)^2}{\boldsymbol{k}!}.
}
\]

Consequently,

\[
\boxed{
 e^{D_2(P_R\|Q)}-1
 \ge
 \sum_{i<j}\rho_{ij}^4
 +8\sum_{i<j<k}(\rho_{ij}\rho_{ik}\rho_{jk})^2.
}
\]

The first displayed sum is the complete fourth-order contribution and the triangle sum is the complete sixth-order contribution near independence. More explicitly, if `A` is a fixed symmetric matrix with zero diagonal and `R_epsilon=I+epsilon A`, then

\[
\boxed{
D_2(P_{R_\varepsilon}\|Q)
=\varepsilon^4\sum_{i<j}a_{ij}^4
+8\varepsilon^6\sum_{i<j<k}(a_{ij}a_{ik}a_{jk})^2
+O(\varepsilon^8).
}
\]

For a standard bivariate Gaussian pair with correlation `rho`, the Hermite series sums geometrically and gives the closed form

\[
\boxed{
D_2\bigl(\mathcal L(|X_1|,|X_2|)\,\|\,
\mathcal L(|X_1|)\otimes\mathcal L(|X_2|)\bigr)
=-\log(1-\rho^4),\qquad |\rho|<1.
}
\]

Thus the order-two dependence of weak Gaussian magnitudes starts at fourth order in correlation, not second order.

## Context

Ouimet and Greaves (2026) prove the strong Gaussian product inequality for arbitrary positive exponents. Their Corollary 6 introduces the order-two Rényi total correlation of Gaussian magnitudes and derives an explicit lower bound from a product-moment test function. The proof deliberately avoids direct evaluation of the folded joint density ratio. The formulas above evaluate that density ratio at integer Rényi orders, characterize its complete finiteness range for every real order greater than one, and give an orthogonal decomposition at order two.

For example, in the bivariate case and with the natural choice `alpha_1=alpha_2=2`, the source certificate gives

\[
D_2\ge \log(1+\rho^4/2),
\]

whereas the exact value is `-log(1-rho^4)`. Both have the correct quartic scale, but their leading constants differ by a factor of two for this test function.

For an equicorrelation matrix with nonnegative correlation `rho`,

\[
\lambda_{\max}=1+(n-1)\rho,
\]

so

\[
D_2(P_R\|Q)<\infty
\quad\Longleftrightarrow\quad
\rho<\frac1{n-1}.
\]

Thus in dimensions at least three, an ordinary nonsingular Gaussian vector can have infinite order-two total correlation after taking coordinatewise absolute values. More generally, its critical Rényi order is

\[
\gamma_c=1+\frac1{(n-1)\rho}.
\]

## Proof

Let `phi` be the `N(0,I)` law on `R^n`, and define the full Gaussian likelihood ratio

\[
L_R(x)=\frac{dN(0,R)}{dN(0,I)}(x)
=|R|^{-1/2}
\exp\left[-\frac12x^T(R^{-1}-I)x\right].
\]

Because a centered Gaussian density is invariant under global sign reversal, the density ratio of the magnitude law relative to the product half-normal law, extended evenly to `R^n`, is

\[
\bar L_R(x)=K^{-1}\sum_{S\in\mathcal G_n}L_R(Sx).
\]

Hence

\[
\exp\{(\gamma-1)D_\gamma(P_R\|Q)\}
=\mathbb E_\phi[\bar L_R(Z)^\gamma].
\]

For `gamma>1`, positivity and convexity give

\[
K^{1-\gamma}\mathbb E_\phi[L_R(Z)^\gamma]
\le
\mathbb E_\phi[\bar L_R(Z)^\gamma]
\le
\mathbb E_\phi[L_R(Z)^\gamma].
\]

The full Gaussian integral is

\[
\mathbb E_\phi[L_R(Z)^\gamma]
=|R|^{-\gamma/2}
\det\bigl(\gamma R^{-1}-(\gamma-1)I\bigr)^{-1/2}
\]

when the matrix in the determinant is positive definite, and is infinite otherwise. Its eigenvalues are

\[
\frac{\gamma}{\lambda_i(R)}-(\gamma-1),
\]

so finiteness is equivalent to

\[
\lambda_{\max}(R)<\frac\gamma{\gamma-1}.
\]

The two-sided comparison also yields

\[
D_\gamma(N(0,R)\|N(0,I))-(n-1)\log2
\le D_\gamma(P_R\|Q)
\le D_\gamma(N(0,R)\|N(0,I)),
\]

whenever the divergences are finite. This proves the exact threshold. If the top eigenvalue has multiplicity `r`, the determinant of `gamma R^{-1}-(gamma-1)I` has a factor asymptotic to `(gamma_c-gamma)^r`; the bounded divergence gap above then gives the stated logarithmic blow-up.

For integer `m`, expand `bar L_R^m`. After a common sign change one of the `m` sign matrices may be fixed to the identity. A Gaussian integral then gives

\[
\mathbb E_\phi\left[
L_R(Z)\prod_{j=2}^m L_R(S_jZ)
\right]
=|R|^{-m/2}
\det\left(
R^{-1}+\sum_{j=2}^mS_jR^{-1}S_j-(m-1)I
\right)^{-1/2},
\]

which proves the finite sign-determinant formula. If the spectral threshold holds, `R^{-1} > ((m-1)/m)I`, so every matrix in the sum is positive definite. If it fails, the all-equal-sign term already diverges.

For the order-two Hermite identity, assume `lambda_max(R)<2`. Then `L_R` is square-integrable under `phi`. The coordinatewise sign average is the orthogonal projection of `L_R` onto the subspace of functions even in every coordinate. The multivariate Hermite basis diagonalizes this projection: all terms with an odd coordinate degree vanish. Since

\[
\mathbb E_\phi[L_R(Z)\prod_iH_{k_i}(Z_i)]
=\mathbb E\prod_iH_{k_i}(X_i),
\]

Parseval's identity gives the displayed series after subtracting the constant term.

For `k_i=k_j=2` and all other entries zero,

\[
\mathbb E[H_2(X_i)H_2(X_j)]=2\rho_{ij}^2,
\]

which contributes `rho_ij^4`. For three coordinates with degree two,

\[
\mathbb E[H_2(X_i)H_2(X_j)H_2(X_k)]
=8\rho_{ij}\rho_{ik}\rho_{jk},
\]

which contributes `8(rho_ij rho_ik rho_jk)^2`. Orthogonality makes all omitted contributions nonnegative. For `R_epsilon=I+epsilon A`, these are respectively the complete degree-four and degree-six terms; analyticity of the determinant formula supplies the `O(epsilon^8)` remainder.

In the bivariate case, the classical Hermite identity

\[
\mathbb E[H_k(X_1)H_l(X_2)]
=\mathbf1_{\{k=l\}}k!\rho^k
\]

reduces the even Parseval series to

\[
e^{D_2}-1=\sum_{j\ge1}\rho^{4j}=\frac{\rho^4}{1-\rho^4},
\]

which proves the closed form.

## Verification

`artifacts/verify_gaussian_magnitude_renyi.py` evaluates the integer-order determinant formula directly. It checks the bivariate identity at several correlations, tests finite versus divergent integer orders on three-dimensional equicorrelation matrices, verifies convergence to the fourth- and sixth-order coefficients for a fixed perturbation matrix, and checks the pair-plus-triangle lower bound numerically. The corresponding output is recorded in `artifacts/verification_output.txt`.

The verification uses Python 3 and NumPy; it is numerical support for the exact analytic derivations above, not a substitute for them.

## Originality and relation to prior work

The strong Gaussian product inequality, its equality characterization, and the product-moment lower bound on order-two Rényi total correlation are due to Ouimet and Greaves (2026) and are not claimed here. Standard formulas for Rényi divergence between unfurled Gaussian measures, Gaussian likelihood integration, Hermite expansions, Wick identities, and finite-group averaging are also prior tools.

The multivariate folded-normal distribution has a substantial literature. Chakraborty and Chatterjee (2013) study its properties; Liu et al. (2023) study marginals, conditionals, independence and estimation; Benko, Hübnerová and Witkovský (2025) derive its characteristic and moment-generating functions. The accessible full text of the 2025 paper contains no Rényi-, Kullback--Leibler-, or entropy-divergence calculation. Tsagris, Beneki and Hassani (2014) study entropy and Kullback--Leibler quantities for the univariate folded normal, which is a different problem.

Searches for folded/multivariate folded normal Rényi divergence, chi-square divergence, Rényi mutual information, Gaussian magnitudes, and equivalent total-correlation terminology did not locate the spectral finiteness criterion, the integer sign-determinant formula, the bivariate identity `-log(1-rho^4)`, or the even-Hermite total-correlation decomposition. The originality claim is therefore limited to these folded-Gaussian dependence formulas and their stated consequences, to the best of our knowledge.

The full texts of Liu et al. (2023) and Chakraborty--Chatterjee (2013) were not fully inspected in this review. They are the most plausible residual literature risk because they study the same multivariate folded-normal family, although the accessible descriptions emphasize distributional properties rather than information divergences.

## Limitations

The main statements assume a positive-definite correlation matrix. Singular Gaussian laws are not analyzed here. Closed determinant formulas are given for integer Rényi orders; for noninteger orders the result characterizes finiteness and critical blow-up but does not provide a comparable finite determinant sum. The Hermite--Wick series and weak-dependence expansion are specialized to order two. No finite-sample statistical estimator or inference theorem is proposed.

## References

1. F. Ouimet and D. Greaves, *A proof of the strong Gaussian product inequality conjecture*, arXiv:2609.20234v1 (2026). https://arxiv.org/abs/2609.20234v1
2. M. Benko, Z. Hübnerová and V. Witkovský, *Characteristic function and moment generating function of multivariate folded normal distribution*, Statistical Papers 66, 96 (2025). https://doi.org/10.1007/s00362-025-01711-z
3. X. Liu, Y. Jin, Y. Yang and X. Pan, *Properties and Estimations of a Multivariate Folded Normal Distribution*, Mathematics 11 (2023), 4860. https://doi.org/10.3390/math11234860
4. A. K. Chakraborty and M. Chatterjee, *On multivariate folded normal distribution*, Sankhya B 75 (2013), 1--15. https://doi.org/10.1007/s13571-013-0064-5
5. M. Tsagris, C. Beneki and H. Hassani, *On the Folded Normal Distribution*, Mathematics 2 (2014), 12--28. https://doi.org/10.3390/math2010012
