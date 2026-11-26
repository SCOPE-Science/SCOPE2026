# Independent mathematical audit

## correctness

PASS

Replayed RESULT.md lines 33–102: the type finishing the first album has count one, so the bounded range gives Var≤(N−1)²/4 for every p and j≥2. With p_N=c/j, the first rare arrival divided by j tends to Exp(c). Given its waiting time G, common occupancies are multinomial with G−1 trials; their normalized centered mean-square errors are O(1/j) for each of the fixed N−1 types, including zero conditional error at N=2. Also the chance that any given common type is still missing when the rare type first arrives is p_N/(p_N+p_i), so the terminal time agrees with G with probability tending to one. The common counts divided by j tend jointly to the same exponential divided by N−1. It has no atom at one, so only deficits 1 and N remain in the limit, with probability e^(−c(N−1)) for 1. Boundedness gives both moment limits; c=log(2)/(N−1) attains the universal envelope asymptotically. Any fixed positive vector instead gives almost-sure eventual deficit N. Independently reproduced both finite laws without running checker.py: independent Poisson streams, summing over the last type k and integrating its first-arrival density p_k e^(−p_k t) times the common-type count factors for 1≤count<j or count≥j. Exact rational integration gave laws on (1,2,3) of (17/108,35/108,14/27) and (272569/656100,185131/656100,1984/6561), hence variances 707/1296 and 416326091/590490000, difference 5887451/36905625. The finite example does not prove the limit or claim a finite-j maximizer.

## originality

PASS

The closest known results share the deficit observable or the coupon-variance theme, but not the claimed fixed-N triangular-array variance limit or its sharp supremum. In particular, Long does establish a deficit-variance asymptotic in a different regime (fixed j, growing N, uniform probabilities). The strongest indexed variance overlap is for N=3 and j=2, not the growing-j theorem; catalogue dating is not used to infer priority.

## value

PASS

The range bound is classical, but the result identifies an admissible, explicit array that asymptotically attains it for every fixed N and gives the full tunable two-atom limit. It separates fixed-law behavior, mean extremality, and variance optimization in a natural coupon model; the exact three-type example shows the distinction already at finite j.

The dated certificate retains the supplied scientific assessment, sources and limitations.
