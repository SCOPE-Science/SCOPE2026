# Scientific review: stable magnitudes through a sharp Cauchy generator

## Correctness (PASS)

The folded density of a Cauchy random variable shifted by \(m\) differentiates to a positive rational prefactor times
\[
(1-3m^2)x^4+2(1+m^2)^2x^2+(1+m^2)^3.
\]
It is positive for every \(x>0\) precisely when \(|m|\le1/\sqrt3\), and becomes negative at large \(x\) otherwise. This proves the exact one-dimensional boundary. The inverted CDF of an independent positive scale mixture is the average \(\mathbb E[G_X(tT)]\) of concave functions, so it stays concave. An analytic continuation of the positive-stable Laplace transform proves the independent Cauchy-subordination representation. Matching the complex characteristic function with the standard stable parameterization gives the explicit skewness interval. Endpoints, positive scales, and the \(\alpha=1\) Cauchy case are treated separately. The standalone exact-rational and complex-arithmetic checker passed 2,530 assertions. The proof is analytical and does not infer infinite-parameter statements from these tests.

## Originality (PASS, with residual risk)

The closest lead paper, Chen–Hu–Shneer–Zou (arXiv:2505.01739, sections 2, 4 and 5), defines inverted concavity and explicitly leaves absolute stable magnitudes as an open question; it includes centered absolute Cauchy and Lévy examples but does not provide the shifted-Cauchy threshold or a skew-stable inverted-concavity band. Classical subordination of skew-stable laws through skew Cauchy distributions is in Mainardi–Pagnini–Gorenflo (arXiv:math/0702133, section 5), and product/mixture closure is an elementary consequence of the lead paper; neither ingredient is claimed as independently new. Bridaa–Jedidi–Sendov (Theorem 6.3, DOI:10.1007/s10959-023-01242-z) establish an earlier exact reciprocal-density classification for **one-sided positive stable** laws, not folded magnitudes of two-sided stable laws with continuously variable skewness. Chen–Shneer (DOI:10.1017/asb.2025.10053) gives other sufficient conditions for stochastic dominance but not the stated exact folded-Cauchy boundary. Targeted searches for inverse-concavity, shifted Cauchy and the explicit trigonometric band found no known covering statement. Previously unpublished or differently indexed equivalents remain possible; the result is not independently audited.

## Value (PASS)

The primary paper expressly asks whether absolute stable magnitudes with indices at most one are inverted concave and provides numerical but not analytic evidence for the associated stochastic-order property. The theorem rigorously covers **every symmetric index in the full continuum** and an explicit nonzero asymmetric skewness interval for each \(0<\alpha<1\), instead of one distribution or one isolated parameter. The exact normalized location threshold \(1/\sqrt3\) determines the maximal shifted-Cauchy input region of this natural stable subordination construction; the transition is a genuine sign obstruction, not a numerical calibration or arbitrary slice. It directly supplies new infinite-mean portfolio models to which the source's majorization theorem applies. The stated skewness interval is a sufficient gateway, **not a claimed global sharp boundary** for general asymmetric stable laws.

## Limits of this review

No assertion is made for stable skewness beyond the displayed interval, stable indices above one, or general nonzero stable location parameters. Nonmembership beyond the Cauchy generator threshold is established only at the Cauchy endpoint; multiplying by positive stable factors may change that conclusion. Prior literature may contain an unindexed equivalent formulation, and external independent validation is absent.

Self-review: passed. Independent audit: not yet performed.
