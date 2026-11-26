# Independent mathematical audit

## correctness

PASS

With h=1/t the chord gain is n times the centered ramp variance divided by d+h, using the mean-zero inverse of the path Laplacian. Summing the ramp and its squares, with left and right constant tails, gives C_n(d)−d^2(l−r)^2/(4n). In wrong parity the best imbalance is one; for d>=3 the mean of the two neighboring centered numerators exceeds this by (n−d)^2/(4n), and the denominators average exactly. At wrong-parity d=2 the d=3 neighbor wins both in bare numerator and in numerator divided by length, so it wins for all h>0. For the centered samples, the adjacent difference after positive cross multiplication is h(d−1)(n+1−d)−d(d−2)(4d−3n−4)/6. The derivative of the continuous interpolant has positive numerator up to 3n/4, then a strictly decreasing numerator with derivative (n/2−x)(x+h). Any equality at an adjacent pair therefore places the unique peak strictly between those two lengths and makes that tie global. Positive crossing criteria form a contiguous block from the top; at each crossing the next lower pair is still ordered toward the higher length, so the times are strictly ordered. The first possible crossing is n=9 and has t=7/4. Independent exact-rational checks sum electrical series/parallel resistances, separating path-tail segments from the two cycle arcs; they reproduced the optimal values and all minimizing endpoints at the checked parameters.

## originality

PASS

The exact gain update and the unit-conductance optimizer are existing coverage, not distinct contributions. The supported distinct content is the ordered transition classification, including every tie and strict exclusion of asymmetric placements, for the freely prescribed positive conductance and all path orders. The sources compared do not supply this variable-conductance family.

## value

PASS

For the canonical transport network P_n and a single fixed-strength repair, a complete classification of where to put the new edge is meaningful. The thresholds show exactly when preferring a long chord to a centered shorter chord ceases to be optimal, and when uniqueness fails. The all-conductance statement is not the catalogue's unit-edge computation or just a use of the inverse update.

The dated certificate retains the supplied scientific assessment, sources and limitations.
