# Scientific review

## Correctness — PASS

The statement fixes both marginal laws and explicitly requires independence across separate cells. For the local polynomial \(z(u)=u(1-u)\), the Fréchet–Hoeffding bound proves the exact global infimum \(\operatorname{Var}[(z(U)+z(V))/2]=1/2880\) over **all** bivariate couplings with uniform marginals, not only deterministic reflections. The half-cell reflection realizes this bound. Uniform \(C^2\) interpolation remainders make the copula comparison stable as mesh size tends to zero. Independence across cells and a Riemann-sum limit prove the sharp \(1/11520\) constant. The comparison constants and quadratic exactness follow directly. Exact-rational verification of multiple mesh sizes and a cubic asymptotic check passed. The calculations do not substitute for the all-coupling proof.

## Originality — PASS, qualified

The half-cell reflection is already a special case of the local dyadic folding transformation studied by Owen (2008); classical countermonotone covariance minimization is also established. Kunsch's (2023) stratified control variates employ independent samples on local interpolant residuals. The assessed claim is restricted to the exact variance-optimal two-sample residual coupling at the same evaluation budget, with all-\(C^2\) leading constants and an exact quadratic witness. The key full-text sections of both papers were read and compared by implication. Accessible prior scientific results concerned other stratified allocation, random trapezoid coupling and graded quadrature objects, not this paired residual copula optimum. Absence of a match does not prove priority. A specialized antithetic or cubature source could still cover these constants.

## Value — PASS

This settles a concrete local sampling-design question for smooth interpolatory stratified Monte Carlo: the usual global antithetic reflection is worst among the three natural choices at leading order, while a previously known local reflection is optimal against **every** two-uniform-marginal copula inside the independent-cell class. The exact factor-eight and factor-sixteen improvements at equal residual-evaluation cost are potentially useful in variance-sensitive numerical integration and distinguish sampling-dependence design from improved approximation order. The finite quadratic witness and continuum optimality both matter; the finding does not claim a new convergence exponent.

## Sources, comparisons and residual risk

- Kunsch, arXiv:2309.09059, Section 2 and Section 4: stratified polynomial-control-variate method, probabilistic rates and experiments; no paired-copula optimum in those inspected sections.
- Owen, arXiv:0811.0528, Introduction, Section 3 and Section 6: local dyadic reflection is prior art, but the sharp interpolatory residual variance constants and their unrestricted within-cell coupling optimum are not stated in inspected passages.
- Classical Fréchet–Hoeffding countermonotone covariance bounds: a proof ingredient, not asserted as new.

Limitations are as stated in RESULT.md. The key unresolved risk is unknown specialized prior work deriving the same interpolation-residual constants or an implication stronger than this exact theorem.

Self-review: passed. Independent audit: not yet performed.
