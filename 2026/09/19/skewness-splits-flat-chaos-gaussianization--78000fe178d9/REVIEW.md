# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

For a flat \(\pm1\) spectrum the fourth effective rank is exactly \(R\), while the standardized third and fourth cumulants are \(2\sqrt2\,\delta_R/\sqrt R\) and \(12/R\). The average cumulant generating function is explicit and analytic near zero. Direct series inversion of \(K'_{\delta}(t)=a\) gives
\[
I_\delta(a)=a^2/2-(\sqrt2\delta/3)a^3+(\delta^2-1/2)a^4+O(a^5).
\]
A conjugate-measure calculation then yields the displayed precise moderate-deviation ratio at \(x\asymp\sqrt{\log p}\). Under \(R/(\log p)^{5/3}\to\infty\), the remainder vanishes at this scale, so the two explicit Cramér terms determine the exceedance intensity. Independence across coordinates converts that intensity into a shifted Gumbel law. The Kolmogorov gap is the exact supremum distance between two translated Gumbel CDFs, and the formula for it follows from a one-variable maximization.

The canonical regimes are internally consistent. With fixed positive sign imbalance, the cubic term has size \((\log p)^{3/2}/\sqrt R\), producing a sharp \((\log p)^3\) scale. Under exact sign balance the cubic term vanishes and the quartic term has size \((\log p)^2/R\), producing a sharp \((\log p)^2\) scale. At \(R\asymp(\log p)^{5/2}\), the unbalanced family is below its cubic threshold while the balanced family is above its quartic threshold, giving the stated distance-one versus distance-zero separation despite identical \(r_4\) and \(\kappa_4\).

The standalone artifact independently checks the Legendre-transform coefficients. It evaluates the positive family using the exact chi-square CDF and the balanced family using the exact Bessel density for a difference of two gamma variables; the finite calculations move toward the predicted critical shifted-Gumbel CDFs.

## Originality

The closest source is Cai--Hu, arXiv:2609.20529v1. It defines the same fourth effective rank for signed Gaussian quadratic chaos and proves a general sufficient Gaussianization condition \(r_{4,\min}/(\log p)^6\to\infty\). The paper explicitly presents the phase curve as schematic. Searches within that source did not locate a third-cumulant, skewness, or sign-imbalance refinement.

The underlying asymptotic tools are classical and are not claimed as new. Cramér/Petrov precise moderate deviations encode tail corrections by cumulants. Anderson--Coles--Hüsler (1997, DOI 10.1214/aoap/1043862420) apply Cramér-series ideas to triangular-array maxima. Bose--Dasgupta--Maulik (2008, arXiv:0803.3518) treat gamma triangular arrays; their Theorem 2.1 already gives a Gumbel limit with an implicit corrected centering in the regime relevant to a positive flat spectrum. Thus the positive-skew cubic correction is close to a specialization of known gamma-maxima theory.

The originality claim is consequently narrower: the explicit two-term signed-flat correction, the exact critical Kolmogorov profile relative to the covariance-matched Gaussian maximum, the crossover from cubic to quartic control as sign imbalance vanishes, and the construction of two indefinite flat spectra with identical fourth effective rank and fourth cumulant but opposite Gaussianization behavior. Searches combining “quadratic chaos”, “effective rank”, “third cumulant”, “skewness”, “signed spectrum”, “chi-square maximum”, “variance-gamma maximum”, “normal maximum”, and the logarithmic scales did not locate these statements.

A concrete residual risk remains: the full theorem text of Anderson--Coles--Hüsler (1997) was not inspected. Its generic Cramér-series machinery may imply parts of the displayed flat-sign expansion after specialization, particularly the orders at which skewness and kurtosis alter extreme centering. What was inspected was its bibliographic abstract and the detailed summary and specialization in Bose--Dasgupta--Maulik. No inspected source connected that classical machinery to fourth effective rank or exhibited the same-\(r_4\) opposite-limit construction. Originality is therefore assessed only **to the best of our knowledge**.

## Value

The result directly sharpens the interpretation of a new high-dimensional U-statistic phase theorem. It identifies a missing spectral coordinate: the third signed spectral moment can alter the critical effective-rank scale by a full power of \(\log p\). The same-effective-rank construction shows that a fourth-cumulant/effective-rank statistic can be a useful sufficient control while still being fundamentally incomplete as a sharp phase parameter. The explicit critical Gumbel shift quantifies, rather than merely detects, the failure of Gaussian calibration.

## Limitations

The sharp theorem is proved for independent coordinates and flat spectra of common absolute eigenvalue. General spectra may require several spectral cumulants and cross-coordinate dependence can change maximum asymptotics. The two-term crossover statement assumes \(R/(\log p)^{5/3}\to\infty\), and no claim is made about a complete lower-rank hierarchy. The result audits the chaos-to-Gaussian step, not the separate finite-sample U-statistic-to-chaos approximation. The Anderson--Coles--Hüsler full-text limitation noted above remains an originality uncertainty. Numerical checks support but do not replace the proof.
