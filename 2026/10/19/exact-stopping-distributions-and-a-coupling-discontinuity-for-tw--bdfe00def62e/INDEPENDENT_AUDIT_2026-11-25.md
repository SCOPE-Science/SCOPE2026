# Independent mathematical audit

## correctness

PASS

For the repaired variant in repairs/4, not for Algorithm 1 as literally printed. The frozen attribution of the zero-quotient rule to the algorithm's iteration was unsupported: Algorithm 1 steps 3 and 6 have unqualified denominators, while the explicit 0/0 convention is attached to the expected matrix in Eq. (15). This is material on events of positive probability: with H=[[2,1/3],[1/3,3]], initial error (1,2), and labels 1,1, the first projection gives (−1/3,2), and the second direction is zero while the error is not. The repair states both zero-quotient rules and explicitly stores the zero direction and counts that draw. Verified the sign change from r=b−Ax and d=−p^k, the line-search numerator identity using orthogonality to the preceding direction, and all four coupled-state transitions. The different label from an active state supplies the second H-orthogonal independent direction and reaches zero; the repeat clears the direction. The label block 1,2,1 forces termination from any nonterminal state, giving a geometric tail. Eliminating the inactive generating functions yields the displayed denominator (1−pz)(1−qz)−(pq)^2 z^4 and numerator. For the means, f_i=1/p_j+p_i f_j gives 1+1/(pq) from the initial state, while the diagonal coupon-collector mixture gives 1/(pq)−1. A coupled coordinate projection preserves both nonzero coordinate errors, so the coordinate-descent contrast holds along every label sequence. The norm-proportional mean and uniform optimum follow by algebra, using b₀ for the second diagonal entry. Repaired RESULT.md, VERIFICATION.md and verify.py agree on the new scope and idle rule. Inspected the checker without executing it; the proof applies beyond its finite cases.

## originality

PASS

The assessed claim is the exact iid-coordinate stopping law for the explicit idle-and-clear extension of RCGLS. Existing exact completion with consecutively nonzero independent directions, general mean-square bounds, and the diagonal coupon-collector identity are not claimed new. The coupled law and its comparison with zero coupling are not supplied by the strongest inspected alternatives.

## value

PASS

The explicit continuation is natural when a zero direction should leave the iterate unchanged while the algorithm stores its new direction. Its exact two-update mean discontinuity reveals a distinction invisible to convergence-rate analysis, and its uniform sampling optimum contrasts with the usual norm-proportional choice for this exact hitting criterion. These are useful qualifications about idle handling in a minimal nontrivial model; no practical timing or tolerance advantage is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
