# Self-review

## Correctness — PASS

The claimed exact covariance follows by conditioning on the two independent reciprocal arc indicators between distinct vertices. One-vertex contributions are categorical, and cross-vertex contributions have exactly three centered Bernoulli components. Binomial-score orthogonality makes the complete Pearson-normalized matrix diagonal on four explicit modes, with the residual mode at eigenvalue \(n\). The proof covers every \(n\ge2\) and \(0<p<1\); the equality cases of the universal variance bound follow from the eigenspaces. The embedded checker uses exact rational arithmetic for all small-size covariance entries and the eigenvector equations, independent of floating-point approximation.

## Originality — PASS, qualified by priority uncertainty

Goldschmidt–Stephenson (2019) gives the same model but studies component scaling. Liebenau–Wormald (2020) studies labeled in/out-degree **sequence** probabilities with fixed edge count, asymptotically; its theorem does not determine finite-size covariance eigenvalues in the unconditional model. Lin–Reinert (2009) handles exact dependence of **undirected** single-degree counts, and Alarfaj–Taylor–Bogachev (2023) investigates undirected degree dependence and fitting. Their inspected results do not imply the complete signed low-rank correction and interaction eigenspace for a directed bidegree count histogram. A hidden equivalent in older random graph theory remains possible, and this scientific priority assessment is not an independent historical certification.

## Value — PASS

An empirical joint in/out-degree histogram carries two conservation constraints and complicated dependence. The result completely classifies its finite-sample covariance geometry and shows the exact variance correction for every linear histogram statistic; the upper inflation factor \(2\) is optimal and independent of edge probability. The third, bilinear mode separates reciprocal-arc interaction from mean-degree fluctuation, a structural distinction absent from marginal analyses.

## Limits

This is strictly a second-moment and eigenspace theorem for homogeneous independent arcs with \(n\ge2\) and \(0<p<1\). It makes no claim about full distribution, asymptotic normality, chi-square calibration, dependent reciprocal arcs, self-loops, or unknown-probability plug-in procedures. The directed-model paper, historical degree-count work, and degree-sequence enumeration are properly attributed.

Self-review: passed. Independent audit: not yet performed.
