# Independent mathematical audit

## correctness

PASS

For a 32-bit periodic word the 2-adic series is -S/(2^32-1); reducing that rational gives the stated positive connection denominator. Rotation multiplies S by a unit modulo 2^32-1 and complement sends S to 2^32-1-S. The unique cyclic occurrence of 00000 fixes rotation but not reversal or complement. I independently generated every canonical word by extending the fixed zero prefix one bit at a time, rejecting repeated length-five factors, and explicitly checking the four wraparound factors. Each admissible word follows one path, and any pruned path cannot be completed. Exact rational reduction reproduced all 2048 CSV rows, all ten (g,q) cells and sixteen unordered reversal cells with counts per cycle, the 632 changed cycles (316 two-element orbits), and the sharp ratio 1285 at {3,3855}. For binary linear complexity, the period denominator over GF(2) is (1+X)^32, and taking the reciprocal preserves the multiplicity at X=1. I independently calculated this multiplicity from the coefficients after substituting X=1+Y using binomial parity. Both g=3855 cycles have linear complexity 31 including the stated witness. This proves only the finite order-five classification and the indicated elementary invariances.

## originality

PASS

Pass for the exact restricted marginal and joint census and its extremal consequences, not for the classical 2-adic representation or the already known failure of general reversal invariance. No inspected statement supplies the census or a dominating conditional result.

## value

PASS

Order five gives a natural complete universe of universal binary cycles, not a sample selected for an extreme example. FCSR denominator and reversal are established invariants and operations of independent interest. The marginal and joint data provide a reusable exact benchmark showing the prevalence and sharp size of the arithmetic asymmetry even though binary linear complexity cannot detect it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
