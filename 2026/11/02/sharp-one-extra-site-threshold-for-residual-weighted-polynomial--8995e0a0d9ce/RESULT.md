# Sharp one-extra-site threshold for residual-weighted polynomial stencil selection

## Finding

Let \(\mathcal P\) be a real polynomial space of dimension \(m\ge1\), and let every \(m\)-point subset of the distinct sample set \(X\) be unisolvent for \(\mathcal P\). Each candidate stencil has exactly \(m\) nodes and is assigned the mean absolute error of its polynomial interpolant at non-stencil sample nodes, as in residual-weighted multinode Shepard interpolation. **At \(m+1\) total nodes, the residual indicators cannot reverse the relative preference of any two candidate deletion stencils as data vary. At \(m+2\) nodes, there are two legal neighboring stencils and one-site evaluation sets for which data can reverse that preference completely.** Thus \(m+2\) is the exact smallest sample count permitting two-sided discrimination by this residual-indicator construction; this is an algebraic possibility threshold, not a guarantee of detection for every geometry or jump.

For \(m+1\) nodes there is a unique, up to scale, nonzero vector \(w\) in the left kernel of the evaluation matrix, and every coordinate of \(w\) is nonzero. For the stencil omitting site \(j\), with its one available indicator site \(j\), the residual is exactly
\[
r_j(f)=\frac{w^\top f}{w_j},\qquad I_j(f)=\frac{|w^\top f|}{|w_j|}.
\]
Consequently all indicator ratios and their ranking are fixed by node geometry whenever \(w^\top f\ne0\). When \(w^\top f=0\), all vanish together.

The obstruction is exact, not merely asymptotic, on a uniform one-dimensional grid. Let \(d\ge1\), \(x_j=jh\) for \(0\le j\le d+1\), and use degree-\(d\) interpolants on the two endpoint stencils \(\{x_0,\ldots,x_d\}\) and \(\{x_1,\ldots,x_{d+1}\}\), checking residuals at their respective omitted endpoints. For every sample vector \(f\), the two absolute residuals are equal. Any inverse-indicator reweighting with \(\epsilon>0\) and exponent \(t>0\) therefore produces **exactly the original, data-independent geometric blend**.

More concretely, take the jump samples \(f_0=\cdots=f_d=0\), \(f_{d+1}=1\). For the two-stencil compact multinode Shepard blend, with geometric exponent \(\mu>0\), both support radii \(R=(d+1)h\), and evaluation at \(x=h/2\), the adapted output is exactly
\[
\widetilde K[f](h/2)=\frac{(-1)^d\binom{2d}{d}}{4^d\,[1+(2d+1)^{2\mu}]}.
\]
This is nonzero independently of \(h\), \(\epsilon\), and \(t\), although the true step function is zero at that evaluation point. The example concerns this explicitly specified two-stencil local blend; it does not claim a failure of the larger automatically selected stencil families used in the motivating paper.

## Assumptions and scope

The abstract result concerns a sample set of cardinality \(n\), an \(m\)-dimensional real polynomial space, and *full-spark evaluation*: every set of \(m\) evaluation rows is linearly independent. Each indicator in the minimal designs uses a single outside point; for the \(n=m+1\) design, this is forced. Indicators are absolute polynomial interpolation residuals. Normalized data-dependent weights have the form \(B_j(x)\propto W_j(x)/(\epsilon+I_j)^t\), with positive geometric weights at a jointly active evaluation point, \(\epsilon>0\), and \(t>0\).

The explicit compact formula uses the paper's factorwise truncated inverse-distance weights and radius \(R=\operatorname{diam}(S_j)+h=(d+1)h\). Here \(h>0\) is the uniform node spacing (also a valid strict upper bound on fill distance for an appropriate short interval domain containing the nodes). Only the two indicated stencils are included. The indicator evaluation sets are the singleton opposite endpoints. It is a local scaled configuration; it is not claimed to be the globally selected configuration on a fixed-domain mesh sequence.

## Proof

**Rank-one obstruction.** Write \(V\in\mathbb R^{(m+1)\times m}\) for the evaluation matrix of a basis of \(\mathcal P\). Full spark implies \(\operatorname{rank}V=m\), so \(\ker(V^\top)\) is one-dimensional. Let \(0\ne w\in\ker(V^\top)\). If \(w_j=0\), the other \(m\) rows are linearly dependent, contradicting full spark. Given data \(f\), let \(p_j\) interpolate all samples except the \(j\)-th one. The vector \(f-Vp_j\) is supported only at index \(j\); taking its inner product with \(w\) gives \(w^\top f=w_j(f_j-p_j(x_j))\), proving the displayed formula. For any two such stencils, \(I_j/I_k=|w_k|/|w_j|\) whenever the numerator is nonzero. Thus neither strict indicator ranking can reverse with data; when the numerator vanishes, both indicators are zero.

**Minimal sufficiency of one more site.** At \(n=m+2\) full-spark sites, index them \(x_0,\ldots,x_{m+1}\). Choose the stencils \(S_L=\{x_0,\ldots,x_{m-1}\}\) and \(S_R=\{x_1,\ldots,x_m\}\), and evaluate their residuals at \(x_m\) and \(x_{m+1}\), respectively. The data vector supported only at \(x_{m+1}\) gives \((I_L,I_R)=(0,1)\). For the vector supported only at \(x_0\), \(I_R=0\), whereas \(I_L=|\ell_0(x_m)|>0\), where \(\ell_0\) is the cardinal basis polynomial at \(x_0\) for \(S_L\). Indeed, if \(\ell_0(x_m)=0\), then the nonzero polynomial \(\ell_0\) would vanish at all \(m\) sites \(x_1,\ldots,x_m\), contradicting full spark. Hence the opposite indicator preferences are both realizable. For \(n\le m\), an \(m\)-node stencil with a nonempty outside-point indicator is impossible, and the \(n=m+1\) obstruction proves minimality. Additional nodes may be ignored for an existence construction.

**Uniform-grid cancellation.** In one dimension, the unique left-null evaluation vector is proportional to the classical barycentric weights
\[
w_j=\left(\prod_{k\ne j}(x_j-x_k)\right)^{-1}.
\]
For the equally spaced \(d+2\) sites, \(|w_0|=|w_{d+1}|\). Thus the residual indicators of the two endpoint stencils are equal for all \(f\), including data with zero divided difference. Their common inverse-indicator factor cancels exactly on normalization for every positive \(\epsilon,t\).

**Exact jump response.** For the displayed step data, the left interpolant is identically zero, while the right interpolant equals the cardinal basis polynomial of its final node. Its residual at the omitted left node has absolute value one, just as the left interpolant's residual at the omitted right node; hence \(I_L=I_R=1\). At \(x=h/2\), direct Lagrange multiplication gives
\[
p_R(h/2)=\prod_{k=1}^{d}\frac{\frac12-k}{d+1-k}
=(-1)^d\frac{\binom{2d}{d}}{4^d}.
\]
The compact geometric stencil numerators share all factors corresponding to nodes \(x_1,\ldots,x_d\), so their ratio is
\[
\frac{W_R(h/2)}{W_L(h/2)}
=\left[\frac{(d+\frac12)^{-1}-(d+1)^{-1}}{(\frac12)^{-1}-(d+1)^{-1}}\right]^\mu
=(2d+1)^{-2\mu}.
\]
Both supports are active because the farthest site from \(h/2\) is at distance \((d+\frac12)h<R\). Equal indicators imply the nonlinear right-stencil share is \(1/[1+(2d+1)^{2\mu}]\). Multiplication by \(p_R(h/2)\) proves the exact response.

**Uniform-grid sharpness at \(d+3\) sites.** With stencils on indices \(0,\ldots,d\) and \(1,\ldots,d+1\), their outside-point indicators at indices \(d+1\) and \(d+2\) evaluate to \((1,0)\) for data supported only at index \(0\), and \((0,1)\) for data supported only at index \(d+2\). The first extrapolation coefficient has absolute value one because the uniform-grid endpoint Lagrange cardinal value at the next site is \((-1)^d\). For any positive base weights, normalized inverse-indicator weighting can favor either stencil arbitrarily strongly as \(\epsilon\downarrow0\).

## Verification

Run `python3 verify.py` with Python 3 standard library. The checker tests exact barycentric/nullspace identities on nonuniform rational nodes through degree eight; exact equality of both residual indicators, compact geometric weight ratios and the jump response through degree eleven with several exponents and regularizers; and opposite endpoint-impulse preferences at \(d+3\) nodes. All identities use `fractions.Fraction`, not floating approximations. It reports 573 exact-rational checks. The general multivariate full-spark assertion follows from the proof, not from finite testing.

## Relationship to prior work

Dell'Accio, Di Tommaso, Larosa, Ruiz-Álvarez, and Yáñez (arXiv:2610.31026v1, first public October 22, 2026) introduce the residual indicator, establish smooth-region rates and conditional separation near jumps, and give a two-dimensional undetected-straddling-stencil example (Definition 4.1 and Remark 5.6). They use larger neighborhoods in their actual implementation. Their statements do not give this full-spark rank-one obstruction, sharp \(m+2\) two-sided discrimination threshold or the exact local compact-weight jump profile. Levin et al. (2025) use auxiliary least-squares residuals, not the single-outside-point interpolation residual design. Classical barycentric identities supply the basic left-nullspace tool; no novelty is claimed for that identity itself. The contribution is the combined sharp design classification and its exact consequence for nonlinear normalized stencil weighting.

## Limitations

This is an algebraic *possibility* threshold; \(m+2\) sites do not automatically guarantee successful jump separation for every geometry, evaluator or data configuration. The rank-one obstruction requires all candidate stencils to use the same \(m+1\) nodes with exactly one excluded point. The explicit compact formula requires the stated two-stencil family and support radii. It does not imply instability or failure of the full, automatically selected multidimensional algorithm, nor does it address other smoothness indicators such as Jiang–Shu derivative energies. A broader older theorem about leave-one-out interpolation residual rank could imply parts of the formulation; exhaustive historical priority is not established.

## References

1. F. Dell'Accio, F. Di Tommaso, F. Larosa, J. Ruiz-Álvarez and D. F. Yáñez, *Data-dependent Compact Multinode Shepard Method*, arXiv:2610.31026v1 (October 22, 2026), https://arxiv.org/html/2610.31026v1 .
2. D. Levin, J. M. Ramón, J. Ruiz-Álvarez and D. F. Yáñez, *Weighted essentially non-oscillatory Shepard method*, Numerical Algorithms 102 (2026), 593–609; first publicly published June 27, 2025, https://doi.org/10.1007/s11075-025-02141-6 .
3. U. S. Vevek, *An efficient algorithm for computing smoothness indicators for WENO schemes*, Journal of Computational Physics 446 (2021), 110619, https://doi.org/10.1016/j.jcp.2021.110619 (related, different indicator design).
