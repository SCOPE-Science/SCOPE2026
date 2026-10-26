# Self-review

## Correctness — PASS

The theorem is proved by identifying rim configurations with a cyclic binary polynomial quotient and writing the exact joint rim/hub map. The factor \((z+1)^k\) in \(z^n+1\) isolates precisely the nilpotent primary summand; the remaining summand is invertible. For odd \(n\), the hub and rim parity swap while the zero-parity rim evolves invertibly. For even \(n\), direct composition gives \(F_n^3(x,h)=(B^3x,0)\). The first two ranks are evaluated separately, and all later ranks follow from multiplication by \((z+1)^{2t}\). The binomial basin factor, sharp transient and polynomial-gcd fixed-point formula follow from this decomposition. The supplied program independently checks 1,195 rank instances, 1,160 temporal fixed-point comparisons, and complete original-state trajectories for 8 wheel sizes. The finite checks do not substitute for the parameter-uniform proof.

## Originality — PASS (bounded by accessible sources)

Klaus Sutner's 1988 *Additive Automata on Graphs* establishes the XOR graph rule and investigates reversibility; his Section 4 treats general reductions and other graph classes, rather than the full wheel recurrent spectrum. Ciandrini et al. (arXiv:0809.1526, first submitted 2008-09-09) derive general XOR network laws and maximum-period principles, concentrating on random interaction graphs and feedback components; their formulas do not state the wheel's parity-dependent sharp preperiod, rank sequence, or all-time gcd census. Indexed work on complete multipartite XOR networks and distance-two Boolean cubes considers nonisomorphic graph families with different spectral behavior. Specific web and mathematical-record searches did not identify a wheel-specific statement implying this combined result. Generic linear dynamics is prior knowledge; the claimed contribution is the explicit solution for this natural infinite graph family. Unindexed equivalent work remains possible, so no claim of literature completeness is made.

## Mathematical value — PASS

A minimal hub-and-cycle network already displays three sharply different features: reversible dynamics for odd rim size, periodic subspace collapse for even rim size with \(n\) a power of two, and a discontinuous transient-depth law controlled by the two-adic valuation for general even rim size. Rather than calculating an arbitrary small graph count, the result classifies all rim sizes and all temporal periods, exact recurrent-state totals, basins and preperiod distributions. These graph-specific formulas provide reproducible benchmarks for finite-field network dynamics.

## Limitations and nearest work

The rule is binary, synchronous, unweighted and open-neighbour only. The temporal periods on the invertible portion are specified by polynomial gcds, which can vary arithmetically with rim size. An equivalent treatment in an unindexed book, table or graph-dynamics paper remains a residual risk. The arXiv source provides an exact first-public UTC date; the older printed work gives a year, not an independently verified day. No independent review is claimed.

Self-review: passed. Independent audit: not yet performed.
