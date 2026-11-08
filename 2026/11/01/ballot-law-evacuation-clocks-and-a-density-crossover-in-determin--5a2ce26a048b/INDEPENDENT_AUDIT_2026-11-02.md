# Independent mathematical audit

## correctness

PASS

PASS: With the rightmost occupied site exiting in one update, parallel internal 10-to-01 swaps all act on disjoint adjacent pairs. An internal maximal pre-upstep-height particle must move and drop its preheight by one; if maximizers sit at the exit, a blocked penultimate occupied site provides the survivor at H-1. Every survivor has new preheight at most H-1; the only nonempty state that empties next is 0^(n-1)1 with H=1-n. Thus T=n+H for every nonempty state, including n=1 and all occupied. Reflection of Bernoulli ±1 paths under the running-height barrier gives the stated Q_p binomial formula; telescoping at p=1/2 gives the shells. Negative drift gives finite supremum and geometric gambler ruin law; zero drift Donsker/reflection gives |Z|; positive drift gives M_n-S_n=O_P(1) and binomial CLT. Fresh independent exhaustive synchronous states n=1..12 (8190 total) matched T, shell counts and weighted CDF at odds 1:2 and 2:1; finite tests support but do not replace the all-n proof.

## originality

PASS

PASS, qualified: The exclusion update is classical cellular automaton Rule 184, and ballot reflections, gambler ruin and Donsker CLT are prior tools. Tilstra–Ernst (1997) materially inspected in full arXiv HTML, especially §2 and §5.4, concerns stochastic-reservoir open-boundary steady-state profiles and mean travel times, not the last non-inflow Bernoulli particle departure distribution. Cividini et al (2013) study injected/extracted open TASEP shock walls, while Dorignac et al (2023) study continuous-time stochastic step-initial exit times. No directly covering finite zero-inflow clearance-time CDF and all-density crossover identified, but unindexed queueing/last-passage encodings remain possible.

## value

PASS

PASS: Evacuation duration is the natural transient invariant of absorbing deterministic traffic. The exact probability law at every road length and arbitrary Bernoulli bias, integer shells independent of road length for early times, and sharp p=1/2 tight/diffusive/ballistic fluctuation transition are substantial mathematical structures; not simply a routine enumeration of small roads.

The dated certificate retains the supplied scientific assessment, sources and limitations.
