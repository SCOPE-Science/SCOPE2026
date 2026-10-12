# Review

## Correctness
PASS. The fixed-point equation is exactly
\[
a(b-a^2)=c(c-1)(c+1).
\]
For \(c\ge2\), integrality of the base is therefore equivalent to the divisor condition. The proof checks both digit inequalities in the two cases \(a>c\) and \(a\le c\), so no formal divisor produces an invalid numeral. For fixed \(a\), admissibility is exactly a periodic congruence. The odd-prime-power local count is \(3\), while the \(2\)-power count is \(2,3,5\) in exponents \(1,2,\ge3\); Chinese remaindering gives the claimed density. Fresh exhaustive replay agrees with all formulas.

## Originality
PASS. The closest full primary comparison is the 2015 selected-base census of Wu, Dang, and Zhang. It explicitly lists cubic fixed points in bases \(2\) through \(16\), including several examples recovered by the theorem, but does not state a varying-base divisor parametrization. Hargreaves--Siksek give an exact fixed-point count only for exponent \(2\), not exponent \(3\). A193594 is a base-indexed attractor count rather than a digit-parameter theorem.

Formula-level and alias searches for two-digit cubic fixed points, perfect digital invariants, Armstrong-style fixed points, and the factor \(c^3-c\) found no equivalent or stronger accessible statement. Residual risk remains for unindexed recreational literature.

## Value
PASS. Cubic digit fixed points are a standard object in generalized happy-number dynamics, and finite-base censuses are explicitly published. The theorem replaces those isolated two-digit examples by a complete all-base normal form. It also yields two exact invariants not present in the inspected literature: \(\tau(c^3-c)\) for a prescribed trailing digit and a multiplicative prime-power formula for the density of admissible trailing digits at fixed leading digit. These expose a genuine divisor/CRT structure rather than merely recomputing a table.

Self-review: passed. Independent audit: not yet performed.
