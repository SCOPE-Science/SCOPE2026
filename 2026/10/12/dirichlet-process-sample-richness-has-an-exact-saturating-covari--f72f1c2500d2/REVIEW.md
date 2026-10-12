# Review

## Correctness

PASS. Conditioning on the latent frequencies turns each richness increment into the discovery functional
\[
\Delta_n(P)=\sum_iP_i(1-P_i)^n.
\]
The equal-species and distinct-species contributions to \(\mathbb E[\Delta_nH]\) are reconstructed from the first two independent GEM beta factors. Subtracting the product of means gives the positive digamma increment. Telescoping and summation by parts yield the finite-sum and trigamma covariance formulas. The saturation and correlation asymptotics follow from standard special-function tails, the exact cluster-count variance, and the sourced Shannon-entropy variance.

The packaged checker independently evaluates the mixed moment by beta-integral and closed digamma routes, then cross-checks the cumulative and asymptotic forms.

## Originality

PASS, with a residual bibliographic risk. Cerquetti's full paper supplies prior and posterior Shannon/diversity moments under Gnedin--Pitman and Poisson--Dirichlet models but no sample-richness/latent-entropy covariance was found. Archer, Park, and Pillow explicitly use the observed unique-symbol count \(K\) in posterior entropy formulas, but their full article does not state the unconditional \(K_n\)-entropy covariance or its saturation law.

Chao, Wang, and Jost relate fixed-population entropy to species-discovery rates. That expectation identity does not imply the covariance created by randomizing the abundance vector under a Dirichlet process.

The nearest own findings are noncovering: one couples two latent diversity functionals, Shannon and Gini--Simpson, while another couples sample richness with an unbiased Gini--Simpson sample statistic. Neither determines the present sample-richness/latent-Shannon mixed moment.

## Value

PASS. Sample richness and Shannon entropy are canonical but differently weighted diversity summaries. Their exact cross-dependence under the Dirichlet process calibrates how much observed richness tracks latent evenness.

The structural point is not merely positivity: \(\operatorname{Var}(K_n)\) grows like \(\theta\log n\), while \(\operatorname{Cov}(K_n,H)\) approaches a finite explicit ceiling. The resulting \(1/\sqrt{\log n}\) correlation decay quantifies diminishing entropy information in continued rare-species discovery.

Self-review: passed. Independent audit: not yet performed.


Deterministic replay: `VERIFY_OK beta_increment_checks=840 closed_form_checks=1680 monotonicity_checks=840 saturation_checks=7 scaled_correlation_checks=5`.
