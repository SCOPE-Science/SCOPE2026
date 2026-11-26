# Independent mathematical audit

## correctness

PASS

For sorted EF1 bundle values x<=y, removing the largest good in the larger bundle is the best possible single deletion; its value is <=h, so x>=y-h and x>= (V-h)/2. This also covers a tie or a largest good outside the larger bundle. Monotonicity of x(V-x) up to V/2 yields xy>=(V^2-h^2)/4. For h>=V/2 the bundle containing a largest good has load z>=h, so z(V-z)<=h(V-h), attained by isolating that good (always feasible in the unrestricted benchmark). Dividing and taking a square root gives the claimed bound. At every prescribed delta, the first two entries of (q,q,h), q=(V-h)/2, must split under EF1, and either last assignment leaves EF1, so every feasible trajectory has product q(q+h) versus 2qh offline. This applies pathwise to randomized as well as clairvoyant policies. The least-loaded assignment preserves EF1 since deleting the new good from its bundle leaves a pre-arrival load no larger than the other one; increasing a bundle cannot give its recipient new envy. Below delta=1/2 the unrestricted product is at most V^2/4, so the ratio squared is at least 1-delta^2>3/4. Above it the sharp squared ratio is strictly greater than 1/2 and tends to 1/2 as delta tends to one. With exactly two positive goods EF1 forces a split and reaches the offline optimum; the three-good witnesses have strict loss, even at the boundary delta=1/2.

## originality

PASS

The supported distinct claim is the exact dominant-item curve on 1/2<delta<1, and its sharp, all-policies three-arrival obstruction giving the two-agent universal infimum. The small-item formula at and below the boundary, the static boundary witness, temporal EF1 feasibility and the existence of some temporal welfare loss all have verified earlier or adjacent coverage and are not the basis for the pass.

## value

PASS

Largest-item fraction is the natural boundary at which isolating that item is always the offline optimum. The result specifies the exact loss throughout that regime and shows a minimum-length witness that no lookahead or randomization can circumvent. It quantifies what is lost by retaining EF1 at every arrival, rather than merely observing that a particular greedy rule can miss optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
