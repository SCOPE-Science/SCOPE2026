# Independent mathematical audit

## correctness

PASS

The B odds multiply by 1/epsilon. With D_k=p+(1-p)epsilon^k and D_0=1, its current-policy value is D_(k+1)/D_k, so the A odds are R_0(gamma/r)^k D_k. The sign of their difference is that of p(gamma-r)+(1-p)epsilon^k(gamma epsilon-r). At r<=gamma epsilon it is strictly positive and at r>=gamma strictly negative, including the endpoints. In between its sign is that of tau-epsilon^k, so the ceiling formula is correctly indexed and equality produces exactly one flat update (also at the start if tau=1). For small p, epsilon^K/tau is confined between epsilon and 1, while tau is of order p; substituting into the odds gives the claimed positive exponent 1-log(gamma/r)/log(1/epsilon). The specified family yields tau=4^(-N), q_N=q_(N+1) with the stated rational expression, and optimal-continuation gap 3/8 throughout, even though the current-policy gap is negative during suppression. At fixed old B value the A update increases value by the two-action variance of the Q values divided by the old value, possibly zero at equality. Replacing the old B value by the strictly larger new value then increases A value strictly since the delayed action retains positive mass.

## originality

PASS

The general Q/V update, product-of-Q formula, and value monotonicity are prior. The supported distinction is the worked two-stage fixed-gap construction with arbitrary suppression depth and duration, together with its exact one-turn law and small-support exponent. The closest analogous suppression theorem inspected uses softmax gradient steps, not this update; the cited general reweighting identities alone do not assert the construction or scaling. This is a best-of-knowledge decision, not a priority certificate.

## value

PASS

This separates value improvement from retention of optimal-action support in a minimal sequential example for an exact update. Arbitrarily many decreasing steps and an arbitrarily deep trough at a fixed positive optimal Bellman gap make this more than a one-step reversal or a vanishing-gap example. The exact turning and trough laws identify the support parameter that controls the effect and give a benchmark for analysis of iterative reweighting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
