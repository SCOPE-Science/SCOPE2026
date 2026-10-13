# Scientific review: sharp log-Pareto majorization boundary

## Correctness — PASS

The log-Pareto CDF is normalized and differentiates to the stated positive density. The displayed identity for \(h_\alpha'= (x^2f_\alpha)'\) is exact. The auxiliary function \(B\) diverges at both endpoints; its derivative has numerator \(q\) with \(q'(x)=x^2/(1+x)^2>0\) and opposite endpoint signs. This proves the unique minimizer and an exact necessary-and-sufficient threshold, including equality. Taylor expansion at the minimum gives the two-root square-root split. Chen et al.'s existing Proposition 2 and Theorem 3 are applied with their required continuity and essential-infimum-zero hypotheses. For the constructive failure above the threshold, the exact one-jump difference is positive and the probability of two or more Poisson jumps is bounded explicitly, producing a strict CDF reversal for low intensity. The accompanying executable checker corroborates numerical constants but is not an infinite-domain certificate.

## Originality — PASS, with priority risk

The closest publication is Chen, Hu, Shneer and Zou, *Stochastic dominance for linear combinations of infinite-mean risks*, arXiv:2505.01739 / DOI 10.1017/jpr.2026.10138. Its Appendix A Example 6 has exactly the necessary derivative but stops at sufficient \(\alpha\le2\). The new claim minimizes that derivative's threshold exactly, shows two post-critical curvature changes with quantitative splitting and constructs a sharp-direction counterexample. The general stochastic-order implication is credited to prior Proposition 2/Theorem 3, not misrepresented as independently discovered. Chen–Shneer and Arab–Lando–Oliveira address a weaker one-parent order rather than the universal multiweight compound-Poisson condition. Targeted semantic database and literature searches found no equivalent; their failure cannot establish absolute priority. An unindexed solution to the specific optimization remains possible, and the Arab et al. primary full text was not independently inspected in full.

## Value — PASS

The original natural sufficient parameter range stops at 2. The new sharp value \(\alpha_*=2.906557937512901\ldots\) identifies the **complete** parameter range for the very class governing weight-majorization comparisons of compound-Poisson infinite-mean risks. It is not an arbitrary parameter slice: \(\alpha\) is the standard shape parameter of an explicitly studied severity family. Above the cutoff a single bounded interval of inverted-curvature failure appears, with square-root emergence, and the result supplies a mathematically explicit two-weight low-intensity reversal. This is a natural complete classification with a substantive risk aggregation interpretation, although it is a parameter-family refinement of powerful established general theorems rather than a new general stochastic-order theorem.

## Scope, literature and limits

The source's first public version is dated 3 May 2025 (arXiv:2505.01739v1). Primary MSC is 60E15 as published. The independent full-text publication and related single-parent articles were compared by their actual implications, not titles. The theorem does **not** say that non-compounded log-Pareto sums fail majorization beyond the boundary, nor that the Poisson order fails at every fixed intensity. Verification beyond the analytical proof is ordinary same-model reproducibility; independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
