# Scientific assessment: sharp two-point interpolation on circular arcs

## Correctness (C): PASS

The definition of the complex interpolation operator and the norm from \(C(K_\theta)\) to itself are explicit. Formula (1) is the exact norm, rather than only an upper estimate, because arbitrary prescribed unimodular values at the two nodes extend continuously inside the closed unit disk. The chord identity gives an exact three-interval Lebesgue function for all \(0<\theta<\pi\), including arcs longer than a semicircle. At the pair midpoint and an exterior test point this yields a universal two-branch lower envelope. Symmetric sample pairs attain that envelope; opposing strict monotonicities locate the unique crossing. A strictly improved exterior test excludes all asymmetric node pairs at the crossing. Every domain restriction and endpoint behavior is accounted for. The Python standard-library checker reproduces 4,539 finite diagnostic assertions, which support but do not replace these analytical steps.

## Originality (O): PASS, with literature risk

Ray's manuscript (arXiv:2610.04608v1) introduces the same function-space family, but its main results concern completely contractive operator maps and isometric classification, not minimal-norm two-point interpolation. The closest separately indexed circular-arc study treats optimal Euclidean/Hilbertian norm distortion, a logically distinct invariant. Chui–Zhong's complex-arc interpolation paper (arXiv:2209.07101) addresses high-degree growth, and Nevskii's interpolation work (arXiv:2405.01254) treats real-affine projectors on convex bodies with a different number and type of sample nodes. Searches for the formula, its inward-node parameterization, and equivalent norm-minimization formulations did not identify a theorem whose conclusion implies the exact two-complex-node minimax here. Search absence alone is not a novelty proof. The earlier theory of complex-arc interpolation remains a genuine residual priority risk, particularly where full text was not available for all sources.

## Mathematical value (V): PASS

The optimization answers a natural exact conditioning question for a newly studied family of complex Banach function spaces, with no arbitrary finite parameter slice. The result gives a sharp constant uniformly for a continuum of arc lengths and a unique, explicit, strictly inward optimizing node pair. More importantly, it proves that naive endpoint sampling is strictly suboptimal and becomes arbitrarily ill-conditioned as the arc tends to a full circle, while the optimal interpolation remains uniformly bounded by \(\sqrt2\). This identifies a precise and practically relevant sampling geometry, rather than merely re-evaluating a known constant.

## Limits and closest literature

This is a theorem about two-node **complex Lagrange interpolation**, not about all bounded projections, all methods of information recovery, or higher-degree polynomial interpolation. Source inspection and comparison cannot guarantee publication priority; relevant older methods might contain the same formula under a different notation. No independent assessment or external certification is claimed.

Self-review: passed. Independent audit: not yet performed.
