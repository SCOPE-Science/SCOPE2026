# Independent mathematical audit

## correctness

PASS

Nine evaluations have rank nine: the exponent choices {0,1,3} in X and {0,1,5} in Y give tensor-product interpolation bases, leaving 15 free coefficients. Local first derivatives screen exactly for smoothness at those nine points. I independently interpolated the full space, applied all 36 invertible matrix pairs to each orbit representative, and tested the affine Jacobian ideal for being the unit ideal (lex F5B over F2), together with univariate gcd tests on the two boundary lines and evaluation at their common corner. Over an algebraic closure a proper ideal has a common zero, so this checks geometric smoothness, not just points of small extension degree. Replay obtained 32768 vectors including zero, 5832 rationally smooth vectors, 206 screened orbits, then 2304 geometrically smooth vectors in 76 orbits of sizes 36, 18, 12, 6 with multiplicities 55, 15, 3, 3. The fixed-point sum is 2736, and all representative masks and sizes match the frozen CSV. A reducible smooth divisor would have disjoint components; any nontrivial partition of an effective divisor class of bidegree (3,5) has positive intersection, excluding that possibility. Adjunction gives genus (3-1)(5-1)=8.

## originality

PASS

Earlier work supplies the rational-point ideal and nearby smooth filling examples or exact censuses of other bidegrees. The inspected statements do not give or force this binary asymmetric bidegree-(3,5) census and stabilizer distribution.

## value

PASS

This is a complete classification at the first asymmetric bidegree beyond the binary minimal (3,4) with first degree fixed at 3. The underlying genus-eight curves fill nine points and carry the two specified projections. The exact census, representatives and stabilizer distribution provide a usable benchmark for binary filling curves and for comparison of embedded families, rather than merely another existence example or a sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
