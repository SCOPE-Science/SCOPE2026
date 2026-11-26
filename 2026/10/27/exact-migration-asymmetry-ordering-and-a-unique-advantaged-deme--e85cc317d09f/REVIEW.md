# Independent mathematical audit

## correctness

PASS

With parent types indexing rows, the survival map is F(q)=1-exp(-lambda Mq). Positivity follows by iterating above a sufficiently small positive Perron vector, since M is positive on the admissible interval and has spectral radius 1. Strict concavity along positive rays rules out two positive fixed points by scaling one to first contact; iteration from 1 gives the survival probabilities. For K=lambda diag(1-q)M, Kq<q componentwise by -p log p<1-p, so rho(K)<1, det(I-K)>0, and the interior fixed point is smooth. Differentiating and inverting gives the displayed typewise derivatives and the average identity, where the mixed terms cancel by the column sums. At balance the antisymmetric slope is lambda q0 p0/[1-z(1-s)]>0; a positive equal-component solution at d!=0 would require equal row sums, which are 1+d and 1-d. This fixes the sign everywhere and exchanging types proves evenness. Independently, for u=(q1+q2)/2 and v=(q1-q2)/2 the sum of the exponents gives (1-u)^2-v^2=exp(-2 lambda u); the derivative of (1-u)^2-exp(-2 lambda u) at q0 is -2p0(1-z). Substituting the antisymmetric slope and using smooth evenness verifies the curvature and O(d^4) remainder. At s=1, q2=1-exp(-lambda(1-d)u) decreases strictly from q0>1-1/lambda to 0 because u decreases and is bounded. The q1 derivative changes sign exactly once at that crossing; q1 on negative d equals q2 on positive d and cannot also maximize. Substituting the crossing into the sum and ratio of exponents gives the stated scalar equation and imbalance, and x+lambda exp(-x) is strictly increasing above log(lambda). The theorem is about an exact Poisson branching model, not finite-population fixation. Inspected RESULT.md, VERIFICATION.md and verify.py; the recorded 148 finite numerical comparisons plus curvature check were not rerun and are not used as proof.

## originality

PASS

Best of current knowledge for the exact, arbitrary-lambda fixed-trace ordering and fixed-lambda curvature, and the exact rank-one type-specific optimum and its location. Abbara–Bitbol already give the exact Poisson model, a comparison with the well-mixed case, and both the suppression and an advantaged-origin optimum at leading weak selection for two types. None of those statements controls the exact ordering between arbitrary imbalances or the shape and location of the maximum at every lambda>1. The closest catalogue theorems differ in migration symmetry, growth parameters, number of types or dynamical model.

## value

PASS

Holding the total exchange and the supercritical multiplier fixed isolates asymmetry in a natural two-type model. The exact comparison orders all balances rather than comparing only to perfect balance or expanding in weak selection. The rank-one result shows why a uniformly averaged objective and a fixed-type objective can favor different imbalances, and the exact curvature describes the near-balance loss at fixed parameters. These are usable model-level conclusions with clear boundaries, not empirical claims about biological fixation or arbitrary migration networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
