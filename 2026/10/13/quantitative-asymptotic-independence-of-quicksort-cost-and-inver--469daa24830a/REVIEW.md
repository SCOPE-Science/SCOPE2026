# Scientific review

## Correctness — PASS

The comparison-cost martingale follows from the exact external-gap identity of binary search trees and the elementary expected-comparison formula. The insertion depth has a uniformly summable squared-increment bound via independent record indicators. The random-permutation suffix is independent of each finite-prefix search-tree cost; the omitted inversion pairs contribute at most \(k/\sqrt n\) after normalization. This proves nonlinear factorization without presuming independence from zero covariance. Independent Lehmer insertion ranks give the inversion central limit, completing the joint limit. Finite exact checks cover all 46,233 permutations through order 8 and the 873 next-step configurations through order 6. The finite checks corroborate, but do not substitute for, universal proof.

## Originality — PASS, subject to independent priority audit

Neininger (2001) proves a multivariate Quicksort cost/exchange limit; exchanges are not input inversions, and its displayed recursions do not give a comparison-cost/inversion limit. Brodal, Fagerberg and Moruz (2004) discuss inverse-pair presortedness and adaptive Quicksort, but not quantitative covariance factorization under uniform random inputs. Iliopoulos (2015) presents marginal algorithm analysis. He, Peng and Xu (2018) bound BST height under inversion-count conditioning, a different response statistic; the full 2018 paper was inaccessible, so stronger implicit implications remain an explicit risk. Baxter and Zeilberger (2010) concern inversion/major-index independence instead. The exact reflection symmetry and univariate Quicksort limit are excluded from the novelty claim. Published mathematical search also found an inversion-refined permutation-avoidance census, logically incomparable with this theorem. No located result directly asserts (1) or (2). Search absence is not proof of priority; implicit coverage by broad joint-limit methods remains a risk. A plausible 2012 Quicksort paper could not be materially inspected due to source-access restrictions.

## Value — PASS

The motivating mathematical question is whether ordinary inversion-defined disorder influences first-pivot Quicksort comparison-cost fluctuations even though their finite covariance is zero. Formula (1) controls all bounded Lipschitz nonlinear tests and proves asymptotic *distributional* decoupling of a nondegenerate algorithmic limit from Gaussian permutation fluctuations. This matters for joint statistical modeling of algorithmic cost and disorder, and cannot be concluded from their separate marginal limits or zero covariance.

## Scientific boundaries

First-element-pivot, order-preserving recursion only. No assertion of optimal decorrelation rate, of finite independence, or of coverage of other partition implementations. The joint-limit priority and residual inaccessible source require independent historical assessment.

Self-review: passed. Independent audit: not yet performed.
