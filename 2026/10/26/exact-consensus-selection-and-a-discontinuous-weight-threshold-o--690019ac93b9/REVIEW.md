# Research review: weighted-median star consensus selection

## Correctness
PASS. Leaf opinion differences are exactly exponentially contracting. Their weighted median endpoints are fixed ranks and follow hub-driven scalar equations. The hub’s closest-admissible median is exactly the projection onto that interval, including the zero-self-weight tie case. Solving the three invariant regions gives the displayed exact consensus, with a separate rational check of the discontinuity. The included script passes independent vector-field residual tests; the all-size statement rests on the proof, not numerics.

## Originality
PASS, subject to bibliographic limitations. Han, Chen, Dörfler, and Mei (2024), arXiv:2404.16318v1, prove global convergence and characterize equilibria. The later Han, Hendrickx, Chen, and Mei revision (v3) adds control analysis. Neither inspected relevant full-text discussion provides an arbitrary-weight star’s exact limit as a function of initial opinions or the half-weight discontinuity. A general existence or consensus theorem does not select this specific limiting value. The prior discrete-time 3-node weighted-median switching question is different; the present continuous-time flow is separately derived. Specialized unindexed prior coverage cannot be excluded.

## Mathematical value
PASS. The theorem completely solves an explicitly motivated hub-and-spoke network with any finite number of leaves and any positive hub-to-leaf weights, identifying its final opinion rather than only its convergence. The sharp half-weight discontinuity gives a concrete robustness boundary for influence calibration, even though interaction support and convergence are unchanged.

## Limitations
The row-stochastic star structure and closest-admissible-value tie convention are essential. This does not generalize unconditionally to arbitrary influence networks, asynchronous rules or time-changing weights. Independent validation is not represented.

Self-review: passed. Independent audit: not yet performed.
