# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The determinant identity follows directly from folding the Gaussian density over the coordinate-sign group. If \(L_R=f_R/\varphi_n\), then the folded likelihood ratio is the sign average \(2^{-n}\sum_sL_R(D_s y)\). Squaring, using sign symmetry of the standard Gaussian measure, and evaluating a quadratic Gaussian integral gives
\[
1+\chi^2(P_R\|Q)
=\frac{1}{2^n\det R}\sum_u
\det(R^{-1}+D_uR^{-1}D_u-I)^{-1/2}.
\]
The all-positive sign term is integrable if and only if \(2R^{-1}-I\succ0\), equivalently \(\lambda_{\max}(R)<2\). Under this condition every sign term is integrable because both \(R^{-1}\) and \(D_uR^{-1}D_u\) dominate \(I/2\). Thus the stated criterion is both necessary and sufficient.

The Hermite square-sum follows from the Kibble--Slepian/Wick expansion and Parseval. Coordinatewise folding annihilates terms with any odd vertex degree. A double edge is the unique two-edge Eulerian graph and yields \(\rho_{ij}^4\) after squaring and applying Hermite norms. A triangle is the unique three-edge Eulerian graph and yields \(8(\rho_{ij}\rho_{jk}\rho_{ki})^2\). All remaining square-sum terms start at total correlation degree eight. Since \(\chi^2=O(\|R-I\|_F^4)\), passing from \(\chi^2\) to \(D_2=\log(1+\chi^2)\) changes only order-eight and higher terms.

For normalized absolute moments, the identity
\[
\mathbb E[|Z|^\alpha H_{2m}(Z)]/\mathbb E|Z|^\alpha
=\prod_{r=0}^{m-1}(\alpha-2r)
\]
was checked algebraically from the Hermite polynomial and Gaussian absolute-moment recurrence. It makes the double-edge coefficient \(\alpha_i\alpha_j/2\) and the triangle coefficient \(\alpha_i\alpha_j\alpha_k\), giving the claimed local GPI expansion. The leading quadratic form is positive definite in the off-diagonal correlations for fixed positive exponents, so the stated local stability bound follows by continuity of the higher-order remainder.

The standalone verification reproduces the bivariate absolute-moment expansion against the classical hypergeometric formula to floating-point precision, checks the exact \((2,2,2)\) Wick identity, verifies \(\chi^2=\rho^4/(1-\rho^4)\) by direct bivariate integration, and matches the three-dimensional determinant formula with tensor Gauss--Hermite integration to approximately \(10^{-15}\) in the reported example.

## Originality

Ouimet--Greaves, arXiv:2609.20234, proves the strong Gaussian product inequality for all positive exponents and gives a Rényi-2 total-correlation lower-bound certificate based on normalized product moments. It does not directly evaluate the folded-Gaussian Rényi divergence. Hu--Zhao--Zhou (2023) gives quantitative two-dimensional Gaussian product inequalities and explicitly asks about higher-dimensional quantitative versions. Those results are prior art for quadratic stability in two dimensions.

The Hermite and diagrammatic methodology is classical and is not claimed as new. Ogasawara's Behaviormetrika article develops infinite-series formulas for untruncated Gaussian absolute product moments, including general multivariate cases; accordingly the all-orders absolute-moment series is used only as proof machinery here. Kamat (1953) is another older source on multivariate absolute Gaussian moments. The full Kamat article and the full published Behaviormetrika article were not inspected, so they remain concrete originality risks for any moment-series formulation.

For the Rényi side, recent multivariate folded-normal work by Benko--Hübnerová--Witkovský (2025) derives density-transform information and moment/characteristic-function formulas. The open article and surrounding literature were searched for Rényi divergence, chi-square divergence, total correlation, Hermite square-sums, and the bivariate expression \(-\log(1-\rho^4)\); no matching statement was located. Searches also did not locate the \(\lambda_{\max}(R)<2\) finiteness criterion or the finite sign-determinant sum for Gaussian magnitudes.

The originality assessment is therefore restricted, **to the best of our knowledge**, to the exact order-2 Rényi determinant formula and finiteness threshold for centered Gaussian magnitudes, its bivariate closed form, the quartic/squared-triangle local expansion, and the explicit contrast with the signed-triangle local geometry of strong-GPI product moments. No novelty is claimed for Kibble--Slepian/Mehler expansions, Wick calculus, general Gaussian absolute-moment series, or the already known qualitative strong GPI.

## Value

The result directly sharpens a consequence of the newly proved strong GPI: the divergence that previously appeared only through a moment-based lower-bound certificate can be evaluated exactly for Gaussian magnitudes. The spectral threshold shows that order-2 total correlation can diverge in dimensions three and above even for a nonsingular smooth Gaussian model. The local expansion explains how much dependence survives loss of all coordinate signs: pairwise information is suppressed from quadratic to quartic order, while triangle geometry changes from a signed cubic term in product moments to a squared sixth-order triangle term in Rényi dependence. The bivariate formula also quantitatively calibrates the source paper's certificate.

## Limitations

The determinant formula is specialized to centered Gaussian magnitudes, although arbitrary marginal scales reduce to the correlation-matrix case. The local expansions hold for fixed dimension near independence and no dimension-uniform remainder is asserted. The local GPI estimate is not a global quantitative strengthening of the strong GPI. Full texts of Kamat (1953) and the published Behaviormetrika version of Ogasawara's series paper were not inspected, so the review deliberately makes no novelty claim for general absolute-moment series. Independent audit has not been performed.
