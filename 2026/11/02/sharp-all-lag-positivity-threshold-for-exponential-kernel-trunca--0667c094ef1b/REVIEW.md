# Review of the exponential-kernel \(\operatorname{TTR}_2\) all-lag threshold

## Correctness — PASS

The normalized generating function is exactly \(h/[5/3+r-(5/2)\zeta+\zeta^2-\zeta^3/6]\). Coefficient matching yields the rational polynomial recurrence and the exact sixth-weight numerator \(g(r)\). A root decomposition produces one real pole and two conjugate poles; the Chebyshev partial-sum formula gives explicit sign bounds for every index. For \(r\le4/5\), the tail estimate starts at index three; for \(4/5\le r\le r_*\), the exact-rational Bernstein certificate handles indices through thirty and a strict analytic bound handles all subsequent indices. For larger \(r\), the sixth coefficient or Pringsheim's theorem proves failure. The 340 exact-rational checks from the standalone source were executed successfully. The infinite proof is analytical, not inferred from tests.

## Originality — PASS, with limits

Ferrari's July 13, 2026 preprint determines the optimized truncated-trapezoidal method under A-stability and studies CQ accuracy, but not every exponential-kernel CQ weight's sign. Banjai's original family and positivity theorem concern wave discretization and discrete quadratic-form coercivity; Karaa (2024) proves quadratic-form positivity under structural conditions on convolution sequences. These results do not imply coefficientwise nonnegativity. Direct comparisons with relevant primary texts found no implication proving the stated quartic boundary. Historical uniqueness remains unverified because some older specialized work may not be indexed.

## Mathematical value — PASS

When the input sequence is nonnegative, nonnegative lag weights are exactly what guarantees a nonnegative discrete convolution. The theorem supplies a precise, non-routine positivity restriction for a natural exponentially decaying memory kernel; the optimal second-order method permits approximately 86.6% more normalized step than BDF2 before a negative weight must occur. It also reveals the first sixth-lag obstruction and proves negativity for every larger parameter, including those beyond the transition to complex-dominant poles. No claim is made for general Laplace symbols, variable steps or PDE positivity.

## Sources and residual risks

Primary texts: Ferrari, arXiv:2607.11422 (complete accessible preprint, especially §3 and Theorem 3.1); Banjai, arXiv:2203.00986 (complete accessible preprint, §§4,6); Karaa, doi:10.5802/crmath.669 (complete accessible eight-page article, main theorems). The primary literature's uses of “positivity” require distinguishing discrete energy forms from individual lag weights. The result has not been independently audited, and an unrecognized historical equivalent remains possible.

Self-review: passed. Independent audit: not yet performed.
