# Review

## Correctness (C): PASS

The proof separates the Bernoulli known-match count from the residual permutation fixed-point count. The sparse-skill limit uses total-variation binomial-to-Poisson convergence and the classical \(\operatorname{Pois}(1)\) limit for fixed points. The near-perfect limit applies a fixed conditional permutation kernel to the Poisson limit of the unresolved count and derives the moved-point mass by choosing and deranging exactly the moved labels. In the interior regime, the binomial variance diverges; the residual fixed-point count is tight because its expectation is at most one, so Slutsky's theorem gives the stated normal limit. The exact centering is \(n\theta_n+1-\theta_n^n\). Finite checks passed but are not used as proof of the limits.

## Originality (O): PASS

The closest inspected source is O'Neill's generalized matching distribution paper, which gives the same model identity, its moments, and a central limit theorem for fixed \(0<\theta<1\). It does not state the triangular-array endpoint limits or the exact Poissonized moved-point law near perfect matching. An earlier result about two-game likelihood ordering in this model is a distinct finite-sample testing claim, not this asymptotic classification. Searches for equivalent descriptions using fixed points, derangements, Poissonized moved points, and endpoint skill scalings did not identify an implication or exact duplicate. This is a bounded literature assessment, not a proof of universal priority.

## Mathematical value (V): PASS

The classification identifies the two boundary laws where a Gaussian approximation is inappropriate and the interior regime where it is appropriate. The near-perfect endpoint is particularly informative: the limiting number of mismatches has an explicit mass function and assigns probability zero to exactly one mismatch. This gives a natural boundary law for inference when matching accuracy is close to one, a setting in which the source paper warns that standard asymptotic confidence intervals perform poorly. The result is a focused asymptotic classification rather than a claim of a broad downstream theorem.

## Closest literature and limitations

Ben O'Neill, “A Generalised Matching Distribution for the Problem of Coincidences,” arXiv:2112.12442; *Methodology and Computing in Applied Probability* 25 (2023), article 93, DOI: 10.1007/s11009-023-10067-6. The main inspected comparison is Theorem 9 (fixed-parameter normal approximation), alongside the exact two-stage representation and the discussion of inference near parameter endpoints. Search was not exhaustive; no convergence rates are claimed.

Self-review: passed. Independent audit: not yet performed.
