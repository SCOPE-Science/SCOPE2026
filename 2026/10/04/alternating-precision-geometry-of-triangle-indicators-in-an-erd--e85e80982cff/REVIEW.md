# Review

## Correctness

PASS. The triangle covariance is exactly diagonal plus the Johnson adjacency contribution: two distinct triangle indicators share randomness only when the triangles share an edge. Positive definiteness follows independently from linear independence of distinct triangle monomials on the full Boolean edge cube.

Permutation symmetry reduces the inverse to four Johnson-distance coefficients. Direct neighbor counting yields the four linear equations in `RESULT.md`; solving them gives the displayed formulas. The factors controlling the denominator and sign are positive for every \(n\ge6\) and \(0<p<1\), which proves the alternating precision signs. The partial-correlation formulas are then the standard normalized precision entries for least-squares residuals.

## Originality

PASS, with an explicit association-scheme residual risk. Reinert--Röllin's full arXiv text was inspected in the Bernoulli-random-graph section and its covariance subsection. It computes aggregate edge, two-star, and triangle count covariances and a multivariate normal approximation, not the all-triangle indicator precision matrix.

Chatterjee's full arXiv text was inspected where triangle triples are classified by overlap with a fixed triple for dependence control. That source uses the same underlying overlap geometry in an upper-tail argument but does not study inverse covariance or partial correlations.

Exact-phrase, alias, and semantic searches for triangle-indicator precision, inverse covariance, Johnson-graph resolvents in this statistical setting, and partial correlations did not locate the displayed formulas. General Johnson-scheme algebra is classical, so the originality claim is limited to the random-graph specialization, exact sign pattern, and linear-partial-correlation interpretation.

## Value

PASS. Triangle indicators are the atomic variables behind one of the most studied random-graph motif counts. Their marginal dependence is extremely sparse, but the inverse covariance reveals a qualitatively different global geometry after linear adjustment. The theorem gives a complete finite classification by overlap type, including exact formulas and a sign reversal for the vertex-sharing class. This is a natural structural statistic of the full motif vector rather than an arbitrary numerical slice.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK neighbor_class_checks=160 inverse_equation_checks=1900 sign_checks=3800 partial_formula_checks=2850 full_product_checks=35451`.
