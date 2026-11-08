# Independent mathematical audit

## correctness

PASS

With r occupied particles and hub occupied, total jump rate r and collision success probability p=(r−1)(n+1)/(nr), while a failed hub-to-empty-leaf move empties the hub and is followed by one Exp(r) return without a collision. Thus a successful stage has 2J+1 independent Exp(r) waits, J geometric(q), q=(n−r+1)/(nr). Conditional success at hub-to-occupied leaf occurs with probability 1/(n+1) independent of holding times; each such success introduces a Bernoulli(1/(n+1)) Exp(r−1) hub-vacancy delay. Independent stages and delays yield the exact finite product Laplace transform and Eτ=H_n+1−(H_n+2)/(n+1). Coupling q_{n,r}≤1/r by shared geometric trials yields L1 difference <=(3H_n−1)/(n+1) from sum of limiting independent S_r. Since their variances sum, the centered series converges almost surely/L2; finite gamma-product telescoping establishes the Laplace transform Γ(1+s)∏_{r≥2}[(r+s)(r+s−1)/((r+s)^2−r)]. Summing exact second and third cumulants gives variance π²/2−1 and κ3=14+14ζ(3)−2π², excluding affinely scaled Gumbel. Independent exact rational full-subset Markov generator solutions reproduced means for n=1..4 (1/2,4/3,15/8,34/15); sympy partial fractions cross-check cumulant summations. Finite checks do not certify infinite limit.

## originality

PASS

Best-of-knowledge qualified: the final statement is not shown to be equivalent to, an implication of, or covered by the materially inspected prior primary statements. General background and known subcases are credited explicitly; inaccessible plausible primary literature is a documented priority risk, not automatic scientific failure.

## value

PASS

The exact all-n coalescence-time transform and centered non-Gumbel limit solve a natural quantitative benchmark left open by the known logarithmic lower bound for star coalescence. The explicit cumulants distinguish it from coupon-collector/Gumbel heuristics and give reusable insight into coalescence on highly inhomogeneous graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
