# Sharp near-rank-one variance and normalization gain for four-matvec XTrace

## Finding

Fix an integer \(n\ge 2\), write \(d=n-1\), and let \(A_\varepsilon=\operatorname{diag}(1,\varepsilon,\ldots,\varepsilon)\in\mathbb R^{n\times n}\) for \(0<\varepsilon<1\). Apply the original two-test-vector, four-matrix-vector-product XTrace construction with independent standard Gaussian vectors. Let \(T_{\mathrm G}(\varepsilon)\) denote its ordinary (unnormalized residual Gaussian) trace estimate and \(T_{\mathrm N}(\varepsilon)\) its residual-direction-normalized version of Epperly--Tropp--Webber, using the same two test vectors and leave-one-out subspaces. Both estimates are unbiased for \(\operatorname{tr} A_\varepsilon=1+d\varepsilon\).

Define the positive dimension constant
\[
c_n=\frac{\sqrt\pi}{2}\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}.
\]
For every fixed \(n\), the **sharp nearly rank-one variances** are
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\operatorname{Var}T_{\mathrm G}(\varepsilon)}{\varepsilon}=c_n,\qquad
\lim_{\varepsilon\downarrow0}\frac{\operatorname{Var}T_{\mathrm N}(\varepsilon)}{\varepsilon}=\frac{n-2}{n+1}c_n.}
\]
For \(n\ge3\), normalization therefore retains exactly the fraction \((n-2)/(n+1)\) of the leading unnormalized variance. For \(n=2\), the normalized estimate equals the exact trace *for every realization and every* \(0<\varepsilon<1\), whereas \(\operatorname{Var}T_{\mathrm G}(\varepsilon)\sim\varepsilon/2\). In dimension three the respective leading coefficients are \(\pi/4\) and \(\pi/16\); in dimension four they are \(1\) and \(2/5\). This is a fixed-dimension asymptotic, not a claim uniform in growing dimension.

The mechanism also has an exact rare-sketch coefficient. If \(P_\varepsilon\) projects onto the line spanned by \(A_\varepsilon\omega\) for a fresh standard Gaussian \(\omega\), and \(B_\varepsilon=(I-P_\varepsilon)A_\varepsilon(I-P_\varepsilon)\), then for every fixed \(t\in(0,1)\),
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{\Pr\{\|B_\varepsilon\|_2>t\}}{\varepsilon}
=\frac{2\Gamma(n/2)}{\sqrt\pi\Gamma((n-1)/2)}\sqrt{\frac{1-t}{t}}.}
\]
Thus events of probability proportional to \(\varepsilon\), rather than typical residuals of size proportional to \(\varepsilon\), determine both leading variances. The leading variance of the posterior sample-variance proxy formed from the two constituent XTrace estimates is equal to the corresponding actual variance, although not claimed exactly equal at fixed positive \(\varepsilon\).

## Assumptions and scope

For \(i\in\{1,2\}\), take \(\omega_i\sim N(0,I_n)\) independently, set \(q_i=A_\varepsilon\omega_i/\|A_\varepsilon\omega_i\|_2\), and let \(P_i=q_iq_i^{\mathsf T}\). All denominators are nonzero almost surely. With \(j=3-i\), put \(B_j=(I-P_j)A_\varepsilon(I-P_j)\) and \(\mu_i=(I-P_j)\omega_i\). Define
\[
Z_{\mathrm G,i}=\operatorname{tr}(P_jA_\varepsilon)+\omega_i^{\mathsf T}B_j\omega_i,
\qquad
Z_{\mathrm N,i}=\operatorname{tr}(P_jA_\varepsilon)
+d\frac{\mu_i^{\mathsf T}A_\varepsilon\mu_i}{\|\mu_i\|_2^2}.
\]
Then \(T_{\mathrm G}=(Z_{\mathrm G,1}+Z_{\mathrm G,2})/2\) and \(T_{\mathrm N}=(Z_{\mathrm N,1}+Z_{\mathrm N,2})/2\). These are exactly the standard XTrace leave-one-out formula and its published residual normalization for two test columns, requiring four applications of the matrix in the standard general-matrix implementation. The matrix is treated as an implicit operator and its special diagonal form is used for analysis, not to alter the estimator. For \(n\ge5\), the four-matvec budget is below the matrix dimension.

All statements concern real Gaussian samples, exact arithmetic, one eigenvalue equal to one, an isotropic small-eigenvalue tail, and the limit \(\varepsilon\downarrow0\) with \(n\) fixed. The symbols \(\operatorname{Var}\) and \(\Pr\) refer solely to the two independent Gaussian test vectors.

## Proof

**1. Unbiasedness and one-sketch geometry.** Conditional on \(\omega_j\), the complementary subspace has dimension \(d\). A standard Gaussian projected into it has conditional covariance \(I-P_j\); after dividing by its length, the direction is uniform on the unit sphere in that subspace. Therefore
\[
\mathbb E[\omega_i^{\mathsf T}B_j\omega_i\mid\omega_j]=\operatorname{tr}B_j,
\quad
\mathbb E\!\left[d\frac{\mu_i^{\mathsf T}A_\varepsilon\mu_i}{\|\mu_i\|_2^2}\,\middle|\,\omega_j\right]=\operatorname{tr}B_j.
\]
As \(\operatorname{tr}(P_jA_\varepsilon)+\operatorname{tr}B_j=\operatorname{tr}A_\varepsilon\), both basic estimators and their averages are unbiased.

Write \(\omega_j=(X,Y)\) with \(X\sim N(0,1)\) and \(Y\sim N(0,I_d)\) independent; let \(R=\|Y\|_2\). The missed leading-eigenvector energy is
\[
H_\varepsilon=\|(I-P_j)e_1\|_2^2
=\frac{\varepsilon^2R^2}{X^2+\varepsilon^2R^2}.
\]
Since \(A_\varepsilon=\varepsilon I+(1-\varepsilon)e_1e_1^{\mathsf T}\),
\[
B_j=\varepsilon(I-P_j)+(1-\varepsilon)vv^{\mathsf T},
\quad v=(I-P_j)e_1,\quad\|v\|_2^2=H_\varepsilon.
\]
On the \(d\)-dimensional complementary subspace, its eigenvalues are \(S_\varepsilon=\varepsilon+(1-\varepsilon)H_\varepsilon\) once and \(\varepsilon\) with multiplicity \(d-1\). Thus \(\|B_j\|_2=S_\varepsilon\).

**2. Exact conditional variances.** Gaussian quadratic-form covariance and the fourth moment of a uniformly spherical unit direction give
\[
\operatorname{Var}(Z_{\mathrm G,i}\mid\omega_j)
=2\operatorname{tr}(B_j^2)=2\bigl(S_\varepsilon^2+(d-1)\varepsilon^2\bigr),
\]
\[
\operatorname{Var}(Z_{\mathrm N,i}\mid\omega_j)
=\frac{2}{d+2}\bigl(d\operatorname{tr}(B_j^2)-(\operatorname{tr}B_j)^2\bigr)
=\frac{2(d-1)}{d+2}(1-\varepsilon)^2H_\varepsilon^2.
\]
For \(d=1\), this last conditional variance is zero and the normalized basic estimator is identically the trace, proving the exact dimension-two statement.

**3. Exact singular moment coefficient.** The density of \(X\) is \(\phi(x)=(2\pi)^{-1/2}e^{-x^2/2}\). Conditional on \(R=r>0\), substitute \(x=\varepsilon r u\) to obtain
\[
\frac{\mathbb E[H_\varepsilon^2\mid R=r]}{\varepsilon}
=r\int_{\mathbb R}\frac{\phi(\varepsilon r u)}{(1+u^2)^2}\,du
\longrightarrow\frac{\pi r}{2\sqrt{2\pi}}.
\]
The integrand is bounded by \(r\phi(0)(1+u^2)^{-2}\), integrable after averaging over the chi-distributed \(R\). Hence dominated convergence applies and, since \(\mathbb E R=\sqrt2\Gamma((d+1)/2)/\Gamma(d/2)\),
\[
\mathbb E H_\varepsilon^2=c_n\varepsilon+o(\varepsilon).
\]
The corresponding first-moment substitution with denominator \(1+u^2\) proves \(\mathbb E H_\varepsilon=O_n(\varepsilon)\), so \(\mathbb E S_\varepsilon=O_n(\varepsilon)\) and \(\mathbb E S_\varepsilon^2=c_n\varepsilon+o(\varepsilon)\).

**4. Leave-one-out dependence does not change the leading coefficient.** Let \(D_{\mathrm G,i}=Z_{\mathrm G,i}-\operatorname{tr}A_\varepsilon\) and similarly \(D_{\mathrm N,i}\). Pointwise,
\[
|D_{\mathrm G,1}D_{\mathrm G,2}|
\le (\|\omega_1\|_2^2+d)(\|\omega_2\|_2^2+d)
\|B_1\|_2\|B_2\|_2.
\]
Each \(B_i\) depends only on the *direction* of \(\omega_i\), which is independent of its Gaussian radial norm. Independence across \(i\) therefore bounds the expectation on the right by
\[
\bigl[(n+d)\mathbb E S_\varepsilon\bigr]^2=O_n(\varepsilon^2).
\]
For normalized residuals, \(|D_{\mathrm N,i}|\le2d\|B_j\|_2\), hence also \(|\mathbb E D_{\mathrm N,1}D_{\mathrm N,2}|=O_n(\varepsilon^2)\). Thus, for each method, the variance of the mean of two constituent estimates is half the variance of one, up to an additive \(O_n(\varepsilon^2)\). Averaging the exact conditional variances of step 2 and invoking step 3 gives the two stated limits. The same covariance estimate, together with the elementary identity for the sample-variance proxy, establishes its leading-order agreement with actual variance.

**5. Rare-event coefficient.** For fixed \(0<t<1\), the event \(H_\varepsilon>t\) is exactly
\[
|X|<\varepsilon R\sqrt{(1-t)/t}.
\]
Apply dominated convergence to the Gaussian small-interval probability divided by \(\varepsilon\), then average over \(R\). This gives the displayed coefficient for \(H_\varepsilon\); replacing \(H_\varepsilon\) by \(S_\varepsilon=\varepsilon+(1-\varepsilon)H_\varepsilon\) preserves that limit at fixed \(t\).

## Verification

The supplementary `verify.py` calculates the exact single-basic-estimator conditional variances by one-dimensional beta-density quadrature (including its integrable endpoint), checks sharp coefficients for dimensions \(2,3,4,6\), verifies the rare-event probability coefficient, and independently implements the original two-probe XTrace formulas by direct vector projection. Six seeded Monte Carlo configurations use 600,000 pairs each. The file `verification_output.txt` records actual successful output; instructions and dependencies appear in `requirements.txt`. These calculations test the formulas but do not substitute for the preceding proof of infinite-probability or limiting assertions.

## Relationship to prior work

The XTrace algorithm, its exchangeable leave-one-out trace estimator, Gaussian unbiasedness, and recommended projected-residual normalization are due to Epperly, Tropp, and Webber (2023 preprint; 2024 journal version). Their variance results give general bounds and their normalization comparison is qualitative/numerical; the present theorem gives sharp leading constants for a singular fixed-dimension spectral family, an explicit comparison of normalized and ordinary versions, and a rare-event coefficient. Hallman (2025) analyzes rotational symmetrization and extended Krylov-space variants of XTrace, rather than the stated near-rank-one two-probe variance limits. Hallman (2024) studies tail extremality for the *ordinary* Gaussian quadratic-form trace estimator, not leave-one-out XTrace. The general fourth-moment identities, Gaussian radial/angular independence, and beta/chi identities used here are classical and are not claimed new.

## Limitations

The statement does not establish optimality among all four-matvec trace estimators, any general advantage over non-Gaussian probing, or a high-dimensional joint limit. Four generic matvecs can already determine a matrix of size at most four, although the theorem remains mathematically valid in those sizes; the nontrivial below-dimension-budget cases start at \(n\ge5\). The spiked form is a natural test of the low-rank spectral-decay regime but is not claimed representative of arbitrary spectra. Normalization is a variant already proposed in the source article, not a new algorithm. Possible equivalent singular-asymptotic calculations elsewhere remain a literature risk.

## References

1. E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825, first submitted 2023-01-19; SIAM Journal on Matrix Analysis and Applications 45 (2024), 1--23, doi:10.1137/23M1548323. In particular, §§1.2.1, 2.3, 3.1, and 5.1.
2. E. Hallman, *Two Variations on the XTrace Algorithm*, arXiv:2512.02316 (2025), §§1, 3--5.
3. E. Hallman, *Extremal Bounds for Gaussian Trace Estimation*, arXiv:2411.15454 (2024), §§1--2.
4. R. A. Meyer, C. Musco, C. Musco, and D. P. Woodruff, *Hutch++: Optimal Stochastic Trace Estimation*, arXiv:2010.09649 (2020), background on trace-variance reduction.
