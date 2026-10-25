# Scientific review: Euclidean contact bifurcation for rectangular radial mean bodies

## Correctness — PASS

The stated theorem is a complete statement for every \(a>b>0\) and every finite \(p>-1\). The exit distance from a uniformly sampled point in the rectangle has an exact, normalized two-factor survival function; integrating its derivative gives the displayed moment for negative and positive exponents, and integrating its logarithm gives the \(p=0\) limit. Branchwise differentiation gives one explicit concave quadratic, whose lower root produces precisely four Euclidean inradius contact directions for every exponent. A strict branch comparison, the known square endpoint inequality (also reproved in RESULT.md), and a strictly increasing elasticity reduce the enclosing-radius problem to exactly one sharp aspect-ratio threshold for \(p>2\). The quartic transition radicals are verified by exact algebra. Numerical quadrature and dense direction checks in `verify.py` passed but do not substitute for these analytic arguments.

## Originality — PASS, with documented historical uncertainty

The closest full-text sources are Langharst's convexity paper (arXiv:2603.14134, Theorem 3 and Proposition 10), the Langharst–Manui–Zvavitch cube calculation (arXiv:2601.20117, Section 3.3, Proposition 34), and the published *A four-to-four contact transition in radial mean bodies of the square* (2026). These give general convexity, a cube/square pointwise integral and, for the square, complete Euclidean directional extrema. The rectangle follows affinely **as a pointwise radial function**, which is acknowledged as prior-determined, but an anisotropic affine map does not preserve Euclidean circles; the exact nonsquare Euclidean minimizing and maximizing directions, aspect-ratio threshold, six-way coexistence, and the quartic radical are distinct assertions requiring further optimization. A full-text 2014 paper on dual quermassintegral inequalities has different integral observables and supplies none of these contacts.

The original 1998 Gardner–Zhang publication could not be accessed in full. No assertion is made that all historical or unindexed literature was searched, and an equivalent specialized rectangle calculation remains a priority risk. This residual uncertainty is not represented as independent certification.

## Mathematical value — PASS

Rectangles are the natural two-parameter, anisotropic affine deformations of the square; because Euclidean radii fail to respect anisotropic affine covariance, their radial mean bodies pose a real additional shape optimization. The theorem resolves that natural family for the entire allowed finite exponent interval, with rigid direction counts. The discontinuous four-to-six-to-two contact change at an exact geometric threshold is not a mere restatement of the known square contact switch in \(p\), and the \(p=4\) algebraic cutoff supplies a reproducible benchmark. The result does not claim a general convex-body theorem or novel representations for known radial mean bodies.

Self-review: passed. Independent audit: not yet performed.
