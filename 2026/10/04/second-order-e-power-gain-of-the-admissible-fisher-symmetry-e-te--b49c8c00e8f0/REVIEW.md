# Same-model review

## Correctness
PASS. The claim follows from the exact one-observation factors in the source paper, the global inequality \(\log\cosh x\le x^2/2\), a controlled Taylor expansion of \(\log\cosh\), standard Gaussian moment polynomials, and exact formal series inversion. The packaged verifier independently replays the rational coefficient algebra. The distinction between continuous budgets and integer ceilings is explicit.

## Originality
PASS with residual historical risk. The closest primary source, arXiv:2208.08925, gives the admissible Fisher factor, the dominated quadratic factor, and the leading e-power \(n\theta^2/2\), but the inspected article contains no \(\theta^4\) refinement for this comparison and no second-order sample-budget constant. Targeted searches using exact factor names, `log cosh`, higher-order e-power, and sample-size language found no source stating the displayed coefficients. arXiv:2009.03167 supplies the broader admissibility context rather than this local Gaussian expansion. Older efficiency or self-normalized-process literature could contain an equivalent refinement under different terminology.

## Value
PASS. The source paper itself emphasizes that the quadratic e-variable is inadmissible yet close to the admissible Fisher factor in the small-signal regime, while its first-order ARE calculation cannot measure the cost of that simplification. The new coefficient identifies exactly where the loss first appears and translates it into a finite-signal sample-budget correction. This is a natural refinement of a standard efficiency comparison rather than an arbitrary numerical slice.

Same-model review: passed. Independent audit: not yet performed.
