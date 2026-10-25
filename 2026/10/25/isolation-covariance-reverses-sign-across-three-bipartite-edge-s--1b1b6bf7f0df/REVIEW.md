# Scientific review

## Correctness: PASS

For the fixed-distinct-edge model, the joint probability of a specified left and right vertex being isolated is an exact hypergeometric ratio. Summing the \(ab\) cross-indicator covariances yields the finite formula. The factorization \((R-t)(C-t)-(J-t)(N-t)=t\) proves strict negativity exactly on the stated range; outside it one indicator aggregate is deterministic or the sample is too small for dependence. Bernoulli edge stars overlap in exactly one edge; endpoint sequences are independent with replacement. The sparse constant follows from a uniform finite product expansion. Exact independent enumeration checks 90 fixed-edge strata, 12 Bernoulli parameter triples, and 16 replacement settings; these tests are corroborative, not the general proof.

## Originality: PASS (inspected sources, residual priority risk)

The motivating Bohman–Warnke–Zhu paper derives binomial-ensemble isolated-vertex probabilities and bounds; it does not give the fixed-distinct-edge cross-class covariance or its negative sparse constant. Blasiak–Durrett explicitly use endpoint sampling with replacement, making the zero-covariance component known rather than new. Glebov–Luria–Simkin study bipartite exposure and matching hitting times, rather than the covariance law. Searches for exact opposite-class degree-zero covariance, empty rows versus columns in fixed-weight binary matrices, and model-ensemble reversals found no dominating result; prior probability records involving one-class occupancy or distinct random graph statistics do not imply the fixed bipartite formula. The novelty assessed is the exact fixed-distinct-edge strict-sign classification and sparse constant, together with their model-sensitivity interpretation—not standalone Bernoulli or replacement facts. A preexisting equivalent hypergeometric identity may exist in older binary-matrix literature.

## Value: PASS

Both classes' isolation counts are natural diagnostics for random incidence matrices, bipartite network null models and matching thresholds. Matching the expected edge count does not match cross-class covariance: the fixed-edge covariance has a finite nonzero negative sparse limit, while Bernoulli covariance is positive on an order-\(n\) scale and replacement covariance is exactly zero. The exact all-parameter sign and limiting constants make the sensitivity quantitative, beyond an arbitrary finite computation or relabeling.

## Closest literature and limitations

Bohman, Warnke and Zhu (arXiv:2401.10486, 2024), *Random Oxford Graphs* by Blasiak and Durrett (2005), and Glebov, Luria and Simkin (arXiv:1805.06944) cover related but distinct ensembles and goals. A direct earlier statement of the fixed-distinct-edge formula has not been definitively excluded, and independent human priority checking may change the originality assessment. The theorem does not assert full-vector negative dependence or dense-scale universality.

Self-review: passed. Independent audit: not yet performed.
