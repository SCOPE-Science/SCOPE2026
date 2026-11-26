# Independent mathematical audit

## correctness

PASS

For viable sizes a=q−j, b=q+j the original-degree restriction is nI−A(K_{a,b}). If both parts are nonempty the all-ones directions give a two-by-two block with diagonal n and off-diagonal −√(ab); the within-part zero-sum vectors have eigenvalue n. If one part is empty the restriction is nI. This proves λ=n−√(q²−j²) and both extrema by strict monotonicity in |j| over its feasible range. The allocation law follows by counting uniformly drawn fixed-cardinality subsets; the hypergeometric variance is mq/(2n−1). The CLT applies because sample and complement sizes are both proportional to n and the success fraction is 1/2. Rationalizing the spectral deficit gives X=λ−m=J²/(q+√(q²−J²)); the denominator is 2q(1+o_P(1)). Therefore X converges to (ρ/4)Z². Hoeffding's bound for sampling without replacement gives P(|J|>t)≤2exp(−t²/m), so X≤J²/q has uniformly bounded moments of order larger than two when q is proportional to n. This proves the claimed mean and variance limits. The nonlinear test is strict: a positive principal vector φ gives H′≤(r−Dλ)H−rH²/∑φ, including equality and the case nI. Above threshold εφ and large constants give ordered positive sub- and supersolutions of the cooperative ODE. If two positive equilibria differed, scaling one by θ>1 until first touch with the other yields f_i(u)≤f_i(θv)=−rθ(θ−1)v_i²<0 at a touching coordinate, contradicting equilibrium. Monotone comparison then gives attraction for strictly positive initial data. The event X<c is therefore exactly persistence, yielding the stated error-function limit for c>0 and zero at c≤0. These steps verify RESULT.md lines 48–112 analytically. The packaged finite checker is supplementary and was not executed.

## originality

PASS

Credit the exact random-placement critical window, including the coefficient and moment limits, and its consequence for persistence; the grounded rank-two reduction, logistic threshold and hypergeometric CLT are standard ingredients. The strongest indexed matrix match supplies the same balanced grounded block, hence the finite spectrum, but studies inverse trace at deterministic allocations rather than the law of the smallest eigenvalue under uniform fixed-size sampling. The closest inspected habitat paper proves a first-order random-edge concentration law, not this order-one fixed-graph fluctuation.

## value

PASS

At the same fixed sink budget the comparison identifies a precise order-one random penalty relative to optimal allocation, while the worst placement costs order n at positive limiting sink fraction. The non-Gaussian distribution quantifies the actual persistence probability when the growth-to-diffusion ratio is tuned within O(1) of the best threshold, where first-order concentration supplies no answer. It is a useful structured-habitat benchmark without claiming the same window for general graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
