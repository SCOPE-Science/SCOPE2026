# Review: sharp Schwarzian phase boundary for quadratic subordination targets

## Correctness

**PASS.** The defining subordination gives \(f''/f'=v+czv^2\) with \(|v|\le1\). Differentiation yields an exact four-term Schwarzian identity. For nonnegative \(c\), the majorant is convex in the parameter and its two endpoint defects have explicit positive decompositions. For negative \(c=-d\), the majorant defect has a sum-of-squares decomposition whose only potentially negative coefficient is \(1/2-d-d^2\). This proves the bound exactly through \(d=(\sqrt3-1)/2\). The maximum principle for analytic disk maps and compactness of the defect away from the origin force every equality case to have \(v(z)=e^{i\theta}z\). Beyond the threshold, a real disk automorphism saturates the Schwarz--Pick derivative estimate and all triangle phases simultaneously; the explicit second-order expansion is positive. The algebra was replayed from `verify.py` in the actual package. Ahlfors--Weill yields the stated sufficient \(3\)-quasiconformal extension.

## Originality

**PASS.** Allu--Kumar (arXiv:2604.16833v1) studies the positive quadratic target and sharp Hankel determinants, not signed-parameter Schwarzian phases. Kanas--Sugawa (DOI:10.4064/ap101-1-8) supplies the closest and strongest general comparison: its Theorem 2.1 reduces Schwarzian norms for *arbitrary* analytic targets to an exact variational optimization. The general reduction must be acknowledged, but its investigated text does not solve the signed quadratic-target optimization, display the radical boundary, or classify all rotation extremizers. The present square-completion and matching automorphism obstruction evaluate a parameter phase not explicitly determined by that theorem. Janowski-convex norm estimates use rational targets, and known pre-Schwarzian estimates address a different invariant. Semantic overlap searches located no covering evaluated result. There is residual risk that an unindexed paper or an unnoticed corollary of the general variational framework already evaluates precisely this case.

## Value

**PASS.** The source family occupies one half of a *natural maximal real univalence interval* of quadratic targets. Extending to the other half reveals a nontrivial, sharp quadratic radical transition for a global geometric control quantity and supplies an explicit univalent/quasiconformally extendible zone even after the positive-real target hypothesis has failed. The equality classification and matching counterexamples delimit the sharp norm-one certificate rather than merely report an isolated bound. No optimal quasiconformal dilatation beyond the sufficient Ahlfors--Weill bound is claimed.

Same-model review: passed. Independent audit: not yet performed.
