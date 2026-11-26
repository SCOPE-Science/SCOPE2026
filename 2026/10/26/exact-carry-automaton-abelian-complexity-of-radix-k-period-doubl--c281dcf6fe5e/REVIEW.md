# Independent mathematical audit

## correctness

PASS

The fixed point records the parity of the exponent of k dividing j+1, also for composite k. Counting multiples and collecting radix digits gives the displayed prefix identity. In the difference across an addition, the column identity a_j+c_j−kc_(j+1) contributes (k+1)(−1)^(j+1)c_j for each carry at position j≥1 after summation, giving precisely the weight claimed. The local inequalities allow arbitrary compatible column choices; finite paths are realized by finite starts. Beyond the leading digit an incoming one persists for a run and stops, and the two alternating-tail corrections are attained. Thus the constant-state dynamic program finds two attained extrema per length, and one-step changes in overlapping windows give every intervening integer. For the alternating digit ladder, every negatively signed carry pairs with the immediately preceding positive carry, including in the tail, and the tail cannot increase the m contributions available up through the highest relevant position. Taking M=0 and M equal to the sum of powers at the nonzero digits gives the extrema zero and m. For m=1 this gives exactly two counts. Primitivity holds at the second iterate. The prefix identity gives frequency 1/(k+1) and unbounded discrepancy along integers with arbitrarily many nonzero digits all at even positions, ruling out even eventual periodicity. The repaired operation count is in integer operations, not a bit-cost assertion.

## originality

PASS

For the repaired arbitrary-length optimization and exact ladder only. Scale invariance at powers of k is already a consequence of the indexed same-family cyclic-class theorem. The inspected radix-two and general balance papers, and other high-radix catalog entries, do not supply the retained explicit formula or the exact values at (k^(2m)−1)/(k+1). Bounded evidence does not settle historical priority.

## value

PASS

For a natural binary higher-radix version of period doubling, this recovers exact extrema at arbitrary lengths from a constant-state procedure rather than testing windows. The infinite ladder gives explicit lengths with exact increasing Abelian complexity, not merely qualitative unbalance, and it is not on the substitution scales already explained by cyclic-class inflation. This separates coarse-scale regularity from the count behavior at genuinely different lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
