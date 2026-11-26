# Independent mathematical audit

## correctness

PASS

Both nested recurrences give complementary adjacent pairs. With state (x,y)=(f(n),f(2n)), the binary children for M1 are (y,x) and (1-y,y if x=1, else 1-y); those for M2 are (y,x XOR y) and (1-y,1-(x XOR y)). Combining two steps in state order 00,11,01,10 gives exactly the frozen tables from the recurrences for all n, not just the tested prefix. The all-zero leading digit fixes the initial state. Independently computed the characteristic determinant at 17 field points for each of 1009, 1013, 1019, 1021 and matched all values of the claimed polynomial. Interpolation gives equality modulo each prime; the coefficient differences are bounded by 2*5^16 since both root multisets have moduli at most 4, and the prime product exceeds this bound. The product transfer has row sum 4, and the sign row annihilates its simple eigenline at 4. The zero Jordan part is killed by step 8; the eigenvalue 1 contributes at most a constant. The quadratic on the radius-two circle has lambda/2+2/lambda=-3/2, different from both real quartic values (3±sqrt(21))/4 in (-2,2), so all six circle eigenvalues are distinct and simple. This bounds each aligned block by K*2^k, which summed over at most three blocks of each base-four size proves the prefix bound. Independent transfer iteration gave -364 and -372 at levels 8 and 9, forcing a nonzero circle coefficient; the Cesaro mean square after normalization is the positive sum of squares of those coefficients. Expanding the pair indicator gives all cell counts, exactly on full blocks where the marginal signed sums vanish. Replay: node /workspace/branches/independent-checks.js (record 1 block). The archived verifier and recorded output were inspected, not executed.

## originality

PASS

The individual words and digit morphisms are prior. No inspected source gives the frozen pair's joint square-root upper and lower orders. The nearest signed-product and automatic-discrepancy statements are for different inputs, and an individual balanced DFAO or even a generic product transfer does not imply the pair's required eigenvalue bound, cancellation and sharpness.

## value

PASS

This resolves a natural joint statistic of the two explicitly introduced balanced sequences: balance individually leaves overlap unsettled. Sharp square-root pair discrepancy and the exact full-block relation give more than a joint density or routine DFAO construction, and distinguish this pair from pairs with slower cancellation or no cancellation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
