# Independent mathematical audit

## correctness

PASS

Independently enumerated all 32,769 numerical binary16 inputs, retaining subnormals and identifying signed zeros. On the 2^24 integer scale, adjacent encoding distances and low-bit parity give exact nearest-even rounding; for G the square is rounded before subtracting from 2. A path-index traversal rather than indegree peeling reproduced every cycle-minimum word, least period, and full basin size for both maps, as well as 1,842 differing transitions, image sizes 2,049 and 1,946, and maximal transient lengths 59 and 69, each with multiplicity two. Exact basin weighting reproduced all four fractions (both initial sets, for both maps). Replay: python3 /workspace/branches/89413691-0878-4f51-83d8-e86b7ed4d105/independent_check.py; full_results.json in the same directory records the data. Inspected the frozen verify.py, not executed. Separately, u=(x+2)/4 conjugates the exact real map to the full logistic map, whose arcsine law is the ergodic pushforward of angle doubling; it is equivalent to Lebesgue measure in the interior and yields the asserted zero almost-sure real mean. Nothing about a physical analogue device is certified.

## originality

PASS

The supported distinct contribution is the exact signed-domain binary16 census for this pair of rounding protocols, not the real quadratic map, low-precision periodicity, or evaluation-order sensitivity as general phenomena. The strongest inspected alternatives give materially different discrete maps and statistics.

## value

PASS

The canonical binary16 format and two common rounding abstractions give a natural, complete cutoff. The exact graph is a benchmark for reproducible low-precision chaotic dynamics: changing where rounding occurs changes the largest nontrivial period from 94 to 44, shifts macroscopic basin weights and changes the exact uniform-stored-state mean. A few simulated paths or the real invariant law cannot answer these questions, and the result does not overclaim transfer to other formats or arithmetic protocols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
