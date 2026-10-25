# Independent mathematical audit

## correctness

PASS

For each simple connected tree T on n>=4, inclusive half-neighbour activation from one seed is monotone. At every step active vertices are connected; for any initially unseeded hub (degree>=3), all active vertices stay on one side of its removal and so at most one neighbour can be active; it never activates. Every low-degree path component K_j of size m_j activates in full when seeded there, while a hub seed activates itself and all incident low-degree components. Thus sum_v C_T(v)=|H|+sum_j(m_j^2+b_j m_j)>=2n-|H|>=2n-floor((n-2)/2). First equality holds iff every K_j is a single leaf; second iff hub count maximal. Degree excess identity fixes all hubs cubic for even n and exactly one quartic for odd n. Constructing hub skeleton trees with attached leaves shows attainment. Independently enumerated unlabeled trees n=4..10 and all seeds; minima were 7,9,10,12,13,15,16 as expected. This independently checks boundary n=4 and parity cases. No stochastic edge transmissions assumed.

## originality

PASS

A precise prescribed-order deterministic tree mean-cascade extremum and all optimizer degree patterns; prior vulnerable-component mechanism is credited.

## value

PASS

The quantity is a natural expected final outbreak size for one uniformly random seed, and optimization at fixed tree order is a meaningful structural extremal problem. Exact optimal value and complete equality cases reveal that maximizing branching hubs, not a star, minimizes mean cascade. The extremal threshold and equality classification are not a routine restatement of the vulnerable-degree condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
