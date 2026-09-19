# Exact Rényi-2 dependence of Gaussian magnitudes and local GPI geometry

## Result

Let \(R=(\rho_{ij})_{1\le i,j\le n}\) be a positive-definite correlation matrix, let
\[
X\sim N(0,R),\qquad Y=(|X_1|,\ldots,|X_n|),
\]
and write \(P_R\) for the law of \(Y\). Let \(Q\) be the product of the marginals of \(P_R\), equivalently the product of \(n\) standard half-normal laws. The order-2 Rényi total correlation is
\[
D_2(P_R\|Q)=\log\int \left(\frac{dP_R}{dQ}\right)^2dQ.
\]

The following exact formula holds. For \(u\in\{-1,1\}^n\), let \(D_u=\operatorname{diag}(u_1,\ldots,u_n)\) and
\[
M_u=R^{-1}+D_uR^{-1}D_u-I.
\]
Then
\[
\boxed{
D_2(P_R\|Q)<\infty\quad\Longleftrightarrow\quad \lambda_{\max}(R)<2.
}
\]
In this finite regime,
\[
\boxed{
D_2(P_R\|Q)
=\log\left[
\frac{1}{2^n\det R}
\sum_{u\in\{-1,1\}^n}
\det(M_u)^{-1/2}
\right].
}
\]
Thus a quantity introduced recently as a lower-bound target for the strong Gaussian product inequality has an explicit finite determinant representation for the Gaussian-magnitude model. The formula also identifies the exact integrability threshold of the order-2 total correlation.

For \(n=2\), if \(\rho=\rho_{12}\), the determinant sum simplifies for every \(|\rho|<1\) to
\[
\boxed{
D_2(P_\rho\|Q)=-\log(1-\rho^4),
\qquad
\chi^2(P_\rho\|Q)=\frac{\rho^4}{1-\rho^4}.
}
\]

There is also an exact Hermite square-sum representation. For a symmetric array of nonnegative integers \(m=(m_{ij})_{i<j}\), define vertex degrees
\[
d_i(m)=\sum_{j\ne i}m_{ij}.
\]
For an even degree vector \(d=(d_1,\ldots,d_n)\in(2\mathbb N_0)^n\), set
\[
A_d(R)=
\sum_{m:\,d(m)=d}
\prod_{i<j}\frac{\rho_{ij}^{m_{ij}}}{m_{ij}!}.
\]
Whenever \(\lambda_{\max}(R)<2\),
\[
\boxed{
\chi^2(P_R\|Q)
=
\sum_{\substack{d\in(2\mathbb N_0)^n\\d\ne0}}
\left(\prod_{i=1}^n d_i!\right)A_d(R)^2.
}
\]
Consequently, as \(R\to I\),
\[
\boxed{
D_2(P_R\|Q)
=
\sum_{i<j}\rho_{ij}^4
+8\sum_{i<j<k}(\rho_{ij}\rho_{jk}\rho_{ki})^2
+O_n(\|R-I\|_F^8).
}
\]
The first dependence information retained by componentwise absolute values is therefore quartic in the correlations; the first closed-loop correction is a squared triangle term of order six.

The same Hermite organization gives a local quantitative form of the strong Gaussian product inequality. For fixed \(\alpha_1,\ldots,\alpha_n>0\), define
\[
M_R(\alpha)=
\frac{\mathbb E_R\prod_i|X_i|^{\alpha_i}}
{\prod_i\mathbb E|Z|^{\alpha_i}},\qquad Z\sim N(0,1).
\]
Then, locally around independence,
\[
\boxed{
M_R(\alpha)
=1+\frac12\sum_{i<j}\alpha_i\alpha_j\rho_{ij}^2
+\sum_{i<j<k}\alpha_i\alpha_j\alpha_k
\rho_{ij}\rho_{jk}\rho_{ki}
+O_{\alpha,n}(\|R-I\|_F^4).
}
\]
In particular,
\[
M_R(\alpha)-1
=\frac12\sum_{i<j}\alpha_i\alpha_j\rho_{ij}^2
+O_{\alpha,n}(\|R-I\|_F^3),
\]
so independence is a locally quadratically stable minimizer. If \(a_*=\min_i\alpha_i\), there exists \(\delta_{\alpha,n}>0\) such that
\[
\boxed{
\|R-I\|_F\le\delta_{\alpha,n}
\quad\Longrightarrow\quad
M_R(\alpha)-1\ge \frac{a_*^2}{8}\|R-I\|_F^2.
}
\]
The cubic term records signed triangle geometry, in contrast with the squared-triangle term in Rényi-2 dependence.

## Proof

Let \(\varphi_n\) be the standard product Gaussian density on \(\mathbb R^n\), \(f_R\) the density of \(N(0,R)\), and
\[
L_R(x)=\frac{f_R(x)}{\varphi_n(x)}.
\]
For \(y\in(0,\infty)^n\), folding over all coordinate signs gives
\[
\frac{dP_R}{dQ}(y)
=2^{-n}\sum_{s\in\{-1,1\}^n}L_R(D_sy).
\]
Because a function of \(|Z|\), \(Z\sim N(0,I)\), has the same expectation under the product half-normal law as under \(\varphi_n\), expanding the square and changing signs yields
\[
1+\chi^2(P_R\|Q)
=2^{-n}\sum_{u\in\{-1,1\}^n}J_u,
\]
where
\[
J_u=\mathbb E_{Z\sim N(0,I)}[L_R(Z)L_R(D_uZ)].
\]
A Gaussian integral gives
\[
J_u
=(\det R)^{-1}\det(R^{-1}+D_uR^{-1}D_u-I)^{-1/2}
\]
when the matrix in the determinant is positive definite, and \(J_u=+\infty\) otherwise. The term \(u=(1,\ldots,1)\) is finite exactly when
\[
2R^{-1}-I\succ0,
\]
which is equivalent to \(\lambda_{\max}(R)<2\). Conversely, under this condition \(R^{-1}\succ I/2\), so every \(M_u\succ0\). This proves both the integrability criterion and the determinant formula.

For the Hermite representation, expand \(L_R\) in the product probabilists' Hermite basis. Wick's formula gives the coefficient of \(\prod_iH_{d_i}(x_i)\) as
\[
\sum_{m:\,d(m)=d}\prod_{i<j}\frac{\rho_{ij}^{m_{ij}}}{m_{ij}!}.
\]
Folding averages over coordinate signs and deletes every term with an odd vertex degree. Even Hermites remain orthogonal under the half-normal law, with
\[
\mathbb E[H_{2r}(|Z|)H_{2s}(|Z|)]=(2r)!\,\mathbf 1_{r=s}.
\]
Parseval therefore gives the square-sum formula. The degree-two Eulerian multigraphs are double edges, contributing \(\rho_{ij}^4\); the degree-three Eulerian multigraphs are triangles, contributing \(8(\rho_{ij}\rho_{jk}\rho_{ki})^2\). All remaining terms start at degree eight after squaring. Since \(\log(1+x)=x+O(x^2)\) and \(\chi^2=O(\|R-I\|_F^4)\), the stated expansion for \(D_2\) follows.

For the product moments, the one-dimensional normalized Hermite coefficient is
\[
\frac{\mathbb E[|Z|^\alpha H_{2r}(Z)]}{\mathbb E|Z|^\alpha}
=\prod_{q=0}^{r-1}(\alpha-2q),
\]
while all odd coefficients vanish. Applying the same multigraph expansion, a double edge gives \(\tfrac12\alpha_i\alpha_j\rho_{ij}^2\) and a triangle gives \(\alpha_i\alpha_j\alpha_k\rho_{ij}\rho_{jk}\rho_{ki}\). This yields the local expansion. The leading quadratic form is at least
\[
\frac{a_*^2}{2}\sum_{i<j}\rho_{ij}^2
=\frac{a_*^2}{4}\|R-I\|_F^2,
\]
and the higher-order terms are \(o(\|R-I\|_F^2)\), giving the displayed local lower bound after shrinking the neighborhood.

## Calibration against the recent Rényi certificate

Ouimet and Greaves proved the strong GPI for all positive exponents and, as a consequence, introduced a Rényi-2 total-correlation certificate based on the normalized product-moment excess. The determinant formula above directly evaluates the target divergence for Gaussian magnitudes instead of lower-bounding it through a test moment.

For a bivariate standard Gaussian pair and the choice \(\alpha_1=\alpha_2=2\),
\[
M_R(2,2)=1+2\rho^2.
\]
The Cauchy--Schwarz certificate in that result gives
\[
D_2(P_\rho\|Q)\ge \log(1+\rho^4/2),
\]
whereas the exact value is
\[
D_2(P_\rho\|Q)=-\log(1-\rho^4).
\]
Thus this particular moment certificate captures one half of the exact leading quartic coefficient near independence.

## Relation to prior work and originality boundary

The strong GPI itself, its equality case, and its Rényi total-correlation certificate are due to Ouimet and Greaves. Quantitative bivariate Gaussian product inequalities were already obtained by Hu, Zhao and Zhou; in several exponent regimes their bound has the correct quadratic tangent at independence, and their paper explicitly asks for quantitative higher-dimensional extensions. The Kibble--Slepian/Mehler Hermite expansion and Wick diagrammatics are classical. Ogasawara has developed general infinite-series formulas for Gaussian absolute product moments, so the all-orders moment graph series used here is not claimed as new. Multivariate folded-normal densities, moments and transforms have also been studied extensively, including recent work by Benko, Hübnerová and Witkovský.

The originality claim is restricted to the following combination, to the best of our knowledge: the exact determinant expression and exact \(\lambda_{\max}(R)<2\) finiteness criterion for Rényi-2 total correlation of centered Gaussian magnitudes; the bivariate closed form \(-\log(1-\rho^4)\); the resulting quartic/squared-triangle local expansion; and the explicit comparison with the local quadratic/signed-triangle geometry of the strong-GPI product-moment excess. Searches of the current strong-GPI paper and folded-normal literature did not locate these statements.

Two older sources remain concrete originality risks for the moment-expansion side rather than the Rényi formula itself. Kamat's 1953 paper on incomplete and absolute multivariate-normal moments was identifiable bibliographically but its full article was not inspected. Ogasawara's 2025/2026 Behaviormetrika article explicitly contains general infinite series for Gaussian product absolute moments, but its full published text was not inspected here. Accordingly no novelty is claimed for the underlying absolute-moment series.

## Limitations

The exact determinant formula concerns centered Gaussian vectors with unit marginal variances; arbitrary positive marginal scales reduce to this case because Rényi divergence is invariant under coordinatewise invertible scaling. For \(n\ge3\), the order-2 total correlation can be infinite even though all densities are positive and smooth; this happens exactly when \(\lambda_{\max}(R)\ge2\). The local expansions are for fixed dimension and fixed positive exponents as \(R\to I\); no dimension-uniform remainder is asserted. The local GPI bound is not a global quantitative strengthening of the newly proved strong GPI.

## Verification

`artifacts/verify_gaussian_magnitudes.py` performs independent numerical and symbolic checks. It compares the bivariate Hermite graph series with the classical hypergeometric formula for absolute Gaussian moments, verifies the \((2,2,2)\) three-variable Wick polynomial, compares the bivariate closed-form chi-square divergence against direct numerical integration, and compares the three-dimensional determinant formula against tensor Gauss--Hermite integration. The corresponding numerical output is in `artifacts/verification.txt`.

## References

1. F. Ouimet and D. Greaves, *A proof of the strong Gaussian product inequality conjecture*, arXiv:2609.20234 (2026).
2. Z.-C. Hu, H. Zhao and Q.-Q. Zhou, *Quantitative versions of the two-dimensional Gaussian product inequalities*, Journal of Inequalities and Applications 2023:2 (2023), DOI 10.1186/s13660-022-02906-w.
3. H. Ogasawara, *Series formulas for the untruncated Gaussian product moments*, Behaviormetrika 53 (2026), DOI 10.1007/s41237-025-00277-2.
4. M. Benko, Z. Hübnerová and V. Witkovský, *Characteristic function and moment generating function of multivariate folded normal distribution*, Statistical Papers 66:96 (2025), DOI 10.1007/s00362-025-01711-z.
5. A. R. Kamat, *Incomplete and absolute moments of the multivariate normal distribution with some applications*, Biometrika 40 (1953), 20--34, DOI 10.1093/biomet/40.1-2.20.
