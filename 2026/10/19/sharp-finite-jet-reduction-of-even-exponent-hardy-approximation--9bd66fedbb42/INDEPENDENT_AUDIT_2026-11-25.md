# Independent mathematical audit

## correctness

PASS

Re-audit of repairs/1/RESULT.md. The frozen proof of the optimal universal replacement degree only rules out smaller jet-matching products; it does not in that step rule out smaller objective-equivalent products without that jet. This is a proof gap, not a counterexample. The repaired proof supplies the converse: writing q=Σaᵢzⁱ, only the (m,m−1) binomial term has that bidegree in (a,ā). Its coefficient of a₀^m∏āᵢ^bᵢ is −m (m−1)!/(∏bᵢ!) times the Taylor coefficient f_{Σ i bᵢ}, with Σbᵢ=m−1. Equality on all complex a entails equality of these formal coefficients by invertible change to real and imaginary coordinates, and all degrees 0 through (m−1)n are representable. This includes m=1 via the empty sum and n=0 via the all-zero frequency. Consequently f=z^(L+1) forces any objective-equivalent Blaschke product to vanish to order at least L+1. For sufficiency, boundary inner modulus cancels each paired power and the test polynomial q^k has degree at most kn; Parseval gives the cutoff and binomial objective. Strict convexity and coercivity give a unique minimizer. Inverse Schur steps insert one order of agreement per step and increase finite degree by at most one; a unimodular terminating iterate is already finite. The original sharp-cutoff witnesses differ by −4m for L>0; constants suffice for L=0. Frozen verification scripts and recorded quadrature and difference output were inspected, not executed. They do not test the repaired converse, which is proved by coefficient extraction.

## originality

PASS

Reassessed for the repaired proof of the same claim. The distinct statement is the full even-Hardy objective invariant for arbitrary degree, now also shown to determine the required jet, with exact cutoff and the optimal degree among all objective-equivalent Blaschke products. Classical Schur interpolation supplies the jet-fitting ingredient, and the H² and low-degree optimizer subcases are not relied on as new results. No stronger inspected statement establishes the audited family.

## value

PASS

Reassessed for the repaired finding. An infinite or singular inner input can be replaced uniformly for every admissible trial polynomial by a sharply bounded finite Blaschke model, not just by an approximation to the optimizer. The exact cutoff and the converse identify precisely the information visible to the entire objective; the lower bound among all objective-equivalent replacements guarantees that the compression is optimal in the worst case. This is a useful finite reduction of a natural nonlinear approximation problem, without claiming a closed-form solution of the remaining optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
