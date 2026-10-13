# Self-review

## Correctness
PASS. Conditioning on the sample maximum gives a rescaled uniform order-statistic sample and determines the conditional first and second order-statistic sums exactly. This yields the quadratic conditional Cramér–von Mises regression. Beta moments of the maximum then give the covariance. The Cramér–von Mises variance is independently reconstructed from the degenerate empirical-process kernel, with exact polynomial integrals \(\operatorname{Var}(h(U,U))=1/180\) and \(\mathbb E[h(U,V)^2]=1/90\). The standalone checker reproduces all displayed finite formulas.

## Originality
PASS. The inspected Cramér–von Mises literature concerns definitions, marginal null distributions, small-sample approximations, and goodness-of-fit implementation. Searches combining the statistic with sample maximum, maximum order statistic, endpoint/boundary gap, covariance, and conditional regression did not locate the stated mixed moment. The checked prior Cramér–von Mises findings concern Watson and Anderson–Darling functionals and do not imply an endpoint-order-statistic regression. The inaccessible complete bodies of older exact-distribution papers remain an explicit residual risk.

## Value
PASS. The boundary gap is the simplest local measure of upper-tail sample coverage, whereas Cramér–von Mises is a canonical global integrated discrepancy. Their exact conditional coupling separates two effects that are otherwise conflated: the conditional mean is convex with a nonzero optimal gap, while the overall covariance is strictly positive. This supplies a finite-sample bridge between endpoint coverage and global EDF discrepancy rather than another marginal distribution formula.

## Closest literature and limitations
Arnold and Emerson provide a complete accessible account of Cramér–von Mises-type tests and their integrated-discrepancy role. Knott and Csörgő–Faraway are the most plausible exact-distribution predecessors; their accessible journal records and summaries focus on the marginal statistic, not endpoint coupling, but their complete bodies were not available in the checked lawful path. Lemeshko, Lemeshko, and Postovalov provide the primary \(62G10\) classification and the verified 2010-01-06 public-date anchor. The theorem is restricted to the continuous-uniform null after probability-integral transformation.

Self-review: passed. Independent audit: not yet performed.
