# Independent mathematical audit

## correctness

PASS

Squaring the score condition gives |a_ij|²≤epsilon(|d_i−d_j|+epsilon). Independently, for t=max d_i and C=Delta² epsilon, let r_i=t+C−d_i. For every edge, r_i r_j≥C(C+|d_i−d_j|)≥Delta²|a_ij|². Scaling (t+C)I−A by diag(r_i^(−1/2)) on both sides therefore gives unit diagonal and off-diagonal absolute row sums at most one. This is Hermitian positive semidefinite and confirms the frozen edge-block proof. The same argument for −A and for principal subsets of the lowest n−k+1 and highest k diagonals gives both bounds by interlacing, with no restriction on ties. In the complete bipartite example the cross-block all-ones matrix vanishes off the two constant-vector directions; there the 2-by-2 block has gap H and coupling Delta sqrt(epsilon(H+epsilon)). Its upper shift divided by epsilon tends to Delta² as H increases, and a scalar shift makes the full matrix positive definite. Degree zero and tolerance zero both reduce to a diagonal matrix. The frozen verifier was read, not run; it generates instances satisfying the score condition by construction and checks finite numerical consequences.

## originality

PASS

The score and all-index certification problem are prior work. The supported distinction is the optimum current-maximum-degree multiplier, with matching sharpness and general Hermitian scope, rather than a new score or a new diagonal scaling technique. No inspected prior statement supplies that degree law.

## value

PASS

The certificate yields uniformly bounded absolute error for sequences with bounded current support degree and growing order, using only local scores and degree. The sharpness family makes the quadratic degree dependence necessary, even for positive definite inputs. This is an actionable improvement in the stated regime, not simply a proof of the dense estimate by a new method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
