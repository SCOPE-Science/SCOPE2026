# Independent mathematical audit

## correctness

PASS

For the sign convention exp(+εI), the uniform centered Mallows score is Z=I−E[I]; the PL score is S_i=1−H_n+H_{n−R_i}. The first-choice term is strictly convex on centered log-weights, all later terms are convex, and positive target mass on rankings beginning with a minimum-weight item gives a cross-entropy lower bound proportional to the log-weight range. Hence the minimizer exists and is unique on the centered subspace; the positive Hessian and implicit function theorem give its local expansion. The quadratic KL term is E[(εZ−θ·S)^2]/2 by a Taylor expansion of normalized smooth families (PL need not be treated as a joint exponential family). Uniform selection-stage martingale increments give G_ii=(n−H_n)/n, and the centered eigenvalue is (n−H_n)/(n−1). Conditioning Z on a label's rank and summing against S_i gives b_i=(i−(n+1)/2)/2; the inversion variance then yields the stated coefficient and derivative. At n=2 the families coincide. At n≥3, swapping the same two labels at two different adjacent ranks changes the inversion score by one but a linear combination of PL scores by a label difference divided by two different stage sizes, proving the residual is positive. The harmonic asymptotic gives n³/288 for the coefficient, not a uniform ε expansion.

## originality

PASS

The supported contribution is the all-size directed local KL coefficient and the associated first-order PL fit, not the families themselves, the standard Fisher projection method, or qualitative non-representability. The inspected comparisons do not give those quantities or mechanically imply them.

## value

PASS

The result quantifies the error and gives the optimal first-order calibration when replacing a Mallows law with the computationally convenient item-weight family near uniformity. In particular it detects positive quadratic loss already at three items, below the range of the cited broader non-representability theorem, and gives a usable scale as n grows. It does more than establish that the families differ or report finite fit experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
