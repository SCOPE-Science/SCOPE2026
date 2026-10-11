# Review of the sharp orthotope width–brightness covariance phase diagram

## Correctness — PASS

For the same uniform normal, the width and codimension-one projection volume are respectively weighted sums of the absolute coordinates of a uniform spherical vector. Exact one- and two-coordinate Dirichlet moments give the covariance formula. Its negative off-diagonal spherical covariance is strictly justified by conditional monotonicity. At fixed aspect ratio the logarithmic-edge statistic is a strictly convex sum of exponentials; midpoint reflection gives its unique minimum, while vertex reduction and an integer optimization give its sharp maximum. The two crossings and their equality cases follow from monotonicity. A gamma-ratio expansion establishes the asymptotic thresholds. The independent finite consistency program `verify.py` returned `VERIFY_OK 6436`; the analytic proof, rather than computation, handles infinitely many edge configurations.

## Originality — PASS, with residual risk

The inspected full mathematical treatments arXiv:1511.08479 and arXiv:1110.0671 concern width moments of regular polytopes, not the joint same-normal width–hyperplane-brightness covariance phase diagram for arbitrary orthotopes. A generic weighted second-moment identity can yield the covariance algebraically; that identity alone is not claimed as the principal novelty. The phase classification uses distinct sharp extremizers for the minimum and maximum of the scale-free reciprocal-edge statistic, gives an exact coexistence interval, and identifies its high-dimensional limits. Published 2026 marginal width and joint width–brightness research (arXiv:2608.03305 and arXiv:2609.26202) was available only at abstract level and could contain stronger, presently unverified coverage. Searches did not identify an equivalent phase classification, but absence of a search hit is not proof of novelty.

## Value — PASS

Width and hyperplane shadow volume are two natural scalar observations of a convex body along one normal. For boxes they need not even move together on average under random orientation: the covariance switches sign, and equal aspect ratio does not fix that sign in dimensions at least three. The theorem provides the complete sharp condition, realizes every intermediate sign, identifies equality shapes, and quantifies the widening coexistence regime from bounded to quadratic aspect-ratio scales with dimension. This is a natural structural classification, beyond a single negative-covariance example or an isolated moment computation.

## Scope and residual limitations

The result concerns orthotopes, positive edges, Haar-uniform normal, and coupled projections only. The result does not identify a general-body sign criterion or the full bivariate law. Some highly relevant newer work was inaccessible in full, so independent literature verification remains important.

Same-model review: passed. Independent audit: not yet performed.
