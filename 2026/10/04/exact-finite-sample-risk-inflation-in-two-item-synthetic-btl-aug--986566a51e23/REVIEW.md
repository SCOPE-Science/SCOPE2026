# Same-model review

## Correctness
PASS. The claim follows from an exact martingale recursion in the Bernoulli sufficient statistic. The conditional mean, conditional variance, product recurrence, Euler sine product, and large-batch expansion were reconstructed independently. Exact-rational finite-state calculations in `verify.py` agree with the formulas. The parameter-space boundary is explicit: the closed probability parameter includes degenerate first batches, while finite log-odds BTL paths are covered when the real first batch contains both outcomes.

## Originality
PASS. The recent BTL paper arXiv:2609.32987 specifies the accumulation recursion and proves high-dimensional rates/asymptotic normality, but does not state the two-item finite-sample product law. Gerstgrasser et al. arXiv:2404.01413 obtain an exact reciprocal-square risk sum for linear regression. Dey--Donoho arXiv:2410.22812 prove the reciprocal-square inflation asymptotically for general exponential-family/AAL estimation, and Barzilai--Shamir arXiv:2505.19046 give nonasymptotic general bounds. Those results explain the limiting \(\pi^2/6\) mechanism but do not imply the exact state-dependent Bernoulli product, its sine-product finite-batch correction, or the conditional no-self-correction identity without the additional calculation given here.

## Value
PASS. The result supplies a sharp finite-sample benchmark for a recent iterative BTL augmentation model and quantitatively bridges exact Bernoulli behavior to the known \(\pi^2/6\) asymptotic pathway. It separates two effects that broad bounds conflate: synthetic accumulation preserves the initial estimate in conditional mean yet injects a nonzero, exactly computable variance floor. The strict finite-batch correction is relevant when comparisons per round are modest, precisely where asymptotic approximations are least informative.

## Closest literature and limitations
The closest general precursor is Dey--Donoho's asymptotic exponential-family universality theorem; the closest exact finite-generation precursor is Gerstgrasser et al.'s linear-regression reciprocal-square risk identity. The main residual risk is that another specialized Bernoulli calculation outside the inspected literature could contain the same finite product. Searches by source title, BTL/two-item terminology, Bernoulli augmentation terminology, martingale terminology, and the sine-product/\(\pi^2/6\) connection did not locate such a statement. The result is intentionally restricted to equal-size, fully observed two-item accumulation and win-probability risk.

Same-model review: passed. Independent audit: not yet performed.
