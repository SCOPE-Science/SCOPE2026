# Review

## Correctness

PASS. Exact elimination of the first-moment and gradient-difference EMA states gives the displayed cubic. Substitution of the paper defaults reduces the cubic Schur conditions to explicit rational inequalities; the active one is \(s<19800/859\), and equality makes \(r=-1\) a root. The squared adaptive state contributes eigenvalue \(0.99\) because its innovation is quadratic at the minimizer.

Risk: the theorem is asymptotic local analysis after bias corrections approach one.

## Originality

PASS. The defining Adan paper provides the Nesterov momentum estimation mechanism and global stochastic complexity theory but does not state this local deterministic cubic or its exact default-parameter stability ceiling. Public implementation notes clarify the coefficient-convention reversal but do not give the Schur analysis. Focused searches over Adan quadratic stability, characteristic polynomials, gradient-difference local dynamics, and exact learning-rate frontiers found no covering statement.

Residual risk: a generic multistep-control analysis may contain an equivalent cubic under non-Adan terminology.

## Value

PASS. Adan is explicitly motivated by large learning-rate tolerance. The exact local calculation identifies a complementary limitation: once the adaptive denominator has decayed to its epsilon floor, the default Nesterov-difference channel has a sharp period-doubling ceiling. The comparison with the same first-moment recurrence without the gradient-difference channel quantifies an \(8.59\)-fold reduction, making the result directly relevant to late-stage tuning and implementation diagnostics.

Same-model review: passed. Independent audit: not yet performed.
