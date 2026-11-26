# Independent mathematical audit

## correctness

PASS

The most recent global reset couples any two copies and gives the unique invariant renewal law with common age exponential of rate r. Between resets the staggered mean mode decays at rate two, giving the stated stationary means. Distinct endpoints contribute total rate one each to the local two-spin equation, and adjacent copies are handled by the coincident product C₀=1. A simultaneous reset contributes r[(-1)^d−C_d]. The bounded solution is the alternating particular solution r(-1)^d/(r+4) plus 4q^d/(r+4), since q+q⁻¹=r+2. On the even ring the two equal boundary values at 0 and N give the normalized sum q^d+q^(N−d) divided by 1+q^N; this tends to q^d at fixed d. Subtracting the product of means produces the alternating residual 4r(-1)^d/[(r+4)(r+2)²], also the signed variance of the common-age mean factor. This proves nondecay and positive even covariances. At d=1 the odd-distance sign expression is 1+q²+q−1>0; for d=2k+1 with k≥1 it is the sign of F_k(q)=q^k(1+q²)+q−1, a strictly increasing function with opposite endpoint signs. F_{k+1}<F_k on (0,1) and r=(1−q)²/q decreases with q, giving both the sign orientation and the strict ordering of the thresholds. If ε=1−q_k, then kε≤W(2k), so kε²=o(1). Taking logs gives kε+log(kε)=log(2k)+o(1); the inverse is 1-Lipschitz since the derivative of x+log x exceeds one. This gives kε=W(2k)+o(1) and the stated rate asymptotic. An independent full-generator solve at N=4,6 and r=0.4,1 reproduced the moments and covariances at every tested separation, with maximum errors below 2×10⁻¹². Replay: /workspace/branches/428fb69c-471c-4523-977a-fc32fc402a49/independent_ring_check.py. These four finite tests do not prove the infinite-volume formula or the exact sign results. The uploaded verifier was inspected, not run.

## originality

PASS

The supported distinct claim is the explicit connected-covariance profile and sharp sign hierarchy for fixed-phase synchronous checkerboard resetting. General renewal, unreset Glauber correlations and the stationary moment method are established tools. A later-catalogued exact raw-correlation result materially overlaps, including for a fixed reset phase; its sign theorem is for random-phase resets, where the raw correlation equals the covariance. That theorem does not give the fixed-phase connected thresholds. No earlier matching fixed-phase connected sign theorem was established in the inspected statements; this is not independent certification of priority.

## value

PASS

The common reset clock generates an explicit long-range covariance even after the site means are subtracted, despite nearest-neighbor copying between resets. The parity and exact distance-dependent sign thresholds distinguish that effect from short-range coalescence and from random-phase raw correlations. The finite-cycle profile and rate asymptotic quantify the phenomenon without implying a finite-cycle threshold theorem or thermodynamic phase transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
