# Independent mathematical audit

## correctness

PASS

Each block i has d_i wrong symbols, which must be exported and re-imported in equal number; therefore d_i<=min(a_i,m-d_i). Conversely choose d_i within min(a_i,floor(m/2)) summing to m and rotate the grouped length-m mismatch color word by floor(m/2): no identical color survives because each monochromatic cyclic block length is <=floor(m/2). This preserves counts and gives exactly m mismatches. Two blocks force parity; for k>=3 the cap sum is enough for every 2<=m<=min(n,2(n-a_max)). Independently enumerated exact permutation DP supports for all 255 ordered positive compositions with 1<=n<=8 and matched the general criterion; inspected supplied broader n<=11 dynamic-programming checker (not treated as proof).

## originality

PASS

Best-of-knowledge qualified originality after exact statement/implication comparisons; primary work covers key ingredients, but the final parameter-specific classification is not established in inspected prior results. Residual risks explicitly retained.

## value

PASS

Exact finite-sample support, an explicit spectrum in terms of largest block, and witnesses for every possible mismatch count answer a natural feasibility question behind multiset fixed-point/derangement statistics; neither distributional moments nor derangement-only counts supply this all-profile classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
