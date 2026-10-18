# Self-review

## Correctness — PASS

With normalized Lebesgue measure, the two orthonormal functions are \(1\) and \((t^\alpha-1/(\alpha+1))/\sqrt v\), with \(v=\alpha^2/[(2\alpha+1)(\alpha+1)^2]\). They give the exact symmetric projector kernel. Integration of its positive/negative endpoint parts gives both piecewise branches. Convexity in the evaluation monomial forces an endpoint maximum. One branch is strictly decreasing and the other strictly increasing, intersecting at \(\alpha=1\); consequently the unique global minimum is \(5/3\). The diagonal Christoffel peak follows independently by maximizing a positive quadratic. Both singular limits follow by logarithmic expansions. The accompanying checker evaluates the same kernel through independent quadrature and deterministic parameter tests, but analytical Steps 1–4 are the justification for every positive real exponent.

## Originality — PASS, subject to historical-priority risk

Milovanović (1999) gives general Müntz orthogonal bases and their numerical evaluation, rather than the sharp \(L^1/L^\infty\) projector Lebesgue function. Noor–Timotin (arXiv:1110.5422v1, 2011) study embeddings between Hilbertian Müntz spaces. Cohen–Migliorati (arXiv:1608.00512v1, 2016) study sampled weighted least squares and Christoffel-based sample complexity. Their theorems do not imply the complete explicit \(\alpha\)-dependent endpoint norm, its unique minimizing exponent, and the stated comparison with the Christoffel peak. The known affine special case is not claimed as new. An older chapter by Gurariy–Lusky on projection types was identified from bibliographic metadata but its full contents were not accessible; an equivalent historical statement remains a real residual risk, and the literature comparison is not a proof of novelty.

## Value — PASS

This is a natural, entire one-parameter deformation of affine least-squares approximation, not an arbitrarily chosen exponent. It resolves how the deterministic worst-case error amplification changes with the Müntz exponent, including a globally optimal exponent, a sharp switch of the worst evaluation endpoint, and two singular regimes where the Christoffel diagonal and Lebesgue amplification have markedly different orders. This distinction is pertinent when deterministic stability and sampled least-squares conditioning are both examined. The result applies only to the two-dimensional unweighted system; no higher-dimensional generalization is asserted.

## Sources and limitations

Primary full-text sources: G. V. Milovanović, *Müntz Orthogonal Polynomials and Their Numerical Evaluation* (1999), https://www.mi.sanu.ac.rs/~gvm/radovi/BC16.pdf; S. W. Noor and D. Timotin, *Embeddings of Müntz spaces: the Hilbertian case* (2011), https://arxiv.org/abs/1110.5422; A. Cohen and G. Migliorati, *Optimal weighted least-squares methods* (2016), https://arxiv.org/abs/1608.00512. Uninspected potentially relevant book chapter: V. Gurariy and W. Lusky, *Projection Types and the Isomorphism Problem for Müntz Spaces* (2005), DOI:10.1007/11551621_10. No independent mathematical or bibliographic audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
