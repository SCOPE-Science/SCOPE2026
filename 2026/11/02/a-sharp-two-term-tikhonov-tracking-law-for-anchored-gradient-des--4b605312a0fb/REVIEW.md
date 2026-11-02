# Research review: sharp two-term anchored-forward tracking law

## Correctness — PASS

The exact recurrence is derived by setting \(s=k+\gamma\) and collecting its \(s^{-1}\), \(s^{-3/2}\) and \(s^{-2}\) coefficients. Invertibility gives three explicit asymptotic vectors. Monotonicity supplies the nonnormal product estimate \(\prod q_s\lesssim((j+\gamma)/(k+\gamma))^{\gamma-1/2}\); the remaining local defect is \(O(s^{-5/2})\). Discrete convolution is summable to the claimed \(O(s^{-3/2})\) or logarithmic endpoint bound, and a separate resolvent expansion yields the exact lag. The embedded standard-library verifier checks 416 rational coefficient identities and 36 trajectory assertions across twelve parameter/matrix cases. Numerical tests are corroborative and are not used to infer the infinite limit.

## Originality — PASS under the examined literature

Cai--Zheng (arXiv:2604.12235v1, Section 3 and proof) gives a universal \(O(k^{-1/2})\) norm bound for the same anchored schedule, without the exact limiting residual vector, second asymptotic coefficient or lag. Surina et al. (arXiv:2604.03782v1, Sections 2--3) prove the corresponding squared-gradient upper bound. Chen (arXiv:2605.30905v1, Section 4.2) supplies an operator-side Tikhonov interpretation and an upper residual bound at \(\gamma=4\); that interpretation is acknowledged as established. None of those statements alone implies the sign and coefficient of the dynamic tracking error. Searches for sharp linear anchored-gradient asymptotics, Halpern/Tikhonov tracking and second-order lag did not identify a dominating theorem. A more general older theorem about slowly varying linear regularizations may still imply the result; this remains a genuine historical-priority risk.

## Value — PASS

The nonzero signed \(1/k\) lag distinguishes actual algorithmic tracking from the static regularized root and permits second-order bias analysis. The residual vector limit demonstrates why the anchored \(k^{-1/2}\) estimate cannot be improved for this schedule even after strengthening the operator to a positive-definite Hessian; it also holds for invertible skew bilinear games. These are precise method-specific performance and design limitations rather than a universal optimization lower bound.

## Scientific limitations

Only finite-dimensional, exact-arithmetic, invertible linear monotone operators, a fixed nonzero anchor and \(\gamma\ge2\) are covered. Nonlinear problems, singular operators, stochastic steps and other schedules are not covered. Historical priority has not been independently established. The residual behavior says nothing adverse about faster unanchored or other anchored algorithms on strongly convex quadratics.

Self-review: passed. Independent audit: not yet performed.
