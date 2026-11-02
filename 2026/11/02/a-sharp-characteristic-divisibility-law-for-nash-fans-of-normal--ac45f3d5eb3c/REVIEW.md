# Scientific review: characteristic-divisibility of toric Nash fans

## Correctness (C): PASS

The theorem is quantified over every integer \(n\ge3\) and every algebraically closed field of characteristic \(p\ge0\), with characteristic zero distinguished. The elementary division-with-remainder argument gives the *complete* Hilbert basis of the saturated semigroup. Three determinant formulas enumerate every admissible rank-three triple, with no three internal \(h_i\)'s independent. The minimum of an arbitrary linear functional in the dual cone is then computed separately for nonnegative and negative third-coordinate weight; the former has minimizer \((2,2,1)\), and the latter has exactly three candidate extrema. This establishes the Newton-polyhedron equality for **all** \(n\) and \(p\), not by a finite sample. Four explicit exposing weights certify its complete vertex list. Two different exposed triangular facets yield primitive interior normal rays \((n-1,n-1,-1)\) and \((n,n,-1)\), proving that the normalized fans differ whenever \(p\mid n\). The standalone exact-integer verifier ran successfully for \(3\le n\le24\) and ten characteristics. No reliance on floating-point polyhedral hulls or on partial enumeration as proof remains.

## Originality (O): PASS, with priority limits

The most relevant primary work is Duarte–Jeffries–Núñez-Betancourt, arXiv:2208.05599v1 (August 11, 2022), whose Theorem 1.9 is the necessary general logarithmic-Jacobian theorem and whose final section works out the exceptional characteristic-two **single case** corresponding to \(n=2\). Its results do not explicitly state the all-parameter Newton vertices, the condition \(p\mid n\) for all primes, or the moving interior fan ray. Atanasov–Lopez–Perry–Proudfoot–Thaddeus, arXiv:0910.5028, gives the characteristic-zero toric Nash polyhedral method and tables for particular cones, including \(n=3\) and \(n=4\), but no prime-characteristic counterpart. Duarte–Núñez-Betancourt, arXiv:2002.07081, studies higher Nash blowups and an \(A_3\) toric surface, not this ordinary-Nash threefold criterion.

The general Nash–monomial-ideal theorem logically supplies an algorithm for any selected \(n,p\), so the new contribution is **not** a new general Nash theorem: it is the closed, sharp infinite-family classification obtained by an additional support-function argument. Comparisons with mathematical research records found no equivalent published parameter-family result. An unindexed or unpublished computation could precede it; independent priority review has not occurred.

## Mathematical value (V): PASS

The source identifies a dimension-three positive-characteristic breakdown at characteristic two, after proving complete characteristic independence in dimension two. An exact criterion for the entire primitive-height family answers a natural structural follow-up: it shows that **each prime** is an obstruction in dimension three, isolates the exceptional primes by divisibility of the cone height, and computes the size and lattice direction of the fan change. This is a parameter-uniform wall-crossing classification, not merely the same two-dimensional theorem with substituted coefficients or one extra finite example. No claim is made about higher iterations or universal threefold resolution, which would require different arguments.

## Scope and residual risks

The primary full text was compared at the characteristic-\(p\) ideal theorem, the surface-independence result, and the displayed threefold example. The earlier characteristic-zero paper was inspected at the polyhedral theorem and its sample-cone tables. The higher-Nash paper was checked for its announced objects and main results, without claiming a negative full-text search beyond what was inspected. The priority risk of an unindexed equivalent generalization remains. Normal fans are compared relative to the fixed base cone; abstract isomorphism types and smoothness of Nash blowups are outside the theorem.

Self-review: passed. Independent audit: not yet performed.
