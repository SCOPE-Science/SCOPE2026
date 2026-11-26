# Independent mathematical audit

## correctness

PASS

The exact sampled update is linear in the three-coordinate state, and independence of the next draw gives closed evolution by the mean matrix. The frozen roots 0, 1/2 and 1/(1+c) are strictly in the unit disk even when the last two coincide. The mean quadratic has α=(b+3)/(4(b+1)) and β=(b−1)²/(16(b+1)); for b>10 the three strict Schur inequalities reduce to β<1, or b<9+4√6. Independently eliminating the estimator on the alternating path gives modes r=−(b−2)/4 and s=b/[2(b+1)] and the stated first-coordinate projections (python /workspace/review_evidence/reproduce_1234.py 1). Since |s/r|<1 and the r-mode projection is nonzero, eventually the magnitude is at least |r|^n/[(b−1)(b+2)]. Squaring and multiplying by event probability 4^(−n) yields the advertised lower bound on the even subsequence; its base exceeds one for b>10. At b=14 the secondary/primary ratio is at most 105(7/45)^3<1/2 for all n≥3 and the bound is exactly as stated. The objective is a positive multiple of x². No almost-sure conclusion, all-initial-data claim or full mean-square frontier is implied.

## originality

PASS

The SPAM recursion, exact first-moment criterion and general possibility of a separation between moment stability notions are prior. The supported distinct contribution is the explicit expected-loss instability on a nonempty open interval for this same exact SPAM recursion, with both frozen-client maps and the full mean stable.

## value

PASS

Frozen and full-mean stability are tempting diagnostics for a stochastic proximal algorithm. The two-client, shared-minimizer counterexample shows they fail to guarantee decreasing expected physical loss, on an open interval rather than only a tuned instance. It ties the failure to a specific rare switched product and quantitative observable growth, without claiming to falsify the source's sufficient guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
