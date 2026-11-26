# Independent mathematical audit

## correctness

PASS

For full column rank A, the normal equations give r orthogonal to im(A), so H and Q are projectors of ranks n and n+1. Their k-minor sums are the respective binomial coefficients, by taking the coefficient of t^k in det(I+tH) and det(I+tQ). For each positive-probability S, H_SS is positive definite, the constraints are feasible, and minimizing the G-norm of x−x_* subject to A_S(x−x_*)=r_S adds exactly r_S^T H_SS^{-1} r_S to the squared residual. By the determinant lemma the per-set normalized loss is det Q_SS / det H_SS. In the average the denominator cancels only on the positive-probability support; adding and subtracting the remaining minors gives the exact formula and the upper equality criterion. The lower bound is pointwise. The Vandermonde and padded-identity constructions meet the two endpoints with nonzero residual for every allowed n,k. Independently checking the strict example gives x_*=(-3,15,1)/7, r=(10,3,13,13,-13)/7 and ||r||²=88/7. The only singular pair has H entries all 3/7 and u_1−u_2=1/||r||, so its augmented determinant is 3/88, giving ratio 175/88 and excess 87/7. This concerns loss inflation with access to every response, not mean parameter bias or a label-efficient regression procedure. CHECK.py and VERIFICATION.md were inspected, not executed; the argument above is an independent exact check.

## originality

PASS

The supported distinct contribution is the exact full-data hard-constraint risk with less than n constrained equations, including the singular-support deficit and attained all-design bounds. The fixed-size DPP normalization and the generic support-restricted likelihood identity are not new. The step tying that ratio to a specific constrained optimizer and the exact subdimension risk is not covered in the closest inspected results. This decision is limited to the stated estimator and loss.

## value

PASS

This is an exact benchmark for the cost of retaining selected hard equations in an inconsistent least-squares system, when the full objective remains available. It answers for every design which upper-bound loss is lost to rank degeneracy, instead of silently treating zero-probability sets as zero augmented minors. The all-design endpoints and strict interior example make this distinction quantitative. This does not offer a convergence or label-efficiency guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
