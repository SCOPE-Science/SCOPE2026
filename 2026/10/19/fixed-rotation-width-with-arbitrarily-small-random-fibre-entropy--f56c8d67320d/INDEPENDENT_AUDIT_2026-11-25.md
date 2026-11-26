# Independent mathematical audit

## correctness

PASS

For finite Delta>0 and integer K>Delta/2, p lies strictly between 0 and 1. The number N_n of active symbols satisfies N_n/n -> p on a single full-measure set; the lift composition is exactly G_K^N_n. Every active displacement lies in [-K,K], while 1/4 and 3/4 are fixed modulo 1 with lift increments K and -K; integrality and G_K(x+1)=G_K(x)+1 make these increments persist. This proves the two extremal limiting velocities and bounds all possible velocities, and the applicable LLR Theorem 2.1 supplies the interval property. The uniform displacement bound verifies its integrability hypothesis. The random n-observation Bowen metric uses exactly the deterministic observation indices 0 through N_{n-1}; M_n=N_{n-1}+1 tends to infinity, eventually takes every integer, and M_n/n -> p. Thus the separated-set limsup at each scale is precisely p times the deterministic one, including the necessary subsequence direction. On [0,1/4] the lift strictly increases from 0 to K+1/4, so the inverse images of [j,j+1/4], 0 <= j <= K, are disjoint compact branches with a positive gap and all map onto [0,1/4] modulo 1. Nested inverse images yield (K+1)^n points separated at a fixed positive scale. Conversely arcs of length less than epsilon/(1+2*pi*K)^(n-1) give a separated-set upper bound of order (1+2*pi*K)^(n-1)/epsilon. These prove both entropy bounds, positive for each K, and even give asymptotic equivalence to Delta log(K)/(2K) as K tends to infinity. Read but did not execute the frozen finite consistency checker; it does not certify the infinite results.

## originality

PASS

The retained obstruction is to a positive bound for the whole quenched fibre entropy at each fixed positive width. Neither the directly compared positivity theorem and fixed-width example nor the adjacent restricted-entropy and rotation-spectrum results establish it. The elementary identity-step clock is not claimed independently as a new general technique.

## value

PASS

This is a motivated quantitative boundary for a recent qualitative positivity theorem: even analytic iid generators with any prescribed positive width give arbitrarily small whole-fibre entropy. It identifies which apparently natural parameter is insufficient and why recurrence or uniform generator control may matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
