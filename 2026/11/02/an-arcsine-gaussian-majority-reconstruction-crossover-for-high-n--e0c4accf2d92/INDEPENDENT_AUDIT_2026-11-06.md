# Independent mathematical audit

## correctness

PASS

For each finite star, couple the original stationary process to a decoupled hub with the same hub resets and leaf update clocks. During [-T,0], no hub-copy events (probability of failure <=T), a common hub reset in the first half, and every leaf updated in the second half force exact full-configuration coalescence. This proves TV <=T+(n+1) exp(-theta T/2). Stationary decoupled hub-filter PDMP has zero flux, Beta(a,a) marginal with a=theta/[2(1+theta)], and Bernoulli hub conditioning. Conditional leaf-count Binomial(n,1/2+(Y-1/2)/(1+theta)) and uniform characteristic functions prove all three theta/sqrt(n) limits when theta/log n ->infinity. Integration yields S(lambda), with derivative -lambda^-2 E[A^2 phi(A/lambda)]<0 and first endpoint 1/2+1/pi. Independent exact CTMC stationary calculations for n=2..4 and beta mixture TV corroborated algebra; these do not prove asymptotic.

## originality

PASS

The exact joint high-noise star stationary configuration approximation and majority arcsine-Gaussian crossover go beyond known fixed-noise star mixing bounds, known two-state PDMP Beta formulas, and general pair moments. General coupling/CLT ingredients are credited; no failed-search-to-novelty inference.

## value

PASS

The fixed-marginal noisy-voter star is a natural test for whether many leaf observations recover a hub under strong independent rerandomization. The exact theta~sqrt(n) crossover and explicit, strictly decreasing reconstruction probability identify a nontrivial inference signal/noise transition with a quantitative full-law coupling; neither a routine moment identity nor arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
