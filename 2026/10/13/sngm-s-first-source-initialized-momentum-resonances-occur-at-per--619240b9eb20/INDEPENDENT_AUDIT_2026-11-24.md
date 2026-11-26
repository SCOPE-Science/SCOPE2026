# Independent mathematical audit

## correctness

PASS

The source Algorithm 1 initializes zero momentum, adds the normalized gradient to β times momentum, and uses that full new momentum for the parameter step. Under the stated deterministic scalar quadratic and away from zero this is exactly the frozen map. For a proposed p-step word s, set U_p=Σ_j s_j β^(p−1−j) and C_p=Σ_{i=1}^p U_i. Telescoping the momentum recurrence gives Σ_j s_j=(1−β)C_p+βU_p. Therefore a return on (0,1) is equivalent to a balanced word with U_p=0 plus sign feasibility. Odd p are impossible. For a reproducible independent exact check, fix the initial sign +, choose p/2−1 other positive signs among indices 1,...,p−1, form U_p in QQ[β], divide out all β−1 factors, and count roots in (0,1) (e.g. Poly.count_roots(0,1); neither endpoint is then a root). For p=2 the only quotient is 1. For p=4 the quotients in lexicographic order with + first are (β+1)^2, β²+1, and β+1. For p=6 the ten quotients in that order are (β²+β+1)^2; β⁴+2β³+β²+2β+1; β⁴+2β³+β²+1; (β²+β−1)(β²+β+1); β⁴+β²+2β+1; (β²−β+1)(β²+β+1); β⁴+β²−1; β⁴−β²+1; β⁴−β²−1; (β²−β−1)(β²+β+1). Only the fourth and seventh have roots inside (0,1), one each. The exact cumulative displacements there are respectively (0,1,φ²,φ²,φ,0,0) and (0,1,β,φ,1/β,0,0); signs of r−C_j for r=x_0/η give the asserted strict intervals, with all x nonzero. The balanced signs cancel r in the absolute-position sum, giving 1+3φ and 1−β+φ+1/β before multiplication by aη/6. Minimality follows from the nonexistence of any shorter return; global sign change covers x_0<0. The exact reduced enumeration and algebraic replay are independent of the frozen verifier, which was read but not run. It uses ordinary double precision for representative trajectory replay, and its period-six candidate assertions alone do not rule out every other factor. No claim is made about longer periods or nonzero initial momentum.

## originality

PASS

The source gives the precise recurrence and stationarity bounds, not the shortest-return classification. The strongest indexed lookalike is scalar Signum, whose ordering of gradient normalization and momentum changes the map. Other inspected cycle and relay sources do not provide the exact discrete source-return classification. The decision concerns the deterministic zero-initialized full state, exact smallest period, and exhaustive pair of first resonance parameters; it does not claim novelty for generic step-size floors or oscillations of momentum methods.

## value

PASS

This determines a natural first-event cutoff, not merely a sample orbit: it rules out every shorter zero-momentum return for all admissible β and identifies every parameter and interval at the first feasible length. The two explicit resonances realize a positive mean-gradient scale proportional to η in the simplest strongly convex model derived from the stated algorithm. This is a diagnostic against fixed-step convergence to the minimizer, not a claim about attraction, stochastic behavior, or all larger periods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
